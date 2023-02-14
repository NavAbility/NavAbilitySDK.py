# Build a Graph

The NavAbilitySDK provides variables and factors useful to robotics.  We start with a `Pose2` variable, i.e. position and orientation for a vehicle traveling on a flat XY plane.  

As before, let's setup a new client-context to talk with the NavAbility platform:
```python
# also create a client connection
client = NavAbilityHttpsClient()

# create a client context user, robot, session
context = Client(
  "guest@navability.io",
  "ExampleRobot",
  "SDKpy_"*(string(uuid4())[1:4]),
)
```

## First Pose

The `addVariable` function with a label `"x0"` and type `:Pose2` adds that variable to  to the factor graph.

```python
result_v0 = await addVariable(client, context, "x0", VariableType.Pose2)
```

Note that asynchronous tasks are used to increase the upload performance.  Each of these events are queued on the server for processing.  While the variable is being created, let's also add a prior factor.

```{eval-rst}
.. autofunction:: navability.services.addVariable
```

### And Zero-Prior

We now have a factor graph with one variable, but to solve it we need some additional information.  In this example, we need the estimated starting point of our robot.
We use unary factors called priors to represent absolute information to be introduced.  In this case we use `PriorPose2`, as our variable type is also `Pose2`.
Since factors represent a probabilistic interaction between variables, we need to specify the distribution our factor will represent. Here we use `FullNormal` which is a [multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution). 

Let's create a `PriorPose2` unary factor with zero mean and a covariance matrix of (`diagm([0.05,0.05,0.01].^2)`):
```python
prior_distribution = FullNormal(mu=np.zeros(3), cov=np.power(np.diag([0.1, 0.1, 0.1]),2))
result_f0 = await addFactor(client, context, ["x0"], PriorPose2(Z=prior_distribution)) 
```

After adding a batch of variables and factors, we can wait on the upload status to ensure the new graph elements have been processed:
```python
# Wait for variable and factor to be loaded to be loaded.
await waitForCompletion(client, [result_v0, result_f0])
```

As before, we can use the NavAbility App to visualize the factor graph
```python
# Click on the generated URL or graphic to open the NavAbility App Graph visualization page for this session
GraphVizApp(context, variableStartsWith="")
```

<!-- ```{eval-rst}
.. automodule:: navability.services
   :members: addVariable
``` -->
```{eval-rst}
.. autofunction:: navability.services.addFactor
```

## Odometry Factor

An odometry factor connects two consecutive robot poses `x0` and `x1` together to form a chain.  Here we use a relative factor of type `Pose2Pose2` with a measurement from pose `x0` to `x1` of `(x=1.0,y=0.0,θ=pi/2)`; the robot drove 1 unit forward (in the x direction).  Similarly to the prior we added above, we use a `FullNormal` distribution to represent the odometry with mean and covariance:
```python
result_v = await addVariable(client, context, "x1", VariableType.Pose2)
print(f"Added x1 with result ID {result_v}")
odo_distribution = FullNormal(mu=[1.0, 0.0, np.pi/2], cov=np.power(np.diag([0.1, 0.1, 0.01]),2))
result_fac_1 = await addFactor(client, context, ["x0", "x1"], Pose2Pose2(Z=odo_distribution)) 
print(f"Added factor with result ID {result_fac_1}")

# Wait for it to be loaded.
await waitForCompletion(client, [result_v, result_fac_1])
```

## Adding Different Sensors

So far we worked with the `Pose2` factor type.  Among others, `NavAbilitySDK` also provides the `Point2` variable and `Pose2Point2BearingRange` factor types, which we will use to represent a landmark sighting in our factor graph.  We will add a landmark `l1` with bearing range measurement of bearing=`(mu=0,sigma=0.03)` `range=(mu=0.5,sigma=0.1)` and continue our robot trajectory by driving around in a square.
```python
results_variables = [
  await addVariable(client, context, "l1", VariableType.Point2),
  await addVariable(client, context, "x2", VariableType.Pose2),
  await addVariable(client, context, "x3", VariableType.Pose2),
  await addVariable(client, context, "x4", VariableType.Pose2)]
results_variables

results_factors = [
  await addFactor(client, context, ["x0", "l1"], Pose2Point2BearingRange(Normal(0.0,0.03), Normal(0.5,0.1))),
  await addFactor(client, context, ["x1", "x2"], Pose2Pose2(odo_distribution)),
  await addFactor(client, context, ["x2", "x3"], Pose2Pose2(odo_distribution)),
  await addFactor(client, context, ["x3", "x4"], Pose2Pose2(odo_distribution)),
]
await waitForCompletion(client, results_variables + results_factors)
```

## One Loop-Closure Example

The robot continued its square trajectory to end off where it started.  To illustrate a loop closure, we add another bearing range sighting to from pose `x4` to landmark `l1`, solve the graph and plot the new results: 
```python
result_factor = await addFactor(client, context, ["x4", "l1"], Pose2Point2BearingRange(Normal(0.0,0.03), Normal(0.5,0.1)))

await waitForCompletion(client, [result_factor])
```

<!-- ```@docs
waitForCompletion
NvaSDK.waitForCompletion2
``` -->