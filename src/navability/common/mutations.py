# This will become common across all SDKs so we can't assume it's going to flake cleanly.
# flake8: noqa

GQL_ADDVARIABLE = """
mutation sdk_addVariable ($variable: FactorGraphInput!) {
    addVariable(variable: $variable)
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


GQL_ADDFACTOR = """
mutation sdk_addFactor ($factor: FactorGraphInput!) {
  addFactor(factor: $factor)
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


GQL_SOLVESESSION = """
mutation sdk_solveSession ($client: ClientInput!, $options: SolveOptionsInput) {
  solveSession(client: $client, options: $options)
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



## =============================================================
## BlobEntry => Blob
## =============================================================


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