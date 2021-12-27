# This will become common across all SDKs so we can't assume it's going to flake cleanly.
# flake8: noqa

gql_addVariable = """
mutation addVariable ($variable: FactorGraphInput!) {
    addVariable(variable: $variable)
}
"""

gql_addFactor = """
mutation addFactor ($factor: FactorGraphInput!) {
  addFactor(factor: $factor)
}
"""

# Replace __TYPE__ and __FIELDS__
# Note that you can request across robots and sessions as these are optional parameters.
gql_list = """
query list($userId: ID!, $robotId: ID, $sessionId: ID, $labelExact: ID, $labelRegex: ID, $tags: [String!], $solvable: Int = 0) {
  __TYPE__(filter: {
        label: $labelExact,
        session: {
          id: $sessionId,
          robot: {
            id: $robotId,
            user: {
              id: $userId
            }}},
        tags_contains: $tags,
        label_regexp: $labelRegex,
        solvable_gte: $solvable})
  {
    __FIELDS__
  }
}
"""

gql_list_fields_default = """
    label
"""

## Fields: Variables
gql_list_fields_variable = """
    label
    timestamp {formatted}
    variableType
    smallData
    solvable
    tags
    _version
    _id
    ppes {
      solveKey
      suggested
      max
      mean
      lastUpdatedTimestamp {formatted}
    }
    solverData
    {
      solveKey
      BayesNetOutVertIDs
      BayesNetVertID
      dimIDs
      dimbw
      dims
      dimval
      dontmargin
      eliminated
      infoPerCoord
      initialized
      ismargin
      separator
      solveInProgress
      solvedCount
      variableType
      vecbw
      vecval
      _version
    }
"""

gql_list_fields_variable_summary = """
    label
    timestamp {formatted}
    tags
    ppes {
      solveKey
      suggested
      max
      mean
      lastUpdatedTimestamp {formatted}
    }
    variableType
    _version
    _id
"""

gql_list_fields_variable_skeleton = """
    label
    tags
"""

## Fields: Factors

gql_list_fields_factor = """
    label
    timestamp {formatted}
    fnctype
    tags
    solvable
    data
    _variableOrderSymbols
    _version
"""

gql_list_fields_factor_summary = """
    label
    timestamp {formatted}
    tags
    _variableOrderSymbols
    _version
"""

gql_list_fields_factor_skeleton = """
    label
    tags
    _variableOrderSymbols
"""


gql_solveSession = """
mutation solveSession ($client: ClientInput!) {
  solveSession(client: $client)
}
"""

gql_getStatusMessages = """
        query getStatusMessages($id: ID!) {
            statusMessages(id: $id) {
                requestId,
                action,
                state,
                timestamp,
                client {
                    userId,
                    robotId,
                    sessionId
                }
            }
        }
"""

gql_getStatusLatest = """
query getStatusLatest($id: ID!) {
  statusLatest(id: $id) {
    requestId,
    action,
    state,
    timestamp,
    client {
      userId,
      robotId,
      sessionId
    }
  }
}
"""
