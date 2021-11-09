import time
from navability.entities.Variable import Variable
from navability.entities.Factor import Factor, FactorPrior
from navability.entities.StatusMessage import StatusMessage
from navability.services.NavAbilityClient import NavAbilityClient
from pprint import pprint

navi = NavAbilityClient()
result = navi.addVariable(Variable("x0", "Pose2"))
time.sleep(1)
statuses = navi.getStatusMessages(result['addVariable'])
pprint(statuses)
result = navi.addVariable(Variable("x1", "Pose2"))
time.sleep(1)
statuses = navi.getStatusMessages(result['addVariable'])
pprint(statuses)

# Add a prior
result = navi.addFactor(FactorPrior("x0f1", "PriorPose2", ["x0"]))
time.sleep(1)
statuses = navi.getStatusMessages(result['addFactor'])
pprint(statuses)

# Add a factor
result = navi.addFactor(Factor("x0x1f1", "Pose2Pose2", ["x0", "x1"]))
time.sleep(1)
statuses = navi.getStatusMessages(result['addFactor'])
pprint(statuses)

# WIP
result = navi.solveSession()


#### Sandbox

from functools import wraps
from time import time
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print 'func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts)
        return result
    return wrap


## Push to NavAbility

query = gql('''
    query  {
        VARIABLE(filter: {
            session: {
            #   id: \$sessionId, 
              robot: {
                # id: \$robotId, 
                user: {
                  id: "Guest"
                }}}}) {
          label
          session {
              id
              robot {id}
            }
        }
    }
''')


### Push to RVIZ

result = client.execute(query)
len(result['VARIABLE'])
## 
query = gql('''
    subscription solverUpdates {
        ...
    }
''')
for result in client.subscribe(query):
    print (result)
