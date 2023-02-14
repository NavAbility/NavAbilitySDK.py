# Example

This script will create variables and factors, list the graph, and solve the session for SLAM estimates.

> NOTES:
> * You'll need to start Python using `python -m asyncio` to support the `await` command.
> * You'll need numpy to run the example.

```python
from uuid import uuid4
import numpy as np
import json
from navability.entities import (
    Client,
    Factor,
    FactorData,
    FullNormal,
    NavAbilityHttpsClient,
    Pose2Pose2,
    PriorPose2,
    Variable,
    VariableType,
)
from navability.services import (
    addFactor,
    addVariable,
    solveSession,
    ls,
    lsf,
    waitForCompletion,
    getVariable
)

navability_client = NavAbilityHttpsClient()
client = Client("Guest", "MyUser", "Session_" + str(uuid4())[0:8])

# Create variables x0, x1, and x2
variables = [
    Variable("x0", VariableType.Pose2.value),
    Variable("x1", VariableType.Pose2.value),
    Variable("x2", VariableType.Pose2.value),
]

# Create factors between them
factors = [
        Factor(
            "x0f1",
            "PriorPose2",
            ["x0"],
            FactorData(
                fnc=PriorPose2(
                    Z=FullNormal(mu=np.zeros(3), cov=np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        Factor(
            "x0x1f1",
            "Pose2Pose2",
            ["x0", "x1"],
            FactorData(
                fnc=Pose2Pose2(
                    Z=FullNormal(
                        mu=[1, 1, np.pi / 3], cov=np.diag([0.1, 0.1, 0.1])
                    )
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        Factor(
            "x1x2f1",
            "Pose2Pose2",
            ["x1", "x2"],
            FactorData(
                fnc=Pose2Pose2(
                    Z=FullNormal(
                        mu=[1, 1, np.pi / 3], cov=np.diag([0.1, 0.1, 0.1])
                    )
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
    ]

# Get the result IDs so we can check on their completion
print("Adding variables and factors..\r\n")
variable_results = [await addVariable(navability_client, client, v) for v in variables]
factor_results = [await addFactor(navability_client, client, f) for f in factors]
result_ids = variable_results + factor_results

# Wait for them to be inserted if they havent already
print("Waiting for them to be loaded..\r\n")
await waitForCompletion(navability_client, result_ids, maxSeconds=120)

# Interrogate the graph
# Get the variables
print("Listing all the variables and factors in the session:\r\n")
vs = await ls(navability_client, client)
print("Variables: " + json.dumps(vs, indent=4, sort_keys=True))
# Get the factors
fs = await lsf(navability_client, client)
print("Factors: " + json.dumps(fs, indent=4, sort_keys=True))
# There's some pretty neat functionality with searching, but we'll save that for more comprehensive tutorials

# Request a SLAM multimodal solve and wait for the response
# Note: Guest sessions solve a little slower than usual because they're using some small hardware we put down for community use. Feel free to reach out if you want faster solving.
print("Requesting that the graph be solved to determine the positions of the variables (poses)...")
request_id = await solveSession(navability_client, client)
await waitForCompletion(navability_client, [request_id], maxSeconds=120)

# Get the solves positions of the variables (these are stores in the PPEs structure)
print("Getting the estimates of the variables (poses)...")
estimates = {v.label: (await getVariable(navability_client, client, v.label)).ppes['default'].suggested for v in variables}
print("Solved estimates for the positions:\r\n")
print(json.dumps(estimates, indent=4, sort_keys=True))
```