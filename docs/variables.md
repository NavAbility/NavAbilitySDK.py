# Working with Variables

## Inspect an Existing Graph

Most use cases will involve retrieving information from a factor graph session already available on the server.  Setup the API server connection, and if not `guest` use an [auth token][nva-app-auth]:
```python
# Define user, robot, session
userLabel = "guest@navability.io"
robotLabel = "TestRobot"
sessionLabel = "TestHex"

# create an authorized client connection
# leave out the auth_token if using `guest@navability.io`
fgclient = DFGClient(userLabel, robotLabel, sessionLabel)

# For authorized users, copy the auth token from the NavAbility App "Connect" page
# auth_token = "r3ft ... eo7_" # e.g. if not guest
# fgclient = DFGClient(userLabel, robotLabel, sessionLabel, auth_token=auth_token)
```

```{eval-rst}
.. autoclass:: navability.entities.DFGClient
```

### Variables

Variables represent state variables of interest such as vehicle or landmark positions, sensor calibration parameters, and more. Variables are likely hidden values that are not directly observed, but we want to estimate them from observed data.  Let's start by listing all the variables in the session:
```python
varLbls = await listVariablesAsync(fgclient)
# ["l1","x0","x1","x2","x3","x4","x5","x6"]
```

The await call is used to wait on the underlying asynchronous call.

```{eval-rst}
.. autofunction:: navability.services.listVariablesAsync
```
<!-- ```{eval-rst}
.. autoclass:: myst_parser.mocking.MockRSTParser
    :show-inheritance:
    :members: parse
``` -->


## Variable Values

The main purpose of using a factor graph is not only as data index but also to deeply connect with the mapping and localization problem.  Variables in the factor graph represent the states to be estimated from the relevant measurement data.  The numerical values for each variable are computed by any number of solver operations.  The numerical results are primarily stored in a variables `solverData` field, such that either parametric or non-parametric inference results can be used:
```python
v0 = await getVariableAsync(fgclient, "x0")
```

### Tags on Variable Node

We can readily check which tags have been added to this variable with:
```python
print('The tags on this variable are', v0.tags)
```


<!-- ```@docs
getVariable
``` -->

### Numerical values, & `solveKey`s

Since various numerical solutions may exists for the same factor graph, we introduce the idea of a `solveKey`.  Different numerical values for different `solveKey`s can exists for any number of reasons.  For example, we may find a different situation in each of three `solveKey`s, `('default', 'parametric', 'graphinit')`, where we can explore some of the properties:
```python
v0.solverData['default'].variableType
# 'RoME.Pose3'
v0.solverData['parametric'].initialized
# False
v0.solverData['grahpinit'].vecval
# [0,0,0...]
```

Each of these `solverData`s are unique identified via the `solveKey`.  The `graphinit` solver values are a duplicate of the numerical values for the variable before inference computation was performed.  In this example the `default` key corresponds to the nonparametric solution, and `parametric` represents a Gaussian only parametric solution.  Repeat solves, or solving via different methods, or solves with different parameter selections can all be supported via `solveKey`s.

The numerical values can be obtained from the `solverData` via:
```python
v0.solverData['graphinit'].vecval
# [-0.001, 0.002, 0.001, ...]
```

### Understanding `PPE`s

To better bridge the gap between non-Gaussian and Gaussian solutions, variables also store a convenience numerical solution (or summary) called the parametric point estimate (`PPE`) for each of the `solveKey`s.  While various forms of `PPE`s can exists---such as mean, max, modes, etc.---a common `suggested` field exists for basic usage.  For example, the suggested parametric equivalent solution from the nonparametric solver (`default`) can be obtained by:
```python
xyr = v0.ppes['default'].suggested
# [-0.00, 0.00, 0.00]
```

:::{seealso}
The [tutorial on leveraging (contradictory) prior data][nva-tut4] is a good example of the on when oversimplified parametric estimates (from a non-Gaussian posterior) break down.
:::

:::{warning} 
At time of writing, the PPE numerical values are stored in coordinates.  These values change to change to on-manifold point representations.  Note that the internal solver computations (i.e. `solverData`) values are already stored as on-manifold points.  For more information, see [the on-manifold points, tangent vectors, and coordinates description presented here][cjl-docs-mani].
:::

## SDK Supported Variables

The list of variable types currently supported by the SDK are:
- `Position1` / `ContinuousScalar`
- `Position2` / `Point2`
- `Pose2`
- `Position3` / `Point3`
- `Pose3`

:::{tip}
Many more variable types are already supported by the solver, see [additional docs here](https://juliarobotics.org/Caesar.jl/latest/concepts/available_varfacs/).  Reach out to NavAbility for help or support in bringing more variable types to the SDK sooner, or for help in building more variable types that may not yet exist in either libraries.
:::


[nva-app-auth]: https://app.navability.io/edge/connect
[cjl-docs-mani]: https://juliarobotics.org/Caesar.jl/latest/concepts/using_manifolds/
[nva-tut4]: sdkpynb:python/navability-sdk/icra-4-contradictorydata