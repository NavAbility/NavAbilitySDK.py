# Build a Graph

The NavAbilitySDK provides variables and factors useful to robotics.  We start with a `Pose2` variable, i.e. position and orientation for a vehicle traveling on a flat XY plane.  

As before, let's setup a new client-context to talk with the NavAbility platform:
```python
from navability.entities import DFGClient, VariableType, PriorPose2, FullNormal
from navability.services import addVariable, ls, addFactor, lsf
import uuid, random, string

userLabel = "guest@navability.io"
robotLabel = "TestRobot"
sessionLabel = "TestPy"

# also create a client connection
fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
```

## Adding Variables

:::{warning}
SDK.py@v0.6.0 currently does not support creating new sessions from "guest", but variables and factors can be added to an existing session.
:::

Let's start with `addVariable`
```{eval-rst}
.. autofunction:: navability.services.addVariable
```

by adding a randomly named variable an existing graph.  Here we call `addVariable` as type `VariableTypes.Pose2`.  Pose2 here refers to position an orientation on a flat 2D plane -- i.e. the variable represents the estimation problem to find the state of variable with freedoms `[x,y,theta]`:
```python
# generate a random variable label
vlabel = 'x_'+''.join(random.choices(string.ascii_letters + string.digits, k=4))

# add the variable to the existing session under guest
v = addVariable(fgclient, vlabel, VariableType.Pose2)
# result_v0 = await addVariable(fgclient, "x0", VariableType.Pose2)
```

:::{tip}
Note that asynchronous tasks could increase client side upload performance.  Each of these events are queued on the server for processing.  While the variable is being created.
:::

## Adding Factors

Next, we can also add a factor.  Have a look at the `addFactor` function followed by how a user defines the factor measurement and observation model in the next section.

```{eval-rst}
.. autofunction:: navability.services.addFactor
```

### A Zero-Prior

Let's first add a Prior.  Priors are absolute information about variables.  
:::{tip}
NavAbility factor graph solutions at this time require a gauge to exist for the graph being solved, hence enough prior information must be included in the graph to constrain the solution (bundles/orbits/locii) to a single solution.  **Note** that this does not imply solutions are necessarily unimodal (Gaussian).
:::

In this example, we'll use the estimated starting point of our robot.
We use unary factors called priors to represent absolute information to be introduced.  In this case we use `PriorPose2`, as our variable type is also `Pose2`.
Since factors represent a probabilistic interaction between variables, we need to specify the distribution our factor will represent. Here we use `FullNormal` which is a [multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution). 

Let's create a `PriorPose2` unary factor with zero mean and a covariance matrix of (`diagm([0.05,0.05,0.01].^2)`):
```python
prior_distribution = FullNormal(mu=np.zeros(3), cov=np.power(np.diag([0.1, 0.1, 0.1]),2))
result_f0 = addFactor(fgclient, ["x0"], PriorPose2(Z=prior_distribution)) 
# result_f0 = await addFactorAsync(fgclient, ["x0"], PriorPose2(Z=prior_distribution)) 
```

## Odometry Factor

An odometry factor connects two consecutive robot poses `x0` and `x1` together to form a chain.  Here we use a relative factor of type `Pose2Pose2` with a measurement from pose `x0` to `x1` of `(x=1.0,y=0.0,θ=pi/2)`; the robot drove 1 unit forward (in the x direction).  Similarly to the prior we added above, we use a `FullNormal` distribution to represent the odometry with mean and covariance:
```python
result_v = addVariable(fgclient, "x1", VariableType.Pose2)
print(f"Added x1 with result ID {result_v}")

odo_distribution = FullNormal(mu=[1.0, 0.0, np.pi/2], cov=np.power(np.diag([0.1, 0.1, 0.01]),2))
result_fac_1 = addFactor(fgclient, ["x0", "x1"], Pose2Pose2(Z=odo_distribution)) 
print(f"Added factor with result ID {result_fac_1}")
```

## Adding Different Sensors

So far we worked with the `Pose2` factor type.  Among others, `NavAbilitySDK` also provides the `Point2` variable and `Pose2Point2BearingRange` factor types, which we will use to represent a landmark sighting in our factor graph.  We will add a landmark `l1` with bearing range measurement of bearing=`(mu=0,sigma=0.03)` `range=(mu=0.5,sigma=0.1)` and continue our robot trajectory by driving around in a square.
```python
addVariable(fgclient, "l1", VariableType.Point2)
addVariable(fgclient, "x2", VariableType.Pose2)
addVariable(fgclient, "x3", VariableType.Pose2)
addVariable(fgclient, "x4", VariableType.Pose2)

addFactor(fgclient, ["x0", "l1"], Pose2Point2BearingRange(Normal(0.0,0.03), Normal(0.5,0.1)))
addFactor(fgclient, ["x1", "x2"], Pose2Pose2(odo_distribution))
addFactor(fgclient, ["x2", "x3"], Pose2Pose2(odo_distribution))
addFactor(fgclient, ["x3", "x4"], Pose2Pose2(odo_distribution))
```

## One Loop-Closure Example

The robot continued its square trajectory to end off where it started.  To illustrate a loop closure, we add another bearing range sighting to from pose `x4` to landmark `l1`, solve the graph and plot the new results: 
```python
result_factor = addFactor(fgclient, ["x4", "l1"], Pose2Point2BearingRange(Normal(0.0,0.03), Normal(0.5,0.1)))
```
