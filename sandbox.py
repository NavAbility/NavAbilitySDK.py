# flake8: noqa

import time
from pprint import pprint

from navability.entities.Client import Client
from navability.entities.Factor import Factor, FactorPrior
from navability.entities.NavAbilityClient import NavAbilityWebsocketClient
from navability.entities.StatusMessage import StatusMessage
from navability.entities.Variable import Variable
from navability.services.Factor import addFactor
from navability.services.Solve import solveSession
from navability.services.Status import getStatusMessages
from navability.services.Variable import addVariable

client = Client("Guest", "DemoRobot", "DemoSession")
navAbilityClient = NavAbilityWebsocketClient()
v = Variable("x0", "Pose2")
res = addVariable(navAbilityClient, client, v)
getStatusMessages(navAbilityClient, res["addVariable"])
solveSession(navAbilityClient, client)

# navi = NavAbilityClient()
# result = navi.addVariable(Variable("x0", "Pose2"))
# time.sleep(1)
# statuses = navi.getStatusMessages(result['addVariable'])
# pprint(statuses)
# result = navi.addVariable(Variable("x1", "Pose2"))
# time.sleep(1)
# statuses = navi.getStatusMessages(result['addVariable'])
# pprint(statuses)

# # Add a prior
# result = navi.addFactor(FactorPrior("x0f1", "PriorPose2", ["x0"]))
# time.sleep(1)
# statuses = navi.getStatusMessages(result['addFactor'])
# pprint(statuses)

# # Add a factor
# result = navi.addFactor(Factor("x0x1f1", "Pose2Pose2", ["x0", "x1"]))
# time.sleep(1)
# statuses = navi.getStatusMessages(result['addFactor'])
# pprint(statuses)

# # WIP
# result = navi.solveSession()


# #### Sandbox

# from functools import wraps
# from time import time
# def timing(f):
#     @wraps(f)
#     def wrap(*args, **kw):
#         ts = time()
#         result = f(*args, **kw)
#         te = time()
#         print 'func:%r args:[%r, %r] took: %2.4f sec' % \
#           (f.__name__, args, kw, te-ts)
#         return result
#     return wrap


## Push to NavAbility

query = gql(
    """
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
"""
)


### Push to RVIZ

result = client.execute(query)
len(result["VARIABLE"])
##
query = gql(
    """
    subscription solverUpdates {
        ...
    }
"""
)
for result in client.subscribe(query):
    print(result)
