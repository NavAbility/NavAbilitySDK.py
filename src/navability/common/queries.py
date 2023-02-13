# This will become common across all SDKs so we can't assume it's going to flake cleanly.
# flake8: noqa

# Very generic find query
GQL_FRAGMENT_VARIABLES = """
fragment ppe_fields on Ppe {
  solveKey
  suggested
  max
  mean
  lastUpdatedTimestamp
}
fragment solverdata_fields on SolverData {
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
fragment variable_skeleton_fields on Variable {
	label
  tags
}
fragment variable_summary_fields on Variable {
  timestamp
  ppes {
    ...ppe_fields
  }
  variableType
  _version
}
fragment variable_full_fields on Variable{
  smallData
  solvable
  solverData
  {
		...solverdata_fields
  }
}
"""

GQL_LISTVARIABLES = """
query sdk_list_variables (
    $userId: ID!, 
    $robotId: ID!, 
    $sessionId: ID!) {
  users(where:{id: $userId}) {
    robots(where:{id: $robotId}) {
      sessions(where:{id: $sessionId}) {
        variables {
          label
        }
      }
    }
  }
}
"""

GQL_GETVARIABLE = """
query sdk_get_variable(
  	$userId: ID!,
  	$robotId: ID!,
  	$sessionId: ID!,
    $label: ID!) {
	users(where:{id: $userId}) {
		robots(where:{id: $robotId}) {
      sessions(where:{id: $sessionId}) {
        variables(where:{label: $label}) {
          ...variable_skeleton_fields
          ...variable_summary_fields
          ...variable_full_fields
        }
      }
    }
  }
}
"""

GQL_GETVARIABLES = """
query sdk_get_variables(
  	$userId: ID!,
  	$robotIds: [ID!]!,
  	$sessionIds: [ID!]!,
    $variable_label_regexp: String = ".*",
    $variable_tags: [String] = ["VARIABLE"],
    $solvable: Int! = 0,
  	$fields_summary: Boolean! = false,
  	$fields_full: Boolean! = false){
	users(where: {id:$userId}) {
    name
		robots(where:{id_IN: $robotIds}) {
      name
      sessions(where:{id_IN: $sessionIds}){
        name
        variables(where:{
            label_MATCHES: $variable_label_regexp,
          	tags: $variable_tags,
          	solvable_GTE: $solvable}) {
          ...variable_skeleton_fields # Always include
          ...variable_summary_fields @include(if: $fields_summary)
          ...variable_full_fields @include(if: $fields_full)
        }
      }
    }
  }
}
"""

GQL_GETVARIABLESFILTERED = """
query sdk_get_variables_filtered(
    $userId: ID!, 
    $robotIds: [ID!]!, 
    $sessionIds: [ID!]!, 
    $variable_label_regexp: String = ".*",
    $variable_tags: [String] = ["VARIABLE"],
    $solvable: Int! = 0,
    $fields_summary: Boolean! = false, 
    $fields_full: Boolean! = false){
  users(where:{id: $userId}) {
    name
    robots(where:{id_in: $robotIds}) {
      name
      sessions(where:{id_in: $sessionIds}){
        name
        variables(where:{
            label_MATCHES: $variable_label_regexp, 
            tags: $variable_tags, 
            solvable_GTE: $solvable}) {
          ...variable_skeleton_fields
          ...variable_summary_fields @include(if: $fields_summary)
          ...variable_full_fields @include(if: $fields_full)
        }
      }
    }
  }
}
"""

GQL_ADD_VARIABLE_PACKED = """
mutation sdk_add_variable_packed(
    $variablePackedInput: AddVariablePackedInput!, 
    $options: AddVariablePackedOptionsInput
  ) {
  addVariablePacked(variable: $variablePackedInput, options:$options) {
    context {
      eventId
    }  
    status {
      state
      progress
    }
  }
}
"""

GQL_INIT_VARIABLE = """
mutation sdk_init_variable(
    $variable: InitVariableInput!, 
    $options: EmptyOptionsInput
  ) {
  initVariable(variable: $variable, options:$options) {
    context {
      eventId
    }
    status {
      state
      progress
    }
  }
}
"""

GQL_LIST_VARIABLE_NEIGHBORS = """
query sdk_list_variable_neighbors (
  $userId: ID!, 
  $robotId: ID!, 
  $sessionId: ID!, 
  $variableLabel: ID!
  ) {
  users(where:{id: $userId}) {
    robots(where:{id: $robotId}) {
      sessions(where:{id: $sessionId}) {
        variables(where:{label: $variableLabel}) {
          factors {
            label
          }
        }
      }
    }
  }
}
"""

## =================================================
## Factor Queries
## =================================================


GQL_FRAGMENT_FACTORS = """
fragment factor_skeleton_fields on Factor {
	label
  tags
  _variableOrderSymbols
}
fragment factor_summary_fields on Factor {
  timestamp
  _version
}
fragment factor_full_fields on Factor {
  fnctype
  solvable
  data
}
"""

GQL_GETFACTOR = """
query sdk_get_variable(
  	$userId: ID!,
  	$robotId: ID!,
  	$sessionId: ID!,
    $label: ID!) {
	users(where:{id: $userId}) {
		robots(where:{id: $robotId}) {
      sessions(where:{id: $sessionId}) {
        factors(where:{label: $label}) {
          ...factor_skeleton_fields
          ...factor_summary_fields
          ...factor_full_fields
        }
      }
    }
  }
}
"""

GQL_GETFACTORS = """
query sdk_get_factors(
  	$userId: ID!,
  	$robotIds: [ID!]!,
  	$sessionIds: [ID!]!,
    $factor_label_regexp: String = ".*",
    $factor_tags: [String] = ["FACTOR"],
    $solvable: Int! = 0,
  	$fields_summary: Boolean! = false,
  	$fields_full: Boolean! = false){
	users(where: {id:$userId}) {
    name
		robots(where:{id_IN: $robotIds}) {
      name
      sessions(where:{id_IN: $sessionIds}){
        name
        factors(where:{
            label_MATCHES: $factor_label_regexp,
          	tags: $factor_tags,
          	solvable_GTE: $solvable}) {
          ...factor_skeleton_fields # Always include
          ...factor_summary_fields @include(if: $fields_summary)
          ...factor_full_fields @include(if: $fields_full)
        }
      }
    }
  }
}"""


GQL_GETFACTORSFILTERED = """
query sdk_get_factors(
    $userId: ID!, 
    $robotIds: [ID!]!, 
    $sessionIds: [ID!]!, 
    $factor_label_regexp: String = ".*",
    $factor_tags: [String] = ["FACTOR"],
    $solvable: Int! = 0,
    $fields_summary: Boolean! = false, 
    $fields_full: Boolean! = false){
  users(where:{id:$userId}) {
    name
    robots(where:{id_IN: $robotIds}) {
      name
      sessions(where:{id_IN: $sessionIds}){
        name
        factors(where:{
          label_MATCHES: $factor_label_regexp, 
          tags: $factor_tags, 
          solvable_GTE: $solvable}) {
          ...factor_skeleton_fields
          ...factor_summary_fields @include(if: $fields_summary)
          ...factor_full_fields @include(if: $fields_full)
        }
      }
    }
  }
}
"""

GQL_DELETEFACTOR = """
  mutation sdk_delete_factor(
    $factor: DeleteFactorInput!, 
    $options: DeleteFactorOptionsInput
  ) {
  deleteFactor(factor: $factor, options: $options) {
    context {
      eventId
    }
    status {
      state
      progress
    }
  }
}
"""


GQL_GETVARIABLESFACTORS = """
query sdk_get_variablesfactors(
  	$userId: ID!,
  	$robotIds: [ID!]!,
  	$sessionIds: [ID!]!,
  	$variables: Boolean! = true,
  	$factors: Boolean! = true,
    $variable_label_regexp: String = ".*",
    $factor_label_regexp: String = ".*",
    $variable_tags: [String] = ["VARIABLE"],
    $factor_tags: [String] = ["FACTOR"],
    $solvable: Int! = 0,
  	$fields_summary: Boolean! = false,
  	$fields_full: Boolean! = false){
	users(where:{id: $userId}) {
    name
		robots(where:{id_IN: $robotIds}) {
      name
      sessions(where:{id_IN: $sessionIds}){
        name
        variables(where:{
            label_MATCHES: $variable_label_regexp,
          	tags: $variable_tags,
          	solvable_GTE: 0}) @include(if: $variables){
          ...variable_skeleton_fields # Always include
          ...variable_summary_fields @include(if: $fields_summary)
          ...variable_full_fields @include(if: $fields_full)
        }
        factors(filter:{
            label_MATCHES: $factor_label_regexp,
          	tags: $factor_tags,
          	solvable_GTE: $solvable}) @include(if: $factors){
          ...factor_skeleton_fields # Always include
          ...factor_summary_fields @include(if: $fields_summary)
          ...factor_full_fields @include(if: $fields_full)
        }
      }
    }
  }
}"""

## ==============================================
## Status GQL
## ==============================================


GQL_GETSTATUSMESSAGES = """
query sdk_ls_statusmessages($id: ID!) {
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

GQL_GETSTATUSLATEST = """
query sdk_get_statuslatest($id: ID!) {
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

GQL_GET_EVENTS_BY_ID = """
query sdk_events_by_id($eventId:String) {
  test: events(event: {context:{eventId:$eventId}}) {
    context {
      eventId
    }
    status {
      state
    }
  }
}
"""

## =============================================
## Session GQL
## =============================================

GQL_GET_SESSION = """
query sdk_get_session(
    $userId: ID!, 
    $robotId: ID!, 
    $sessionId: ID!
  ) {
  users(where: {id: $userId}) {
    id
    robots(where:{id: $robotId}) {
      id
      sessions(where:{id: $sessionId}) {
        variables {
          label
        }
        factors {
          label
        }
      }
    }
  }
}
"""

MUTATION_EXPORT_SESSION = """
mutation sdk_export_session(
    $session: ExportSessionInput!, 
    $options: ExportSessionOptions
  ){
  exportSession(session:$session, options:$options) {
    context {
      eventId
    }
    status {
      state
      progress
    }
  }
}
"""

GQL_GET_EXPORT_SESSION_COMPLETE_EVENT_BY_ID = """
query events_by_id($eventId:String) {
  events(where: {status:{state:Complete}, context:{eventId:$eventId}}) {
    status {
      state
    }
    data {
      ... on ExportSessionComplete {
        blob {
          id
        }
      }
      ... on AddBlobMetadataComplete {
        blob {
          id
        }
      }
    }
  }
}
"""

## =================================================
## DataBlobs
## =================================================


GQL_CREATEDOWNLOAD = """
mutation sdk_url_createdownload ($userId: String!, $fileId: ID!) {
  url: createDownload(
    userId: $userId
    fileId: $fileId
  )
}
"""


GQL_CREATE_UPLOAD = """
mutation sdk_url_createupload($filename: String!, $filesize: BigInt!, $parts: Int!) {
  createUpload(
    file: {
      filename: $filename,
      filesize: $filesize
    },
    parts: $parts
  ) {
    uploadId
    parts {
      partNumber
      url
    }
    file {
      id
    }
  }
}
"""


GQL_COMPLETEUPLOAD_SINGLE = """
mutation completeUpload($fileId: ID!, $uploadId: ID!, $eTag: String) {
  completeUpload (
    fileId: $fileId,
    completedUpload: {
      uploadId: $uploadId,
      parts: [
        {
          partNumber: 1,
          eTag: $eTag
        }
      ]
    }
  )
}
"""


GQL_ADDDATAENTRY = """
mutation sdk_adddataentry($userId: ResourceId!, $robotId: ResourceId!, $sessionId: ResourceId!, $variableLabel: String!, $dataId: UUID!, $dataLabel: String!, $mimeType: String) {
  addDataEntry (
    dataEntry: {
      client: {
        userId: $userId,
        robotId: $robotId,
        sessionId: $sessionId
      },
      blobStoreEntry: {
        id: $dataId,
        label: $dataLabel
        mimetype: $mimeType
      },
      nodeLabel: $variableLabel
    }
  )
}
"""

GQL_ADDBLOBENTRY = """
mutation sdk_addblobentry(
  $userId: String!
  $robotId: String!
  $sessionId: String!
  $variableLabel: String!
  $blobId: UUID!
  $dataLabel: String!
  $blobSize: Int!
  $mimeType: String
) {
  addBlobEntry(
    blob: {
      id: $blobId
      label: $dataLabel
      size: $blobSize
      mimeType: $mimeType
      blobstore: NAVABILITY
    }
    options: {
      links: [
        {
          key: {
            user: { userLabel: $userId }
            variable: {
              userId: $userId
              robotId: $robotId
              sessionId: $sessionId
              variableLabel: $variableLabel
            }
          }
        }
      ]
    }
  ) {
    context {
      eventId
    } 
    status {
      state
      progress
    }
  }
}
"""

GQL_LISTDATAENTRIES = """
query sdk_listdataentries($userId: ID!, $robotId: ID!, $sessionId: ID!, $variableLabel: ID!) {
  users (
    where: {id: $userId}
  ) {
    robots (
      where: {id: $robotId}
    ) {
      sessions (
        where: {id: $sessionId}
      ) {
        variables (
          where: {label: $variableLabel}
        ) {
          data {
            id
            label
            mimeType
          }
        }
      }
    }
  }
}
"""

GQL_LISTDATABLOBS = """
query sdk_listdatablobs {
  files {
    id
    filename
    filesize
  }
}
"""