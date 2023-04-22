from enum import Enum
from typing import Any, ClassVar, List, Optional, TypedDict


## Scalars

DateTime = Any

UUID = Any

ULID = Any

Symbol = Any

B64JSON = Any

ComingSoon = Any

BigInt = Any

EmailAddress = Any

Latitude = Any

Longitude = Any

Metadata = Any

EventData = TypedDict('EventData', {
	'noop': Optional[str],
})


EventOptions = TypedDict('EventOptions', {
	'noop': Optional[str],
})


Node = TypedDict('Node', {
	'id': 'UUID',
	'label': str,
	'description': Optional[str],
	'tags': Optional[List[str]],
	'createdTimestamp': 'DateTime',
	'updatedTimestamp': 'DateTime',
})


Satellite = TypedDict('Satellite', {
	'id': 'UUID',
	'label': str,
	'description': Optional[str],
	'tags': Optional[List[str]],
	'createdTimestamp': 'DateTime',
	'updatedTimestamp': 'DateTime',
	'additionalFieldExample': Optional[str],
})


NvaNode = TypedDict('NvaNode', {
	'id': str,
	'label': str,
	'_version': str,
	'metadata': Optional['Metadata'],
	'createdTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
})


UserMapRole = TypedDict('UserMapRole', {
	'role': str,
})


Blobstore = Enum('Blobstore', 'NAVABILITY LOCAL')


HashAlgorithm = Enum('HashAlgorithm', 'MD5')


SortDirection = Enum('SortDirection', 'ASC DESC')


Command = Enum('Command', 'Add Init Export Update Delete Unknown')


NodeType = Enum('NodeType', 'USER ROBOT SESSION VARIABLE FACTOR BLOB PPE UNKNOWN')


State = Enum('State', 'Accepted Queued Processing Complete Failed Unknown')


FactorType = Enum('FactorType', 'POSE2POSE2')


BagFormat = Enum('BagFormat', 'NVA ROS1BAG MCAP')


VariableType = Enum('VariableType', 'POINT2 POINT3 POSE2 POSE2Z POSE3')


Query = TypedDict('Query', {
	'events': 'EventsQueryResult',
	'users': 'UsersQueryResult',
	'robots': 'RobotsQueryResult',
	'sessions': 'SessionsQueryResult',
	'variables': 'VariablesQueryResult',
	'factors': 'FactorsQueryResult',
	'maps': 'MapsQueryResult',
	'workflows': 'WorkflowsQueryResult',
	'blobs': 'BlobsQueryResult',
})


EventsParams = TypedDict('EventsParams', {
	'event': Optional['GetEventInput'],
	'options': Optional['GetEventOptionsInput'],
})


EventsQueryResult = ClassVar[Optional[List['Event']]]


UsersParams = TypedDict('UsersParams', {
	'where': Optional['UserWhere'],
	'options': Optional['UserOptions'],
})


UsersQueryResult = ClassVar[List['User']]


RobotsParams = TypedDict('RobotsParams', {
	'where': Optional['RobotWhere'],
	'options': Optional['RobotOptions'],
})


RobotsQueryResult = ClassVar[List['Robot']]


SessionsParams = TypedDict('SessionsParams', {
	'where': Optional['SessionWhere'],
	'options': Optional['SessionOptions'],
})


SessionsQueryResult = ClassVar[List['Session']]


VariablesParams = TypedDict('VariablesParams', {
	'where': Optional['VariableWhere'],
	'options': Optional['VariableOptions'],
})


VariablesQueryResult = ClassVar[List['Variable']]


FactorsParams = TypedDict('FactorsParams', {
	'where': Optional['FactorWhere'],
	'options': Optional['FactorOptions'],
})


FactorsQueryResult = ClassVar[List['Factor']]


MapsParams = TypedDict('MapsParams', {
	'where': Optional['MapWhere'],
	'options': Optional['MapOptions'],
})


MapsQueryResult = ClassVar[List['Map']]


WorkflowsParams = TypedDict('WorkflowsParams', {
	'where': Optional['WorkflowWhere'],
	'options': Optional['WorkflowOptions'],
})


WorkflowsQueryResult = ClassVar[List['Workflow']]


BlobsParams = TypedDict('BlobsParams', {
	'where': Optional['BlobQueryFilter'],
})


BlobsQueryResult = ClassVar[Optional[List['Blob']]]


Mutation = TypedDict('Mutation', {
	'solveEnvironment': 'SolveEnvironmentMutationResult',
	'addFactorPacked': 'AddFactorPackedMutationResult',
	'addNodes': 'AddNodesMutationResult',
	'importSession': 'ImportSessionMutationResult',
	'exportSession': 'ExportSessionMutationResult',
	'solveSessionImproved': 'SolveSessionImprovedMutationResult',
	'addVariablePacked': 'AddVariablePackedMutationResult',
	'initVariable': 'InitVariableMutationResult',
	'addRobots': 'AddRobotsMutationResult',
	'deleteRobots': 'DeleteRobotsMutationResult',
	'updateRobots': 'UpdateRobotsMutationResult',
	'addSessions': 'AddSessionsMutationResult',
	'deleteSessions': 'DeleteSessionsMutationResult',
	'updateSessions': 'UpdateSessionsMutationResult',
	'addVariables': 'AddVariablesMutationResult',
	'deleteVariables': 'DeleteVariablesMutationResult',
	'updateVariables': 'UpdateVariablesMutationResult',
	'addPpes': 'AddPpesMutationResult',
	'deletePpes': 'DeletePpesMutationResult',
	'updatePpes': 'UpdatePpesMutationResult',
	'addBlobEntries': 'AddBlobEntriesMutationResult',
	'deleteBlobEntries': 'DeleteBlobEntriesMutationResult',
	'updateBlobEntries': 'UpdateBlobEntriesMutationResult',
	'addSolverData': 'AddSolverDataMutationResult',
	'deleteSolverData': 'DeleteSolverDataMutationResult',
	'updateSolverData': 'UpdateSolverDataMutationResult',
	'addFactors': 'AddFactorsMutationResult',
	'deleteFactors': 'DeleteFactorsMutationResult',
	'updateFactors': 'UpdateFactorsMutationResult',
	'addMaps': 'AddMapsMutationResult',
	'deleteMaps': 'DeleteMapsMutationResult',
	'updateMaps': 'UpdateMapsMutationResult',
	'addWorkflows': 'AddWorkflowsMutationResult',
	'deleteWorkflows': 'DeleteWorkflowsMutationResult',
	'updateWorkflows': 'UpdateWorkflowsMutationResult',
	'createUpload': 'CreateUploadMutationResult',
	'abortUpload': 'AbortUploadMutationResult',
	'completeUpload': 'CompleteUploadMutationResult',
	'deleteBlob': 'DeleteBlobMutationResult',
	'createDownload': 'CreateDownloadMutationResult',
})


SolveEnvironmentParams = TypedDict('SolveEnvironmentParams', {
	'environment': 'SolveEnvironmentInput',
	'options': Optional['SolveEnvironmentOptionsInput'],
})


SolveEnvironmentMutationResult = ClassVar[Optional['Event']]


AddFactorPackedParams = TypedDict('AddFactorPackedParams', {
	'factor': 'AddFactorPackedInput',
	'options': Optional['AddFactorPackedOptionsInput'],
})


AddFactorPackedMutationResult = ClassVar[Optional['Event']]


AddNodesParams = TypedDict('AddNodesParams', {
	'nodes': 'AddNodesInput',
	'options': Optional['AddNodesOptionsInput'],
})


AddNodesMutationResult = ClassVar[Optional['Event']]


ImportSessionParams = TypedDict('ImportSessionParams', {
	'session': 'ImportSessionInput',
	'options': Optional['ImportSessionOptionsInput'],
})


ImportSessionMutationResult = ClassVar[Optional['Event']]


ExportSessionParams = TypedDict('ExportSessionParams', {
	'session': 'ExportSessionInput',
	'options': Optional['ExportSessionOptionsInput'],
})


ExportSessionMutationResult = ClassVar[Optional['Event']]


SolveSessionImprovedParams = TypedDict('SolveSessionImprovedParams', {
	'session': 'SolveSessionInput',
	'options': Optional['SolveSessionOptionsInput'],
})


SolveSessionImprovedMutationResult = ClassVar[Optional['Event']]


AddVariablePackedParams = TypedDict('AddVariablePackedParams', {
	'variable': 'AddVariablePackedInput',
	'options': Optional['AddVariablePackedOptionsInput'],
})


AddVariablePackedMutationResult = ClassVar[Optional['Event']]


InitVariableParams = TypedDict('InitVariableParams', {
	'variable': 'InitVariableInput',
	'options': Optional['EmptyOptionsInput'],
})


InitVariableMutationResult = ClassVar[Optional['Event']]


AddRobotsParams = TypedDict('AddRobotsParams', {
	'input': List['RobotCreateInput'],
})


AddRobotsMutationResult = ClassVar['CreateRobotsMutationResponse']


DeleteRobotsParams = TypedDict('DeleteRobotsParams', {
	'where': Optional['RobotWhere'],
	'delete': Optional['RobotDeleteInput'],
})


DeleteRobotsMutationResult = ClassVar['DeleteInfo']


UpdateRobotsParams = TypedDict('UpdateRobotsParams', {
	'where': Optional['RobotWhere'],
	'update': Optional['RobotUpdateInput'],
	'connect': Optional['RobotConnectInput'],
	'disconnect': Optional['RobotDisconnectInput'],
	'create': Optional['RobotRelationInput'],
	'delete': Optional['RobotDeleteInput'],
	'connectOrCreate': Optional['RobotConnectOrCreateInput'],
})


UpdateRobotsMutationResult = ClassVar['UpdateRobotsMutationResponse']


AddSessionsParams = TypedDict('AddSessionsParams', {
	'input': List['SessionCreateInput'],
})


AddSessionsMutationResult = ClassVar['CreateSessionsMutationResponse']


DeleteSessionsParams = TypedDict('DeleteSessionsParams', {
	'where': Optional['SessionWhere'],
	'delete': Optional['SessionDeleteInput'],
})


DeleteSessionsMutationResult = ClassVar['DeleteInfo']


UpdateSessionsParams = TypedDict('UpdateSessionsParams', {
	'where': Optional['SessionWhere'],
	'update': Optional['SessionUpdateInput'],
	'connect': Optional['SessionConnectInput'],
	'disconnect': Optional['SessionDisconnectInput'],
	'create': Optional['SessionRelationInput'],
	'delete': Optional['SessionDeleteInput'],
	'connectOrCreate': Optional['SessionConnectOrCreateInput'],
})


UpdateSessionsMutationResult = ClassVar['UpdateSessionsMutationResponse']


AddVariablesParams = TypedDict('AddVariablesParams', {
	'input': List['VariableCreateInput'],
})


AddVariablesMutationResult = ClassVar['CreateVariablesMutationResponse']


DeleteVariablesParams = TypedDict('DeleteVariablesParams', {
	'where': Optional['VariableWhere'],
	'delete': Optional['VariableDeleteInput'],
})


DeleteVariablesMutationResult = ClassVar['DeleteInfo']


UpdateVariablesParams = TypedDict('UpdateVariablesParams', {
	'where': Optional['VariableWhere'],
	'update': Optional['VariableUpdateInput'],
	'connect': Optional['VariableConnectInput'],
	'disconnect': Optional['VariableDisconnectInput'],
	'create': Optional['VariableRelationInput'],
	'delete': Optional['VariableDeleteInput'],
	'connectOrCreate': Optional['VariableConnectOrCreateInput'],
})


UpdateVariablesMutationResult = ClassVar['UpdateVariablesMutationResponse']


AddPpesParams = TypedDict('AddPpesParams', {
	'input': List['PPECreateInput'],
})


AddPpesMutationResult = ClassVar['CreatePpesMutationResponse']


DeletePpesParams = TypedDict('DeletePpesParams', {
	'where': Optional['PPEWhere'],
	'delete': Optional['PPEDeleteInput'],
})


DeletePpesMutationResult = ClassVar['DeleteInfo']


UpdatePpesParams = TypedDict('UpdatePpesParams', {
	'where': Optional['PPEWhere'],
	'update': Optional['PPEUpdateInput'],
	'connect': Optional['PPEConnectInput'],
	'disconnect': Optional['PPEDisconnectInput'],
	'create': Optional['PPERelationInput'],
	'delete': Optional['PPEDeleteInput'],
	'connectOrCreate': Optional['PPEConnectOrCreateInput'],
})


UpdatePpesMutationResult = ClassVar['UpdatePpesMutationResponse']


AddBlobEntriesParams = TypedDict('AddBlobEntriesParams', {
	'input': List['BlobEntryCreateInput'],
})


AddBlobEntriesMutationResult = ClassVar['CreateBlobEntriesMutationResponse']


DeleteBlobEntriesParams = TypedDict('DeleteBlobEntriesParams', {
	'where': Optional['BlobEntryWhere'],
	'delete': Optional['BlobEntryDeleteInput'],
})


DeleteBlobEntriesMutationResult = ClassVar['DeleteInfo']


UpdateBlobEntriesParams = TypedDict('UpdateBlobEntriesParams', {
	'where': Optional['BlobEntryWhere'],
	'update': Optional['BlobEntryUpdateInput'],
	'connect': Optional['BlobEntryConnectInput'],
	'disconnect': Optional['BlobEntryDisconnectInput'],
	'create': Optional['BlobEntryRelationInput'],
	'delete': Optional['BlobEntryDeleteInput'],
	'connectOrCreate': Optional['BlobEntryConnectOrCreateInput'],
})


UpdateBlobEntriesMutationResult = ClassVar['UpdateBlobEntriesMutationResponse']


AddSolverDataParams = TypedDict('AddSolverDataParams', {
	'input': List['SolverDataCreateInput'],
})


AddSolverDataMutationResult = ClassVar['CreateSolverDataMutationResponse']


DeleteSolverDataParams = TypedDict('DeleteSolverDataParams', {
	'where': Optional['SolverDataWhere'],
	'delete': Optional['SolverDataDeleteInput'],
})


DeleteSolverDataMutationResult = ClassVar['DeleteInfo']


UpdateSolverDataParams = TypedDict('UpdateSolverDataParams', {
	'where': Optional['SolverDataWhere'],
	'update': Optional['SolverDataUpdateInput'],
	'connect': Optional['SolverDataConnectInput'],
	'disconnect': Optional['SolverDataDisconnectInput'],
	'create': Optional['SolverDataRelationInput'],
	'delete': Optional['SolverDataDeleteInput'],
	'connectOrCreate': Optional['SolverDataConnectOrCreateInput'],
})


UpdateSolverDataMutationResult = ClassVar['UpdateSolverDataMutationResponse']


AddFactorsParams = TypedDict('AddFactorsParams', {
	'input': List['FactorCreateInput'],
})


AddFactorsMutationResult = ClassVar['CreateFactorsMutationResponse']


DeleteFactorsParams = TypedDict('DeleteFactorsParams', {
	'where': Optional['FactorWhere'],
	'delete': Optional['FactorDeleteInput'],
})


DeleteFactorsMutationResult = ClassVar['DeleteInfo']


UpdateFactorsParams = TypedDict('UpdateFactorsParams', {
	'where': Optional['FactorWhere'],
	'update': Optional['FactorUpdateInput'],
	'connect': Optional['FactorConnectInput'],
	'disconnect': Optional['FactorDisconnectInput'],
	'create': Optional['FactorRelationInput'],
	'delete': Optional['FactorDeleteInput'],
	'connectOrCreate': Optional['FactorConnectOrCreateInput'],
})


UpdateFactorsMutationResult = ClassVar['UpdateFactorsMutationResponse']


AddMapsParams = TypedDict('AddMapsParams', {
	'input': List['MapCreateInput'],
})


AddMapsMutationResult = ClassVar['CreateMapsMutationResponse']


DeleteMapsParams = TypedDict('DeleteMapsParams', {
	'where': Optional['MapWhere'],
	'delete': Optional['MapDeleteInput'],
})


DeleteMapsMutationResult = ClassVar['DeleteInfo']


UpdateMapsParams = TypedDict('UpdateMapsParams', {
	'where': Optional['MapWhere'],
	'update': Optional['MapUpdateInput'],
	'connect': Optional['MapConnectInput'],
	'disconnect': Optional['MapDisconnectInput'],
	'create': Optional['MapRelationInput'],
	'delete': Optional['MapDeleteInput'],
	'connectOrCreate': Optional['MapConnectOrCreateInput'],
})


UpdateMapsMutationResult = ClassVar['UpdateMapsMutationResponse']


AddWorkflowsParams = TypedDict('AddWorkflowsParams', {
	'input': List['WorkflowCreateInput'],
})


AddWorkflowsMutationResult = ClassVar['CreateWorkflowsMutationResponse']


DeleteWorkflowsParams = TypedDict('DeleteWorkflowsParams', {
	'where': Optional['WorkflowWhere'],
	'delete': Optional['WorkflowDeleteInput'],
})


DeleteWorkflowsMutationResult = ClassVar['DeleteInfo']


UpdateWorkflowsParams = TypedDict('UpdateWorkflowsParams', {
	'where': Optional['WorkflowWhere'],
	'update': Optional['WorkflowUpdateInput'],
	'connect': Optional['WorkflowConnectInput'],
	'disconnect': Optional['WorkflowDisconnectInput'],
	'create': Optional['WorkflowRelationInput'],
	'delete': Optional['WorkflowDeleteInput'],
	'connectOrCreate': Optional['WorkflowConnectOrCreateInput'],
})


UpdateWorkflowsMutationResult = ClassVar['UpdateWorkflowsMutationResponse']


CreateUploadParams = TypedDict('CreateUploadParams', {
	'blob': 'BlobInput',
	'parts': Optional[int],
})


CreateUploadMutationResult = ClassVar[Optional['UploadInfo']]


AbortUploadParams = TypedDict('AbortUploadParams', {
	'blobId': str,
	'uploadId': str,
})


AbortUploadMutationResult = str


CompleteUploadParams = TypedDict('CompleteUploadParams', {
	'blobId': str,
	'completedUpload': 'CompletedUploadInput',
})


CompleteUploadMutationResult = str


DeleteBlobParams = TypedDict('DeleteBlobParams', {
	'blobId': str,
})


DeleteBlobMutationResult = str


CreateDownloadParams = TypedDict('CreateDownloadParams', {
	'blobId': str,
	'userId': Optional[str],
})


CreateDownloadMutationResult = str


Subscription = TypedDict('Subscription', {
	'eventChanged': 'EventChangedSubscriptionResult',
	'factorChanged': 'FactorChangedSubscriptionResult',
	'variableChanged': 'VariableChangedSubscriptionResult',
})


EventChangedParams = TypedDict('EventChangedParams', {
	'event': Optional['GetEventInput'],
})


EventChangedSubscriptionResult = ClassVar[Optional['Event']]


FactorChangedParams = TypedDict('FactorChangedParams', {
	'factor': Optional['GetFactorInput'],
})


FactorChangedSubscriptionResult = ClassVar[Optional['ComingSoon']]


VariableChangedParams = TypedDict('VariableChangedParams', {
	'variable': Optional['GetVariableInput'],
})


VariableChangedSubscriptionResult = ClassVar[Optional['ComingSoon']]


Hash = TypedDict('Hash', {
	'alg': Optional['HashAlgorithm'],
	'hash': Optional[str],
})


CartesianPoint = TypedDict('CartesianPoint', {
	'x': float,
	'y': float,
	'z': Optional[float],
	'rotx': Optional[float],
	'roty': Optional[float],
	'rotz': Optional[float],
})


Point = TypedDict('Point', {
	'latitude': float,
	'longitude': float,
	'height': Optional[float],
	'crs': str,
	'srid': int,
})


SolveEnvironmentAccepted = TypedDict('SolveEnvironmentAccepted', {
	'noop': Optional[str],
})


EventStatus = TypedDict('EventStatus', {
	'command': Optional['Command'],
	'nodeType': Optional['NodeType'],
	'state': Optional['State'],
	'progress': Optional[int],
	'details': Optional[str],
	'timestamp': Optional['DateTime'],
})


EventContext = TypedDict('EventContext', {
	'userId': str,
	'eventId': str,
	'connectionId': Optional[str],
})


Event = TypedDict('Event', {
	'status': Optional['EventStatus'],
	'context': Optional['EventContext'],
	'data': Optional['EventData'],
	'options': Optional['EventOptions'],
})


AddFactorTypedAccepted = TypedDict('AddFactorTypedAccepted', {
	'noop': Optional[str],
})


AddFactorPackedAccepted = TypedDict('AddFactorPackedAccepted', {
	'noop': Optional[str],
})


ImportSessionAccepted = TypedDict('ImportSessionAccepted', {
	'noop': Optional[str],
})


ImportSessionComplete = TypedDict('ImportSessionComplete', {
	'noop': Optional[str],
})


ExportSessionAccepted = TypedDict('ExportSessionAccepted', {
	'noop': Optional[str],
})


ExportSessionComplete = TypedDict('ExportSessionComplete', {
	'noop': Optional[str],
})


SolveSessionAccepted = TypedDict('SolveSessionAccepted', {
	'noop': Optional[str],
})


SolveSessionComplete = TypedDict('SolveSessionComplete', {
	'noop': Optional[str],
	'session': Optional['SessionId'],
})


SessionId = TypedDict('SessionId', {
	'id': Optional['UUID'],
	'key': Optional['SessionKey'],
})


SessionKey = TypedDict('SessionKey', {
	'userId': Optional[str],
	'robotId': Optional[str],
	'sessionId': Optional[str],
})


DeleteUserAccepted = TypedDict('DeleteUserAccepted', {
	'noop': Optional[str],
})


DeleteUserComplete = TypedDict('DeleteUserComplete', {
	'noop': Optional[str],
})


AddVariableTypedAccepted = TypedDict('AddVariableTypedAccepted', {
	'noop': Optional[str],
})


AddVariablePackedAccepted = TypedDict('AddVariablePackedAccepted', {
	'noop': Optional[str],
})


InitVariableAccepted = TypedDict('InitVariableAccepted', {
	'noop': Optional[str],
})


Affordance = TypedDict('Affordance', {
	'id': str,
	'label': str,
	'position': List[float],
	'rotation': List[float],
	'scale': List[float],
})


AffordanceAggregateSelection = TypedDict('AffordanceAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
})


AffordanceEdge = TypedDict('AffordanceEdge', {
	'cursor': str,
	'node': 'Affordance',
})


AffordancesConnection = TypedDict('AffordancesConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['AffordanceEdge'],
})


Annotation = TypedDict('Annotation', {
	'id': str,
	'text': str,
	'position': List[float],
})


AnnotationAggregateSelection = TypedDict('AnnotationAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'text': 'StringAggregateSelectionNonNullable',
})


AnnotationEdge = TypedDict('AnnotationEdge', {
	'cursor': str,
	'node': 'Annotation',
})


AnnotationsConnection = TypedDict('AnnotationsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['AnnotationEdge'],
})


BigIntAggregateSelectionNonNullable = TypedDict('BigIntAggregateSelectionNonNullable', {
	'max': 'BigInt',
	'min': 'BigInt',
	'average': 'BigInt',
	'sum': 'BigInt',
})


BigIntAggregateSelectionNullable = TypedDict('BigIntAggregateSelectionNullable', {
	'max': Optional['BigInt'],
	'min': Optional['BigInt'],
	'average': Optional['BigInt'],
	'sum': Optional['BigInt'],
})


BlobEntriesConnection = TypedDict('BlobEntriesConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['BlobEntryEdge'],
})


BlobEntry = TypedDict('BlobEntry', {
	'id': str,
	'blobId': str,
	'originId': str,
	'label': str,
	'description': Optional[str],
	'hash': Optional[str],
	'mimeType': Optional[str],
	'blobstore': Optional[str],
	'origin': Optional[str],
	'nstime': Optional['BigInt'],
	'_type': str,
	'_version': str,
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'variableLabel': Optional[str],
	'factorLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': Optional['DateTime'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'user': List['Variable'],
	'userAggregate': Optional['BlobEntryVariableUserAggregationSelection'],
	'robot': List['Robot'],
	'robotAggregate': Optional['BlobEntryRobotRobotAggregationSelection'],
	'session': List['Session'],
	'sessionAggregate': Optional['BlobEntrySessionSessionAggregationSelection'],
	'variable': List['Variable'],
	'variableAggregate': Optional['BlobEntryVariableVariableAggregationSelection'],
	'factor': List['Factor'],
	'factorAggregate': Optional['BlobEntryFactorFactorAggregationSelection'],
	'userConnection': 'BlobEntryUserConnection',
	'robotConnection': 'BlobEntryRobotConnection',
	'sessionConnection': 'BlobEntrySessionConnection',
	'variableConnection': 'BlobEntryVariableConnection',
	'factorConnection': 'BlobEntryFactorConnection',
})


BlobEntryAggregateSelection = TypedDict('BlobEntryAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'blobId': 'IDAggregateSelectionNonNullable',
	'originId': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'hash': 'StringAggregateSelectionNullable',
	'mimeType': 'StringAggregateSelectionNullable',
	'blobstore': 'StringAggregateSelectionNullable',
	'origin': 'StringAggregateSelectionNullable',
	'nstime': 'BigIntAggregateSelectionNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNullable',
	'robotLabel': 'StringAggregateSelectionNullable',
	'sessionLabel': 'StringAggregateSelectionNullable',
	'variableLabel': 'StringAggregateSelectionNullable',
	'factorLabel': 'StringAggregateSelectionNullable',
	'timestamp': 'DateTimeAggregateSelectionNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


BlobEntryEdge = TypedDict('BlobEntryEdge', {
	'cursor': str,
	'node': 'BlobEntry',
})


BlobEntryFactorConnection = TypedDict('BlobEntryFactorConnection', {
	'edges': List['BlobEntryFactorRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


BlobEntryFactorFactorAggregationSelection = TypedDict('BlobEntryFactorFactorAggregationSelection', {
	'count': int,
	'node': Optional['BlobEntryFactorFactorNodeAggregateSelection'],
})


BlobEntryFactorFactorNodeAggregateSelection = TypedDict('BlobEntryFactorFactorNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'fnctype': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'data': 'StringAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


BlobEntryFactorRelationship = TypedDict('BlobEntryFactorRelationship', {
	'cursor': str,
	'node': 'Factor',
})


BlobEntryRobotConnection = TypedDict('BlobEntryRobotConnection', {
	'edges': List['BlobEntryRobotRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


BlobEntryRobotRelationship = TypedDict('BlobEntryRobotRelationship', {
	'cursor': str,
	'node': 'Robot',
})


BlobEntryRobotRobotAggregationSelection = TypedDict('BlobEntryRobotRobotAggregationSelection', {
	'count': int,
	'node': Optional['BlobEntryRobotRobotNodeAggregateSelection'],
})


BlobEntryRobotRobotNodeAggregateSelection = TypedDict('BlobEntryRobotRobotNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


BlobEntrySessionConnection = TypedDict('BlobEntrySessionConnection', {
	'edges': List['BlobEntrySessionRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


BlobEntrySessionRelationship = TypedDict('BlobEntrySessionRelationship', {
	'cursor': str,
	'node': 'Session',
})


BlobEntrySessionSessionAggregationSelection = TypedDict('BlobEntrySessionSessionAggregationSelection', {
	'count': int,
	'node': Optional['BlobEntrySessionSessionNodeAggregateSelection'],
})


BlobEntrySessionSessionNodeAggregateSelection = TypedDict('BlobEntrySessionSessionNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


BlobEntryUserConnection = TypedDict('BlobEntryUserConnection', {
	'edges': List['BlobEntryUserRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


BlobEntryUserRelationship = TypedDict('BlobEntryUserRelationship', {
	'cursor': str,
	'node': 'Variable',
})


BlobEntryVariableConnection = TypedDict('BlobEntryVariableConnection', {
	'edges': List['BlobEntryVariableRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


BlobEntryVariableRelationship = TypedDict('BlobEntryVariableRelationship', {
	'cursor': str,
	'node': 'Variable',
})


BlobEntryVariableUserAggregationSelection = TypedDict('BlobEntryVariableUserAggregationSelection', {
	'count': int,
	'node': Optional['BlobEntryVariableUserNodeAggregateSelection'],
})


BlobEntryVariableUserNodeAggregateSelection = TypedDict('BlobEntryVariableUserNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


BlobEntryVariableVariableAggregationSelection = TypedDict('BlobEntryVariableVariableAggregationSelection', {
	'count': int,
	'node': Optional['BlobEntryVariableVariableNodeAggregateSelection'],
})


BlobEntryVariableVariableNodeAggregateSelection = TypedDict('BlobEntryVariableVariableNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


CreateAffordancesMutationResponse = TypedDict('CreateAffordancesMutationResponse', {
	'info': 'CreateInfo',
	'affordances': List['Affordance'],
})


CreateAnnotationsMutationResponse = TypedDict('CreateAnnotationsMutationResponse', {
	'info': 'CreateInfo',
	'annotations': List['Annotation'],
})


CreateBlobEntriesMutationResponse = TypedDict('CreateBlobEntriesMutationResponse', {
	'info': 'CreateInfo',
	'blobEntries': List['BlobEntry'],
})


CreateFactorsMutationResponse = TypedDict('CreateFactorsMutationResponse', {
	'info': 'CreateInfo',
	'factors': List['Factor'],
})


CreateInfo = TypedDict('CreateInfo', {
	'bookmark': Optional[str],
	'nodesCreated': int,
	'relationshipsCreated': int,
})


CreateMapsMutationResponse = TypedDict('CreateMapsMutationResponse', {
	'info': 'CreateInfo',
	'maps': List['Map'],
})


CreatePpesMutationResponse = TypedDict('CreatePpesMutationResponse', {
	'info': 'CreateInfo',
	'ppes': List['PPE'],
})


CreateRobotsMutationResponse = TypedDict('CreateRobotsMutationResponse', {
	'info': 'CreateInfo',
	'robots': List['Robot'],
})


CreateSessionsMutationResponse = TypedDict('CreateSessionsMutationResponse', {
	'info': 'CreateInfo',
	'sessions': List['Session'],
})


CreateSolverDataMutationResponse = TypedDict('CreateSolverDataMutationResponse', {
	'info': 'CreateInfo',
	'solverData': List['SolverData'],
})


CreateUserIdsMutationResponse = TypedDict('CreateUserIdsMutationResponse', {
	'info': 'CreateInfo',
	'userIds': List['UserId'],
})


CreateUsersMutationResponse = TypedDict('CreateUsersMutationResponse', {
	'info': 'CreateInfo',
	'users': List['User'],
})


CreateVariablesMutationResponse = TypedDict('CreateVariablesMutationResponse', {
	'info': 'CreateInfo',
	'variables': List['Variable'],
})


CreateVisualizationBlobsMutationResponse = TypedDict('CreateVisualizationBlobsMutationResponse', {
	'info': 'CreateInfo',
	'visualizationBlobs': List['VisualizationBlob'],
})


CreateWorkflowsMutationResponse = TypedDict('CreateWorkflowsMutationResponse', {
	'info': 'CreateInfo',
	'workflows': List['Workflow'],
})


DateTimeAggregateSelectionNonNullable = TypedDict('DateTimeAggregateSelectionNonNullable', {
	'min': 'DateTime',
	'max': 'DateTime',
})


DateTimeAggregateSelectionNullable = TypedDict('DateTimeAggregateSelectionNullable', {
	'min': Optional['DateTime'],
	'max': Optional['DateTime'],
})


DeleteInfo = TypedDict('DeleteInfo', {
	'bookmark': Optional[str],
	'nodesDeleted': int,
	'relationshipsDeleted': int,
})


Factor = TypedDict('Factor', {
	'id': str,
	'label': str,
	'tags': List[str],
	'nstime': 'BigInt',
	'fnctype': str,
	'solvable': int,
	'data': str,
	'_variableOrderSymbols': Optional[List[str]],
	'_type': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'sessionId': Optional[str],
	'robotId': Optional[str],
	'userId': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': 'DateTime',
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'variables': List['Variable'],
	'variablesAggregate': Optional['FactorVariableVariablesAggregationSelection'],
	'blobEntries': List['BlobEntry'],
	'blobEntriesAggregate': Optional['FactorBlobEntryBlobEntriesAggregationSelection'],
	'session': 'Session',
	'sessionAggregate': Optional['FactorSessionSessionAggregationSelection'],
	'variablesConnection': 'FactorVariablesConnection',
	'blobEntriesConnection': 'FactorBlobEntriesConnection',
	'sessionConnection': 'FactorSessionConnection',
})


FactorAggregateSelection = TypedDict('FactorAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'fnctype': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'data': 'StringAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


FactorBlobEntriesConnection = TypedDict('FactorBlobEntriesConnection', {
	'edges': List['FactorBlobEntriesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


FactorBlobEntriesRelationship = TypedDict('FactorBlobEntriesRelationship', {
	'cursor': str,
	'node': 'BlobEntry',
})


FactorBlobEntryBlobEntriesAggregationSelection = TypedDict('FactorBlobEntryBlobEntriesAggregationSelection', {
	'count': int,
	'node': Optional['FactorBlobEntryBlobEntriesNodeAggregateSelection'],
})


FactorBlobEntryBlobEntriesNodeAggregateSelection = TypedDict('FactorBlobEntryBlobEntriesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'blobId': 'IDAggregateSelectionNonNullable',
	'originId': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'hash': 'StringAggregateSelectionNullable',
	'mimeType': 'StringAggregateSelectionNullable',
	'blobstore': 'StringAggregateSelectionNullable',
	'origin': 'StringAggregateSelectionNullable',
	'nstime': 'BigIntAggregateSelectionNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNullable',
	'robotLabel': 'StringAggregateSelectionNullable',
	'sessionLabel': 'StringAggregateSelectionNullable',
	'variableLabel': 'StringAggregateSelectionNullable',
	'factorLabel': 'StringAggregateSelectionNullable',
	'timestamp': 'DateTimeAggregateSelectionNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


FactorEdge = TypedDict('FactorEdge', {
	'cursor': str,
	'node': 'Factor',
})


FactorsConnection = TypedDict('FactorsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['FactorEdge'],
})


FactorSessionConnection = TypedDict('FactorSessionConnection', {
	'edges': List['FactorSessionRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


FactorSessionRelationship = TypedDict('FactorSessionRelationship', {
	'cursor': str,
	'node': 'Session',
})


FactorSessionSessionAggregationSelection = TypedDict('FactorSessionSessionAggregationSelection', {
	'count': int,
	'node': Optional['FactorSessionSessionNodeAggregateSelection'],
})


FactorSessionSessionNodeAggregateSelection = TypedDict('FactorSessionSessionNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


FactorVariablesConnection = TypedDict('FactorVariablesConnection', {
	'edges': List['FactorVariablesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


FactorVariablesRelationship = TypedDict('FactorVariablesRelationship', {
	'cursor': str,
	'node': 'Variable',
})


FactorVariableVariablesAggregationSelection = TypedDict('FactorVariableVariablesAggregationSelection', {
	'count': int,
	'node': Optional['FactorVariableVariablesNodeAggregateSelection'],
})


FactorVariableVariablesNodeAggregateSelection = TypedDict('FactorVariableVariablesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


IDAggregateSelectionNonNullable = TypedDict('IDAggregateSelectionNonNullable', {
	'shortest': str,
	'longest': str,
})


IntAggregateSelectionNonNullable = TypedDict('IntAggregateSelectionNonNullable', {
	'max': int,
	'min': int,
	'average': float,
	'sum': int,
})


Map = TypedDict('Map', {
	'id': str,
	'label': str,
	'description': Optional[str],
	'status': str,
	'data': Optional['B64JSON'],
	'thumbnailId': Optional['UUID'],
	'exportedMapId': Optional['UUID'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'visualization': Optional['VisualizationBlob'],
	'visualizationAggregate': Optional['MapVisualizationBlobVisualizationAggregationSelection'],
	'annotations': List['Annotation'],
	'annotationsAggregate': Optional['MapAnnotationAnnotationsAggregationSelection'],
	'affordances': List['Affordance'],
	'affordancesAggregate': Optional['MapAffordanceAffordancesAggregationSelection'],
	'sessions': List['Session'],
	'sessionsAggregate': Optional['MapSessionSessionsAggregationSelection'],
	'users': List['User'],
	'usersAggregate': Optional['MapUserUsersAggregationSelection'],
	'workflows': List['Workflow'],
	'workflowsAggregate': Optional['MapWorkflowWorkflowsAggregationSelection'],
	'visualizationConnection': 'MapVisualizationConnection',
	'annotationsConnection': 'MapAnnotationsConnection',
	'affordancesConnection': 'MapAffordancesConnection',
	'sessionsConnection': 'MapSessionsConnection',
	'usersConnection': 'MapUsersConnection',
	'workflowsConnection': 'MapWorkflowsConnection',
})


MapAffordanceAffordancesAggregationSelection = TypedDict('MapAffordanceAffordancesAggregationSelection', {
	'count': int,
	'node': Optional['MapAffordanceAffordancesNodeAggregateSelection'],
})


MapAffordanceAffordancesNodeAggregateSelection = TypedDict('MapAffordanceAffordancesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
})


MapAffordancesConnection = TypedDict('MapAffordancesConnection', {
	'edges': List['MapAffordancesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


MapAffordancesRelationship = TypedDict('MapAffordancesRelationship', {
	'cursor': str,
	'node': 'Affordance',
})


MapAggregateSelection = TypedDict('MapAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


MapAnnotationAnnotationsAggregationSelection = TypedDict('MapAnnotationAnnotationsAggregationSelection', {
	'count': int,
	'node': Optional['MapAnnotationAnnotationsNodeAggregateSelection'],
})


MapAnnotationAnnotationsNodeAggregateSelection = TypedDict('MapAnnotationAnnotationsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'text': 'StringAggregateSelectionNonNullable',
})


MapAnnotationsConnection = TypedDict('MapAnnotationsConnection', {
	'edges': List['MapAnnotationsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


MapAnnotationsRelationship = TypedDict('MapAnnotationsRelationship', {
	'cursor': str,
	'node': 'Annotation',
})


MapEdge = TypedDict('MapEdge', {
	'cursor': str,
	'node': 'Map',
})


MapsConnection = TypedDict('MapsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['MapEdge'],
})


MapSessionsConnection = TypedDict('MapSessionsConnection', {
	'edges': List['MapSessionsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


MapSessionSessionsAggregationSelection = TypedDict('MapSessionSessionsAggregationSelection', {
	'count': int,
	'node': Optional['MapSessionSessionsNodeAggregateSelection'],
})


MapSessionSessionsNodeAggregateSelection = TypedDict('MapSessionSessionsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


MapSessionsRelationship = TypedDict('MapSessionsRelationship', {
	'cursor': str,
	'node': 'Session',
})


MapUsersConnection = TypedDict('MapUsersConnection', {
	'edges': List['MapUsersRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


MapUsersRelationship = TypedDict('MapUsersRelationship', {
	'cursor': str,
	'node': 'User',
	'role': str,
})


MapUserUsersAggregationSelection = TypedDict('MapUserUsersAggregationSelection', {
	'count': int,
	'node': Optional['MapUserUsersNodeAggregateSelection'],
	'edge': Optional['MapUserUsersEdgeAggregateSelection'],
})


MapUserUsersEdgeAggregateSelection = TypedDict('MapUserUsersEdgeAggregateSelection', {
	'role': 'StringAggregateSelectionNonNullable',
})


MapUserUsersNodeAggregateSelection = TypedDict('MapUserUsersNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'sub': 'StringAggregateSelectionNonNullable',
	'givenName': 'StringAggregateSelectionNonNullable',
	'familyName': 'StringAggregateSelectionNonNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastAuthenticatedTimestamp': 'DateTimeAggregateSelectionNullable',
})


MapVisualizationBlobVisualizationAggregationSelection = TypedDict('MapVisualizationBlobVisualizationAggregationSelection', {
	'count': int,
})


MapVisualizationConnection = TypedDict('MapVisualizationConnection', {
	'edges': List['MapVisualizationRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


MapVisualizationRelationship = TypedDict('MapVisualizationRelationship', {
	'cursor': str,
	'node': 'VisualizationBlob',
})


MapWorkflowsConnection = TypedDict('MapWorkflowsConnection', {
	'edges': List['MapWorkflowsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


MapWorkflowsRelationship = TypedDict('MapWorkflowsRelationship', {
	'cursor': str,
	'node': 'Workflow',
})


MapWorkflowWorkflowsAggregationSelection = TypedDict('MapWorkflowWorkflowsAggregationSelection', {
	'count': int,
	'node': Optional['MapWorkflowWorkflowsNodeAggregateSelection'],
})


MapWorkflowWorkflowsNodeAggregateSelection = TypedDict('MapWorkflowWorkflowsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


PageInfo = TypedDict('PageInfo', {
	'hasNextPage': bool,
	'hasPreviousPage': bool,
	'startCursor': Optional[str],
	'endCursor': Optional[str],
})


PPE = TypedDict('PPE', {
	'id': str,
	'solveKey': str,
	'suggested': Optional[List[float]],
	'max': Optional[List[float]],
	'mean': Optional[List[float]],
	'_type': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'variableLabel': str,
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'suggested_cartesian': Optional['Point'],
	'max_cartesian': Optional['Point'],
	'mean_cartesian': Optional['Point'],
	'variable': Optional['Variable'],
	'variableAggregate': Optional['PPEVariableVariableAggregationSelection'],
	'variableConnection': 'PPEVariableConnection',
})


PPEAggregateSelection = TypedDict('PPEAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'solveKey': 'IDAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'variableLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


PPEEdge = TypedDict('PPEEdge', {
	'cursor': str,
	'node': 'PPE',
})


PpesConnection = TypedDict('PpesConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['PPEEdge'],
})


PPEVariableConnection = TypedDict('PPEVariableConnection', {
	'edges': List['PPEVariableRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


PPEVariableRelationship = TypedDict('PPEVariableRelationship', {
	'cursor': str,
	'node': 'Variable',
})


PPEVariableVariableAggregationSelection = TypedDict('PPEVariableVariableAggregationSelection', {
	'count': int,
	'node': Optional['PPEVariableVariableNodeAggregateSelection'],
})


PPEVariableVariableNodeAggregateSelection = TypedDict('PPEVariableVariableNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


Robot = TypedDict('Robot', {
	'id': str,
	'label': str,
	'_version': str,
	'userLabel': str,
	'userId': Optional[str],
	'metadata': Optional['Metadata'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'sessions': List['Session'],
	'blobEntries': List['BlobEntry'],
	'blobEntriesAggregate': Optional['RobotBlobEntryBlobEntriesAggregationSelection'],
	'user': List['User'],
	'blobEntriesConnection': 'RobotBlobEntriesConnection',
})


RobotAggregateSelection = TypedDict('RobotAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


RobotBlobEntriesConnection = TypedDict('RobotBlobEntriesConnection', {
	'edges': List['RobotBlobEntriesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


RobotBlobEntriesRelationship = TypedDict('RobotBlobEntriesRelationship', {
	'cursor': str,
	'node': 'BlobEntry',
})


RobotBlobEntryBlobEntriesAggregationSelection = TypedDict('RobotBlobEntryBlobEntriesAggregationSelection', {
	'count': int,
	'node': Optional['RobotBlobEntryBlobEntriesNodeAggregateSelection'],
})


RobotBlobEntryBlobEntriesNodeAggregateSelection = TypedDict('RobotBlobEntryBlobEntriesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'blobId': 'IDAggregateSelectionNonNullable',
	'originId': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'hash': 'StringAggregateSelectionNullable',
	'mimeType': 'StringAggregateSelectionNullable',
	'blobstore': 'StringAggregateSelectionNullable',
	'origin': 'StringAggregateSelectionNullable',
	'nstime': 'BigIntAggregateSelectionNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNullable',
	'robotLabel': 'StringAggregateSelectionNullable',
	'sessionLabel': 'StringAggregateSelectionNullable',
	'variableLabel': 'StringAggregateSelectionNullable',
	'factorLabel': 'StringAggregateSelectionNullable',
	'timestamp': 'DateTimeAggregateSelectionNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


RobotEdge = TypedDict('RobotEdge', {
	'cursor': str,
	'node': 'Robot',
})


RobotsConnection = TypedDict('RobotsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['RobotEdge'],
})


RobotSessionsConnection = TypedDict('RobotSessionsConnection', {
	'edges': List['RobotSessionsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


RobotSessionSessionsAggregationSelection = TypedDict('RobotSessionSessionsAggregationSelection', {
	'count': int,
	'node': Optional['RobotSessionSessionsNodeAggregateSelection'],
})


RobotSessionSessionsNodeAggregateSelection = TypedDict('RobotSessionSessionsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


RobotSessionsRelationship = TypedDict('RobotSessionsRelationship', {
	'cursor': str,
	'node': 'Session',
})


RobotUserConnection = TypedDict('RobotUserConnection', {
	'edges': List['RobotUserRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


RobotUserRelationship = TypedDict('RobotUserRelationship', {
	'cursor': str,
	'node': 'User',
})


RobotUserUserAggregationSelection = TypedDict('RobotUserUserAggregationSelection', {
	'count': int,
	'node': Optional['RobotUserUserNodeAggregateSelection'],
})


RobotUserUserNodeAggregateSelection = TypedDict('RobotUserUserNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'sub': 'StringAggregateSelectionNonNullable',
	'givenName': 'StringAggregateSelectionNonNullable',
	'familyName': 'StringAggregateSelectionNonNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastAuthenticatedTimestamp': 'DateTimeAggregateSelectionNullable',
})


Session = TypedDict('Session', {
	'id': str,
	'label': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'robotId': Optional[str],
	'userId': Optional[str],
	'numVariables': Optional[int],
	'numFactors': Optional[int],
	'solveKeys': Optional[List[str]],
	'metadata': Optional['Metadata'],
	'originLatitude': Optional['Latitude'],
	'originLongitude': Optional['Longitude'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'robot': 'Robot',
	'variables': List['Variable'],
	'factors': List['Factor'],
	'blobEntries': List['BlobEntry'],
	'blobEntriesAggregate': Optional['SessionBlobEntryBlobEntriesAggregationSelection'],
	'blobEntriesConnection': 'SessionBlobEntriesConnection',
})


SessionAggregateSelection = TypedDict('SessionAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


SessionBlobEntriesConnection = TypedDict('SessionBlobEntriesConnection', {
	'edges': List['SessionBlobEntriesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


SessionBlobEntriesRelationship = TypedDict('SessionBlobEntriesRelationship', {
	'cursor': str,
	'node': 'BlobEntry',
})


SessionBlobEntryBlobEntriesAggregationSelection = TypedDict('SessionBlobEntryBlobEntriesAggregationSelection', {
	'count': int,
	'node': Optional['SessionBlobEntryBlobEntriesNodeAggregateSelection'],
})


SessionBlobEntryBlobEntriesNodeAggregateSelection = TypedDict('SessionBlobEntryBlobEntriesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'blobId': 'IDAggregateSelectionNonNullable',
	'originId': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'hash': 'StringAggregateSelectionNullable',
	'mimeType': 'StringAggregateSelectionNullable',
	'blobstore': 'StringAggregateSelectionNullable',
	'origin': 'StringAggregateSelectionNullable',
	'nstime': 'BigIntAggregateSelectionNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNullable',
	'robotLabel': 'StringAggregateSelectionNullable',
	'sessionLabel': 'StringAggregateSelectionNullable',
	'variableLabel': 'StringAggregateSelectionNullable',
	'factorLabel': 'StringAggregateSelectionNullable',
	'timestamp': 'DateTimeAggregateSelectionNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


SessionEdge = TypedDict('SessionEdge', {
	'cursor': str,
	'node': 'Session',
})


SessionFactorFactorsAggregationSelection = TypedDict('SessionFactorFactorsAggregationSelection', {
	'count': int,
	'node': Optional['SessionFactorFactorsNodeAggregateSelection'],
})


SessionFactorFactorsNodeAggregateSelection = TypedDict('SessionFactorFactorsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'fnctype': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'data': 'StringAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


SessionFactorsConnection = TypedDict('SessionFactorsConnection', {
	'edges': List['SessionFactorsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


SessionFactorsRelationship = TypedDict('SessionFactorsRelationship', {
	'cursor': str,
	'node': 'Factor',
})


SessionRobotConnection = TypedDict('SessionRobotConnection', {
	'edges': List['SessionRobotRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


SessionRobotRelationship = TypedDict('SessionRobotRelationship', {
	'cursor': str,
	'node': 'Robot',
})


SessionRobotRobotAggregationSelection = TypedDict('SessionRobotRobotAggregationSelection', {
	'count': int,
	'node': Optional['SessionRobotRobotNodeAggregateSelection'],
})


SessionRobotRobotNodeAggregateSelection = TypedDict('SessionRobotRobotNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


SessionsConnection = TypedDict('SessionsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['SessionEdge'],
})


SessionVariablesConnection = TypedDict('SessionVariablesConnection', {
	'edges': List['SessionVariablesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


SessionVariablesRelationship = TypedDict('SessionVariablesRelationship', {
	'cursor': str,
	'node': 'Variable',
})


SessionVariableVariablesAggregationSelection = TypedDict('SessionVariableVariablesAggregationSelection', {
	'count': int,
	'node': Optional['SessionVariableVariablesNodeAggregateSelection'],
})


SessionVariableVariablesNodeAggregateSelection = TypedDict('SessionVariableVariablesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


SolverData = TypedDict('SolverData', {
	'id': str,
	'solveKey': str,
	'BayesNetOutVertIDs': Optional[List[str]],
	'BayesNetVertID': Optional[str],
	'dimIDs': List[int],
	'dimbw': int,
	'dims': int,
	'dimval': int,
	'dontmargin': bool,
	'eliminated': bool,
	'infoPerCoord': List[float],
	'initialized': bool,
	'ismargin': bool,
	'separator': Optional[List[str]],
	'solveInProgress': int,
	'solvedCount': int,
	'variableType': str,
	'vecbw': Optional[List[float]],
	'vecval': Optional[List[float]],
	'covar': Optional[List[float]],
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'variableLabel': str,
	'ppe': Optional['PPE'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'variable': 'Variable',
	'variableAggregate': Optional['SolverDataVariableVariableAggregationSelection'],
	'variableConnection': 'SolverDataVariableConnection',
})


SolverDataAggregateSelection = TypedDict('SolverDataAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'solveKey': 'IDAggregateSelectionNonNullable',
	'BayesNetVertID': 'StringAggregateSelectionNullable',
	'dimbw': 'IntAggregateSelectionNonNullable',
	'dims': 'IntAggregateSelectionNonNullable',
	'dimval': 'IntAggregateSelectionNonNullable',
	'solveInProgress': 'IntAggregateSelectionNonNullable',
	'solvedCount': 'IntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'variableLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


SolverDataConnection = TypedDict('SolverDataConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['SolverDataEdge'],
})


SolverDataEdge = TypedDict('SolverDataEdge', {
	'cursor': str,
	'node': 'SolverData',
})


SolverDataVariableConnection = TypedDict('SolverDataVariableConnection', {
	'edges': List['SolverDataVariableRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


SolverDataVariableRelationship = TypedDict('SolverDataVariableRelationship', {
	'cursor': str,
	'node': 'Variable',
})


SolverDataVariableVariableAggregationSelection = TypedDict('SolverDataVariableVariableAggregationSelection', {
	'count': int,
	'node': Optional['SolverDataVariableVariableNodeAggregateSelection'],
})


SolverDataVariableVariableNodeAggregateSelection = TypedDict('SolverDataVariableVariableNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


StringAggregateSelectionNonNullable = TypedDict('StringAggregateSelectionNonNullable', {
	'shortest': str,
	'longest': str,
})


StringAggregateSelectionNullable = TypedDict('StringAggregateSelectionNullable', {
	'shortest': Optional[str],
	'longest': Optional[str],
})


UpdateAffordancesMutationResponse = TypedDict('UpdateAffordancesMutationResponse', {
	'info': 'UpdateInfo',
	'affordances': List['Affordance'],
})


UpdateAnnotationsMutationResponse = TypedDict('UpdateAnnotationsMutationResponse', {
	'info': 'UpdateInfo',
	'annotations': List['Annotation'],
})


UpdateBlobEntriesMutationResponse = TypedDict('UpdateBlobEntriesMutationResponse', {
	'info': 'UpdateInfo',
	'blobEntries': List['BlobEntry'],
})


UpdateFactorsMutationResponse = TypedDict('UpdateFactorsMutationResponse', {
	'info': 'UpdateInfo',
	'factors': List['Factor'],
})


UpdateInfo = TypedDict('UpdateInfo', {
	'bookmark': Optional[str],
	'nodesCreated': int,
	'nodesDeleted': int,
	'relationshipsCreated': int,
	'relationshipsDeleted': int,
})


UpdateMapsMutationResponse = TypedDict('UpdateMapsMutationResponse', {
	'info': 'UpdateInfo',
	'maps': List['Map'],
})


UpdatePpesMutationResponse = TypedDict('UpdatePpesMutationResponse', {
	'info': 'UpdateInfo',
	'ppes': List['PPE'],
})


UpdateRobotsMutationResponse = TypedDict('UpdateRobotsMutationResponse', {
	'info': 'UpdateInfo',
	'robots': List['Robot'],
})


UpdateSessionsMutationResponse = TypedDict('UpdateSessionsMutationResponse', {
	'info': 'UpdateInfo',
	'sessions': List['Session'],
})


UpdateSolverDataMutationResponse = TypedDict('UpdateSolverDataMutationResponse', {
	'info': 'UpdateInfo',
	'solverData': List['SolverData'],
})


UpdateUserIdsMutationResponse = TypedDict('UpdateUserIdsMutationResponse', {
	'info': 'UpdateInfo',
	'userIds': List['UserId'],
})


UpdateUsersMutationResponse = TypedDict('UpdateUsersMutationResponse', {
	'info': 'UpdateInfo',
	'users': List['User'],
})


UpdateVariablesMutationResponse = TypedDict('UpdateVariablesMutationResponse', {
	'info': 'UpdateInfo',
	'variables': List['Variable'],
})


UpdateVisualizationBlobsMutationResponse = TypedDict('UpdateVisualizationBlobsMutationResponse', {
	'info': 'UpdateInfo',
	'visualizationBlobs': List['VisualizationBlob'],
})


UpdateWorkflowsMutationResponse = TypedDict('UpdateWorkflowsMutationResponse', {
	'info': 'UpdateInfo',
	'workflows': List['Workflow'],
})


User = TypedDict('User', {
	'id': str,
	'sub': str,
	'givenName': str,
	'familyName': str,
	'status': str,
	'_version': str,
	'permissions': List[str],
	'label': 'EmailAddress',
	'metadata': Optional['Metadata'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'lastAuthenticatedTimestamp': Optional['DateTime'],
	'blobEntries': List['BlobEntry'],
	'blobEntriesAggregate': Optional['UserBlobEntryBlobEntriesAggregationSelection'],
	'robots': List['Robot'],
	'maps': List['Map'],
	'mapsAggregate': Optional['UserMapMapsAggregationSelection'],
	'blobEntriesConnection': 'UserBlobEntriesConnection',
	'mapsConnection': 'UserMapsConnection',
})


UserAggregateSelection = TypedDict('UserAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'sub': 'StringAggregateSelectionNonNullable',
	'givenName': 'StringAggregateSelectionNonNullable',
	'familyName': 'StringAggregateSelectionNonNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastAuthenticatedTimestamp': 'DateTimeAggregateSelectionNullable',
})


UserBlobEntriesConnection = TypedDict('UserBlobEntriesConnection', {
	'edges': List['UserBlobEntriesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


UserBlobEntriesRelationship = TypedDict('UserBlobEntriesRelationship', {
	'cursor': str,
	'node': 'BlobEntry',
})


UserBlobEntryBlobEntriesAggregationSelection = TypedDict('UserBlobEntryBlobEntriesAggregationSelection', {
	'count': int,
	'node': Optional['UserBlobEntryBlobEntriesNodeAggregateSelection'],
})


UserBlobEntryBlobEntriesNodeAggregateSelection = TypedDict('UserBlobEntryBlobEntriesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'blobId': 'IDAggregateSelectionNonNullable',
	'originId': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'hash': 'StringAggregateSelectionNullable',
	'mimeType': 'StringAggregateSelectionNullable',
	'blobstore': 'StringAggregateSelectionNullable',
	'origin': 'StringAggregateSelectionNullable',
	'nstime': 'BigIntAggregateSelectionNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNullable',
	'robotLabel': 'StringAggregateSelectionNullable',
	'sessionLabel': 'StringAggregateSelectionNullable',
	'variableLabel': 'StringAggregateSelectionNullable',
	'factorLabel': 'StringAggregateSelectionNullable',
	'timestamp': 'DateTimeAggregateSelectionNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


UserEdge = TypedDict('UserEdge', {
	'cursor': str,
	'node': 'User',
})


UserId = TypedDict('UserId', {
	'id': 'UUID',
})


UserIdAggregateSelection = TypedDict('UserIdAggregateSelection', {
	'count': int,
})


UserIdEdge = TypedDict('UserIdEdge', {
	'cursor': str,
	'node': 'UserId',
})


UserIdsConnection = TypedDict('UserIdsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['UserIdEdge'],
})


UserMapMapsAggregationSelection = TypedDict('UserMapMapsAggregationSelection', {
	'count': int,
	'node': Optional['UserMapMapsNodeAggregateSelection'],
	'edge': Optional['UserMapMapsEdgeAggregateSelection'],
})


UserMapMapsEdgeAggregateSelection = TypedDict('UserMapMapsEdgeAggregateSelection', {
	'role': 'StringAggregateSelectionNonNullable',
})


UserMapMapsNodeAggregateSelection = TypedDict('UserMapMapsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


UserMapsConnection = TypedDict('UserMapsConnection', {
	'edges': List['UserMapsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


UserMapsRelationship = TypedDict('UserMapsRelationship', {
	'cursor': str,
	'node': 'Map',
	'role': str,
})


UserRobotRobotsAggregationSelection = TypedDict('UserRobotRobotsAggregationSelection', {
	'count': int,
	'node': Optional['UserRobotRobotsNodeAggregateSelection'],
})


UserRobotRobotsNodeAggregateSelection = TypedDict('UserRobotRobotsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


UserRobotsConnection = TypedDict('UserRobotsConnection', {
	'edges': List['UserRobotsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


UserRobotsRelationship = TypedDict('UserRobotsRelationship', {
	'cursor': str,
	'node': 'Robot',
})


UsersConnection = TypedDict('UsersConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['UserEdge'],
})


Variable = TypedDict('Variable', {
	'id': str,
	'label': str,
	'nstime': 'BigInt',
	'variableType': str,
	'solvable': int,
	'tags': List[str],
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'sessionId': Optional[str],
	'robotId': Optional[str],
	'userId': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': 'DateTime',
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'ppes': List['PPE'],
	'ppesAggregate': Optional['VariablePPEPpesAggregationSelection'],
	'blobEntries': List['BlobEntry'],
	'blobEntriesAggregate': Optional['VariableBlobEntryBlobEntriesAggregationSelection'],
	'solverData': List['SolverData'],
	'solverDataAggregate': Optional['VariableSolverDataSolverDataAggregationSelection'],
	'factors': List['Factor'],
	'factorsAggregate': Optional['VariableFactorFactorsAggregationSelection'],
	'session': 'Session',
	'sessionAggregate': Optional['VariableSessionSessionAggregationSelection'],
	'ppesConnection': 'VariablePpesConnection',
	'blobEntriesConnection': 'VariableBlobEntriesConnection',
	'solverDataConnection': 'VariableSolverDataConnection',
	'factorsConnection': 'VariableFactorsConnection',
	'sessionConnection': 'VariableSessionConnection',
})


VariableAggregateSelection = TypedDict('VariableAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


VariableBlobEntriesConnection = TypedDict('VariableBlobEntriesConnection', {
	'edges': List['VariableBlobEntriesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


VariableBlobEntriesRelationship = TypedDict('VariableBlobEntriesRelationship', {
	'cursor': str,
	'node': 'BlobEntry',
})


VariableBlobEntryBlobEntriesAggregationSelection = TypedDict('VariableBlobEntryBlobEntriesAggregationSelection', {
	'count': int,
	'node': Optional['VariableBlobEntryBlobEntriesNodeAggregateSelection'],
})


VariableBlobEntryBlobEntriesNodeAggregateSelection = TypedDict('VariableBlobEntryBlobEntriesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'blobId': 'IDAggregateSelectionNonNullable',
	'originId': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'hash': 'StringAggregateSelectionNullable',
	'mimeType': 'StringAggregateSelectionNullable',
	'blobstore': 'StringAggregateSelectionNullable',
	'origin': 'StringAggregateSelectionNullable',
	'nstime': 'BigIntAggregateSelectionNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNullable',
	'robotLabel': 'StringAggregateSelectionNullable',
	'sessionLabel': 'StringAggregateSelectionNullable',
	'variableLabel': 'StringAggregateSelectionNullable',
	'factorLabel': 'StringAggregateSelectionNullable',
	'timestamp': 'DateTimeAggregateSelectionNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


VariableEdge = TypedDict('VariableEdge', {
	'cursor': str,
	'node': 'Variable',
})


VariableFactorFactorsAggregationSelection = TypedDict('VariableFactorFactorsAggregationSelection', {
	'count': int,
	'node': Optional['VariableFactorFactorsNodeAggregateSelection'],
})


VariableFactorFactorsNodeAggregateSelection = TypedDict('VariableFactorFactorsNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'nstime': 'BigIntAggregateSelectionNonNullable',
	'fnctype': 'StringAggregateSelectionNonNullable',
	'solvable': 'IntAggregateSelectionNonNullable',
	'data': 'StringAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'timestamp': 'DateTimeAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


VariableFactorsConnection = TypedDict('VariableFactorsConnection', {
	'edges': List['VariableFactorsRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


VariableFactorsRelationship = TypedDict('VariableFactorsRelationship', {
	'cursor': str,
	'node': 'Factor',
})


VariablePPEPpesAggregationSelection = TypedDict('VariablePPEPpesAggregationSelection', {
	'count': int,
	'node': Optional['VariablePPEPpesNodeAggregateSelection'],
})


VariablePPEPpesNodeAggregateSelection = TypedDict('VariablePPEPpesNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'solveKey': 'IDAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'variableLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


VariablePpesConnection = TypedDict('VariablePpesConnection', {
	'edges': List['VariablePpesRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


VariablePpesRelationship = TypedDict('VariablePpesRelationship', {
	'cursor': str,
	'node': 'PPE',
})


VariablesConnection = TypedDict('VariablesConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['VariableEdge'],
})


VariableSessionConnection = TypedDict('VariableSessionConnection', {
	'edges': List['VariableSessionRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


VariableSessionRelationship = TypedDict('VariableSessionRelationship', {
	'cursor': str,
	'node': 'Session',
})


VariableSessionSessionAggregationSelection = TypedDict('VariableSessionSessionAggregationSelection', {
	'count': int,
	'node': Optional['VariableSessionSessionNodeAggregateSelection'],
})


VariableSessionSessionNodeAggregateSelection = TypedDict('VariableSessionSessionNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


VariableSolverDataConnection = TypedDict('VariableSolverDataConnection', {
	'edges': List['VariableSolverDataRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


VariableSolverDataRelationship = TypedDict('VariableSolverDataRelationship', {
	'cursor': str,
	'node': 'SolverData',
})


VariableSolverDataSolverDataAggregationSelection = TypedDict('VariableSolverDataSolverDataAggregationSelection', {
	'count': int,
	'node': Optional['VariableSolverDataSolverDataNodeAggregateSelection'],
})


VariableSolverDataSolverDataNodeAggregateSelection = TypedDict('VariableSolverDataSolverDataNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'solveKey': 'IDAggregateSelectionNonNullable',
	'BayesNetVertID': 'StringAggregateSelectionNullable',
	'dimbw': 'IntAggregateSelectionNonNullable',
	'dims': 'IntAggregateSelectionNonNullable',
	'dimval': 'IntAggregateSelectionNonNullable',
	'solveInProgress': 'IntAggregateSelectionNonNullable',
	'solvedCount': 'IntAggregateSelectionNonNullable',
	'variableType': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'userLabel': 'StringAggregateSelectionNonNullable',
	'robotLabel': 'StringAggregateSelectionNonNullable',
	'sessionLabel': 'StringAggregateSelectionNonNullable',
	'variableLabel': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


VisualizationBlob = TypedDict('VisualizationBlob', {
	'hierarchyId': Optional['UUID'],
	'octreeId': Optional['UUID'],
	'metadataId': Optional['UUID'],
})


VisualizationBlobAggregateSelection = TypedDict('VisualizationBlobAggregateSelection', {
	'count': int,
})


VisualizationBlobEdge = TypedDict('VisualizationBlobEdge', {
	'cursor': str,
	'node': 'VisualizationBlob',
})


VisualizationBlobsConnection = TypedDict('VisualizationBlobsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['VisualizationBlobEdge'],
})


Workflow = TypedDict('Workflow', {
	'id': str,
	'label': str,
	'description': Optional[str],
	'status': str,
	'_type': str,
	'_version': str,
	'data': Optional['B64JSON'],
	'result': Optional['B64JSON'],
	'createdTimestamp': 'DateTime',
	'lastUpdatedTimestamp': 'DateTime',
	'createdBy': 'User',
	'createdByAggregate': Optional['WorkflowUserCreatedByAggregationSelection'],
	'map': 'Map',
	'mapAggregate': Optional['WorkflowMapMapAggregationSelection'],
	'createdByConnection': 'WorkflowCreatedByConnection',
	'mapConnection': 'WorkflowMapConnection',
})


WorkflowAggregateSelection = TypedDict('WorkflowAggregateSelection', {
	'count': int,
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'_type': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


WorkflowCreatedByConnection = TypedDict('WorkflowCreatedByConnection', {
	'edges': List['WorkflowCreatedByRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


WorkflowCreatedByRelationship = TypedDict('WorkflowCreatedByRelationship', {
	'cursor': str,
	'node': 'User',
})


WorkflowEdge = TypedDict('WorkflowEdge', {
	'cursor': str,
	'node': 'Workflow',
})


WorkflowMapConnection = TypedDict('WorkflowMapConnection', {
	'edges': List['WorkflowMapRelationship'],
	'totalCount': int,
	'pageInfo': 'PageInfo',
})


WorkflowMapMapAggregationSelection = TypedDict('WorkflowMapMapAggregationSelection', {
	'count': int,
	'node': Optional['WorkflowMapMapNodeAggregateSelection'],
})


WorkflowMapMapNodeAggregateSelection = TypedDict('WorkflowMapMapNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'label': 'StringAggregateSelectionNonNullable',
	'description': 'StringAggregateSelectionNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
})


WorkflowMapRelationship = TypedDict('WorkflowMapRelationship', {
	'cursor': str,
	'node': 'Map',
})


WorkflowsConnection = TypedDict('WorkflowsConnection', {
	'totalCount': int,
	'pageInfo': 'PageInfo',
	'edges': List['WorkflowEdge'],
})


WorkflowUserCreatedByAggregationSelection = TypedDict('WorkflowUserCreatedByAggregationSelection', {
	'count': int,
	'node': Optional['WorkflowUserCreatedByNodeAggregateSelection'],
})


WorkflowUserCreatedByNodeAggregateSelection = TypedDict('WorkflowUserCreatedByNodeAggregateSelection', {
	'id': 'IDAggregateSelectionNonNullable',
	'sub': 'StringAggregateSelectionNonNullable',
	'givenName': 'StringAggregateSelectionNonNullable',
	'familyName': 'StringAggregateSelectionNonNullable',
	'status': 'StringAggregateSelectionNonNullable',
	'_version': 'StringAggregateSelectionNonNullable',
	'createdTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastUpdatedTimestamp': 'DateTimeAggregateSelectionNonNullable',
	'lastAuthenticatedTimestamp': 'DateTimeAggregateSelectionNullable',
})


Blob = TypedDict('Blob', {
	'id': str,
	'name': str,
	'size': Optional['BigInt'],
	'createdTimestamp': Optional[str],
})


UploadPart = TypedDict('UploadPart', {
	'partNumber': int,
	'url': Optional[str],
})


UploadInfo = TypedDict('UploadInfo', {
	'uploadId': str,
	'parts': List['UploadPart'],
	'blob': 'Blob',
	'expiration': Optional[str],
})


AgentIdInput = TypedDict('AgentIdInput', {
	'id': Optional['UUID'],
	'key': Optional['AgentKeyInput'],
})


RobotIdInput = TypedDict('RobotIdInput', {
	'id': Optional['UUID'],
	'key': Optional['RobotKeyInput'],
})


AgentKeyInput = TypedDict('AgentKeyInput', {
	'userLabel': str,
	'agentLabel': str,
})


RobotKeyInput = TypedDict('RobotKeyInput', {
	'userLabel': str,
	'robotLabel': str,
})


DeleteAgentInput = TypedDict('DeleteAgentInput', {
	'id': 'AgentIdInput',
})


DeleteRobotInput = TypedDict('DeleteRobotInput', {
	'id': 'RobotIdInput',
})


DeleteAgentOptionsInput = TypedDict('DeleteAgentOptionsInput', {
	'noop': Optional[str],
})


DeleteRobotOptionsInput = TypedDict('DeleteRobotOptionsInput', {
	'noop': Optional[str],
})


AuthUser = TypedDict('AuthUser', {
	'sub': str,
	'given_name': str,
	'family_name': str,
	'email': str,
	'iss': Optional[str],
	'iat': Optional[int],
	'exp': Optional[int],
	'aud': Optional[str],
})


CartesianPointInput = TypedDict('CartesianPointInput', {
	'x': float,
	'y': float,
	'z': Optional[float],
	'rotx': Optional[float],
	'roty': Optional[float],
	'rotz': Optional[float],
})


EmptyOptionsInput = TypedDict('EmptyOptionsInput', {
	'noop': Optional[str],
})


DistributionInput = TypedDict('DistributionInput', {
	'particle': Optional['ParticleInput'],
	'rayleigh': Optional['RayleighInput'],
})


ParticleInput = TypedDict('ParticleInput', {
	'points': Optional[List['CartesianPointInput']],
})


RayleighInput = TypedDict('RayleighInput', {
	'sigma': float,
})


FullNormalInput = TypedDict('FullNormalInput', {
	'mu': float,
	'cov': 'ComingSoon',
})


SolveEnvironmentInput = TypedDict('SolveEnvironmentInput', {
	'sessions': List['SessionIdInput'],
	'tags': Optional[List[str]],
})


SolveEnvironmentOptionsInput = TypedDict('SolveEnvironmentOptionsInput', {
	'noop': Optional[str],
})


EventStatusFilterInput = TypedDict('EventStatusFilterInput', {
	'state': Optional['State'],
	'command': Optional['Command'],
	'nodeType': Optional['NodeType'],
	'timestamp_GT': Optional['DateTime'],
})


EventContextFilterInput = TypedDict('EventContextFilterInput', {
	'eventId': Optional[str],
})


EventDataFilterInput = TypedDict('EventDataFilterInput', {
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
})


GetEventInput = TypedDict('GetEventInput', {
	'status': Optional['EventStatusFilterInput'],
	'context': Optional['EventContextFilterInput'],
	'data': Optional['EventDataFilterInput'],
})


GetEventOptionsInput = TypedDict('GetEventOptionsInput', {
	'limit': Optional[int],
	'offset': Optional[int],
})


FactorKeyInput = TypedDict('FactorKeyInput', {
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'factorLabel': str,
})


FactorIdInput = TypedDict('FactorIdInput', {
	'id': Optional['UUID'],
	'key': Optional['FactorKeyInput'],
})


AddFactorPackedInput = TypedDict('AddFactorPackedInput', {
	'session': 'SessionIdInput',
	'packedData': 'B64JSON',
})


AddFactorPackedOptionsInput = TypedDict('AddFactorPackedOptionsInput', {
	'force': Optional[bool],
})


UpdateFactorPackedInput = TypedDict('UpdateFactorPackedInput', {
	'session': 'SessionIdInput',
	'packedData': 'B64JSON',
})


UpdateFactorPackedOptionsInput = TypedDict('UpdateFactorPackedOptionsInput', {
	'force': Optional[bool],
})


AddFactorTypedOptionsInput = TypedDict('AddFactorTypedOptionsInput', {
	'force': Optional[bool],
})


Pose2Pose2Input = TypedDict('Pose2Pose2Input', {
	'noop': Optional[str],
})


FactorInput = TypedDict('FactorInput', {
	'pose2pose2': Optional['Pose2Pose2Input'],
})


AddFactorTypedInput = TypedDict('AddFactorTypedInput', {
	'session': 'SessionIdInput',
	'factorType': 'FactorType',
	'factor': 'FactorInput',
})


UpdateFactorInput = TypedDict('UpdateFactorInput', {
	'id': 'FactorIdInput',
	'factorType': 'FactorType',
	'factor': 'FactorInput',
})


UpdateFactorOptionsInput = TypedDict('UpdateFactorOptionsInput', {
	'force': Optional[bool],
})


DeleteFactorInput = TypedDict('DeleteFactorInput', {
	'id': 'FactorIdInput',
})


DeleteFactorOptionsInput = TypedDict('DeleteFactorOptionsInput', {
	'noop': Optional[str],
})


GetFactorInput = TypedDict('GetFactorInput', {
	'sessionKey': 'SessionKeyInput',
	'label': str,
	'factorType': 'FactorType',
})


GetFactorOptionsInput = TypedDict('GetFactorOptionsInput', {
	'limit': Optional[int],
	'offset': Optional[int],
})


NodeInput = TypedDict('NodeInput', {
	'label': Optional[str],
})


NodeIdInput = TypedDict('NodeIdInput', {
	'id': Optional['UUID'],
	'key': Optional['NodeKeyInput'],
})


NodeKeyInput = TypedDict('NodeKeyInput', {
	'user': Optional['UserKeyInput'],
	'variable': Optional['VariableKeyInput'],
})


AddNodesInput = TypedDict('AddNodesInput', {
	'variables': Optional[List['AddVariableTypedInput']],
	'variablesPacked': Optional[List['AddVariablePackedInput']],
	'factors': Optional[List['AddFactorTypedInput']],
	'factorsPacked': Optional[List['AddFactorPackedInput']],
})


AddNodesOptionsInput = TypedDict('AddNodesOptionsInput', {
	'parallelize': Optional[bool],
})


MetadataValueInput = TypedDict('MetadataValueInput', {
	'string': Optional[str],
	'int': Optional[int],
	'float': Optional[float],
	'datetime': Optional['DateTime'],
})


MetadataInput = TypedDict('MetadataInput', {
	'key': str,
	'value': List['MetadataValueInput'],
})


SessionIdInput = TypedDict('SessionIdInput', {
	'id': Optional['UUID'],
	'key': Optional['SessionKeyInput'],
})


SessionKeyInput = TypedDict('SessionKeyInput', {
	'userId': str,
	'robotId': str,
	'sessionId': str,
})


ImportSessionInput = TypedDict('ImportSessionInput', {
	'id': 'SessionIdInput',
	'filename': str,
	'blobId': 'UUID',
})


Ros1Topic = TypedDict('Ros1Topic', {
	'topic': str,
	'type': str,
	'keyframe': Optional[int],
	'maxIterations': Optional[int],
})


ImportSessionOptionsInput = TypedDict('ImportSessionOptionsInput', {
	'format': Optional['BagFormat'],
	'topics': Optional[List['Ros1Topic']],
})


ExportSessionInput = TypedDict('ExportSessionInput', {
	'id': 'SessionIdInput',
	'filename': str,
})


ExportSessionOptionsInput = TypedDict('ExportSessionOptionsInput', {
	'format': Optional['BagFormat'],
})


SolveSessionInput = TypedDict('SolveSessionInput', {
	'id': 'SessionIdInput',
})


SolveSessionOptionsInput = TypedDict('SolveSessionOptionsInput', {
	'key': Optional[str],
	'parametric': Optional[bool],
})


DeleteSessionInput = TypedDict('DeleteSessionInput', {
	'id': 'SessionIdInput',
})


DeleteSessionOptionsInput = TypedDict('DeleteSessionOptionsInput', {
	'noop': Optional[str],
})


UserIdInput = TypedDict('UserIdInput', {
	'id': Optional['UUID'],
	'key': Optional['UserKeyInput'],
})


UserKeyInput = TypedDict('UserKeyInput', {
	'userLabel': str,
})


DeleteUserInput = TypedDict('DeleteUserInput', {
	'id': 'UserIdInput',
})


DeleteUserOptionsInput = TypedDict('DeleteUserOptionsInput', {
	'noop': Optional[str],
})


VariableIdInput = TypedDict('VariableIdInput', {
	'id': Optional['UUID'],
	'key': Optional['VariableKeyInput'],
})


VariableKeyInput = TypedDict('VariableKeyInput', {
	'userId': str,
	'robotId': str,
	'sessionId': str,
	'variableLabel': str,
})


AddVariablePackedInput = TypedDict('AddVariablePackedInput', {
	'session': 'SessionIdInput',
	'packedData': 'B64JSON',
})


AddVariablePackedOptionsInput = TypedDict('AddVariablePackedOptionsInput', {
	'force': Optional[bool],
})


AddVariableTypedInput = TypedDict('AddVariableTypedInput', {
	'label': str,
	'variableType': 'VariableType',
	'session': 'SessionIdInput',
})


InitVariableInput = TypedDict('InitVariableInput', {
	'id': 'VariableIdInput',
	'variableType': 'VariableType',
	'distribution': 'DistributionInput',
	'bandwidth': Optional[List[float]],
})


UpdateVariableInput = TypedDict('UpdateVariableInput', {
	'noop': Optional['ComingSoon'],
})


UpdateVariableOptionsInput = TypedDict('UpdateVariableOptionsInput', {
	'force': Optional[bool],
})


DeleteVariableInput = TypedDict('DeleteVariableInput', {
	'id': 'VariableIdInput',
})


DeleteVariableOptionsInput = TypedDict('DeleteVariableOptionsInput', {
	'noop': Optional[str],
})


GetVariableInput = TypedDict('GetVariableInput', {
	'id': 'VariableIdInput',
})


GetVariableOptionsInput = TypedDict('GetVariableOptionsInput', {
	'limit': Optional[int],
	'offset': Optional[int],
})


AffordanceConnectOrCreateWhere = TypedDict('AffordanceConnectOrCreateWhere', {
	'node': 'AffordanceUniqueWhere',
})


AffordanceConnectWhere = TypedDict('AffordanceConnectWhere', {
	'node': 'AffordanceWhere',
})


AffordanceCreateInput = TypedDict('AffordanceCreateInput', {
	'label': str,
	'position': List[float],
	'rotation': List[float],
	'scale': List[float],
})


AffordanceOnCreateInput = TypedDict('AffordanceOnCreateInput', {
	'label': str,
	'position': List[float],
	'rotation': List[float],
	'scale': List[float],
})


AffordanceOptions = TypedDict('AffordanceOptions', {
	'sort': Optional[List['AffordanceSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


AffordanceSort = TypedDict('AffordanceSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
})


AffordanceUniqueWhere = TypedDict('AffordanceUniqueWhere', {
	'id': Optional[str],
})


AffordanceUpdateInput = TypedDict('AffordanceUpdateInput', {
	'label': Optional[str],
	'position': Optional[List[float]],
	'rotation': Optional[List[float]],
	'scale': Optional[List[float]],
	'position_POP': Optional[int],
	'position_PUSH': Optional[List[float]],
	'rotation_POP': Optional[int],
	'rotation_PUSH': Optional[List[float]],
	'scale_POP': Optional[int],
	'scale_PUSH': Optional[List[float]],
})


AffordanceWhere = TypedDict('AffordanceWhere', {
	'OR': Optional[List['AffordanceWhere']],
	'AND': Optional[List['AffordanceWhere']],
	'NOT': Optional['AffordanceWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'position': Optional[List[float]],
	'position_INCLUDES': Optional[float],
	'rotation': Optional[List[float]],
	'rotation_INCLUDES': Optional[float],
	'scale': Optional[List[float]],
	'scale_INCLUDES': Optional[float],
})


AnnotationConnectOrCreateWhere = TypedDict('AnnotationConnectOrCreateWhere', {
	'node': 'AnnotationUniqueWhere',
})


AnnotationConnectWhere = TypedDict('AnnotationConnectWhere', {
	'node': 'AnnotationWhere',
})


AnnotationCreateInput = TypedDict('AnnotationCreateInput', {
	'text': str,
	'position': List[float],
})


AnnotationOnCreateInput = TypedDict('AnnotationOnCreateInput', {
	'text': str,
	'position': List[float],
})


AnnotationOptions = TypedDict('AnnotationOptions', {
	'sort': Optional[List['AnnotationSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


AnnotationSort = TypedDict('AnnotationSort', {
	'id': Optional['SortDirection'],
	'text': Optional['SortDirection'],
})


AnnotationUniqueWhere = TypedDict('AnnotationUniqueWhere', {
	'id': Optional[str],
})


AnnotationUpdateInput = TypedDict('AnnotationUpdateInput', {
	'text': Optional[str],
	'position': Optional[List[float]],
	'position_POP': Optional[int],
	'position_PUSH': Optional[List[float]],
})


AnnotationWhere = TypedDict('AnnotationWhere', {
	'OR': Optional[List['AnnotationWhere']],
	'AND': Optional[List['AnnotationWhere']],
	'NOT': Optional['AnnotationWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'text': Optional[str],
	'text_IN': Optional[List[str]],
	'text_MATCHES': Optional[str],
	'text_CONTAINS': Optional[str],
	'text_STARTS_WITH': Optional[str],
	'text_ENDS_WITH': Optional[str],
	'position': Optional[List[float]],
	'position_INCLUDES': Optional[float],
})


BlobEntryConnectInput = TypedDict('BlobEntryConnectInput', {
	'user': Optional[List['BlobEntryUserConnectFieldInput']],
	'robot': Optional[List['BlobEntryRobotConnectFieldInput']],
	'session': Optional[List['BlobEntrySessionConnectFieldInput']],
	'variable': Optional[List['BlobEntryVariableConnectFieldInput']],
	'factor': Optional[List['BlobEntryFactorConnectFieldInput']],
})


BlobEntryConnectOrCreateInput = TypedDict('BlobEntryConnectOrCreateInput', {
	'user': Optional[List['BlobEntryUserConnectOrCreateFieldInput']],
	'robot': Optional[List['BlobEntryRobotConnectOrCreateFieldInput']],
	'session': Optional[List['BlobEntrySessionConnectOrCreateFieldInput']],
	'variable': Optional[List['BlobEntryVariableConnectOrCreateFieldInput']],
	'factor': Optional[List['BlobEntryFactorConnectOrCreateFieldInput']],
})


BlobEntryConnectOrCreateWhere = TypedDict('BlobEntryConnectOrCreateWhere', {
	'node': 'BlobEntryUniqueWhere',
})


BlobEntryConnectWhere = TypedDict('BlobEntryConnectWhere', {
	'node': 'BlobEntryWhere',
})


BlobEntryCreateInput = TypedDict('BlobEntryCreateInput', {
	'blobId': str,
	'originId': str,
	'label': str,
	'description': Optional[str],
	'hash': Optional[str],
	'mimeType': Optional[str],
	'blobstore': Optional[str],
	'origin': Optional[str],
	'nstime': Optional['BigInt'],
	'_type': str,
	'_version': str,
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'variableLabel': Optional[str],
	'factorLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': Optional['DateTime'],
	'user': Optional['BlobEntryUserFieldInput'],
	'robot': Optional['BlobEntryRobotFieldInput'],
	'session': Optional['BlobEntrySessionFieldInput'],
	'variable': Optional['BlobEntryVariableFieldInput'],
	'factor': Optional['BlobEntryFactorFieldInput'],
})


BlobEntryDeleteInput = TypedDict('BlobEntryDeleteInput', {
	'user': Optional[List['BlobEntryUserDeleteFieldInput']],
	'robot': Optional[List['BlobEntryRobotDeleteFieldInput']],
	'session': Optional[List['BlobEntrySessionDeleteFieldInput']],
	'variable': Optional[List['BlobEntryVariableDeleteFieldInput']],
	'factor': Optional[List['BlobEntryFactorDeleteFieldInput']],
})


BlobEntryDisconnectInput = TypedDict('BlobEntryDisconnectInput', {
	'user': Optional[List['BlobEntryUserDisconnectFieldInput']],
	'robot': Optional[List['BlobEntryRobotDisconnectFieldInput']],
	'session': Optional[List['BlobEntrySessionDisconnectFieldInput']],
	'variable': Optional[List['BlobEntryVariableDisconnectFieldInput']],
	'factor': Optional[List['BlobEntryFactorDisconnectFieldInput']],
})


BlobEntryFactorAggregateInput = TypedDict('BlobEntryFactorAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['BlobEntryFactorAggregateInput']],
	'OR': Optional[List['BlobEntryFactorAggregateInput']],
	'NOT': Optional['BlobEntryFactorAggregateInput'],
	'node': Optional['BlobEntryFactorNodeAggregationWhereInput'],
})


BlobEntryFactorConnectFieldInput = TypedDict('BlobEntryFactorConnectFieldInput', {
	'where': Optional['FactorConnectWhere'],
	'connect': Optional[List['FactorConnectInput']],
	'overwrite': bool,
})


BlobEntryFactorConnectionSort = TypedDict('BlobEntryFactorConnectionSort', {
	'node': Optional['FactorSort'],
})


BlobEntryFactorConnectionWhere = TypedDict('BlobEntryFactorConnectionWhere', {
	'AND': Optional[List['BlobEntryFactorConnectionWhere']],
	'OR': Optional[List['BlobEntryFactorConnectionWhere']],
	'NOT': Optional['BlobEntryFactorConnectionWhere'],
	'node': Optional['FactorWhere'],
})


BlobEntryFactorConnectOrCreateFieldInput = TypedDict('BlobEntryFactorConnectOrCreateFieldInput', {
	'where': 'FactorConnectOrCreateWhere',
	'onCreate': 'BlobEntryFactorConnectOrCreateFieldInputOnCreate',
})


BlobEntryFactorConnectOrCreateFieldInputOnCreate = TypedDict('BlobEntryFactorConnectOrCreateFieldInputOnCreate', {
	'node': 'FactorOnCreateInput',
})


BlobEntryFactorCreateFieldInput = TypedDict('BlobEntryFactorCreateFieldInput', {
	'node': 'FactorCreateInput',
})


BlobEntryFactorDeleteFieldInput = TypedDict('BlobEntryFactorDeleteFieldInput', {
	'where': Optional['BlobEntryFactorConnectionWhere'],
	'delete': Optional['FactorDeleteInput'],
})


BlobEntryFactorDisconnectFieldInput = TypedDict('BlobEntryFactorDisconnectFieldInput', {
	'where': Optional['BlobEntryFactorConnectionWhere'],
	'disconnect': Optional['FactorDisconnectInput'],
})


BlobEntryFactorFieldInput = TypedDict('BlobEntryFactorFieldInput', {
	'create': Optional[List['BlobEntryFactorCreateFieldInput']],
	'connect': Optional[List['BlobEntryFactorConnectFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryFactorConnectOrCreateFieldInput']],
})


BlobEntryFactorNodeAggregationWhereInput = TypedDict('BlobEntryFactorNodeAggregationWhereInput', {
	'AND': Optional[List['BlobEntryFactorNodeAggregationWhereInput']],
	'OR': Optional[List['BlobEntryFactorNodeAggregationWhereInput']],
	'NOT': Optional['BlobEntryFactorNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'fnctype_AVERAGE_LENGTH_EQUAL': Optional[float],
	'fnctype_LONGEST_LENGTH_EQUAL': Optional[int],
	'fnctype_SHORTEST_LENGTH_EQUAL': Optional[int],
	'fnctype_AVERAGE_LENGTH_GT': Optional[float],
	'fnctype_LONGEST_LENGTH_GT': Optional[int],
	'fnctype_SHORTEST_LENGTH_GT': Optional[int],
	'fnctype_AVERAGE_LENGTH_GTE': Optional[float],
	'fnctype_LONGEST_LENGTH_GTE': Optional[int],
	'fnctype_SHORTEST_LENGTH_GTE': Optional[int],
	'fnctype_AVERAGE_LENGTH_LT': Optional[float],
	'fnctype_LONGEST_LENGTH_LT': Optional[int],
	'fnctype_SHORTEST_LENGTH_LT': Optional[int],
	'fnctype_AVERAGE_LENGTH_LTE': Optional[float],
	'fnctype_LONGEST_LENGTH_LTE': Optional[int],
	'fnctype_SHORTEST_LENGTH_LTE': Optional[int],
	'data_AVERAGE_LENGTH_EQUAL': Optional[float],
	'data_LONGEST_LENGTH_EQUAL': Optional[int],
	'data_SHORTEST_LENGTH_EQUAL': Optional[int],
	'data_AVERAGE_LENGTH_GT': Optional[float],
	'data_LONGEST_LENGTH_GT': Optional[int],
	'data_SHORTEST_LENGTH_GT': Optional[int],
	'data_AVERAGE_LENGTH_GTE': Optional[float],
	'data_LONGEST_LENGTH_GTE': Optional[int],
	'data_SHORTEST_LENGTH_GTE': Optional[int],
	'data_AVERAGE_LENGTH_LT': Optional[float],
	'data_LONGEST_LENGTH_LT': Optional[int],
	'data_SHORTEST_LENGTH_LT': Optional[int],
	'data_AVERAGE_LENGTH_LTE': Optional[float],
	'data_LONGEST_LENGTH_LTE': Optional[int],
	'data_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


BlobEntryFactorUpdateConnectionInput = TypedDict('BlobEntryFactorUpdateConnectionInput', {
	'node': Optional['FactorUpdateInput'],
})


BlobEntryFactorUpdateFieldInput = TypedDict('BlobEntryFactorUpdateFieldInput', {
	'where': Optional['BlobEntryFactorConnectionWhere'],
	'update': Optional['BlobEntryFactorUpdateConnectionInput'],
	'connect': Optional[List['BlobEntryFactorConnectFieldInput']],
	'disconnect': Optional[List['BlobEntryFactorDisconnectFieldInput']],
	'create': Optional[List['BlobEntryFactorCreateFieldInput']],
	'delete': Optional[List['BlobEntryFactorDeleteFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryFactorConnectOrCreateFieldInput']],
})


BlobEntryOnCreateInput = TypedDict('BlobEntryOnCreateInput', {
	'blobId': str,
	'originId': str,
	'label': str,
	'description': Optional[str],
	'hash': Optional[str],
	'mimeType': Optional[str],
	'blobstore': Optional[str],
	'origin': Optional[str],
	'nstime': Optional['BigInt'],
	'_type': str,
	'_version': str,
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'variableLabel': Optional[str],
	'factorLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': Optional['DateTime'],
})


BlobEntryOptions = TypedDict('BlobEntryOptions', {
	'sort': Optional[List['BlobEntrySort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


BlobEntryRelationInput = TypedDict('BlobEntryRelationInput', {
	'user': Optional[List['BlobEntryUserCreateFieldInput']],
	'robot': Optional[List['BlobEntryRobotCreateFieldInput']],
	'session': Optional[List['BlobEntrySessionCreateFieldInput']],
	'variable': Optional[List['BlobEntryVariableCreateFieldInput']],
	'factor': Optional[List['BlobEntryFactorCreateFieldInput']],
})


BlobEntryRobotAggregateInput = TypedDict('BlobEntryRobotAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['BlobEntryRobotAggregateInput']],
	'OR': Optional[List['BlobEntryRobotAggregateInput']],
	'NOT': Optional['BlobEntryRobotAggregateInput'],
	'node': Optional['BlobEntryRobotNodeAggregationWhereInput'],
})


BlobEntryRobotConnectFieldInput = TypedDict('BlobEntryRobotConnectFieldInput', {
	'where': Optional['RobotConnectWhere'],
	'connect': Optional[List['RobotConnectInput']],
	'overwrite': bool,
})


BlobEntryRobotConnectionSort = TypedDict('BlobEntryRobotConnectionSort', {
	'node': Optional['RobotSort'],
})


BlobEntryRobotConnectionWhere = TypedDict('BlobEntryRobotConnectionWhere', {
	'AND': Optional[List['BlobEntryRobotConnectionWhere']],
	'OR': Optional[List['BlobEntryRobotConnectionWhere']],
	'NOT': Optional['BlobEntryRobotConnectionWhere'],
	'node': Optional['RobotWhere'],
})


BlobEntryRobotConnectOrCreateFieldInput = TypedDict('BlobEntryRobotConnectOrCreateFieldInput', {
	'where': 'RobotConnectOrCreateWhere',
	'onCreate': 'BlobEntryRobotConnectOrCreateFieldInputOnCreate',
})


BlobEntryRobotConnectOrCreateFieldInputOnCreate = TypedDict('BlobEntryRobotConnectOrCreateFieldInputOnCreate', {
	'node': 'RobotOnCreateInput',
})


BlobEntryRobotCreateFieldInput = TypedDict('BlobEntryRobotCreateFieldInput', {
	'node': 'RobotCreateInput',
})


BlobEntryRobotDeleteFieldInput = TypedDict('BlobEntryRobotDeleteFieldInput', {
	'where': Optional['BlobEntryRobotConnectionWhere'],
	'delete': Optional['RobotDeleteInput'],
})


BlobEntryRobotDisconnectFieldInput = TypedDict('BlobEntryRobotDisconnectFieldInput', {
	'where': Optional['BlobEntryRobotConnectionWhere'],
	'disconnect': Optional['RobotDisconnectInput'],
})


BlobEntryRobotFieldInput = TypedDict('BlobEntryRobotFieldInput', {
	'create': Optional[List['BlobEntryRobotCreateFieldInput']],
	'connect': Optional[List['BlobEntryRobotConnectFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryRobotConnectOrCreateFieldInput']],
})


BlobEntryRobotNodeAggregationWhereInput = TypedDict('BlobEntryRobotNodeAggregationWhereInput', {
	'AND': Optional[List['BlobEntryRobotNodeAggregationWhereInput']],
	'OR': Optional[List['BlobEntryRobotNodeAggregationWhereInput']],
	'NOT': Optional['BlobEntryRobotNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


BlobEntryRobotUpdateConnectionInput = TypedDict('BlobEntryRobotUpdateConnectionInput', {
	'node': Optional['RobotUpdateInput'],
})


BlobEntryRobotUpdateFieldInput = TypedDict('BlobEntryRobotUpdateFieldInput', {
	'where': Optional['BlobEntryRobotConnectionWhere'],
	'update': Optional['BlobEntryRobotUpdateConnectionInput'],
	'connect': Optional[List['BlobEntryRobotConnectFieldInput']],
	'disconnect': Optional[List['BlobEntryRobotDisconnectFieldInput']],
	'create': Optional[List['BlobEntryRobotCreateFieldInput']],
	'delete': Optional[List['BlobEntryRobotDeleteFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryRobotConnectOrCreateFieldInput']],
})


BlobEntrySessionAggregateInput = TypedDict('BlobEntrySessionAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['BlobEntrySessionAggregateInput']],
	'OR': Optional[List['BlobEntrySessionAggregateInput']],
	'NOT': Optional['BlobEntrySessionAggregateInput'],
	'node': Optional['BlobEntrySessionNodeAggregationWhereInput'],
})


BlobEntrySessionConnectFieldInput = TypedDict('BlobEntrySessionConnectFieldInput', {
	'where': Optional['SessionConnectWhere'],
	'connect': Optional[List['SessionConnectInput']],
	'overwrite': bool,
})


BlobEntrySessionConnectionSort = TypedDict('BlobEntrySessionConnectionSort', {
	'node': Optional['SessionSort'],
})


BlobEntrySessionConnectionWhere = TypedDict('BlobEntrySessionConnectionWhere', {
	'AND': Optional[List['BlobEntrySessionConnectionWhere']],
	'OR': Optional[List['BlobEntrySessionConnectionWhere']],
	'NOT': Optional['BlobEntrySessionConnectionWhere'],
	'node': Optional['SessionWhere'],
})


BlobEntrySessionConnectOrCreateFieldInput = TypedDict('BlobEntrySessionConnectOrCreateFieldInput', {
	'where': 'SessionConnectOrCreateWhere',
	'onCreate': 'BlobEntrySessionConnectOrCreateFieldInputOnCreate',
})


BlobEntrySessionConnectOrCreateFieldInputOnCreate = TypedDict('BlobEntrySessionConnectOrCreateFieldInputOnCreate', {
	'node': 'SessionOnCreateInput',
})


BlobEntrySessionCreateFieldInput = TypedDict('BlobEntrySessionCreateFieldInput', {
	'node': 'SessionCreateInput',
})


BlobEntrySessionDeleteFieldInput = TypedDict('BlobEntrySessionDeleteFieldInput', {
	'where': Optional['BlobEntrySessionConnectionWhere'],
	'delete': Optional['SessionDeleteInput'],
})


BlobEntrySessionDisconnectFieldInput = TypedDict('BlobEntrySessionDisconnectFieldInput', {
	'where': Optional['BlobEntrySessionConnectionWhere'],
	'disconnect': Optional['SessionDisconnectInput'],
})


BlobEntrySessionFieldInput = TypedDict('BlobEntrySessionFieldInput', {
	'create': Optional[List['BlobEntrySessionCreateFieldInput']],
	'connect': Optional[List['BlobEntrySessionConnectFieldInput']],
	'connectOrCreate': Optional[List['BlobEntrySessionConnectOrCreateFieldInput']],
})


BlobEntrySessionNodeAggregationWhereInput = TypedDict('BlobEntrySessionNodeAggregationWhereInput', {
	'AND': Optional[List['BlobEntrySessionNodeAggregationWhereInput']],
	'OR': Optional[List['BlobEntrySessionNodeAggregationWhereInput']],
	'NOT': Optional['BlobEntrySessionNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


BlobEntrySessionUpdateConnectionInput = TypedDict('BlobEntrySessionUpdateConnectionInput', {
	'node': Optional['SessionUpdateInput'],
})


BlobEntrySessionUpdateFieldInput = TypedDict('BlobEntrySessionUpdateFieldInput', {
	'where': Optional['BlobEntrySessionConnectionWhere'],
	'update': Optional['BlobEntrySessionUpdateConnectionInput'],
	'connect': Optional[List['BlobEntrySessionConnectFieldInput']],
	'disconnect': Optional[List['BlobEntrySessionDisconnectFieldInput']],
	'create': Optional[List['BlobEntrySessionCreateFieldInput']],
	'delete': Optional[List['BlobEntrySessionDeleteFieldInput']],
	'connectOrCreate': Optional[List['BlobEntrySessionConnectOrCreateFieldInput']],
})


BlobEntrySort = TypedDict('BlobEntrySort', {
	'id': Optional['SortDirection'],
	'blobId': Optional['SortDirection'],
	'originId': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'description': Optional['SortDirection'],
	'hash': Optional['SortDirection'],
	'mimeType': Optional['SortDirection'],
	'blobstore': Optional['SortDirection'],
	'origin': Optional['SortDirection'],
	'nstime': Optional['SortDirection'],
	'_type': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'robotLabel': Optional['SortDirection'],
	'sessionLabel': Optional['SortDirection'],
	'variableLabel': Optional['SortDirection'],
	'factorLabel': Optional['SortDirection'],
	'metadata': Optional['SortDirection'],
	'timestamp': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
})


BlobEntryUniqueWhere = TypedDict('BlobEntryUniqueWhere', {
	'id': Optional[str],
})


BlobEntryUpdateInput = TypedDict('BlobEntryUpdateInput', {
	'blobId': Optional[str],
	'originId': Optional[str],
	'label': Optional[str],
	'description': Optional[str],
	'hash': Optional[str],
	'mimeType': Optional[str],
	'blobstore': Optional[str],
	'origin': Optional[str],
	'nstime': Optional['BigInt'],
	'_type': Optional[str],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'variableLabel': Optional[str],
	'factorLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': Optional['DateTime'],
	'nstime_INCREMENT': Optional['BigInt'],
	'nstime_DECREMENT': Optional['BigInt'],
	'user': Optional[List['BlobEntryUserUpdateFieldInput']],
	'robot': Optional[List['BlobEntryRobotUpdateFieldInput']],
	'session': Optional[List['BlobEntrySessionUpdateFieldInput']],
	'variable': Optional[List['BlobEntryVariableUpdateFieldInput']],
	'factor': Optional[List['BlobEntryFactorUpdateFieldInput']],
})


BlobEntryUserAggregateInput = TypedDict('BlobEntryUserAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['BlobEntryUserAggregateInput']],
	'OR': Optional[List['BlobEntryUserAggregateInput']],
	'NOT': Optional['BlobEntryUserAggregateInput'],
	'node': Optional['BlobEntryUserNodeAggregationWhereInput'],
})


BlobEntryUserConnectFieldInput = TypedDict('BlobEntryUserConnectFieldInput', {
	'where': Optional['VariableConnectWhere'],
	'connect': Optional[List['VariableConnectInput']],
	'overwrite': bool,
})


BlobEntryUserConnectionSort = TypedDict('BlobEntryUserConnectionSort', {
	'node': Optional['VariableSort'],
})


BlobEntryUserConnectionWhere = TypedDict('BlobEntryUserConnectionWhere', {
	'AND': Optional[List['BlobEntryUserConnectionWhere']],
	'OR': Optional[List['BlobEntryUserConnectionWhere']],
	'NOT': Optional['BlobEntryUserConnectionWhere'],
	'node': Optional['VariableWhere'],
})


BlobEntryUserConnectOrCreateFieldInput = TypedDict('BlobEntryUserConnectOrCreateFieldInput', {
	'where': 'VariableConnectOrCreateWhere',
	'onCreate': 'BlobEntryUserConnectOrCreateFieldInputOnCreate',
})


BlobEntryUserConnectOrCreateFieldInputOnCreate = TypedDict('BlobEntryUserConnectOrCreateFieldInputOnCreate', {
	'node': 'VariableOnCreateInput',
})


BlobEntryUserCreateFieldInput = TypedDict('BlobEntryUserCreateFieldInput', {
	'node': 'VariableCreateInput',
})


BlobEntryUserDeleteFieldInput = TypedDict('BlobEntryUserDeleteFieldInput', {
	'where': Optional['BlobEntryUserConnectionWhere'],
	'delete': Optional['VariableDeleteInput'],
})


BlobEntryUserDisconnectFieldInput = TypedDict('BlobEntryUserDisconnectFieldInput', {
	'where': Optional['BlobEntryUserConnectionWhere'],
	'disconnect': Optional['VariableDisconnectInput'],
})


BlobEntryUserFieldInput = TypedDict('BlobEntryUserFieldInput', {
	'create': Optional[List['BlobEntryUserCreateFieldInput']],
	'connect': Optional[List['BlobEntryUserConnectFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryUserConnectOrCreateFieldInput']],
})


BlobEntryUserNodeAggregationWhereInput = TypedDict('BlobEntryUserNodeAggregationWhereInput', {
	'AND': Optional[List['BlobEntryUserNodeAggregationWhereInput']],
	'OR': Optional[List['BlobEntryUserNodeAggregationWhereInput']],
	'NOT': Optional['BlobEntryUserNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


BlobEntryUserUpdateConnectionInput = TypedDict('BlobEntryUserUpdateConnectionInput', {
	'node': Optional['VariableUpdateInput'],
})


BlobEntryUserUpdateFieldInput = TypedDict('BlobEntryUserUpdateFieldInput', {
	'where': Optional['BlobEntryUserConnectionWhere'],
	'update': Optional['BlobEntryUserUpdateConnectionInput'],
	'connect': Optional[List['BlobEntryUserConnectFieldInput']],
	'disconnect': Optional[List['BlobEntryUserDisconnectFieldInput']],
	'create': Optional[List['BlobEntryUserCreateFieldInput']],
	'delete': Optional[List['BlobEntryUserDeleteFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryUserConnectOrCreateFieldInput']],
})


BlobEntryVariableAggregateInput = TypedDict('BlobEntryVariableAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['BlobEntryVariableAggregateInput']],
	'OR': Optional[List['BlobEntryVariableAggregateInput']],
	'NOT': Optional['BlobEntryVariableAggregateInput'],
	'node': Optional['BlobEntryVariableNodeAggregationWhereInput'],
})


BlobEntryVariableConnectFieldInput = TypedDict('BlobEntryVariableConnectFieldInput', {
	'where': Optional['VariableConnectWhere'],
	'connect': Optional[List['VariableConnectInput']],
	'overwrite': bool,
})


BlobEntryVariableConnectionSort = TypedDict('BlobEntryVariableConnectionSort', {
	'node': Optional['VariableSort'],
})


BlobEntryVariableConnectionWhere = TypedDict('BlobEntryVariableConnectionWhere', {
	'AND': Optional[List['BlobEntryVariableConnectionWhere']],
	'OR': Optional[List['BlobEntryVariableConnectionWhere']],
	'NOT': Optional['BlobEntryVariableConnectionWhere'],
	'node': Optional['VariableWhere'],
})


BlobEntryVariableConnectOrCreateFieldInput = TypedDict('BlobEntryVariableConnectOrCreateFieldInput', {
	'where': 'VariableConnectOrCreateWhere',
	'onCreate': 'BlobEntryVariableConnectOrCreateFieldInputOnCreate',
})


BlobEntryVariableConnectOrCreateFieldInputOnCreate = TypedDict('BlobEntryVariableConnectOrCreateFieldInputOnCreate', {
	'node': 'VariableOnCreateInput',
})


BlobEntryVariableCreateFieldInput = TypedDict('BlobEntryVariableCreateFieldInput', {
	'node': 'VariableCreateInput',
})


BlobEntryVariableDeleteFieldInput = TypedDict('BlobEntryVariableDeleteFieldInput', {
	'where': Optional['BlobEntryVariableConnectionWhere'],
	'delete': Optional['VariableDeleteInput'],
})


BlobEntryVariableDisconnectFieldInput = TypedDict('BlobEntryVariableDisconnectFieldInput', {
	'where': Optional['BlobEntryVariableConnectionWhere'],
	'disconnect': Optional['VariableDisconnectInput'],
})


BlobEntryVariableFieldInput = TypedDict('BlobEntryVariableFieldInput', {
	'create': Optional[List['BlobEntryVariableCreateFieldInput']],
	'connect': Optional[List['BlobEntryVariableConnectFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryVariableConnectOrCreateFieldInput']],
})


BlobEntryVariableNodeAggregationWhereInput = TypedDict('BlobEntryVariableNodeAggregationWhereInput', {
	'AND': Optional[List['BlobEntryVariableNodeAggregationWhereInput']],
	'OR': Optional[List['BlobEntryVariableNodeAggregationWhereInput']],
	'NOT': Optional['BlobEntryVariableNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


BlobEntryVariableUpdateConnectionInput = TypedDict('BlobEntryVariableUpdateConnectionInput', {
	'node': Optional['VariableUpdateInput'],
})


BlobEntryVariableUpdateFieldInput = TypedDict('BlobEntryVariableUpdateFieldInput', {
	'where': Optional['BlobEntryVariableConnectionWhere'],
	'update': Optional['BlobEntryVariableUpdateConnectionInput'],
	'connect': Optional[List['BlobEntryVariableConnectFieldInput']],
	'disconnect': Optional[List['BlobEntryVariableDisconnectFieldInput']],
	'create': Optional[List['BlobEntryVariableCreateFieldInput']],
	'delete': Optional[List['BlobEntryVariableDeleteFieldInput']],
	'connectOrCreate': Optional[List['BlobEntryVariableConnectOrCreateFieldInput']],
})


BlobEntryWhere = TypedDict('BlobEntryWhere', {
	'OR': Optional[List['BlobEntryWhere']],
	'AND': Optional[List['BlobEntryWhere']],
	'NOT': Optional['BlobEntryWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'blobId': Optional[str],
	'blobId_IN': Optional[List[str]],
	'blobId_MATCHES': Optional[str],
	'blobId_CONTAINS': Optional[str],
	'blobId_STARTS_WITH': Optional[str],
	'blobId_ENDS_WITH': Optional[str],
	'originId': Optional[str],
	'originId_IN': Optional[List[str]],
	'originId_MATCHES': Optional[str],
	'originId_CONTAINS': Optional[str],
	'originId_STARTS_WITH': Optional[str],
	'originId_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'description': Optional[str],
	'description_IN': Optional[List[str]],
	'description_MATCHES': Optional[str],
	'description_CONTAINS': Optional[str],
	'description_STARTS_WITH': Optional[str],
	'description_ENDS_WITH': Optional[str],
	'hash': Optional[str],
	'hash_IN': Optional[List[str]],
	'hash_MATCHES': Optional[str],
	'hash_CONTAINS': Optional[str],
	'hash_STARTS_WITH': Optional[str],
	'hash_ENDS_WITH': Optional[str],
	'mimeType': Optional[str],
	'mimeType_IN': Optional[List[str]],
	'mimeType_MATCHES': Optional[str],
	'mimeType_CONTAINS': Optional[str],
	'mimeType_STARTS_WITH': Optional[str],
	'mimeType_ENDS_WITH': Optional[str],
	'blobstore': Optional[str],
	'blobstore_IN': Optional[List[str]],
	'blobstore_MATCHES': Optional[str],
	'blobstore_CONTAINS': Optional[str],
	'blobstore_STARTS_WITH': Optional[str],
	'blobstore_ENDS_WITH': Optional[str],
	'origin': Optional[str],
	'origin_IN': Optional[List[str]],
	'origin_MATCHES': Optional[str],
	'origin_CONTAINS': Optional[str],
	'origin_STARTS_WITH': Optional[str],
	'origin_ENDS_WITH': Optional[str],
	'nstime': Optional['BigInt'],
	'nstime_IN': Optional[List['BigInt']],
	'nstime_LT': Optional['BigInt'],
	'nstime_LTE': Optional['BigInt'],
	'nstime_GT': Optional['BigInt'],
	'nstime_GTE': Optional['BigInt'],
	'_type': Optional[str],
	'_type_IN': Optional[List[str]],
	'_type_MATCHES': Optional[str],
	'_type_CONTAINS': Optional[str],
	'_type_STARTS_WITH': Optional[str],
	'_type_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'robotLabel': Optional[str],
	'robotLabel_IN': Optional[List[str]],
	'robotLabel_MATCHES': Optional[str],
	'robotLabel_CONTAINS': Optional[str],
	'robotLabel_STARTS_WITH': Optional[str],
	'robotLabel_ENDS_WITH': Optional[str],
	'sessionLabel': Optional[str],
	'sessionLabel_IN': Optional[List[str]],
	'sessionLabel_MATCHES': Optional[str],
	'sessionLabel_CONTAINS': Optional[str],
	'sessionLabel_STARTS_WITH': Optional[str],
	'sessionLabel_ENDS_WITH': Optional[str],
	'variableLabel': Optional[str],
	'variableLabel_IN': Optional[List[str]],
	'variableLabel_MATCHES': Optional[str],
	'variableLabel_CONTAINS': Optional[str],
	'variableLabel_STARTS_WITH': Optional[str],
	'variableLabel_ENDS_WITH': Optional[str],
	'factorLabel': Optional[str],
	'factorLabel_IN': Optional[List[str]],
	'factorLabel_MATCHES': Optional[str],
	'factorLabel_CONTAINS': Optional[str],
	'factorLabel_STARTS_WITH': Optional[str],
	'factorLabel_ENDS_WITH': Optional[str],
	'timestamp': Optional['DateTime'],
	'timestamp_IN': Optional[List['DateTime']],
	'timestamp_LT': Optional['DateTime'],
	'timestamp_LTE': Optional['DateTime'],
	'timestamp_GT': Optional['DateTime'],
	'timestamp_GTE': Optional['DateTime'],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'metadata': Optional['Metadata'],
	'metadata_IN': Optional[List['Metadata']],
	'userAggregate': Optional['BlobEntryUserAggregateInput'],
	'user_ALL': Optional['VariableWhere'],
	'user_NONE': Optional['VariableWhere'],
	'user_SINGLE': Optional['VariableWhere'],
	'user_SOME': Optional['VariableWhere'],
	'robotAggregate': Optional['BlobEntryRobotAggregateInput'],
	'robot_ALL': Optional['RobotWhere'],
	'robot_NONE': Optional['RobotWhere'],
	'robot_SINGLE': Optional['RobotWhere'],
	'robot_SOME': Optional['RobotWhere'],
	'sessionAggregate': Optional['BlobEntrySessionAggregateInput'],
	'session_ALL': Optional['SessionWhere'],
	'session_NONE': Optional['SessionWhere'],
	'session_SINGLE': Optional['SessionWhere'],
	'session_SOME': Optional['SessionWhere'],
	'variableAggregate': Optional['BlobEntryVariableAggregateInput'],
	'variable_ALL': Optional['VariableWhere'],
	'variable_NONE': Optional['VariableWhere'],
	'variable_SINGLE': Optional['VariableWhere'],
	'variable_SOME': Optional['VariableWhere'],
	'factorAggregate': Optional['BlobEntryFactorAggregateInput'],
	'factor_ALL': Optional['FactorWhere'],
	'factor_NONE': Optional['FactorWhere'],
	'factor_SINGLE': Optional['FactorWhere'],
	'factor_SOME': Optional['FactorWhere'],
	'userConnection_ALL': Optional['BlobEntryUserConnectionWhere'],
	'userConnection_NONE': Optional['BlobEntryUserConnectionWhere'],
	'userConnection_SINGLE': Optional['BlobEntryUserConnectionWhere'],
	'userConnection_SOME': Optional['BlobEntryUserConnectionWhere'],
	'robotConnection_ALL': Optional['BlobEntryRobotConnectionWhere'],
	'robotConnection_NONE': Optional['BlobEntryRobotConnectionWhere'],
	'robotConnection_SINGLE': Optional['BlobEntryRobotConnectionWhere'],
	'robotConnection_SOME': Optional['BlobEntryRobotConnectionWhere'],
	'sessionConnection_ALL': Optional['BlobEntrySessionConnectionWhere'],
	'sessionConnection_NONE': Optional['BlobEntrySessionConnectionWhere'],
	'sessionConnection_SINGLE': Optional['BlobEntrySessionConnectionWhere'],
	'sessionConnection_SOME': Optional['BlobEntrySessionConnectionWhere'],
	'variableConnection_ALL': Optional['BlobEntryVariableConnectionWhere'],
	'variableConnection_NONE': Optional['BlobEntryVariableConnectionWhere'],
	'variableConnection_SINGLE': Optional['BlobEntryVariableConnectionWhere'],
	'variableConnection_SOME': Optional['BlobEntryVariableConnectionWhere'],
	'factorConnection_ALL': Optional['BlobEntryFactorConnectionWhere'],
	'factorConnection_NONE': Optional['BlobEntryFactorConnectionWhere'],
	'factorConnection_SINGLE': Optional['BlobEntryFactorConnectionWhere'],
	'factorConnection_SOME': Optional['BlobEntryFactorConnectionWhere'],
})


FactorBlobEntriesAggregateInput = TypedDict('FactorBlobEntriesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['FactorBlobEntriesAggregateInput']],
	'OR': Optional[List['FactorBlobEntriesAggregateInput']],
	'NOT': Optional['FactorBlobEntriesAggregateInput'],
	'node': Optional['FactorBlobEntriesNodeAggregationWhereInput'],
})


FactorBlobEntriesConnectFieldInput = TypedDict('FactorBlobEntriesConnectFieldInput', {
	'where': Optional['BlobEntryConnectWhere'],
	'connect': Optional[List['BlobEntryConnectInput']],
	'overwrite': bool,
})


FactorBlobEntriesConnectionSort = TypedDict('FactorBlobEntriesConnectionSort', {
	'node': Optional['BlobEntrySort'],
})


FactorBlobEntriesConnectionWhere = TypedDict('FactorBlobEntriesConnectionWhere', {
	'AND': Optional[List['FactorBlobEntriesConnectionWhere']],
	'OR': Optional[List['FactorBlobEntriesConnectionWhere']],
	'NOT': Optional['FactorBlobEntriesConnectionWhere'],
	'node': Optional['BlobEntryWhere'],
})


FactorBlobEntriesConnectOrCreateFieldInput = TypedDict('FactorBlobEntriesConnectOrCreateFieldInput', {
	'where': 'BlobEntryConnectOrCreateWhere',
	'onCreate': 'FactorBlobEntriesConnectOrCreateFieldInputOnCreate',
})


FactorBlobEntriesConnectOrCreateFieldInputOnCreate = TypedDict('FactorBlobEntriesConnectOrCreateFieldInputOnCreate', {
	'node': 'BlobEntryOnCreateInput',
})


FactorBlobEntriesCreateFieldInput = TypedDict('FactorBlobEntriesCreateFieldInput', {
	'node': 'BlobEntryCreateInput',
})


FactorBlobEntriesDeleteFieldInput = TypedDict('FactorBlobEntriesDeleteFieldInput', {
	'where': Optional['FactorBlobEntriesConnectionWhere'],
	'delete': Optional['BlobEntryDeleteInput'],
})


FactorBlobEntriesDisconnectFieldInput = TypedDict('FactorBlobEntriesDisconnectFieldInput', {
	'where': Optional['FactorBlobEntriesConnectionWhere'],
	'disconnect': Optional['BlobEntryDisconnectInput'],
})


FactorBlobEntriesFieldInput = TypedDict('FactorBlobEntriesFieldInput', {
	'create': Optional[List['FactorBlobEntriesCreateFieldInput']],
	'connect': Optional[List['FactorBlobEntriesConnectFieldInput']],
	'connectOrCreate': Optional[List['FactorBlobEntriesConnectOrCreateFieldInput']],
})


FactorBlobEntriesNodeAggregationWhereInput = TypedDict('FactorBlobEntriesNodeAggregationWhereInput', {
	'AND': Optional[List['FactorBlobEntriesNodeAggregationWhereInput']],
	'OR': Optional[List['FactorBlobEntriesNodeAggregationWhereInput']],
	'NOT': Optional['FactorBlobEntriesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'hash_AVERAGE_LENGTH_EQUAL': Optional[float],
	'hash_LONGEST_LENGTH_EQUAL': Optional[int],
	'hash_SHORTEST_LENGTH_EQUAL': Optional[int],
	'hash_AVERAGE_LENGTH_GT': Optional[float],
	'hash_LONGEST_LENGTH_GT': Optional[int],
	'hash_SHORTEST_LENGTH_GT': Optional[int],
	'hash_AVERAGE_LENGTH_GTE': Optional[float],
	'hash_LONGEST_LENGTH_GTE': Optional[int],
	'hash_SHORTEST_LENGTH_GTE': Optional[int],
	'hash_AVERAGE_LENGTH_LT': Optional[float],
	'hash_LONGEST_LENGTH_LT': Optional[int],
	'hash_SHORTEST_LENGTH_LT': Optional[int],
	'hash_AVERAGE_LENGTH_LTE': Optional[float],
	'hash_LONGEST_LENGTH_LTE': Optional[int],
	'hash_SHORTEST_LENGTH_LTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'mimeType_LONGEST_LENGTH_EQUAL': Optional[int],
	'mimeType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'mimeType_AVERAGE_LENGTH_GT': Optional[float],
	'mimeType_LONGEST_LENGTH_GT': Optional[int],
	'mimeType_SHORTEST_LENGTH_GT': Optional[int],
	'mimeType_AVERAGE_LENGTH_GTE': Optional[float],
	'mimeType_LONGEST_LENGTH_GTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_GTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_LT': Optional[float],
	'mimeType_LONGEST_LENGTH_LT': Optional[int],
	'mimeType_SHORTEST_LENGTH_LT': Optional[int],
	'mimeType_AVERAGE_LENGTH_LTE': Optional[float],
	'mimeType_LONGEST_LENGTH_LTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_LTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_EQUAL': Optional[float],
	'blobstore_LONGEST_LENGTH_EQUAL': Optional[int],
	'blobstore_SHORTEST_LENGTH_EQUAL': Optional[int],
	'blobstore_AVERAGE_LENGTH_GT': Optional[float],
	'blobstore_LONGEST_LENGTH_GT': Optional[int],
	'blobstore_SHORTEST_LENGTH_GT': Optional[int],
	'blobstore_AVERAGE_LENGTH_GTE': Optional[float],
	'blobstore_LONGEST_LENGTH_GTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_GTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_LT': Optional[float],
	'blobstore_LONGEST_LENGTH_LT': Optional[int],
	'blobstore_SHORTEST_LENGTH_LT': Optional[int],
	'blobstore_AVERAGE_LENGTH_LTE': Optional[float],
	'blobstore_LONGEST_LENGTH_LTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_LTE': Optional[int],
	'origin_AVERAGE_LENGTH_EQUAL': Optional[float],
	'origin_LONGEST_LENGTH_EQUAL': Optional[int],
	'origin_SHORTEST_LENGTH_EQUAL': Optional[int],
	'origin_AVERAGE_LENGTH_GT': Optional[float],
	'origin_LONGEST_LENGTH_GT': Optional[int],
	'origin_SHORTEST_LENGTH_GT': Optional[int],
	'origin_AVERAGE_LENGTH_GTE': Optional[float],
	'origin_LONGEST_LENGTH_GTE': Optional[int],
	'origin_SHORTEST_LENGTH_GTE': Optional[int],
	'origin_AVERAGE_LENGTH_LT': Optional[float],
	'origin_LONGEST_LENGTH_LT': Optional[int],
	'origin_SHORTEST_LENGTH_LT': Optional[int],
	'origin_AVERAGE_LENGTH_LTE': Optional[float],
	'origin_LONGEST_LENGTH_LTE': Optional[int],
	'origin_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'factorLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GT': Optional[float],
	'factorLabel_LONGEST_LENGTH_GT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_GTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LT': Optional[float],
	'factorLabel_LONGEST_LENGTH_LT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_LTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


FactorBlobEntriesUpdateConnectionInput = TypedDict('FactorBlobEntriesUpdateConnectionInput', {
	'node': Optional['BlobEntryUpdateInput'],
})


FactorBlobEntriesUpdateFieldInput = TypedDict('FactorBlobEntriesUpdateFieldInput', {
	'where': Optional['FactorBlobEntriesConnectionWhere'],
	'update': Optional['FactorBlobEntriesUpdateConnectionInput'],
	'connect': Optional[List['FactorBlobEntriesConnectFieldInput']],
	'disconnect': Optional[List['FactorBlobEntriesDisconnectFieldInput']],
	'create': Optional[List['FactorBlobEntriesCreateFieldInput']],
	'delete': Optional[List['FactorBlobEntriesDeleteFieldInput']],
	'connectOrCreate': Optional[List['FactorBlobEntriesConnectOrCreateFieldInput']],
})


FactorConnectInput = TypedDict('FactorConnectInput', {
	'variables': Optional[List['FactorVariablesConnectFieldInput']],
	'blobEntries': Optional[List['FactorBlobEntriesConnectFieldInput']],
	'session': Optional['FactorSessionConnectFieldInput'],
})


FactorConnectOrCreateInput = TypedDict('FactorConnectOrCreateInput', {
	'variables': Optional[List['FactorVariablesConnectOrCreateFieldInput']],
	'blobEntries': Optional[List['FactorBlobEntriesConnectOrCreateFieldInput']],
	'session': Optional['FactorSessionConnectOrCreateFieldInput'],
})


FactorConnectOrCreateWhere = TypedDict('FactorConnectOrCreateWhere', {
	'node': 'FactorUniqueWhere',
})


FactorConnectWhere = TypedDict('FactorConnectWhere', {
	'node': 'FactorWhere',
})


FactorCreateInput = TypedDict('FactorCreateInput', {
	'label': str,
	'tags': List[str],
	'nstime': 'BigInt',
	'fnctype': str,
	'solvable': int,
	'data': str,
	'_variableOrderSymbols': Optional[List[str]],
	'_type': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'metadata': Optional['Metadata'],
	'timestamp': 'DateTime',
	'variables': Optional['FactorVariablesFieldInput'],
	'blobEntries': Optional['FactorBlobEntriesFieldInput'],
	'session': Optional['FactorSessionFieldInput'],
})


FactorDeleteInput = TypedDict('FactorDeleteInput', {
	'variables': Optional[List['FactorVariablesDeleteFieldInput']],
	'blobEntries': Optional[List['FactorBlobEntriesDeleteFieldInput']],
	'session': Optional['FactorSessionDeleteFieldInput'],
})


FactorDisconnectInput = TypedDict('FactorDisconnectInput', {
	'variables': Optional[List['FactorVariablesDisconnectFieldInput']],
	'blobEntries': Optional[List['FactorBlobEntriesDisconnectFieldInput']],
	'session': Optional['FactorSessionDisconnectFieldInput'],
})


FactorOnCreateInput = TypedDict('FactorOnCreateInput', {
	'label': str,
	'tags': List[str],
	'nstime': 'BigInt',
	'fnctype': str,
	'solvable': int,
	'data': str,
	'_variableOrderSymbols': Optional[List[str]],
	'_type': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'metadata': Optional['Metadata'],
	'timestamp': 'DateTime',
})


FactorOptions = TypedDict('FactorOptions', {
	'sort': Optional[List['FactorSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


FactorRelationInput = TypedDict('FactorRelationInput', {
	'variables': Optional[List['FactorVariablesCreateFieldInput']],
	'blobEntries': Optional[List['FactorBlobEntriesCreateFieldInput']],
	'session': Optional['FactorSessionCreateFieldInput'],
})


FactorSessionAggregateInput = TypedDict('FactorSessionAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['FactorSessionAggregateInput']],
	'OR': Optional[List['FactorSessionAggregateInput']],
	'NOT': Optional['FactorSessionAggregateInput'],
	'node': Optional['FactorSessionNodeAggregationWhereInput'],
})


FactorSessionConnectFieldInput = TypedDict('FactorSessionConnectFieldInput', {
	'where': Optional['SessionConnectWhere'],
	'connect': Optional['SessionConnectInput'],
	'overwrite': bool,
})


FactorSessionConnectionSort = TypedDict('FactorSessionConnectionSort', {
	'node': Optional['SessionSort'],
})


FactorSessionConnectionWhere = TypedDict('FactorSessionConnectionWhere', {
	'AND': Optional[List['FactorSessionConnectionWhere']],
	'OR': Optional[List['FactorSessionConnectionWhere']],
	'NOT': Optional['FactorSessionConnectionWhere'],
	'node': Optional['SessionWhere'],
})


FactorSessionConnectOrCreateFieldInput = TypedDict('FactorSessionConnectOrCreateFieldInput', {
	'where': 'SessionConnectOrCreateWhere',
	'onCreate': 'FactorSessionConnectOrCreateFieldInputOnCreate',
})


FactorSessionConnectOrCreateFieldInputOnCreate = TypedDict('FactorSessionConnectOrCreateFieldInputOnCreate', {
	'node': 'SessionOnCreateInput',
})


FactorSessionCreateFieldInput = TypedDict('FactorSessionCreateFieldInput', {
	'node': 'SessionCreateInput',
})


FactorSessionDeleteFieldInput = TypedDict('FactorSessionDeleteFieldInput', {
	'where': Optional['FactorSessionConnectionWhere'],
	'delete': Optional['SessionDeleteInput'],
})


FactorSessionDisconnectFieldInput = TypedDict('FactorSessionDisconnectFieldInput', {
	'where': Optional['FactorSessionConnectionWhere'],
	'disconnect': Optional['SessionDisconnectInput'],
})


FactorSessionFieldInput = TypedDict('FactorSessionFieldInput', {
	'create': Optional['FactorSessionCreateFieldInput'],
	'connect': Optional['FactorSessionConnectFieldInput'],
	'connectOrCreate': Optional['FactorSessionConnectOrCreateFieldInput'],
})


FactorSessionNodeAggregationWhereInput = TypedDict('FactorSessionNodeAggregationWhereInput', {
	'AND': Optional[List['FactorSessionNodeAggregationWhereInput']],
	'OR': Optional[List['FactorSessionNodeAggregationWhereInput']],
	'NOT': Optional['FactorSessionNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


FactorSessionUpdateConnectionInput = TypedDict('FactorSessionUpdateConnectionInput', {
	'node': Optional['SessionUpdateInput'],
})


FactorSessionUpdateFieldInput = TypedDict('FactorSessionUpdateFieldInput', {
	'where': Optional['FactorSessionConnectionWhere'],
	'update': Optional['FactorSessionUpdateConnectionInput'],
	'connect': Optional['FactorSessionConnectFieldInput'],
	'disconnect': Optional['FactorSessionDisconnectFieldInput'],
	'create': Optional['FactorSessionCreateFieldInput'],
	'delete': Optional['FactorSessionDeleteFieldInput'],
	'connectOrCreate': Optional['FactorSessionConnectOrCreateFieldInput'],
})


FactorSort = TypedDict('FactorSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'nstime': Optional['SortDirection'],
	'fnctype': Optional['SortDirection'],
	'solvable': Optional['SortDirection'],
	'data': Optional['SortDirection'],
	'_type': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'robotLabel': Optional['SortDirection'],
	'sessionLabel': Optional['SortDirection'],
	'metadata': Optional['SortDirection'],
	'timestamp': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
	'sessionId': Optional['SortDirection'],
	'robotId': Optional['SortDirection'],
	'userId': Optional['SortDirection'],
})


FactorUniqueWhere = TypedDict('FactorUniqueWhere', {
	'id': Optional[str],
})


FactorUpdateInput = TypedDict('FactorUpdateInput', {
	'label': Optional[str],
	'tags': Optional[List[str]],
	'nstime': Optional['BigInt'],
	'fnctype': Optional[str],
	'solvable': Optional[int],
	'data': Optional[str],
	'_variableOrderSymbols': Optional[List[str]],
	'_type': Optional[str],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': Optional['DateTime'],
	'nstime_INCREMENT': Optional['BigInt'],
	'nstime_DECREMENT': Optional['BigInt'],
	'solvable_INCREMENT': Optional[int],
	'solvable_DECREMENT': Optional[int],
	'tags_POP': Optional[int],
	'tags_PUSH': Optional[List[str]],
	'_variableOrderSymbols_POP': Optional[int],
	'_variableOrderSymbols_PUSH': Optional[List[str]],
	'variables': Optional[List['FactorVariablesUpdateFieldInput']],
	'blobEntries': Optional[List['FactorBlobEntriesUpdateFieldInput']],
	'session': Optional['FactorSessionUpdateFieldInput'],
})


FactorVariablesAggregateInput = TypedDict('FactorVariablesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['FactorVariablesAggregateInput']],
	'OR': Optional[List['FactorVariablesAggregateInput']],
	'NOT': Optional['FactorVariablesAggregateInput'],
	'node': Optional['FactorVariablesNodeAggregationWhereInput'],
})


FactorVariablesConnectFieldInput = TypedDict('FactorVariablesConnectFieldInput', {
	'where': Optional['VariableConnectWhere'],
	'connect': Optional[List['VariableConnectInput']],
	'overwrite': bool,
})


FactorVariablesConnectionSort = TypedDict('FactorVariablesConnectionSort', {
	'node': Optional['VariableSort'],
})


FactorVariablesConnectionWhere = TypedDict('FactorVariablesConnectionWhere', {
	'AND': Optional[List['FactorVariablesConnectionWhere']],
	'OR': Optional[List['FactorVariablesConnectionWhere']],
	'NOT': Optional['FactorVariablesConnectionWhere'],
	'node': Optional['VariableWhere'],
})


FactorVariablesConnectOrCreateFieldInput = TypedDict('FactorVariablesConnectOrCreateFieldInput', {
	'where': 'VariableConnectOrCreateWhere',
	'onCreate': 'FactorVariablesConnectOrCreateFieldInputOnCreate',
})


FactorVariablesConnectOrCreateFieldInputOnCreate = TypedDict('FactorVariablesConnectOrCreateFieldInputOnCreate', {
	'node': 'VariableOnCreateInput',
})


FactorVariablesCreateFieldInput = TypedDict('FactorVariablesCreateFieldInput', {
	'node': 'VariableCreateInput',
})


FactorVariablesDeleteFieldInput = TypedDict('FactorVariablesDeleteFieldInput', {
	'where': Optional['FactorVariablesConnectionWhere'],
	'delete': Optional['VariableDeleteInput'],
})


FactorVariablesDisconnectFieldInput = TypedDict('FactorVariablesDisconnectFieldInput', {
	'where': Optional['FactorVariablesConnectionWhere'],
	'disconnect': Optional['VariableDisconnectInput'],
})


FactorVariablesFieldInput = TypedDict('FactorVariablesFieldInput', {
	'create': Optional[List['FactorVariablesCreateFieldInput']],
	'connect': Optional[List['FactorVariablesConnectFieldInput']],
	'connectOrCreate': Optional[List['FactorVariablesConnectOrCreateFieldInput']],
})


FactorVariablesNodeAggregationWhereInput = TypedDict('FactorVariablesNodeAggregationWhereInput', {
	'AND': Optional[List['FactorVariablesNodeAggregationWhereInput']],
	'OR': Optional[List['FactorVariablesNodeAggregationWhereInput']],
	'NOT': Optional['FactorVariablesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


FactorVariablesUpdateConnectionInput = TypedDict('FactorVariablesUpdateConnectionInput', {
	'node': Optional['VariableUpdateInput'],
})


FactorVariablesUpdateFieldInput = TypedDict('FactorVariablesUpdateFieldInput', {
	'where': Optional['FactorVariablesConnectionWhere'],
	'update': Optional['FactorVariablesUpdateConnectionInput'],
	'connect': Optional[List['FactorVariablesConnectFieldInput']],
	'disconnect': Optional[List['FactorVariablesDisconnectFieldInput']],
	'create': Optional[List['FactorVariablesCreateFieldInput']],
	'delete': Optional[List['FactorVariablesDeleteFieldInput']],
	'connectOrCreate': Optional[List['FactorVariablesConnectOrCreateFieldInput']],
})


FactorWhere = TypedDict('FactorWhere', {
	'OR': Optional[List['FactorWhere']],
	'AND': Optional[List['FactorWhere']],
	'NOT': Optional['FactorWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'tags': Optional[List[str]],
	'tags_INCLUDES': Optional[str],
	'nstime': Optional['BigInt'],
	'nstime_IN': Optional[List['BigInt']],
	'nstime_LT': Optional['BigInt'],
	'nstime_LTE': Optional['BigInt'],
	'nstime_GT': Optional['BigInt'],
	'nstime_GTE': Optional['BigInt'],
	'fnctype': Optional[str],
	'fnctype_IN': Optional[List[str]],
	'fnctype_MATCHES': Optional[str],
	'fnctype_CONTAINS': Optional[str],
	'fnctype_STARTS_WITH': Optional[str],
	'fnctype_ENDS_WITH': Optional[str],
	'solvable': Optional[int],
	'solvable_IN': Optional[List[int]],
	'solvable_LT': Optional[int],
	'solvable_LTE': Optional[int],
	'solvable_GT': Optional[int],
	'solvable_GTE': Optional[int],
	'data': Optional[str],
	'data_IN': Optional[List[str]],
	'data_MATCHES': Optional[str],
	'data_CONTAINS': Optional[str],
	'data_STARTS_WITH': Optional[str],
	'data_ENDS_WITH': Optional[str],
	'_variableOrderSymbols': Optional[List[str]],
	'_variableOrderSymbols_INCLUDES': Optional[str],
	'_type': Optional[str],
	'_type_IN': Optional[List[str]],
	'_type_MATCHES': Optional[str],
	'_type_CONTAINS': Optional[str],
	'_type_STARTS_WITH': Optional[str],
	'_type_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'robotLabel': Optional[str],
	'robotLabel_IN': Optional[List[str]],
	'robotLabel_MATCHES': Optional[str],
	'robotLabel_CONTAINS': Optional[str],
	'robotLabel_STARTS_WITH': Optional[str],
	'robotLabel_ENDS_WITH': Optional[str],
	'sessionLabel': Optional[str],
	'sessionLabel_IN': Optional[List[str]],
	'sessionLabel_MATCHES': Optional[str],
	'sessionLabel_CONTAINS': Optional[str],
	'sessionLabel_STARTS_WITH': Optional[str],
	'sessionLabel_ENDS_WITH': Optional[str],
	'timestamp': Optional['DateTime'],
	'timestamp_IN': Optional[List['DateTime']],
	'timestamp_LT': Optional['DateTime'],
	'timestamp_LTE': Optional['DateTime'],
	'timestamp_GT': Optional['DateTime'],
	'timestamp_GTE': Optional['DateTime'],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'metadata': Optional['Metadata'],
	'metadata_IN': Optional[List['Metadata']],
	'variablesAggregate': Optional['FactorVariablesAggregateInput'],
	'variables_ALL': Optional['VariableWhere'],
	'variables_NONE': Optional['VariableWhere'],
	'variables_SINGLE': Optional['VariableWhere'],
	'variables_SOME': Optional['VariableWhere'],
	'blobEntriesAggregate': Optional['FactorBlobEntriesAggregateInput'],
	'blobEntries_ALL': Optional['BlobEntryWhere'],
	'blobEntries_NONE': Optional['BlobEntryWhere'],
	'blobEntries_SINGLE': Optional['BlobEntryWhere'],
	'blobEntries_SOME': Optional['BlobEntryWhere'],
	'sessionAggregate': Optional['FactorSessionAggregateInput'],
	'variablesConnection_ALL': Optional['FactorVariablesConnectionWhere'],
	'variablesConnection_NONE': Optional['FactorVariablesConnectionWhere'],
	'variablesConnection_SINGLE': Optional['FactorVariablesConnectionWhere'],
	'variablesConnection_SOME': Optional['FactorVariablesConnectionWhere'],
	'blobEntriesConnection_ALL': Optional['FactorBlobEntriesConnectionWhere'],
	'blobEntriesConnection_NONE': Optional['FactorBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SINGLE': Optional['FactorBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SOME': Optional['FactorBlobEntriesConnectionWhere'],
	'sessionConnection': Optional['FactorSessionConnectionWhere'],
})


MapAffordancesAggregateInput = TypedDict('MapAffordancesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['MapAffordancesAggregateInput']],
	'OR': Optional[List['MapAffordancesAggregateInput']],
	'NOT': Optional['MapAffordancesAggregateInput'],
	'node': Optional['MapAffordancesNodeAggregationWhereInput'],
})


MapAffordancesConnectFieldInput = TypedDict('MapAffordancesConnectFieldInput', {
	'where': Optional['AffordanceConnectWhere'],
	'overwrite': bool,
})


MapAffordancesConnectionSort = TypedDict('MapAffordancesConnectionSort', {
	'node': Optional['AffordanceSort'],
})


MapAffordancesConnectionWhere = TypedDict('MapAffordancesConnectionWhere', {
	'AND': Optional[List['MapAffordancesConnectionWhere']],
	'OR': Optional[List['MapAffordancesConnectionWhere']],
	'NOT': Optional['MapAffordancesConnectionWhere'],
	'node': Optional['AffordanceWhere'],
})


MapAffordancesConnectOrCreateFieldInput = TypedDict('MapAffordancesConnectOrCreateFieldInput', {
	'where': 'AffordanceConnectOrCreateWhere',
	'onCreate': 'MapAffordancesConnectOrCreateFieldInputOnCreate',
})


MapAffordancesConnectOrCreateFieldInputOnCreate = TypedDict('MapAffordancesConnectOrCreateFieldInputOnCreate', {
	'node': 'AffordanceOnCreateInput',
})


MapAffordancesCreateFieldInput = TypedDict('MapAffordancesCreateFieldInput', {
	'node': 'AffordanceCreateInput',
})


MapAffordancesDeleteFieldInput = TypedDict('MapAffordancesDeleteFieldInput', {
	'where': Optional['MapAffordancesConnectionWhere'],
})


MapAffordancesDisconnectFieldInput = TypedDict('MapAffordancesDisconnectFieldInput', {
	'where': Optional['MapAffordancesConnectionWhere'],
})


MapAffordancesFieldInput = TypedDict('MapAffordancesFieldInput', {
	'create': Optional[List['MapAffordancesCreateFieldInput']],
	'connect': Optional[List['MapAffordancesConnectFieldInput']],
	'connectOrCreate': Optional[List['MapAffordancesConnectOrCreateFieldInput']],
})


MapAffordancesNodeAggregationWhereInput = TypedDict('MapAffordancesNodeAggregationWhereInput', {
	'AND': Optional[List['MapAffordancesNodeAggregationWhereInput']],
	'OR': Optional[List['MapAffordancesNodeAggregationWhereInput']],
	'NOT': Optional['MapAffordancesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
})


MapAffordancesUpdateConnectionInput = TypedDict('MapAffordancesUpdateConnectionInput', {
	'node': Optional['AffordanceUpdateInput'],
})


MapAffordancesUpdateFieldInput = TypedDict('MapAffordancesUpdateFieldInput', {
	'where': Optional['MapAffordancesConnectionWhere'],
	'update': Optional['MapAffordancesUpdateConnectionInput'],
	'connect': Optional[List['MapAffordancesConnectFieldInput']],
	'disconnect': Optional[List['MapAffordancesDisconnectFieldInput']],
	'create': Optional[List['MapAffordancesCreateFieldInput']],
	'delete': Optional[List['MapAffordancesDeleteFieldInput']],
	'connectOrCreate': Optional[List['MapAffordancesConnectOrCreateFieldInput']],
})


MapAnnotationsAggregateInput = TypedDict('MapAnnotationsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['MapAnnotationsAggregateInput']],
	'OR': Optional[List['MapAnnotationsAggregateInput']],
	'NOT': Optional['MapAnnotationsAggregateInput'],
	'node': Optional['MapAnnotationsNodeAggregationWhereInput'],
})


MapAnnotationsConnectFieldInput = TypedDict('MapAnnotationsConnectFieldInput', {
	'where': Optional['AnnotationConnectWhere'],
	'overwrite': bool,
})


MapAnnotationsConnectionSort = TypedDict('MapAnnotationsConnectionSort', {
	'node': Optional['AnnotationSort'],
})


MapAnnotationsConnectionWhere = TypedDict('MapAnnotationsConnectionWhere', {
	'AND': Optional[List['MapAnnotationsConnectionWhere']],
	'OR': Optional[List['MapAnnotationsConnectionWhere']],
	'NOT': Optional['MapAnnotationsConnectionWhere'],
	'node': Optional['AnnotationWhere'],
})


MapAnnotationsConnectOrCreateFieldInput = TypedDict('MapAnnotationsConnectOrCreateFieldInput', {
	'where': 'AnnotationConnectOrCreateWhere',
	'onCreate': 'MapAnnotationsConnectOrCreateFieldInputOnCreate',
})


MapAnnotationsConnectOrCreateFieldInputOnCreate = TypedDict('MapAnnotationsConnectOrCreateFieldInputOnCreate', {
	'node': 'AnnotationOnCreateInput',
})


MapAnnotationsCreateFieldInput = TypedDict('MapAnnotationsCreateFieldInput', {
	'node': 'AnnotationCreateInput',
})


MapAnnotationsDeleteFieldInput = TypedDict('MapAnnotationsDeleteFieldInput', {
	'where': Optional['MapAnnotationsConnectionWhere'],
})


MapAnnotationsDisconnectFieldInput = TypedDict('MapAnnotationsDisconnectFieldInput', {
	'where': Optional['MapAnnotationsConnectionWhere'],
})


MapAnnotationsFieldInput = TypedDict('MapAnnotationsFieldInput', {
	'create': Optional[List['MapAnnotationsCreateFieldInput']],
	'connect': Optional[List['MapAnnotationsConnectFieldInput']],
	'connectOrCreate': Optional[List['MapAnnotationsConnectOrCreateFieldInput']],
})


MapAnnotationsNodeAggregationWhereInput = TypedDict('MapAnnotationsNodeAggregationWhereInput', {
	'AND': Optional[List['MapAnnotationsNodeAggregationWhereInput']],
	'OR': Optional[List['MapAnnotationsNodeAggregationWhereInput']],
	'NOT': Optional['MapAnnotationsNodeAggregationWhereInput'],
	'text_AVERAGE_LENGTH_EQUAL': Optional[float],
	'text_LONGEST_LENGTH_EQUAL': Optional[int],
	'text_SHORTEST_LENGTH_EQUAL': Optional[int],
	'text_AVERAGE_LENGTH_GT': Optional[float],
	'text_LONGEST_LENGTH_GT': Optional[int],
	'text_SHORTEST_LENGTH_GT': Optional[int],
	'text_AVERAGE_LENGTH_GTE': Optional[float],
	'text_LONGEST_LENGTH_GTE': Optional[int],
	'text_SHORTEST_LENGTH_GTE': Optional[int],
	'text_AVERAGE_LENGTH_LT': Optional[float],
	'text_LONGEST_LENGTH_LT': Optional[int],
	'text_SHORTEST_LENGTH_LT': Optional[int],
	'text_AVERAGE_LENGTH_LTE': Optional[float],
	'text_LONGEST_LENGTH_LTE': Optional[int],
	'text_SHORTEST_LENGTH_LTE': Optional[int],
})


MapAnnotationsUpdateConnectionInput = TypedDict('MapAnnotationsUpdateConnectionInput', {
	'node': Optional['AnnotationUpdateInput'],
})


MapAnnotationsUpdateFieldInput = TypedDict('MapAnnotationsUpdateFieldInput', {
	'where': Optional['MapAnnotationsConnectionWhere'],
	'update': Optional['MapAnnotationsUpdateConnectionInput'],
	'connect': Optional[List['MapAnnotationsConnectFieldInput']],
	'disconnect': Optional[List['MapAnnotationsDisconnectFieldInput']],
	'create': Optional[List['MapAnnotationsCreateFieldInput']],
	'delete': Optional[List['MapAnnotationsDeleteFieldInput']],
	'connectOrCreate': Optional[List['MapAnnotationsConnectOrCreateFieldInput']],
})


MapConnectInput = TypedDict('MapConnectInput', {
	'visualization': Optional['MapVisualizationConnectFieldInput'],
	'annotations': Optional[List['MapAnnotationsConnectFieldInput']],
	'affordances': Optional[List['MapAffordancesConnectFieldInput']],
	'sessions': Optional[List['MapSessionsConnectFieldInput']],
	'users': Optional[List['MapUsersConnectFieldInput']],
	'workflows': Optional[List['MapWorkflowsConnectFieldInput']],
})


MapConnectOrCreateInput = TypedDict('MapConnectOrCreateInput', {
	'annotations': Optional[List['MapAnnotationsConnectOrCreateFieldInput']],
	'affordances': Optional[List['MapAffordancesConnectOrCreateFieldInput']],
	'sessions': Optional[List['MapSessionsConnectOrCreateFieldInput']],
	'workflows': Optional[List['MapWorkflowsConnectOrCreateFieldInput']],
})


MapConnectOrCreateWhere = TypedDict('MapConnectOrCreateWhere', {
	'node': 'MapUniqueWhere',
})


MapConnectWhere = TypedDict('MapConnectWhere', {
	'node': 'MapWhere',
})


MapCreateInput = TypedDict('MapCreateInput', {
	'label': str,
	'description': Optional[str],
	'status': str,
	'data': Optional['B64JSON'],
	'thumbnailId': Optional['UUID'],
	'exportedMapId': Optional['UUID'],
	'visualization': Optional['MapVisualizationFieldInput'],
	'annotations': Optional['MapAnnotationsFieldInput'],
	'affordances': Optional['MapAffordancesFieldInput'],
	'sessions': Optional['MapSessionsFieldInput'],
	'users': Optional['MapUsersFieldInput'],
	'workflows': Optional['MapWorkflowsFieldInput'],
})


MapDeleteInput = TypedDict('MapDeleteInput', {
	'visualization': Optional['MapVisualizationDeleteFieldInput'],
	'annotations': Optional[List['MapAnnotationsDeleteFieldInput']],
	'affordances': Optional[List['MapAffordancesDeleteFieldInput']],
	'sessions': Optional[List['MapSessionsDeleteFieldInput']],
	'workflows': Optional[List['MapWorkflowsDeleteFieldInput']],
})


MapDisconnectInput = TypedDict('MapDisconnectInput', {
	'visualization': Optional['MapVisualizationDisconnectFieldInput'],
	'annotations': Optional[List['MapAnnotationsDisconnectFieldInput']],
	'affordances': Optional[List['MapAffordancesDisconnectFieldInput']],
	'sessions': Optional[List['MapSessionsDisconnectFieldInput']],
	'users': Optional[List['MapUsersDisconnectFieldInput']],
	'workflows': Optional[List['MapWorkflowsDisconnectFieldInput']],
})


MapOnCreateInput = TypedDict('MapOnCreateInput', {
	'label': str,
	'description': Optional[str],
	'status': str,
	'data': Optional['B64JSON'],
	'thumbnailId': Optional['UUID'],
	'exportedMapId': Optional['UUID'],
})


MapOptions = TypedDict('MapOptions', {
	'sort': Optional[List['MapSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


MapRelationInput = TypedDict('MapRelationInput', {
	'visualization': Optional['MapVisualizationCreateFieldInput'],
	'annotations': Optional[List['MapAnnotationsCreateFieldInput']],
	'affordances': Optional[List['MapAffordancesCreateFieldInput']],
	'sessions': Optional[List['MapSessionsCreateFieldInput']],
	'workflows': Optional[List['MapWorkflowsCreateFieldInput']],
})


MapSessionsAggregateInput = TypedDict('MapSessionsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['MapSessionsAggregateInput']],
	'OR': Optional[List['MapSessionsAggregateInput']],
	'NOT': Optional['MapSessionsAggregateInput'],
	'node': Optional['MapSessionsNodeAggregationWhereInput'],
})


MapSessionsConnectFieldInput = TypedDict('MapSessionsConnectFieldInput', {
	'where': Optional['SessionConnectWhere'],
	'connect': Optional[List['SessionConnectInput']],
	'overwrite': bool,
})


MapSessionsConnectionSort = TypedDict('MapSessionsConnectionSort', {
	'node': Optional['SessionSort'],
})


MapSessionsConnectionWhere = TypedDict('MapSessionsConnectionWhere', {
	'AND': Optional[List['MapSessionsConnectionWhere']],
	'OR': Optional[List['MapSessionsConnectionWhere']],
	'NOT': Optional['MapSessionsConnectionWhere'],
	'node': Optional['SessionWhere'],
})


MapSessionsConnectOrCreateFieldInput = TypedDict('MapSessionsConnectOrCreateFieldInput', {
	'where': 'SessionConnectOrCreateWhere',
	'onCreate': 'MapSessionsConnectOrCreateFieldInputOnCreate',
})


MapSessionsConnectOrCreateFieldInputOnCreate = TypedDict('MapSessionsConnectOrCreateFieldInputOnCreate', {
	'node': 'SessionOnCreateInput',
})


MapSessionsCreateFieldInput = TypedDict('MapSessionsCreateFieldInput', {
	'node': 'SessionCreateInput',
})


MapSessionsDeleteFieldInput = TypedDict('MapSessionsDeleteFieldInput', {
	'where': Optional['MapSessionsConnectionWhere'],
	'delete': Optional['SessionDeleteInput'],
})


MapSessionsDisconnectFieldInput = TypedDict('MapSessionsDisconnectFieldInput', {
	'where': Optional['MapSessionsConnectionWhere'],
	'disconnect': Optional['SessionDisconnectInput'],
})


MapSessionsFieldInput = TypedDict('MapSessionsFieldInput', {
	'create': Optional[List['MapSessionsCreateFieldInput']],
	'connect': Optional[List['MapSessionsConnectFieldInput']],
	'connectOrCreate': Optional[List['MapSessionsConnectOrCreateFieldInput']],
})


MapSessionsNodeAggregationWhereInput = TypedDict('MapSessionsNodeAggregationWhereInput', {
	'AND': Optional[List['MapSessionsNodeAggregationWhereInput']],
	'OR': Optional[List['MapSessionsNodeAggregationWhereInput']],
	'NOT': Optional['MapSessionsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


MapSessionsUpdateConnectionInput = TypedDict('MapSessionsUpdateConnectionInput', {
	'node': Optional['SessionUpdateInput'],
})


MapSessionsUpdateFieldInput = TypedDict('MapSessionsUpdateFieldInput', {
	'where': Optional['MapSessionsConnectionWhere'],
	'update': Optional['MapSessionsUpdateConnectionInput'],
	'connect': Optional[List['MapSessionsConnectFieldInput']],
	'disconnect': Optional[List['MapSessionsDisconnectFieldInput']],
	'create': Optional[List['MapSessionsCreateFieldInput']],
	'delete': Optional[List['MapSessionsDeleteFieldInput']],
	'connectOrCreate': Optional[List['MapSessionsConnectOrCreateFieldInput']],
})


MapSort = TypedDict('MapSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'description': Optional['SortDirection'],
	'status': Optional['SortDirection'],
	'data': Optional['SortDirection'],
	'thumbnailId': Optional['SortDirection'],
	'exportedMapId': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
})


MapUniqueWhere = TypedDict('MapUniqueWhere', {
	'id': Optional[str],
})


MapUpdateInput = TypedDict('MapUpdateInput', {
	'label': Optional[str],
	'description': Optional[str],
	'status': Optional[str],
	'data': Optional['B64JSON'],
	'thumbnailId': Optional['UUID'],
	'exportedMapId': Optional['UUID'],
	'visualization': Optional['MapVisualizationUpdateFieldInput'],
	'annotations': Optional[List['MapAnnotationsUpdateFieldInput']],
	'affordances': Optional[List['MapAffordancesUpdateFieldInput']],
	'sessions': Optional[List['MapSessionsUpdateFieldInput']],
	'users': Optional[List['MapUsersUpdateFieldInput']],
	'workflows': Optional[List['MapWorkflowsUpdateFieldInput']],
})


MapUsersAggregateInput = TypedDict('MapUsersAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['MapUsersAggregateInput']],
	'OR': Optional[List['MapUsersAggregateInput']],
	'NOT': Optional['MapUsersAggregateInput'],
	'node': Optional['MapUsersNodeAggregationWhereInput'],
	'edge': Optional['MapUsersEdgeAggregationWhereInput'],
})


MapUsersConnectFieldInput = TypedDict('MapUsersConnectFieldInput', {
	'where': Optional['UserConnectWhere'],
	'connect': Optional[List['UserConnectInput']],
	'edge': 'UserMapRoleCreateInput',
	'overwrite': bool,
})


MapUsersConnectionSort = TypedDict('MapUsersConnectionSort', {
	'edge': Optional['UserMapRoleSort'],
	'node': Optional['UserSort'],
})


MapUsersConnectionWhere = TypedDict('MapUsersConnectionWhere', {
	'AND': Optional[List['MapUsersConnectionWhere']],
	'OR': Optional[List['MapUsersConnectionWhere']],
	'NOT': Optional['MapUsersConnectionWhere'],
	'edge': Optional['UserMapRoleWhere'],
	'node': Optional['UserWhere'],
})


MapUsersConnectOrCreateFieldInputOnCreate = TypedDict('MapUsersConnectOrCreateFieldInputOnCreate', {
	'node': 'UserOnCreateInput',
	'edge': 'UserMapRoleCreateInput',
})


MapUsersDisconnectFieldInput = TypedDict('MapUsersDisconnectFieldInput', {
	'where': Optional['MapUsersConnectionWhere'],
	'disconnect': Optional['UserDisconnectInput'],
})


MapUsersEdgeAggregationWhereInput = TypedDict('MapUsersEdgeAggregationWhereInput', {
	'AND': Optional[List['MapUsersEdgeAggregationWhereInput']],
	'OR': Optional[List['MapUsersEdgeAggregationWhereInput']],
	'NOT': Optional['MapUsersEdgeAggregationWhereInput'],
	'role_AVERAGE_LENGTH_EQUAL': Optional[float],
	'role_LONGEST_LENGTH_EQUAL': Optional[int],
	'role_SHORTEST_LENGTH_EQUAL': Optional[int],
	'role_AVERAGE_LENGTH_GT': Optional[float],
	'role_LONGEST_LENGTH_GT': Optional[int],
	'role_SHORTEST_LENGTH_GT': Optional[int],
	'role_AVERAGE_LENGTH_GTE': Optional[float],
	'role_LONGEST_LENGTH_GTE': Optional[int],
	'role_SHORTEST_LENGTH_GTE': Optional[int],
	'role_AVERAGE_LENGTH_LT': Optional[float],
	'role_LONGEST_LENGTH_LT': Optional[int],
	'role_SHORTEST_LENGTH_LT': Optional[int],
	'role_AVERAGE_LENGTH_LTE': Optional[float],
	'role_LONGEST_LENGTH_LTE': Optional[int],
	'role_SHORTEST_LENGTH_LTE': Optional[int],
})


MapUsersFieldInput = TypedDict('MapUsersFieldInput', {
	'connect': Optional[List['MapUsersConnectFieldInput']],
})


MapUsersNodeAggregationWhereInput = TypedDict('MapUsersNodeAggregationWhereInput', {
	'AND': Optional[List['MapUsersNodeAggregationWhereInput']],
	'OR': Optional[List['MapUsersNodeAggregationWhereInput']],
	'NOT': Optional['MapUsersNodeAggregationWhereInput'],
	'sub_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sub_LONGEST_LENGTH_EQUAL': Optional[int],
	'sub_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sub_AVERAGE_LENGTH_GT': Optional[float],
	'sub_LONGEST_LENGTH_GT': Optional[int],
	'sub_SHORTEST_LENGTH_GT': Optional[int],
	'sub_AVERAGE_LENGTH_GTE': Optional[float],
	'sub_LONGEST_LENGTH_GTE': Optional[int],
	'sub_SHORTEST_LENGTH_GTE': Optional[int],
	'sub_AVERAGE_LENGTH_LT': Optional[float],
	'sub_LONGEST_LENGTH_LT': Optional[int],
	'sub_SHORTEST_LENGTH_LT': Optional[int],
	'sub_AVERAGE_LENGTH_LTE': Optional[float],
	'sub_LONGEST_LENGTH_LTE': Optional[int],
	'sub_SHORTEST_LENGTH_LTE': Optional[int],
	'givenName_AVERAGE_LENGTH_EQUAL': Optional[float],
	'givenName_LONGEST_LENGTH_EQUAL': Optional[int],
	'givenName_SHORTEST_LENGTH_EQUAL': Optional[int],
	'givenName_AVERAGE_LENGTH_GT': Optional[float],
	'givenName_LONGEST_LENGTH_GT': Optional[int],
	'givenName_SHORTEST_LENGTH_GT': Optional[int],
	'givenName_AVERAGE_LENGTH_GTE': Optional[float],
	'givenName_LONGEST_LENGTH_GTE': Optional[int],
	'givenName_SHORTEST_LENGTH_GTE': Optional[int],
	'givenName_AVERAGE_LENGTH_LT': Optional[float],
	'givenName_LONGEST_LENGTH_LT': Optional[int],
	'givenName_SHORTEST_LENGTH_LT': Optional[int],
	'givenName_AVERAGE_LENGTH_LTE': Optional[float],
	'givenName_LONGEST_LENGTH_LTE': Optional[int],
	'givenName_SHORTEST_LENGTH_LTE': Optional[int],
	'familyName_AVERAGE_LENGTH_EQUAL': Optional[float],
	'familyName_LONGEST_LENGTH_EQUAL': Optional[int],
	'familyName_SHORTEST_LENGTH_EQUAL': Optional[int],
	'familyName_AVERAGE_LENGTH_GT': Optional[float],
	'familyName_LONGEST_LENGTH_GT': Optional[int],
	'familyName_SHORTEST_LENGTH_GT': Optional[int],
	'familyName_AVERAGE_LENGTH_GTE': Optional[float],
	'familyName_LONGEST_LENGTH_GTE': Optional[int],
	'familyName_SHORTEST_LENGTH_GTE': Optional[int],
	'familyName_AVERAGE_LENGTH_LT': Optional[float],
	'familyName_LONGEST_LENGTH_LT': Optional[int],
	'familyName_SHORTEST_LENGTH_LT': Optional[int],
	'familyName_AVERAGE_LENGTH_LTE': Optional[float],
	'familyName_LONGEST_LENGTH_LTE': Optional[int],
	'familyName_SHORTEST_LENGTH_LTE': Optional[int],
	'status_AVERAGE_LENGTH_EQUAL': Optional[float],
	'status_LONGEST_LENGTH_EQUAL': Optional[int],
	'status_SHORTEST_LENGTH_EQUAL': Optional[int],
	'status_AVERAGE_LENGTH_GT': Optional[float],
	'status_LONGEST_LENGTH_GT': Optional[int],
	'status_SHORTEST_LENGTH_GT': Optional[int],
	'status_AVERAGE_LENGTH_GTE': Optional[float],
	'status_LONGEST_LENGTH_GTE': Optional[int],
	'status_SHORTEST_LENGTH_GTE': Optional[int],
	'status_AVERAGE_LENGTH_LT': Optional[float],
	'status_LONGEST_LENGTH_LT': Optional[int],
	'status_SHORTEST_LENGTH_LT': Optional[int],
	'status_AVERAGE_LENGTH_LTE': Optional[float],
	'status_LONGEST_LENGTH_LTE': Optional[int],
	'status_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_LTE': Optional['DateTime'],
})


MapUsersUpdateFieldInput = TypedDict('MapUsersUpdateFieldInput', {
	'where': Optional['MapUsersConnectionWhere'],
	'connect': Optional[List['MapUsersConnectFieldInput']],
	'disconnect': Optional[List['MapUsersDisconnectFieldInput']],
})


MapVisualizationAggregateInput = TypedDict('MapVisualizationAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['MapVisualizationAggregateInput']],
	'OR': Optional[List['MapVisualizationAggregateInput']],
	'NOT': Optional['MapVisualizationAggregateInput'],
})


MapVisualizationConnectFieldInput = TypedDict('MapVisualizationConnectFieldInput', {
	'where': Optional['VisualizationBlobConnectWhere'],
	'overwrite': bool,
})


MapVisualizationConnectionSort = TypedDict('MapVisualizationConnectionSort', {
	'node': Optional['VisualizationBlobSort'],
})


MapVisualizationConnectionWhere = TypedDict('MapVisualizationConnectionWhere', {
	'AND': Optional[List['MapVisualizationConnectionWhere']],
	'OR': Optional[List['MapVisualizationConnectionWhere']],
	'NOT': Optional['MapVisualizationConnectionWhere'],
	'node': Optional['VisualizationBlobWhere'],
})


MapVisualizationCreateFieldInput = TypedDict('MapVisualizationCreateFieldInput', {
	'node': 'VisualizationBlobCreateInput',
})


MapVisualizationDeleteFieldInput = TypedDict('MapVisualizationDeleteFieldInput', {
	'where': Optional['MapVisualizationConnectionWhere'],
})


MapVisualizationDisconnectFieldInput = TypedDict('MapVisualizationDisconnectFieldInput', {
	'where': Optional['MapVisualizationConnectionWhere'],
})


MapVisualizationFieldInput = TypedDict('MapVisualizationFieldInput', {
	'create': Optional['MapVisualizationCreateFieldInput'],
	'connect': Optional['MapVisualizationConnectFieldInput'],
})


MapVisualizationUpdateConnectionInput = TypedDict('MapVisualizationUpdateConnectionInput', {
	'node': Optional['VisualizationBlobUpdateInput'],
})


MapVisualizationUpdateFieldInput = TypedDict('MapVisualizationUpdateFieldInput', {
	'where': Optional['MapVisualizationConnectionWhere'],
	'update': Optional['MapVisualizationUpdateConnectionInput'],
	'connect': Optional['MapVisualizationConnectFieldInput'],
	'disconnect': Optional['MapVisualizationDisconnectFieldInput'],
	'create': Optional['MapVisualizationCreateFieldInput'],
	'delete': Optional['MapVisualizationDeleteFieldInput'],
})


MapWhere = TypedDict('MapWhere', {
	'OR': Optional[List['MapWhere']],
	'AND': Optional[List['MapWhere']],
	'NOT': Optional['MapWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'description': Optional[str],
	'description_IN': Optional[List[str]],
	'description_MATCHES': Optional[str],
	'description_CONTAINS': Optional[str],
	'description_STARTS_WITH': Optional[str],
	'description_ENDS_WITH': Optional[str],
	'status': Optional[str],
	'status_IN': Optional[List[str]],
	'status_MATCHES': Optional[str],
	'status_CONTAINS': Optional[str],
	'status_STARTS_WITH': Optional[str],
	'status_ENDS_WITH': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'data': Optional['B64JSON'],
	'data_IN': Optional[List['B64JSON']],
	'thumbnailId': Optional['UUID'],
	'thumbnailId_IN': Optional[List['UUID']],
	'exportedMapId': Optional['UUID'],
	'exportedMapId_IN': Optional[List['UUID']],
	'visualizationAggregate': Optional['MapVisualizationAggregateInput'],
	'annotationsAggregate': Optional['MapAnnotationsAggregateInput'],
	'annotations_ALL': Optional['AnnotationWhere'],
	'annotations_NONE': Optional['AnnotationWhere'],
	'annotations_SINGLE': Optional['AnnotationWhere'],
	'annotations_SOME': Optional['AnnotationWhere'],
	'affordancesAggregate': Optional['MapAffordancesAggregateInput'],
	'affordances_ALL': Optional['AffordanceWhere'],
	'affordances_NONE': Optional['AffordanceWhere'],
	'affordances_SINGLE': Optional['AffordanceWhere'],
	'affordances_SOME': Optional['AffordanceWhere'],
	'sessionsAggregate': Optional['MapSessionsAggregateInput'],
	'sessions_ALL': Optional['SessionWhere'],
	'sessions_NONE': Optional['SessionWhere'],
	'sessions_SINGLE': Optional['SessionWhere'],
	'sessions_SOME': Optional['SessionWhere'],
	'usersAggregate': Optional['MapUsersAggregateInput'],
	'users_ALL': Optional['UserWhere'],
	'users_NONE': Optional['UserWhere'],
	'users_SINGLE': Optional['UserWhere'],
	'users_SOME': Optional['UserWhere'],
	'workflowsAggregate': Optional['MapWorkflowsAggregateInput'],
	'workflows_ALL': Optional['WorkflowWhere'],
	'workflows_NONE': Optional['WorkflowWhere'],
	'workflows_SINGLE': Optional['WorkflowWhere'],
	'workflows_SOME': Optional['WorkflowWhere'],
	'visualizationConnection': Optional['MapVisualizationConnectionWhere'],
	'annotationsConnection_ALL': Optional['MapAnnotationsConnectionWhere'],
	'annotationsConnection_NONE': Optional['MapAnnotationsConnectionWhere'],
	'annotationsConnection_SINGLE': Optional['MapAnnotationsConnectionWhere'],
	'annotationsConnection_SOME': Optional['MapAnnotationsConnectionWhere'],
	'affordancesConnection_ALL': Optional['MapAffordancesConnectionWhere'],
	'affordancesConnection_NONE': Optional['MapAffordancesConnectionWhere'],
	'affordancesConnection_SINGLE': Optional['MapAffordancesConnectionWhere'],
	'affordancesConnection_SOME': Optional['MapAffordancesConnectionWhere'],
	'sessionsConnection_ALL': Optional['MapSessionsConnectionWhere'],
	'sessionsConnection_NONE': Optional['MapSessionsConnectionWhere'],
	'sessionsConnection_SINGLE': Optional['MapSessionsConnectionWhere'],
	'sessionsConnection_SOME': Optional['MapSessionsConnectionWhere'],
	'usersConnection_ALL': Optional['MapUsersConnectionWhere'],
	'usersConnection_NONE': Optional['MapUsersConnectionWhere'],
	'usersConnection_SINGLE': Optional['MapUsersConnectionWhere'],
	'usersConnection_SOME': Optional['MapUsersConnectionWhere'],
	'workflowsConnection_ALL': Optional['MapWorkflowsConnectionWhere'],
	'workflowsConnection_NONE': Optional['MapWorkflowsConnectionWhere'],
	'workflowsConnection_SINGLE': Optional['MapWorkflowsConnectionWhere'],
	'workflowsConnection_SOME': Optional['MapWorkflowsConnectionWhere'],
})


MapWorkflowsAggregateInput = TypedDict('MapWorkflowsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['MapWorkflowsAggregateInput']],
	'OR': Optional[List['MapWorkflowsAggregateInput']],
	'NOT': Optional['MapWorkflowsAggregateInput'],
	'node': Optional['MapWorkflowsNodeAggregationWhereInput'],
})


MapWorkflowsConnectFieldInput = TypedDict('MapWorkflowsConnectFieldInput', {
	'where': Optional['WorkflowConnectWhere'],
	'connect': Optional[List['WorkflowConnectInput']],
	'overwrite': bool,
})


MapWorkflowsConnectionSort = TypedDict('MapWorkflowsConnectionSort', {
	'node': Optional['WorkflowSort'],
})


MapWorkflowsConnectionWhere = TypedDict('MapWorkflowsConnectionWhere', {
	'AND': Optional[List['MapWorkflowsConnectionWhere']],
	'OR': Optional[List['MapWorkflowsConnectionWhere']],
	'NOT': Optional['MapWorkflowsConnectionWhere'],
	'node': Optional['WorkflowWhere'],
})


MapWorkflowsConnectOrCreateFieldInput = TypedDict('MapWorkflowsConnectOrCreateFieldInput', {
	'where': 'WorkflowConnectOrCreateWhere',
	'onCreate': 'MapWorkflowsConnectOrCreateFieldInputOnCreate',
})


MapWorkflowsConnectOrCreateFieldInputOnCreate = TypedDict('MapWorkflowsConnectOrCreateFieldInputOnCreate', {
	'node': 'WorkflowOnCreateInput',
})


MapWorkflowsCreateFieldInput = TypedDict('MapWorkflowsCreateFieldInput', {
	'node': 'WorkflowCreateInput',
})


MapWorkflowsDeleteFieldInput = TypedDict('MapWorkflowsDeleteFieldInput', {
	'where': Optional['MapWorkflowsConnectionWhere'],
	'delete': Optional['WorkflowDeleteInput'],
})


MapWorkflowsDisconnectFieldInput = TypedDict('MapWorkflowsDisconnectFieldInput', {
	'where': Optional['MapWorkflowsConnectionWhere'],
	'disconnect': Optional['WorkflowDisconnectInput'],
})


MapWorkflowsFieldInput = TypedDict('MapWorkflowsFieldInput', {
	'create': Optional[List['MapWorkflowsCreateFieldInput']],
	'connect': Optional[List['MapWorkflowsConnectFieldInput']],
	'connectOrCreate': Optional[List['MapWorkflowsConnectOrCreateFieldInput']],
})


MapWorkflowsNodeAggregationWhereInput = TypedDict('MapWorkflowsNodeAggregationWhereInput', {
	'AND': Optional[List['MapWorkflowsNodeAggregationWhereInput']],
	'OR': Optional[List['MapWorkflowsNodeAggregationWhereInput']],
	'NOT': Optional['MapWorkflowsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'status_AVERAGE_LENGTH_EQUAL': Optional[float],
	'status_LONGEST_LENGTH_EQUAL': Optional[int],
	'status_SHORTEST_LENGTH_EQUAL': Optional[int],
	'status_AVERAGE_LENGTH_GT': Optional[float],
	'status_LONGEST_LENGTH_GT': Optional[int],
	'status_SHORTEST_LENGTH_GT': Optional[int],
	'status_AVERAGE_LENGTH_GTE': Optional[float],
	'status_LONGEST_LENGTH_GTE': Optional[int],
	'status_SHORTEST_LENGTH_GTE': Optional[int],
	'status_AVERAGE_LENGTH_LT': Optional[float],
	'status_LONGEST_LENGTH_LT': Optional[int],
	'status_SHORTEST_LENGTH_LT': Optional[int],
	'status_AVERAGE_LENGTH_LTE': Optional[float],
	'status_LONGEST_LENGTH_LTE': Optional[int],
	'status_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


MapWorkflowsUpdateConnectionInput = TypedDict('MapWorkflowsUpdateConnectionInput', {
	'node': Optional['WorkflowUpdateInput'],
})


MapWorkflowsUpdateFieldInput = TypedDict('MapWorkflowsUpdateFieldInput', {
	'where': Optional['MapWorkflowsConnectionWhere'],
	'update': Optional['MapWorkflowsUpdateConnectionInput'],
	'connect': Optional[List['MapWorkflowsConnectFieldInput']],
	'disconnect': Optional[List['MapWorkflowsDisconnectFieldInput']],
	'create': Optional[List['MapWorkflowsCreateFieldInput']],
	'delete': Optional[List['MapWorkflowsDeleteFieldInput']],
	'connectOrCreate': Optional[List['MapWorkflowsConnectOrCreateFieldInput']],
})


PointDistance = TypedDict('PointDistance', {
	'point': 'PointInput',
	'distance': float,
})


PointInput = TypedDict('PointInput', {
	'longitude': float,
	'latitude': float,
	'height': Optional[float],
})


PPEConnectInput = TypedDict('PPEConnectInput', {
	'variable': Optional['PPEVariableConnectFieldInput'],
})


PPEConnectOrCreateInput = TypedDict('PPEConnectOrCreateInput', {
	'variable': Optional['PPEVariableConnectOrCreateFieldInput'],
})


PPEConnectOrCreateWhere = TypedDict('PPEConnectOrCreateWhere', {
	'node': 'PPEUniqueWhere',
})


PPEConnectWhere = TypedDict('PPEConnectWhere', {
	'node': 'PPEWhere',
})


PPECreateInput = TypedDict('PPECreateInput', {
	'solveKey': str,
	'suggested': Optional[List[float]],
	'max': Optional[List[float]],
	'mean': Optional[List[float]],
	'_type': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'variableLabel': str,
	'suggested_cartesian': Optional['PointInput'],
	'max_cartesian': Optional['PointInput'],
	'mean_cartesian': Optional['PointInput'],
	'variable': Optional['PPEVariableFieldInput'],
})


PPEDeleteInput = TypedDict('PPEDeleteInput', {
	'variable': Optional['PPEVariableDeleteFieldInput'],
})


PPEDisconnectInput = TypedDict('PPEDisconnectInput', {
	'variable': Optional['PPEVariableDisconnectFieldInput'],
})


PPEOnCreateInput = TypedDict('PPEOnCreateInput', {
	'solveKey': str,
	'suggested': Optional[List[float]],
	'max': Optional[List[float]],
	'mean': Optional[List[float]],
	'_type': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'variableLabel': str,
	'suggested_cartesian': Optional['PointInput'],
	'max_cartesian': Optional['PointInput'],
	'mean_cartesian': Optional['PointInput'],
})


PPEOptions = TypedDict('PPEOptions', {
	'sort': Optional[List['PPESort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


PPERelationInput = TypedDict('PPERelationInput', {
	'variable': Optional['PPEVariableCreateFieldInput'],
})


PPESort = TypedDict('PPESort', {
	'id': Optional['SortDirection'],
	'solveKey': Optional['SortDirection'],
	'_type': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'robotLabel': Optional['SortDirection'],
	'sessionLabel': Optional['SortDirection'],
	'variableLabel': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
	'suggested_cartesian': Optional['SortDirection'],
	'max_cartesian': Optional['SortDirection'],
	'mean_cartesian': Optional['SortDirection'],
})


PPEUniqueWhere = TypedDict('PPEUniqueWhere', {
	'id': Optional[str],
})


PPEUpdateInput = TypedDict('PPEUpdateInput', {
	'solveKey': Optional[str],
	'suggested': Optional[List[float]],
	'max': Optional[List[float]],
	'mean': Optional[List[float]],
	'_type': Optional[str],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'variableLabel': Optional[str],
	'suggested_cartesian': Optional['PointInput'],
	'max_cartesian': Optional['PointInput'],
	'mean_cartesian': Optional['PointInput'],
	'suggested_POP': Optional[int],
	'suggested_PUSH': Optional[List[float]],
	'max_POP': Optional[int],
	'max_PUSH': Optional[List[float]],
	'mean_POP': Optional[int],
	'mean_PUSH': Optional[List[float]],
	'variable': Optional['PPEVariableUpdateFieldInput'],
})


PPEVariableAggregateInput = TypedDict('PPEVariableAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['PPEVariableAggregateInput']],
	'OR': Optional[List['PPEVariableAggregateInput']],
	'NOT': Optional['PPEVariableAggregateInput'],
	'node': Optional['PPEVariableNodeAggregationWhereInput'],
})


PPEVariableConnectFieldInput = TypedDict('PPEVariableConnectFieldInput', {
	'where': Optional['VariableConnectWhere'],
	'connect': Optional['VariableConnectInput'],
	'overwrite': bool,
})


PPEVariableConnectionSort = TypedDict('PPEVariableConnectionSort', {
	'node': Optional['VariableSort'],
})


PPEVariableConnectionWhere = TypedDict('PPEVariableConnectionWhere', {
	'AND': Optional[List['PPEVariableConnectionWhere']],
	'OR': Optional[List['PPEVariableConnectionWhere']],
	'NOT': Optional['PPEVariableConnectionWhere'],
	'node': Optional['VariableWhere'],
})


PPEVariableConnectOrCreateFieldInput = TypedDict('PPEVariableConnectOrCreateFieldInput', {
	'where': 'VariableConnectOrCreateWhere',
	'onCreate': 'PPEVariableConnectOrCreateFieldInputOnCreate',
})


PPEVariableConnectOrCreateFieldInputOnCreate = TypedDict('PPEVariableConnectOrCreateFieldInputOnCreate', {
	'node': 'VariableOnCreateInput',
})


PPEVariableCreateFieldInput = TypedDict('PPEVariableCreateFieldInput', {
	'node': 'VariableCreateInput',
})


PPEVariableDeleteFieldInput = TypedDict('PPEVariableDeleteFieldInput', {
	'where': Optional['PPEVariableConnectionWhere'],
	'delete': Optional['VariableDeleteInput'],
})


PPEVariableDisconnectFieldInput = TypedDict('PPEVariableDisconnectFieldInput', {
	'where': Optional['PPEVariableConnectionWhere'],
	'disconnect': Optional['VariableDisconnectInput'],
})


PPEVariableFieldInput = TypedDict('PPEVariableFieldInput', {
	'create': Optional['PPEVariableCreateFieldInput'],
	'connect': Optional['PPEVariableConnectFieldInput'],
	'connectOrCreate': Optional['PPEVariableConnectOrCreateFieldInput'],
})


PPEVariableNodeAggregationWhereInput = TypedDict('PPEVariableNodeAggregationWhereInput', {
	'AND': Optional[List['PPEVariableNodeAggregationWhereInput']],
	'OR': Optional[List['PPEVariableNodeAggregationWhereInput']],
	'NOT': Optional['PPEVariableNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


PPEVariableUpdateConnectionInput = TypedDict('PPEVariableUpdateConnectionInput', {
	'node': Optional['VariableUpdateInput'],
})


PPEVariableUpdateFieldInput = TypedDict('PPEVariableUpdateFieldInput', {
	'where': Optional['PPEVariableConnectionWhere'],
	'update': Optional['PPEVariableUpdateConnectionInput'],
	'connect': Optional['PPEVariableConnectFieldInput'],
	'disconnect': Optional['PPEVariableDisconnectFieldInput'],
	'create': Optional['PPEVariableCreateFieldInput'],
	'delete': Optional['PPEVariableDeleteFieldInput'],
	'connectOrCreate': Optional['PPEVariableConnectOrCreateFieldInput'],
})


PPEWhere = TypedDict('PPEWhere', {
	'OR': Optional[List['PPEWhere']],
	'AND': Optional[List['PPEWhere']],
	'NOT': Optional['PPEWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'solveKey': Optional[str],
	'solveKey_IN': Optional[List[str]],
	'solveKey_MATCHES': Optional[str],
	'solveKey_CONTAINS': Optional[str],
	'solveKey_STARTS_WITH': Optional[str],
	'solveKey_ENDS_WITH': Optional[str],
	'suggested': Optional[List[float]],
	'suggested_INCLUDES': Optional[float],
	'max': Optional[List[float]],
	'max_INCLUDES': Optional[float],
	'mean': Optional[List[float]],
	'mean_INCLUDES': Optional[float],
	'_type': Optional[str],
	'_type_IN': Optional[List[str]],
	'_type_MATCHES': Optional[str],
	'_type_CONTAINS': Optional[str],
	'_type_STARTS_WITH': Optional[str],
	'_type_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'robotLabel': Optional[str],
	'robotLabel_IN': Optional[List[str]],
	'robotLabel_MATCHES': Optional[str],
	'robotLabel_CONTAINS': Optional[str],
	'robotLabel_STARTS_WITH': Optional[str],
	'robotLabel_ENDS_WITH': Optional[str],
	'sessionLabel': Optional[str],
	'sessionLabel_IN': Optional[List[str]],
	'sessionLabel_MATCHES': Optional[str],
	'sessionLabel_CONTAINS': Optional[str],
	'sessionLabel_STARTS_WITH': Optional[str],
	'sessionLabel_ENDS_WITH': Optional[str],
	'variableLabel': Optional[str],
	'variableLabel_IN': Optional[List[str]],
	'variableLabel_MATCHES': Optional[str],
	'variableLabel_CONTAINS': Optional[str],
	'variableLabel_STARTS_WITH': Optional[str],
	'variableLabel_ENDS_WITH': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'suggested_cartesian': Optional['PointInput'],
	'suggested_cartesian_IN': Optional[List['PointInput']],
	'suggested_cartesian_DISTANCE': Optional['PointDistance'],
	'suggested_cartesian_LT': Optional['PointDistance'],
	'suggested_cartesian_LTE': Optional['PointDistance'],
	'suggested_cartesian_GT': Optional['PointDistance'],
	'suggested_cartesian_GTE': Optional['PointDistance'],
	'max_cartesian': Optional['PointInput'],
	'max_cartesian_IN': Optional[List['PointInput']],
	'max_cartesian_DISTANCE': Optional['PointDistance'],
	'max_cartesian_LT': Optional['PointDistance'],
	'max_cartesian_LTE': Optional['PointDistance'],
	'max_cartesian_GT': Optional['PointDistance'],
	'max_cartesian_GTE': Optional['PointDistance'],
	'mean_cartesian': Optional['PointInput'],
	'mean_cartesian_IN': Optional[List['PointInput']],
	'mean_cartesian_DISTANCE': Optional['PointDistance'],
	'mean_cartesian_LT': Optional['PointDistance'],
	'mean_cartesian_LTE': Optional['PointDistance'],
	'mean_cartesian_GT': Optional['PointDistance'],
	'mean_cartesian_GTE': Optional['PointDistance'],
	'variableAggregate': Optional['PPEVariableAggregateInput'],
	'variableConnection': Optional['PPEVariableConnectionWhere'],
})


RobotBlobEntriesAggregateInput = TypedDict('RobotBlobEntriesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['RobotBlobEntriesAggregateInput']],
	'OR': Optional[List['RobotBlobEntriesAggregateInput']],
	'NOT': Optional['RobotBlobEntriesAggregateInput'],
	'node': Optional['RobotBlobEntriesNodeAggregationWhereInput'],
})


RobotBlobEntriesConnectFieldInput = TypedDict('RobotBlobEntriesConnectFieldInput', {
	'where': Optional['BlobEntryConnectWhere'],
	'connect': Optional[List['BlobEntryConnectInput']],
	'overwrite': bool,
})


RobotBlobEntriesConnectionSort = TypedDict('RobotBlobEntriesConnectionSort', {
	'node': Optional['BlobEntrySort'],
})


RobotBlobEntriesConnectionWhere = TypedDict('RobotBlobEntriesConnectionWhere', {
	'AND': Optional[List['RobotBlobEntriesConnectionWhere']],
	'OR': Optional[List['RobotBlobEntriesConnectionWhere']],
	'NOT': Optional['RobotBlobEntriesConnectionWhere'],
	'node': Optional['BlobEntryWhere'],
})


RobotBlobEntriesConnectOrCreateFieldInput = TypedDict('RobotBlobEntriesConnectOrCreateFieldInput', {
	'where': 'BlobEntryConnectOrCreateWhere',
	'onCreate': 'RobotBlobEntriesConnectOrCreateFieldInputOnCreate',
})


RobotBlobEntriesConnectOrCreateFieldInputOnCreate = TypedDict('RobotBlobEntriesConnectOrCreateFieldInputOnCreate', {
	'node': 'BlobEntryOnCreateInput',
})


RobotBlobEntriesCreateFieldInput = TypedDict('RobotBlobEntriesCreateFieldInput', {
	'node': 'BlobEntryCreateInput',
})


RobotBlobEntriesDeleteFieldInput = TypedDict('RobotBlobEntriesDeleteFieldInput', {
	'where': Optional['RobotBlobEntriesConnectionWhere'],
	'delete': Optional['BlobEntryDeleteInput'],
})


RobotBlobEntriesDisconnectFieldInput = TypedDict('RobotBlobEntriesDisconnectFieldInput', {
	'where': Optional['RobotBlobEntriesConnectionWhere'],
	'disconnect': Optional['BlobEntryDisconnectInput'],
})


RobotBlobEntriesFieldInput = TypedDict('RobotBlobEntriesFieldInput', {
	'create': Optional[List['RobotBlobEntriesCreateFieldInput']],
	'connect': Optional[List['RobotBlobEntriesConnectFieldInput']],
	'connectOrCreate': Optional[List['RobotBlobEntriesConnectOrCreateFieldInput']],
})


RobotBlobEntriesNodeAggregationWhereInput = TypedDict('RobotBlobEntriesNodeAggregationWhereInput', {
	'AND': Optional[List['RobotBlobEntriesNodeAggregationWhereInput']],
	'OR': Optional[List['RobotBlobEntriesNodeAggregationWhereInput']],
	'NOT': Optional['RobotBlobEntriesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'hash_AVERAGE_LENGTH_EQUAL': Optional[float],
	'hash_LONGEST_LENGTH_EQUAL': Optional[int],
	'hash_SHORTEST_LENGTH_EQUAL': Optional[int],
	'hash_AVERAGE_LENGTH_GT': Optional[float],
	'hash_LONGEST_LENGTH_GT': Optional[int],
	'hash_SHORTEST_LENGTH_GT': Optional[int],
	'hash_AVERAGE_LENGTH_GTE': Optional[float],
	'hash_LONGEST_LENGTH_GTE': Optional[int],
	'hash_SHORTEST_LENGTH_GTE': Optional[int],
	'hash_AVERAGE_LENGTH_LT': Optional[float],
	'hash_LONGEST_LENGTH_LT': Optional[int],
	'hash_SHORTEST_LENGTH_LT': Optional[int],
	'hash_AVERAGE_LENGTH_LTE': Optional[float],
	'hash_LONGEST_LENGTH_LTE': Optional[int],
	'hash_SHORTEST_LENGTH_LTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'mimeType_LONGEST_LENGTH_EQUAL': Optional[int],
	'mimeType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'mimeType_AVERAGE_LENGTH_GT': Optional[float],
	'mimeType_LONGEST_LENGTH_GT': Optional[int],
	'mimeType_SHORTEST_LENGTH_GT': Optional[int],
	'mimeType_AVERAGE_LENGTH_GTE': Optional[float],
	'mimeType_LONGEST_LENGTH_GTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_GTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_LT': Optional[float],
	'mimeType_LONGEST_LENGTH_LT': Optional[int],
	'mimeType_SHORTEST_LENGTH_LT': Optional[int],
	'mimeType_AVERAGE_LENGTH_LTE': Optional[float],
	'mimeType_LONGEST_LENGTH_LTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_LTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_EQUAL': Optional[float],
	'blobstore_LONGEST_LENGTH_EQUAL': Optional[int],
	'blobstore_SHORTEST_LENGTH_EQUAL': Optional[int],
	'blobstore_AVERAGE_LENGTH_GT': Optional[float],
	'blobstore_LONGEST_LENGTH_GT': Optional[int],
	'blobstore_SHORTEST_LENGTH_GT': Optional[int],
	'blobstore_AVERAGE_LENGTH_GTE': Optional[float],
	'blobstore_LONGEST_LENGTH_GTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_GTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_LT': Optional[float],
	'blobstore_LONGEST_LENGTH_LT': Optional[int],
	'blobstore_SHORTEST_LENGTH_LT': Optional[int],
	'blobstore_AVERAGE_LENGTH_LTE': Optional[float],
	'blobstore_LONGEST_LENGTH_LTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_LTE': Optional[int],
	'origin_AVERAGE_LENGTH_EQUAL': Optional[float],
	'origin_LONGEST_LENGTH_EQUAL': Optional[int],
	'origin_SHORTEST_LENGTH_EQUAL': Optional[int],
	'origin_AVERAGE_LENGTH_GT': Optional[float],
	'origin_LONGEST_LENGTH_GT': Optional[int],
	'origin_SHORTEST_LENGTH_GT': Optional[int],
	'origin_AVERAGE_LENGTH_GTE': Optional[float],
	'origin_LONGEST_LENGTH_GTE': Optional[int],
	'origin_SHORTEST_LENGTH_GTE': Optional[int],
	'origin_AVERAGE_LENGTH_LT': Optional[float],
	'origin_LONGEST_LENGTH_LT': Optional[int],
	'origin_SHORTEST_LENGTH_LT': Optional[int],
	'origin_AVERAGE_LENGTH_LTE': Optional[float],
	'origin_LONGEST_LENGTH_LTE': Optional[int],
	'origin_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'factorLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GT': Optional[float],
	'factorLabel_LONGEST_LENGTH_GT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_GTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LT': Optional[float],
	'factorLabel_LONGEST_LENGTH_LT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_LTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


RobotBlobEntriesUpdateConnectionInput = TypedDict('RobotBlobEntriesUpdateConnectionInput', {
	'node': Optional['BlobEntryUpdateInput'],
})


RobotBlobEntriesUpdateFieldInput = TypedDict('RobotBlobEntriesUpdateFieldInput', {
	'where': Optional['RobotBlobEntriesConnectionWhere'],
	'update': Optional['RobotBlobEntriesUpdateConnectionInput'],
	'connect': Optional[List['RobotBlobEntriesConnectFieldInput']],
	'disconnect': Optional[List['RobotBlobEntriesDisconnectFieldInput']],
	'create': Optional[List['RobotBlobEntriesCreateFieldInput']],
	'delete': Optional[List['RobotBlobEntriesDeleteFieldInput']],
	'connectOrCreate': Optional[List['RobotBlobEntriesConnectOrCreateFieldInput']],
})


RobotConnectInput = TypedDict('RobotConnectInput', {
	'sessions': Optional[List['RobotSessionsConnectFieldInput']],
	'blobEntries': Optional[List['RobotBlobEntriesConnectFieldInput']],
	'user': Optional[List['RobotUserConnectFieldInput']],
})


RobotConnectOrCreateInput = TypedDict('RobotConnectOrCreateInput', {
	'sessions': Optional[List['RobotSessionsConnectOrCreateFieldInput']],
	'blobEntries': Optional[List['RobotBlobEntriesConnectOrCreateFieldInput']],
})


RobotConnectOrCreateWhere = TypedDict('RobotConnectOrCreateWhere', {
	'node': 'RobotUniqueWhere',
})


RobotConnectWhere = TypedDict('RobotConnectWhere', {
	'node': 'RobotWhere',
})


RobotCreateInput = TypedDict('RobotCreateInput', {
	'label': str,
	'_version': str,
	'userLabel': str,
	'metadata': Optional['Metadata'],
	'sessions': Optional['RobotSessionsFieldInput'],
	'blobEntries': Optional['RobotBlobEntriesFieldInput'],
	'user': Optional['RobotUserFieldInput'],
})


RobotDeleteInput = TypedDict('RobotDeleteInput', {
	'sessions': Optional[List['RobotSessionsDeleteFieldInput']],
	'blobEntries': Optional[List['RobotBlobEntriesDeleteFieldInput']],
})


RobotDisconnectInput = TypedDict('RobotDisconnectInput', {
	'sessions': Optional[List['RobotSessionsDisconnectFieldInput']],
	'blobEntries': Optional[List['RobotBlobEntriesDisconnectFieldInput']],
	'user': Optional[List['RobotUserDisconnectFieldInput']],
})


RobotOnCreateInput = TypedDict('RobotOnCreateInput', {
	'label': str,
	'_version': str,
	'userLabel': str,
	'metadata': Optional['Metadata'],
})


RobotOptions = TypedDict('RobotOptions', {
	'sort': Optional[List['RobotSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


RobotRelationInput = TypedDict('RobotRelationInput', {
	'sessions': Optional[List['RobotSessionsCreateFieldInput']],
	'blobEntries': Optional[List['RobotBlobEntriesCreateFieldInput']],
})


RobotSessionsAggregateInput = TypedDict('RobotSessionsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['RobotSessionsAggregateInput']],
	'OR': Optional[List['RobotSessionsAggregateInput']],
	'NOT': Optional['RobotSessionsAggregateInput'],
	'node': Optional['RobotSessionsNodeAggregationWhereInput'],
})


RobotSessionsConnectFieldInput = TypedDict('RobotSessionsConnectFieldInput', {
	'where': Optional['SessionConnectWhere'],
	'connect': Optional[List['SessionConnectInput']],
	'overwrite': bool,
})


RobotSessionsConnectionSort = TypedDict('RobotSessionsConnectionSort', {
	'node': Optional['SessionSort'],
})


RobotSessionsConnectionWhere = TypedDict('RobotSessionsConnectionWhere', {
	'AND': Optional[List['RobotSessionsConnectionWhere']],
	'OR': Optional[List['RobotSessionsConnectionWhere']],
	'NOT': Optional['RobotSessionsConnectionWhere'],
	'node': Optional['SessionWhere'],
})


RobotSessionsConnectOrCreateFieldInput = TypedDict('RobotSessionsConnectOrCreateFieldInput', {
	'where': 'SessionConnectOrCreateWhere',
	'onCreate': 'RobotSessionsConnectOrCreateFieldInputOnCreate',
})


RobotSessionsConnectOrCreateFieldInputOnCreate = TypedDict('RobotSessionsConnectOrCreateFieldInputOnCreate', {
	'node': 'SessionOnCreateInput',
})


RobotSessionsCreateFieldInput = TypedDict('RobotSessionsCreateFieldInput', {
	'node': 'SessionCreateInput',
})


RobotSessionsDeleteFieldInput = TypedDict('RobotSessionsDeleteFieldInput', {
	'where': Optional['RobotSessionsConnectionWhere'],
	'delete': Optional['SessionDeleteInput'],
})


RobotSessionsDisconnectFieldInput = TypedDict('RobotSessionsDisconnectFieldInput', {
	'where': Optional['RobotSessionsConnectionWhere'],
	'disconnect': Optional['SessionDisconnectInput'],
})


RobotSessionsFieldInput = TypedDict('RobotSessionsFieldInput', {
	'create': Optional[List['RobotSessionsCreateFieldInput']],
	'connect': Optional[List['RobotSessionsConnectFieldInput']],
	'connectOrCreate': Optional[List['RobotSessionsConnectOrCreateFieldInput']],
})


RobotSessionsNodeAggregationWhereInput = TypedDict('RobotSessionsNodeAggregationWhereInput', {
	'AND': Optional[List['RobotSessionsNodeAggregationWhereInput']],
	'OR': Optional[List['RobotSessionsNodeAggregationWhereInput']],
	'NOT': Optional['RobotSessionsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


RobotSessionsUpdateConnectionInput = TypedDict('RobotSessionsUpdateConnectionInput', {
	'node': Optional['SessionUpdateInput'],
})


RobotSessionsUpdateFieldInput = TypedDict('RobotSessionsUpdateFieldInput', {
	'where': Optional['RobotSessionsConnectionWhere'],
	'update': Optional['RobotSessionsUpdateConnectionInput'],
	'connect': Optional[List['RobotSessionsConnectFieldInput']],
	'disconnect': Optional[List['RobotSessionsDisconnectFieldInput']],
	'create': Optional[List['RobotSessionsCreateFieldInput']],
	'delete': Optional[List['RobotSessionsDeleteFieldInput']],
	'connectOrCreate': Optional[List['RobotSessionsConnectOrCreateFieldInput']],
})


RobotSort = TypedDict('RobotSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'metadata': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
	'userId': Optional['SortDirection'],
})


RobotUniqueWhere = TypedDict('RobotUniqueWhere', {
	'id': Optional[str],
})


RobotUpdateInput = TypedDict('RobotUpdateInput', {
	'label': Optional[str],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'sessions': Optional[List['RobotSessionsUpdateFieldInput']],
	'blobEntries': Optional[List['RobotBlobEntriesUpdateFieldInput']],
})


RobotUserAggregateInput = TypedDict('RobotUserAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['RobotUserAggregateInput']],
	'OR': Optional[List['RobotUserAggregateInput']],
	'NOT': Optional['RobotUserAggregateInput'],
	'node': Optional['RobotUserNodeAggregationWhereInput'],
})


RobotUserConnectFieldInput = TypedDict('RobotUserConnectFieldInput', {
	'where': Optional['UserConnectWhere'],
	'connect': Optional[List['UserConnectInput']],
	'overwrite': bool,
})


RobotUserConnectionSort = TypedDict('RobotUserConnectionSort', {
	'node': Optional['UserSort'],
})


RobotUserConnectionWhere = TypedDict('RobotUserConnectionWhere', {
	'AND': Optional[List['RobotUserConnectionWhere']],
	'OR': Optional[List['RobotUserConnectionWhere']],
	'NOT': Optional['RobotUserConnectionWhere'],
	'node': Optional['UserWhere'],
})


RobotUserConnectOrCreateFieldInputOnCreate = TypedDict('RobotUserConnectOrCreateFieldInputOnCreate', {
	'node': 'UserOnCreateInput',
})


RobotUserDisconnectFieldInput = TypedDict('RobotUserDisconnectFieldInput', {
	'where': Optional['RobotUserConnectionWhere'],
	'disconnect': Optional['UserDisconnectInput'],
})


RobotUserFieldInput = TypedDict('RobotUserFieldInput', {
	'connect': Optional[List['RobotUserConnectFieldInput']],
})


RobotUserNodeAggregationWhereInput = TypedDict('RobotUserNodeAggregationWhereInput', {
	'AND': Optional[List['RobotUserNodeAggregationWhereInput']],
	'OR': Optional[List['RobotUserNodeAggregationWhereInput']],
	'NOT': Optional['RobotUserNodeAggregationWhereInput'],
	'sub_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sub_LONGEST_LENGTH_EQUAL': Optional[int],
	'sub_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sub_AVERAGE_LENGTH_GT': Optional[float],
	'sub_LONGEST_LENGTH_GT': Optional[int],
	'sub_SHORTEST_LENGTH_GT': Optional[int],
	'sub_AVERAGE_LENGTH_GTE': Optional[float],
	'sub_LONGEST_LENGTH_GTE': Optional[int],
	'sub_SHORTEST_LENGTH_GTE': Optional[int],
	'sub_AVERAGE_LENGTH_LT': Optional[float],
	'sub_LONGEST_LENGTH_LT': Optional[int],
	'sub_SHORTEST_LENGTH_LT': Optional[int],
	'sub_AVERAGE_LENGTH_LTE': Optional[float],
	'sub_LONGEST_LENGTH_LTE': Optional[int],
	'sub_SHORTEST_LENGTH_LTE': Optional[int],
	'givenName_AVERAGE_LENGTH_EQUAL': Optional[float],
	'givenName_LONGEST_LENGTH_EQUAL': Optional[int],
	'givenName_SHORTEST_LENGTH_EQUAL': Optional[int],
	'givenName_AVERAGE_LENGTH_GT': Optional[float],
	'givenName_LONGEST_LENGTH_GT': Optional[int],
	'givenName_SHORTEST_LENGTH_GT': Optional[int],
	'givenName_AVERAGE_LENGTH_GTE': Optional[float],
	'givenName_LONGEST_LENGTH_GTE': Optional[int],
	'givenName_SHORTEST_LENGTH_GTE': Optional[int],
	'givenName_AVERAGE_LENGTH_LT': Optional[float],
	'givenName_LONGEST_LENGTH_LT': Optional[int],
	'givenName_SHORTEST_LENGTH_LT': Optional[int],
	'givenName_AVERAGE_LENGTH_LTE': Optional[float],
	'givenName_LONGEST_LENGTH_LTE': Optional[int],
	'givenName_SHORTEST_LENGTH_LTE': Optional[int],
	'familyName_AVERAGE_LENGTH_EQUAL': Optional[float],
	'familyName_LONGEST_LENGTH_EQUAL': Optional[int],
	'familyName_SHORTEST_LENGTH_EQUAL': Optional[int],
	'familyName_AVERAGE_LENGTH_GT': Optional[float],
	'familyName_LONGEST_LENGTH_GT': Optional[int],
	'familyName_SHORTEST_LENGTH_GT': Optional[int],
	'familyName_AVERAGE_LENGTH_GTE': Optional[float],
	'familyName_LONGEST_LENGTH_GTE': Optional[int],
	'familyName_SHORTEST_LENGTH_GTE': Optional[int],
	'familyName_AVERAGE_LENGTH_LT': Optional[float],
	'familyName_LONGEST_LENGTH_LT': Optional[int],
	'familyName_SHORTEST_LENGTH_LT': Optional[int],
	'familyName_AVERAGE_LENGTH_LTE': Optional[float],
	'familyName_LONGEST_LENGTH_LTE': Optional[int],
	'familyName_SHORTEST_LENGTH_LTE': Optional[int],
	'status_AVERAGE_LENGTH_EQUAL': Optional[float],
	'status_LONGEST_LENGTH_EQUAL': Optional[int],
	'status_SHORTEST_LENGTH_EQUAL': Optional[int],
	'status_AVERAGE_LENGTH_GT': Optional[float],
	'status_LONGEST_LENGTH_GT': Optional[int],
	'status_SHORTEST_LENGTH_GT': Optional[int],
	'status_AVERAGE_LENGTH_GTE': Optional[float],
	'status_LONGEST_LENGTH_GTE': Optional[int],
	'status_SHORTEST_LENGTH_GTE': Optional[int],
	'status_AVERAGE_LENGTH_LT': Optional[float],
	'status_LONGEST_LENGTH_LT': Optional[int],
	'status_SHORTEST_LENGTH_LT': Optional[int],
	'status_AVERAGE_LENGTH_LTE': Optional[float],
	'status_LONGEST_LENGTH_LTE': Optional[int],
	'status_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_LTE': Optional['DateTime'],
})


RobotWhere = TypedDict('RobotWhere', {
	'OR': Optional[List['RobotWhere']],
	'AND': Optional[List['RobotWhere']],
	'NOT': Optional['RobotWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'metadata': Optional['Metadata'],
	'metadata_IN': Optional[List['Metadata']],
	'sessionsAggregate': Optional['RobotSessionsAggregateInput'],
	'sessions_ALL': Optional['SessionWhere'],
	'sessions_NONE': Optional['SessionWhere'],
	'sessions_SINGLE': Optional['SessionWhere'],
	'sessions_SOME': Optional['SessionWhere'],
	'blobEntriesAggregate': Optional['RobotBlobEntriesAggregateInput'],
	'blobEntries_ALL': Optional['BlobEntryWhere'],
	'blobEntries_NONE': Optional['BlobEntryWhere'],
	'blobEntries_SINGLE': Optional['BlobEntryWhere'],
	'blobEntries_SOME': Optional['BlobEntryWhere'],
	'userAggregate': Optional['RobotUserAggregateInput'],
	'user_ALL': Optional['UserWhere'],
	'user_NONE': Optional['UserWhere'],
	'user_SINGLE': Optional['UserWhere'],
	'user_SOME': Optional['UserWhere'],
	'sessionsConnection_ALL': Optional['RobotSessionsConnectionWhere'],
	'sessionsConnection_NONE': Optional['RobotSessionsConnectionWhere'],
	'sessionsConnection_SINGLE': Optional['RobotSessionsConnectionWhere'],
	'sessionsConnection_SOME': Optional['RobotSessionsConnectionWhere'],
	'blobEntriesConnection_ALL': Optional['RobotBlobEntriesConnectionWhere'],
	'blobEntriesConnection_NONE': Optional['RobotBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SINGLE': Optional['RobotBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SOME': Optional['RobotBlobEntriesConnectionWhere'],
	'userConnection_ALL': Optional['RobotUserConnectionWhere'],
	'userConnection_NONE': Optional['RobotUserConnectionWhere'],
	'userConnection_SINGLE': Optional['RobotUserConnectionWhere'],
	'userConnection_SOME': Optional['RobotUserConnectionWhere'],
})


SessionBlobEntriesAggregateInput = TypedDict('SessionBlobEntriesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['SessionBlobEntriesAggregateInput']],
	'OR': Optional[List['SessionBlobEntriesAggregateInput']],
	'NOT': Optional['SessionBlobEntriesAggregateInput'],
	'node': Optional['SessionBlobEntriesNodeAggregationWhereInput'],
})


SessionBlobEntriesConnectFieldInput = TypedDict('SessionBlobEntriesConnectFieldInput', {
	'where': Optional['BlobEntryConnectWhere'],
	'connect': Optional[List['BlobEntryConnectInput']],
	'overwrite': bool,
})


SessionBlobEntriesConnectionSort = TypedDict('SessionBlobEntriesConnectionSort', {
	'node': Optional['BlobEntrySort'],
})


SessionBlobEntriesConnectionWhere = TypedDict('SessionBlobEntriesConnectionWhere', {
	'AND': Optional[List['SessionBlobEntriesConnectionWhere']],
	'OR': Optional[List['SessionBlobEntriesConnectionWhere']],
	'NOT': Optional['SessionBlobEntriesConnectionWhere'],
	'node': Optional['BlobEntryWhere'],
})


SessionBlobEntriesConnectOrCreateFieldInput = TypedDict('SessionBlobEntriesConnectOrCreateFieldInput', {
	'where': 'BlobEntryConnectOrCreateWhere',
	'onCreate': 'SessionBlobEntriesConnectOrCreateFieldInputOnCreate',
})


SessionBlobEntriesConnectOrCreateFieldInputOnCreate = TypedDict('SessionBlobEntriesConnectOrCreateFieldInputOnCreate', {
	'node': 'BlobEntryOnCreateInput',
})


SessionBlobEntriesCreateFieldInput = TypedDict('SessionBlobEntriesCreateFieldInput', {
	'node': 'BlobEntryCreateInput',
})


SessionBlobEntriesDeleteFieldInput = TypedDict('SessionBlobEntriesDeleteFieldInput', {
	'where': Optional['SessionBlobEntriesConnectionWhere'],
	'delete': Optional['BlobEntryDeleteInput'],
})


SessionBlobEntriesDisconnectFieldInput = TypedDict('SessionBlobEntriesDisconnectFieldInput', {
	'where': Optional['SessionBlobEntriesConnectionWhere'],
	'disconnect': Optional['BlobEntryDisconnectInput'],
})


SessionBlobEntriesFieldInput = TypedDict('SessionBlobEntriesFieldInput', {
	'create': Optional[List['SessionBlobEntriesCreateFieldInput']],
	'connect': Optional[List['SessionBlobEntriesConnectFieldInput']],
	'connectOrCreate': Optional[List['SessionBlobEntriesConnectOrCreateFieldInput']],
})


SessionBlobEntriesNodeAggregationWhereInput = TypedDict('SessionBlobEntriesNodeAggregationWhereInput', {
	'AND': Optional[List['SessionBlobEntriesNodeAggregationWhereInput']],
	'OR': Optional[List['SessionBlobEntriesNodeAggregationWhereInput']],
	'NOT': Optional['SessionBlobEntriesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'hash_AVERAGE_LENGTH_EQUAL': Optional[float],
	'hash_LONGEST_LENGTH_EQUAL': Optional[int],
	'hash_SHORTEST_LENGTH_EQUAL': Optional[int],
	'hash_AVERAGE_LENGTH_GT': Optional[float],
	'hash_LONGEST_LENGTH_GT': Optional[int],
	'hash_SHORTEST_LENGTH_GT': Optional[int],
	'hash_AVERAGE_LENGTH_GTE': Optional[float],
	'hash_LONGEST_LENGTH_GTE': Optional[int],
	'hash_SHORTEST_LENGTH_GTE': Optional[int],
	'hash_AVERAGE_LENGTH_LT': Optional[float],
	'hash_LONGEST_LENGTH_LT': Optional[int],
	'hash_SHORTEST_LENGTH_LT': Optional[int],
	'hash_AVERAGE_LENGTH_LTE': Optional[float],
	'hash_LONGEST_LENGTH_LTE': Optional[int],
	'hash_SHORTEST_LENGTH_LTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'mimeType_LONGEST_LENGTH_EQUAL': Optional[int],
	'mimeType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'mimeType_AVERAGE_LENGTH_GT': Optional[float],
	'mimeType_LONGEST_LENGTH_GT': Optional[int],
	'mimeType_SHORTEST_LENGTH_GT': Optional[int],
	'mimeType_AVERAGE_LENGTH_GTE': Optional[float],
	'mimeType_LONGEST_LENGTH_GTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_GTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_LT': Optional[float],
	'mimeType_LONGEST_LENGTH_LT': Optional[int],
	'mimeType_SHORTEST_LENGTH_LT': Optional[int],
	'mimeType_AVERAGE_LENGTH_LTE': Optional[float],
	'mimeType_LONGEST_LENGTH_LTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_LTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_EQUAL': Optional[float],
	'blobstore_LONGEST_LENGTH_EQUAL': Optional[int],
	'blobstore_SHORTEST_LENGTH_EQUAL': Optional[int],
	'blobstore_AVERAGE_LENGTH_GT': Optional[float],
	'blobstore_LONGEST_LENGTH_GT': Optional[int],
	'blobstore_SHORTEST_LENGTH_GT': Optional[int],
	'blobstore_AVERAGE_LENGTH_GTE': Optional[float],
	'blobstore_LONGEST_LENGTH_GTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_GTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_LT': Optional[float],
	'blobstore_LONGEST_LENGTH_LT': Optional[int],
	'blobstore_SHORTEST_LENGTH_LT': Optional[int],
	'blobstore_AVERAGE_LENGTH_LTE': Optional[float],
	'blobstore_LONGEST_LENGTH_LTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_LTE': Optional[int],
	'origin_AVERAGE_LENGTH_EQUAL': Optional[float],
	'origin_LONGEST_LENGTH_EQUAL': Optional[int],
	'origin_SHORTEST_LENGTH_EQUAL': Optional[int],
	'origin_AVERAGE_LENGTH_GT': Optional[float],
	'origin_LONGEST_LENGTH_GT': Optional[int],
	'origin_SHORTEST_LENGTH_GT': Optional[int],
	'origin_AVERAGE_LENGTH_GTE': Optional[float],
	'origin_LONGEST_LENGTH_GTE': Optional[int],
	'origin_SHORTEST_LENGTH_GTE': Optional[int],
	'origin_AVERAGE_LENGTH_LT': Optional[float],
	'origin_LONGEST_LENGTH_LT': Optional[int],
	'origin_SHORTEST_LENGTH_LT': Optional[int],
	'origin_AVERAGE_LENGTH_LTE': Optional[float],
	'origin_LONGEST_LENGTH_LTE': Optional[int],
	'origin_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'factorLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GT': Optional[float],
	'factorLabel_LONGEST_LENGTH_GT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_GTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LT': Optional[float],
	'factorLabel_LONGEST_LENGTH_LT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_LTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


SessionBlobEntriesUpdateConnectionInput = TypedDict('SessionBlobEntriesUpdateConnectionInput', {
	'node': Optional['BlobEntryUpdateInput'],
})


SessionBlobEntriesUpdateFieldInput = TypedDict('SessionBlobEntriesUpdateFieldInput', {
	'where': Optional['SessionBlobEntriesConnectionWhere'],
	'update': Optional['SessionBlobEntriesUpdateConnectionInput'],
	'connect': Optional[List['SessionBlobEntriesConnectFieldInput']],
	'disconnect': Optional[List['SessionBlobEntriesDisconnectFieldInput']],
	'create': Optional[List['SessionBlobEntriesCreateFieldInput']],
	'delete': Optional[List['SessionBlobEntriesDeleteFieldInput']],
	'connectOrCreate': Optional[List['SessionBlobEntriesConnectOrCreateFieldInput']],
})


SessionConnectInput = TypedDict('SessionConnectInput', {
	'robot': Optional['SessionRobotConnectFieldInput'],
	'variables': Optional[List['SessionVariablesConnectFieldInput']],
	'factors': Optional[List['SessionFactorsConnectFieldInput']],
	'blobEntries': Optional[List['SessionBlobEntriesConnectFieldInput']],
})


SessionConnectOrCreateInput = TypedDict('SessionConnectOrCreateInput', {
	'robot': Optional['SessionRobotConnectOrCreateFieldInput'],
	'variables': Optional[List['SessionVariablesConnectOrCreateFieldInput']],
	'factors': Optional[List['SessionFactorsConnectOrCreateFieldInput']],
	'blobEntries': Optional[List['SessionBlobEntriesConnectOrCreateFieldInput']],
})


SessionConnectOrCreateWhere = TypedDict('SessionConnectOrCreateWhere', {
	'node': 'SessionUniqueWhere',
})


SessionConnectWhere = TypedDict('SessionConnectWhere', {
	'node': 'SessionWhere',
})


SessionCreateInput = TypedDict('SessionCreateInput', {
	'label': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'metadata': Optional['Metadata'],
	'originLatitude': Optional['Latitude'],
	'originLongitude': Optional['Longitude'],
	'robot': Optional['SessionRobotFieldInput'],
	'variables': Optional['SessionVariablesFieldInput'],
	'factors': Optional['SessionFactorsFieldInput'],
	'blobEntries': Optional['SessionBlobEntriesFieldInput'],
})


SessionDeleteInput = TypedDict('SessionDeleteInput', {
	'robot': Optional['SessionRobotDeleteFieldInput'],
	'variables': Optional[List['SessionVariablesDeleteFieldInput']],
	'factors': Optional[List['SessionFactorsDeleteFieldInput']],
	'blobEntries': Optional[List['SessionBlobEntriesDeleteFieldInput']],
})


SessionDisconnectInput = TypedDict('SessionDisconnectInput', {
	'robot': Optional['SessionRobotDisconnectFieldInput'],
	'variables': Optional[List['SessionVariablesDisconnectFieldInput']],
	'factors': Optional[List['SessionFactorsDisconnectFieldInput']],
	'blobEntries': Optional[List['SessionBlobEntriesDisconnectFieldInput']],
})


SessionFactorsAggregateInput = TypedDict('SessionFactorsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['SessionFactorsAggregateInput']],
	'OR': Optional[List['SessionFactorsAggregateInput']],
	'NOT': Optional['SessionFactorsAggregateInput'],
	'node': Optional['SessionFactorsNodeAggregationWhereInput'],
})


SessionFactorsConnectFieldInput = TypedDict('SessionFactorsConnectFieldInput', {
	'where': Optional['FactorConnectWhere'],
	'connect': Optional[List['FactorConnectInput']],
	'overwrite': bool,
})


SessionFactorsConnectionSort = TypedDict('SessionFactorsConnectionSort', {
	'node': Optional['FactorSort'],
})


SessionFactorsConnectionWhere = TypedDict('SessionFactorsConnectionWhere', {
	'AND': Optional[List['SessionFactorsConnectionWhere']],
	'OR': Optional[List['SessionFactorsConnectionWhere']],
	'NOT': Optional['SessionFactorsConnectionWhere'],
	'node': Optional['FactorWhere'],
})


SessionFactorsConnectOrCreateFieldInput = TypedDict('SessionFactorsConnectOrCreateFieldInput', {
	'where': 'FactorConnectOrCreateWhere',
	'onCreate': 'SessionFactorsConnectOrCreateFieldInputOnCreate',
})


SessionFactorsConnectOrCreateFieldInputOnCreate = TypedDict('SessionFactorsConnectOrCreateFieldInputOnCreate', {
	'node': 'FactorOnCreateInput',
})


SessionFactorsCreateFieldInput = TypedDict('SessionFactorsCreateFieldInput', {
	'node': 'FactorCreateInput',
})


SessionFactorsDeleteFieldInput = TypedDict('SessionFactorsDeleteFieldInput', {
	'where': Optional['SessionFactorsConnectionWhere'],
	'delete': Optional['FactorDeleteInput'],
})


SessionFactorsDisconnectFieldInput = TypedDict('SessionFactorsDisconnectFieldInput', {
	'where': Optional['SessionFactorsConnectionWhere'],
	'disconnect': Optional['FactorDisconnectInput'],
})


SessionFactorsFieldInput = TypedDict('SessionFactorsFieldInput', {
	'create': Optional[List['SessionFactorsCreateFieldInput']],
	'connect': Optional[List['SessionFactorsConnectFieldInput']],
	'connectOrCreate': Optional[List['SessionFactorsConnectOrCreateFieldInput']],
})


SessionFactorsNodeAggregationWhereInput = TypedDict('SessionFactorsNodeAggregationWhereInput', {
	'AND': Optional[List['SessionFactorsNodeAggregationWhereInput']],
	'OR': Optional[List['SessionFactorsNodeAggregationWhereInput']],
	'NOT': Optional['SessionFactorsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'fnctype_AVERAGE_LENGTH_EQUAL': Optional[float],
	'fnctype_LONGEST_LENGTH_EQUAL': Optional[int],
	'fnctype_SHORTEST_LENGTH_EQUAL': Optional[int],
	'fnctype_AVERAGE_LENGTH_GT': Optional[float],
	'fnctype_LONGEST_LENGTH_GT': Optional[int],
	'fnctype_SHORTEST_LENGTH_GT': Optional[int],
	'fnctype_AVERAGE_LENGTH_GTE': Optional[float],
	'fnctype_LONGEST_LENGTH_GTE': Optional[int],
	'fnctype_SHORTEST_LENGTH_GTE': Optional[int],
	'fnctype_AVERAGE_LENGTH_LT': Optional[float],
	'fnctype_LONGEST_LENGTH_LT': Optional[int],
	'fnctype_SHORTEST_LENGTH_LT': Optional[int],
	'fnctype_AVERAGE_LENGTH_LTE': Optional[float],
	'fnctype_LONGEST_LENGTH_LTE': Optional[int],
	'fnctype_SHORTEST_LENGTH_LTE': Optional[int],
	'data_AVERAGE_LENGTH_EQUAL': Optional[float],
	'data_LONGEST_LENGTH_EQUAL': Optional[int],
	'data_SHORTEST_LENGTH_EQUAL': Optional[int],
	'data_AVERAGE_LENGTH_GT': Optional[float],
	'data_LONGEST_LENGTH_GT': Optional[int],
	'data_SHORTEST_LENGTH_GT': Optional[int],
	'data_AVERAGE_LENGTH_GTE': Optional[float],
	'data_LONGEST_LENGTH_GTE': Optional[int],
	'data_SHORTEST_LENGTH_GTE': Optional[int],
	'data_AVERAGE_LENGTH_LT': Optional[float],
	'data_LONGEST_LENGTH_LT': Optional[int],
	'data_SHORTEST_LENGTH_LT': Optional[int],
	'data_AVERAGE_LENGTH_LTE': Optional[float],
	'data_LONGEST_LENGTH_LTE': Optional[int],
	'data_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


SessionFactorsUpdateConnectionInput = TypedDict('SessionFactorsUpdateConnectionInput', {
	'node': Optional['FactorUpdateInput'],
})


SessionFactorsUpdateFieldInput = TypedDict('SessionFactorsUpdateFieldInput', {
	'where': Optional['SessionFactorsConnectionWhere'],
	'update': Optional['SessionFactorsUpdateConnectionInput'],
	'connect': Optional[List['SessionFactorsConnectFieldInput']],
	'disconnect': Optional[List['SessionFactorsDisconnectFieldInput']],
	'create': Optional[List['SessionFactorsCreateFieldInput']],
	'delete': Optional[List['SessionFactorsDeleteFieldInput']],
	'connectOrCreate': Optional[List['SessionFactorsConnectOrCreateFieldInput']],
})


SessionOnCreateInput = TypedDict('SessionOnCreateInput', {
	'label': str,
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'metadata': Optional['Metadata'],
	'originLatitude': Optional['Latitude'],
	'originLongitude': Optional['Longitude'],
})


SessionOptions = TypedDict('SessionOptions', {
	'sort': Optional[List['SessionSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


SessionRelationInput = TypedDict('SessionRelationInput', {
	'robot': Optional['SessionRobotCreateFieldInput'],
	'variables': Optional[List['SessionVariablesCreateFieldInput']],
	'factors': Optional[List['SessionFactorsCreateFieldInput']],
	'blobEntries': Optional[List['SessionBlobEntriesCreateFieldInput']],
})


SessionRobotAggregateInput = TypedDict('SessionRobotAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['SessionRobotAggregateInput']],
	'OR': Optional[List['SessionRobotAggregateInput']],
	'NOT': Optional['SessionRobotAggregateInput'],
	'node': Optional['SessionRobotNodeAggregationWhereInput'],
})


SessionRobotConnectFieldInput = TypedDict('SessionRobotConnectFieldInput', {
	'where': Optional['RobotConnectWhere'],
	'connect': Optional['RobotConnectInput'],
	'overwrite': bool,
})


SessionRobotConnectionSort = TypedDict('SessionRobotConnectionSort', {
	'node': Optional['RobotSort'],
})


SessionRobotConnectionWhere = TypedDict('SessionRobotConnectionWhere', {
	'AND': Optional[List['SessionRobotConnectionWhere']],
	'OR': Optional[List['SessionRobotConnectionWhere']],
	'NOT': Optional['SessionRobotConnectionWhere'],
	'node': Optional['RobotWhere'],
})


SessionRobotConnectOrCreateFieldInput = TypedDict('SessionRobotConnectOrCreateFieldInput', {
	'where': 'RobotConnectOrCreateWhere',
	'onCreate': 'SessionRobotConnectOrCreateFieldInputOnCreate',
})


SessionRobotConnectOrCreateFieldInputOnCreate = TypedDict('SessionRobotConnectOrCreateFieldInputOnCreate', {
	'node': 'RobotOnCreateInput',
})


SessionRobotCreateFieldInput = TypedDict('SessionRobotCreateFieldInput', {
	'node': 'RobotCreateInput',
})


SessionRobotDeleteFieldInput = TypedDict('SessionRobotDeleteFieldInput', {
	'where': Optional['SessionRobotConnectionWhere'],
	'delete': Optional['RobotDeleteInput'],
})


SessionRobotDisconnectFieldInput = TypedDict('SessionRobotDisconnectFieldInput', {
	'where': Optional['SessionRobotConnectionWhere'],
	'disconnect': Optional['RobotDisconnectInput'],
})


SessionRobotFieldInput = TypedDict('SessionRobotFieldInput', {
	'create': Optional['SessionRobotCreateFieldInput'],
	'connect': Optional['SessionRobotConnectFieldInput'],
	'connectOrCreate': Optional['SessionRobotConnectOrCreateFieldInput'],
})


SessionRobotNodeAggregationWhereInput = TypedDict('SessionRobotNodeAggregationWhereInput', {
	'AND': Optional[List['SessionRobotNodeAggregationWhereInput']],
	'OR': Optional[List['SessionRobotNodeAggregationWhereInput']],
	'NOT': Optional['SessionRobotNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


SessionRobotUpdateConnectionInput = TypedDict('SessionRobotUpdateConnectionInput', {
	'node': Optional['RobotUpdateInput'],
})


SessionRobotUpdateFieldInput = TypedDict('SessionRobotUpdateFieldInput', {
	'where': Optional['SessionRobotConnectionWhere'],
	'update': Optional['SessionRobotUpdateConnectionInput'],
	'connect': Optional['SessionRobotConnectFieldInput'],
	'disconnect': Optional['SessionRobotDisconnectFieldInput'],
	'create': Optional['SessionRobotCreateFieldInput'],
	'delete': Optional['SessionRobotDeleteFieldInput'],
	'connectOrCreate': Optional['SessionRobotConnectOrCreateFieldInput'],
})


SessionSort = TypedDict('SessionSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'robotLabel': Optional['SortDirection'],
	'metadata': Optional['SortDirection'],
	'originLatitude': Optional['SortDirection'],
	'originLongitude': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
	'robotId': Optional['SortDirection'],
	'userId': Optional['SortDirection'],
	'numVariables': Optional['SortDirection'],
	'numFactors': Optional['SortDirection'],
})


SessionUniqueWhere = TypedDict('SessionUniqueWhere', {
	'id': Optional[str],
})


SessionUpdateInput = TypedDict('SessionUpdateInput', {
	'label': Optional[str],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'originLatitude': Optional['Latitude'],
	'originLongitude': Optional['Longitude'],
	'robot': Optional['SessionRobotUpdateFieldInput'],
	'variables': Optional[List['SessionVariablesUpdateFieldInput']],
	'factors': Optional[List['SessionFactorsUpdateFieldInput']],
	'blobEntries': Optional[List['SessionBlobEntriesUpdateFieldInput']],
})


SessionVariablesAggregateInput = TypedDict('SessionVariablesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['SessionVariablesAggregateInput']],
	'OR': Optional[List['SessionVariablesAggregateInput']],
	'NOT': Optional['SessionVariablesAggregateInput'],
	'node': Optional['SessionVariablesNodeAggregationWhereInput'],
})


SessionVariablesConnectFieldInput = TypedDict('SessionVariablesConnectFieldInput', {
	'where': Optional['VariableConnectWhere'],
	'connect': Optional[List['VariableConnectInput']],
	'overwrite': bool,
})


SessionVariablesConnectionSort = TypedDict('SessionVariablesConnectionSort', {
	'node': Optional['VariableSort'],
})


SessionVariablesConnectionWhere = TypedDict('SessionVariablesConnectionWhere', {
	'AND': Optional[List['SessionVariablesConnectionWhere']],
	'OR': Optional[List['SessionVariablesConnectionWhere']],
	'NOT': Optional['SessionVariablesConnectionWhere'],
	'node': Optional['VariableWhere'],
})


SessionVariablesConnectOrCreateFieldInput = TypedDict('SessionVariablesConnectOrCreateFieldInput', {
	'where': 'VariableConnectOrCreateWhere',
	'onCreate': 'SessionVariablesConnectOrCreateFieldInputOnCreate',
})


SessionVariablesConnectOrCreateFieldInputOnCreate = TypedDict('SessionVariablesConnectOrCreateFieldInputOnCreate', {
	'node': 'VariableOnCreateInput',
})


SessionVariablesCreateFieldInput = TypedDict('SessionVariablesCreateFieldInput', {
	'node': 'VariableCreateInput',
})


SessionVariablesDeleteFieldInput = TypedDict('SessionVariablesDeleteFieldInput', {
	'where': Optional['SessionVariablesConnectionWhere'],
	'delete': Optional['VariableDeleteInput'],
})


SessionVariablesDisconnectFieldInput = TypedDict('SessionVariablesDisconnectFieldInput', {
	'where': Optional['SessionVariablesConnectionWhere'],
	'disconnect': Optional['VariableDisconnectInput'],
})


SessionVariablesFieldInput = TypedDict('SessionVariablesFieldInput', {
	'create': Optional[List['SessionVariablesCreateFieldInput']],
	'connect': Optional[List['SessionVariablesConnectFieldInput']],
	'connectOrCreate': Optional[List['SessionVariablesConnectOrCreateFieldInput']],
})


SessionVariablesNodeAggregationWhereInput = TypedDict('SessionVariablesNodeAggregationWhereInput', {
	'AND': Optional[List['SessionVariablesNodeAggregationWhereInput']],
	'OR': Optional[List['SessionVariablesNodeAggregationWhereInput']],
	'NOT': Optional['SessionVariablesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


SessionVariablesUpdateConnectionInput = TypedDict('SessionVariablesUpdateConnectionInput', {
	'node': Optional['VariableUpdateInput'],
})


SessionVariablesUpdateFieldInput = TypedDict('SessionVariablesUpdateFieldInput', {
	'where': Optional['SessionVariablesConnectionWhere'],
	'update': Optional['SessionVariablesUpdateConnectionInput'],
	'connect': Optional[List['SessionVariablesConnectFieldInput']],
	'disconnect': Optional[List['SessionVariablesDisconnectFieldInput']],
	'create': Optional[List['SessionVariablesCreateFieldInput']],
	'delete': Optional[List['SessionVariablesDeleteFieldInput']],
	'connectOrCreate': Optional[List['SessionVariablesConnectOrCreateFieldInput']],
})


SessionWhere = TypedDict('SessionWhere', {
	'OR': Optional[List['SessionWhere']],
	'AND': Optional[List['SessionWhere']],
	'NOT': Optional['SessionWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'robotLabel': Optional[str],
	'robotLabel_IN': Optional[List[str]],
	'robotLabel_MATCHES': Optional[str],
	'robotLabel_CONTAINS': Optional[str],
	'robotLabel_STARTS_WITH': Optional[str],
	'robotLabel_ENDS_WITH': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'metadata': Optional['Metadata'],
	'metadata_IN': Optional[List['Metadata']],
	'originLatitude': Optional['Latitude'],
	'originLatitude_IN': Optional[List['Latitude']],
	'originLongitude': Optional['Longitude'],
	'originLongitude_IN': Optional[List['Longitude']],
	'robotAggregate': Optional['SessionRobotAggregateInput'],
	'variablesAggregate': Optional['SessionVariablesAggregateInput'],
	'variables_ALL': Optional['VariableWhere'],
	'variables_NONE': Optional['VariableWhere'],
	'variables_SINGLE': Optional['VariableWhere'],
	'variables_SOME': Optional['VariableWhere'],
	'factorsAggregate': Optional['SessionFactorsAggregateInput'],
	'factors_ALL': Optional['FactorWhere'],
	'factors_NONE': Optional['FactorWhere'],
	'factors_SINGLE': Optional['FactorWhere'],
	'factors_SOME': Optional['FactorWhere'],
	'blobEntriesAggregate': Optional['SessionBlobEntriesAggregateInput'],
	'blobEntries_ALL': Optional['BlobEntryWhere'],
	'blobEntries_NONE': Optional['BlobEntryWhere'],
	'blobEntries_SINGLE': Optional['BlobEntryWhere'],
	'blobEntries_SOME': Optional['BlobEntryWhere'],
	'robotConnection': Optional['SessionRobotConnectionWhere'],
	'variablesConnection_ALL': Optional['SessionVariablesConnectionWhere'],
	'variablesConnection_NONE': Optional['SessionVariablesConnectionWhere'],
	'variablesConnection_SINGLE': Optional['SessionVariablesConnectionWhere'],
	'variablesConnection_SOME': Optional['SessionVariablesConnectionWhere'],
	'factorsConnection_ALL': Optional['SessionFactorsConnectionWhere'],
	'factorsConnection_NONE': Optional['SessionFactorsConnectionWhere'],
	'factorsConnection_SINGLE': Optional['SessionFactorsConnectionWhere'],
	'factorsConnection_SOME': Optional['SessionFactorsConnectionWhere'],
	'blobEntriesConnection_ALL': Optional['SessionBlobEntriesConnectionWhere'],
	'blobEntriesConnection_NONE': Optional['SessionBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SINGLE': Optional['SessionBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SOME': Optional['SessionBlobEntriesConnectionWhere'],
})


SolverDataConnectInput = TypedDict('SolverDataConnectInput', {
	'variable': Optional['SolverDataVariableConnectFieldInput'],
})


SolverDataConnectOrCreateInput = TypedDict('SolverDataConnectOrCreateInput', {
	'variable': Optional['SolverDataVariableConnectOrCreateFieldInput'],
})


SolverDataConnectOrCreateWhere = TypedDict('SolverDataConnectOrCreateWhere', {
	'node': 'SolverDataUniqueWhere',
})


SolverDataConnectWhere = TypedDict('SolverDataConnectWhere', {
	'node': 'SolverDataWhere',
})


SolverDataCreateInput = TypedDict('SolverDataCreateInput', {
	'solveKey': str,
	'BayesNetOutVertIDs': Optional[List[str]],
	'BayesNetVertID': Optional[str],
	'dimIDs': List[int],
	'dimbw': int,
	'dims': int,
	'dimval': int,
	'dontmargin': bool,
	'eliminated': bool,
	'infoPerCoord': List[float],
	'initialized': bool,
	'ismargin': bool,
	'separator': Optional[List[str]],
	'solveInProgress': int,
	'solvedCount': int,
	'variableType': str,
	'vecbw': Optional[List[float]],
	'vecval': Optional[List[float]],
	'covar': Optional[List[float]],
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'variableLabel': str,
	'variable': Optional['SolverDataVariableFieldInput'],
})


SolverDataDeleteInput = TypedDict('SolverDataDeleteInput', {
	'variable': Optional['SolverDataVariableDeleteFieldInput'],
})


SolverDataDisconnectInput = TypedDict('SolverDataDisconnectInput', {
	'variable': Optional['SolverDataVariableDisconnectFieldInput'],
})


SolverDataOnCreateInput = TypedDict('SolverDataOnCreateInput', {
	'solveKey': str,
	'BayesNetOutVertIDs': Optional[List[str]],
	'BayesNetVertID': Optional[str],
	'dimIDs': List[int],
	'dimbw': int,
	'dims': int,
	'dimval': int,
	'dontmargin': bool,
	'eliminated': bool,
	'infoPerCoord': List[float],
	'initialized': bool,
	'ismargin': bool,
	'separator': Optional[List[str]],
	'solveInProgress': int,
	'solvedCount': int,
	'variableType': str,
	'vecbw': Optional[List[float]],
	'vecval': Optional[List[float]],
	'covar': Optional[List[float]],
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'variableLabel': str,
})


SolverDataOptions = TypedDict('SolverDataOptions', {
	'sort': Optional[List['SolverDataSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


SolverDataRelationInput = TypedDict('SolverDataRelationInput', {
	'variable': Optional['SolverDataVariableCreateFieldInput'],
})


SolverDataSort = TypedDict('SolverDataSort', {
	'id': Optional['SortDirection'],
	'solveKey': Optional['SortDirection'],
	'BayesNetVertID': Optional['SortDirection'],
	'dimbw': Optional['SortDirection'],
	'dims': Optional['SortDirection'],
	'dimval': Optional['SortDirection'],
	'dontmargin': Optional['SortDirection'],
	'eliminated': Optional['SortDirection'],
	'initialized': Optional['SortDirection'],
	'ismargin': Optional['SortDirection'],
	'solveInProgress': Optional['SortDirection'],
	'solvedCount': Optional['SortDirection'],
	'variableType': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'robotLabel': Optional['SortDirection'],
	'sessionLabel': Optional['SortDirection'],
	'variableLabel': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
})


SolverDataUniqueWhere = TypedDict('SolverDataUniqueWhere', {
	'id': Optional[str],
})


SolverDataUpdateInput = TypedDict('SolverDataUpdateInput', {
	'solveKey': Optional[str],
	'BayesNetOutVertIDs': Optional[List[str]],
	'BayesNetVertID': Optional[str],
	'dimIDs': Optional[List[int]],
	'dimbw': Optional[int],
	'dims': Optional[int],
	'dimval': Optional[int],
	'dontmargin': Optional[bool],
	'eliminated': Optional[bool],
	'infoPerCoord': Optional[List[float]],
	'initialized': Optional[bool],
	'ismargin': Optional[bool],
	'separator': Optional[List[str]],
	'solveInProgress': Optional[int],
	'solvedCount': Optional[int],
	'variableType': Optional[str],
	'vecbw': Optional[List[float]],
	'vecval': Optional[List[float]],
	'covar': Optional[List[float]],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'variableLabel': Optional[str],
	'dimbw_INCREMENT': Optional[int],
	'dimbw_DECREMENT': Optional[int],
	'dims_INCREMENT': Optional[int],
	'dims_DECREMENT': Optional[int],
	'dimval_INCREMENT': Optional[int],
	'dimval_DECREMENT': Optional[int],
	'solveInProgress_INCREMENT': Optional[int],
	'solveInProgress_DECREMENT': Optional[int],
	'solvedCount_INCREMENT': Optional[int],
	'solvedCount_DECREMENT': Optional[int],
	'BayesNetOutVertIDs_POP': Optional[int],
	'BayesNetOutVertIDs_PUSH': Optional[List[str]],
	'dimIDs_POP': Optional[int],
	'dimIDs_PUSH': Optional[List[int]],
	'infoPerCoord_POP': Optional[int],
	'infoPerCoord_PUSH': Optional[List[float]],
	'separator_POP': Optional[int],
	'separator_PUSH': Optional[List[str]],
	'vecbw_POP': Optional[int],
	'vecbw_PUSH': Optional[List[float]],
	'vecval_POP': Optional[int],
	'vecval_PUSH': Optional[List[float]],
	'covar_POP': Optional[int],
	'covar_PUSH': Optional[List[float]],
	'variable': Optional['SolverDataVariableUpdateFieldInput'],
})


SolverDataVariableAggregateInput = TypedDict('SolverDataVariableAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['SolverDataVariableAggregateInput']],
	'OR': Optional[List['SolverDataVariableAggregateInput']],
	'NOT': Optional['SolverDataVariableAggregateInput'],
	'node': Optional['SolverDataVariableNodeAggregationWhereInput'],
})


SolverDataVariableConnectFieldInput = TypedDict('SolverDataVariableConnectFieldInput', {
	'where': Optional['VariableConnectWhere'],
	'connect': Optional['VariableConnectInput'],
	'overwrite': bool,
})


SolverDataVariableConnectionSort = TypedDict('SolverDataVariableConnectionSort', {
	'node': Optional['VariableSort'],
})


SolverDataVariableConnectionWhere = TypedDict('SolverDataVariableConnectionWhere', {
	'AND': Optional[List['SolverDataVariableConnectionWhere']],
	'OR': Optional[List['SolverDataVariableConnectionWhere']],
	'NOT': Optional['SolverDataVariableConnectionWhere'],
	'node': Optional['VariableWhere'],
})


SolverDataVariableConnectOrCreateFieldInput = TypedDict('SolverDataVariableConnectOrCreateFieldInput', {
	'where': 'VariableConnectOrCreateWhere',
	'onCreate': 'SolverDataVariableConnectOrCreateFieldInputOnCreate',
})


SolverDataVariableConnectOrCreateFieldInputOnCreate = TypedDict('SolverDataVariableConnectOrCreateFieldInputOnCreate', {
	'node': 'VariableOnCreateInput',
})


SolverDataVariableCreateFieldInput = TypedDict('SolverDataVariableCreateFieldInput', {
	'node': 'VariableCreateInput',
})


SolverDataVariableDeleteFieldInput = TypedDict('SolverDataVariableDeleteFieldInput', {
	'where': Optional['SolverDataVariableConnectionWhere'],
	'delete': Optional['VariableDeleteInput'],
})


SolverDataVariableDisconnectFieldInput = TypedDict('SolverDataVariableDisconnectFieldInput', {
	'where': Optional['SolverDataVariableConnectionWhere'],
	'disconnect': Optional['VariableDisconnectInput'],
})


SolverDataVariableFieldInput = TypedDict('SolverDataVariableFieldInput', {
	'create': Optional['SolverDataVariableCreateFieldInput'],
	'connect': Optional['SolverDataVariableConnectFieldInput'],
	'connectOrCreate': Optional['SolverDataVariableConnectOrCreateFieldInput'],
})


SolverDataVariableNodeAggregationWhereInput = TypedDict('SolverDataVariableNodeAggregationWhereInput', {
	'AND': Optional[List['SolverDataVariableNodeAggregationWhereInput']],
	'OR': Optional[List['SolverDataVariableNodeAggregationWhereInput']],
	'NOT': Optional['SolverDataVariableNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


SolverDataVariableUpdateConnectionInput = TypedDict('SolverDataVariableUpdateConnectionInput', {
	'node': Optional['VariableUpdateInput'],
})


SolverDataVariableUpdateFieldInput = TypedDict('SolverDataVariableUpdateFieldInput', {
	'where': Optional['SolverDataVariableConnectionWhere'],
	'update': Optional['SolverDataVariableUpdateConnectionInput'],
	'connect': Optional['SolverDataVariableConnectFieldInput'],
	'disconnect': Optional['SolverDataVariableDisconnectFieldInput'],
	'create': Optional['SolverDataVariableCreateFieldInput'],
	'delete': Optional['SolverDataVariableDeleteFieldInput'],
	'connectOrCreate': Optional['SolverDataVariableConnectOrCreateFieldInput'],
})


SolverDataWhere = TypedDict('SolverDataWhere', {
	'OR': Optional[List['SolverDataWhere']],
	'AND': Optional[List['SolverDataWhere']],
	'NOT': Optional['SolverDataWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'solveKey': Optional[str],
	'solveKey_IN': Optional[List[str]],
	'solveKey_MATCHES': Optional[str],
	'solveKey_CONTAINS': Optional[str],
	'solveKey_STARTS_WITH': Optional[str],
	'solveKey_ENDS_WITH': Optional[str],
	'BayesNetOutVertIDs': Optional[List[str]],
	'BayesNetOutVertIDs_INCLUDES': Optional[str],
	'BayesNetVertID': Optional[str],
	'BayesNetVertID_IN': Optional[List[str]],
	'BayesNetVertID_MATCHES': Optional[str],
	'BayesNetVertID_CONTAINS': Optional[str],
	'BayesNetVertID_STARTS_WITH': Optional[str],
	'BayesNetVertID_ENDS_WITH': Optional[str],
	'dimIDs': Optional[List[int]],
	'dimIDs_INCLUDES': Optional[int],
	'dimbw': Optional[int],
	'dimbw_IN': Optional[List[int]],
	'dimbw_LT': Optional[int],
	'dimbw_LTE': Optional[int],
	'dimbw_GT': Optional[int],
	'dimbw_GTE': Optional[int],
	'dims': Optional[int],
	'dims_IN': Optional[List[int]],
	'dims_LT': Optional[int],
	'dims_LTE': Optional[int],
	'dims_GT': Optional[int],
	'dims_GTE': Optional[int],
	'dimval': Optional[int],
	'dimval_IN': Optional[List[int]],
	'dimval_LT': Optional[int],
	'dimval_LTE': Optional[int],
	'dimval_GT': Optional[int],
	'dimval_GTE': Optional[int],
	'dontmargin': Optional[bool],
	'eliminated': Optional[bool],
	'infoPerCoord': Optional[List[float]],
	'infoPerCoord_INCLUDES': Optional[float],
	'initialized': Optional[bool],
	'ismargin': Optional[bool],
	'separator': Optional[List[str]],
	'separator_INCLUDES': Optional[str],
	'solveInProgress': Optional[int],
	'solveInProgress_IN': Optional[List[int]],
	'solveInProgress_LT': Optional[int],
	'solveInProgress_LTE': Optional[int],
	'solveInProgress_GT': Optional[int],
	'solveInProgress_GTE': Optional[int],
	'solvedCount': Optional[int],
	'solvedCount_IN': Optional[List[int]],
	'solvedCount_LT': Optional[int],
	'solvedCount_LTE': Optional[int],
	'solvedCount_GT': Optional[int],
	'solvedCount_GTE': Optional[int],
	'variableType': Optional[str],
	'variableType_IN': Optional[List[str]],
	'variableType_MATCHES': Optional[str],
	'variableType_CONTAINS': Optional[str],
	'variableType_STARTS_WITH': Optional[str],
	'variableType_ENDS_WITH': Optional[str],
	'vecbw': Optional[List[float]],
	'vecbw_INCLUDES': Optional[float],
	'vecval': Optional[List[float]],
	'vecval_INCLUDES': Optional[float],
	'covar': Optional[List[float]],
	'covar_INCLUDES': Optional[float],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'robotLabel': Optional[str],
	'robotLabel_IN': Optional[List[str]],
	'robotLabel_MATCHES': Optional[str],
	'robotLabel_CONTAINS': Optional[str],
	'robotLabel_STARTS_WITH': Optional[str],
	'robotLabel_ENDS_WITH': Optional[str],
	'sessionLabel': Optional[str],
	'sessionLabel_IN': Optional[List[str]],
	'sessionLabel_MATCHES': Optional[str],
	'sessionLabel_CONTAINS': Optional[str],
	'sessionLabel_STARTS_WITH': Optional[str],
	'sessionLabel_ENDS_WITH': Optional[str],
	'variableLabel': Optional[str],
	'variableLabel_IN': Optional[List[str]],
	'variableLabel_MATCHES': Optional[str],
	'variableLabel_CONTAINS': Optional[str],
	'variableLabel_STARTS_WITH': Optional[str],
	'variableLabel_ENDS_WITH': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'variableAggregate': Optional['SolverDataVariableAggregateInput'],
	'variableConnection': Optional['SolverDataVariableConnectionWhere'],
})


UserBlobEntriesAggregateInput = TypedDict('UserBlobEntriesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['UserBlobEntriesAggregateInput']],
	'OR': Optional[List['UserBlobEntriesAggregateInput']],
	'NOT': Optional['UserBlobEntriesAggregateInput'],
	'node': Optional['UserBlobEntriesNodeAggregationWhereInput'],
})


UserBlobEntriesConnectFieldInput = TypedDict('UserBlobEntriesConnectFieldInput', {
	'where': Optional['BlobEntryConnectWhere'],
	'connect': Optional[List['BlobEntryConnectInput']],
	'overwrite': bool,
})


UserBlobEntriesConnectionSort = TypedDict('UserBlobEntriesConnectionSort', {
	'node': Optional['BlobEntrySort'],
})


UserBlobEntriesConnectionWhere = TypedDict('UserBlobEntriesConnectionWhere', {
	'AND': Optional[List['UserBlobEntriesConnectionWhere']],
	'OR': Optional[List['UserBlobEntriesConnectionWhere']],
	'NOT': Optional['UserBlobEntriesConnectionWhere'],
	'node': Optional['BlobEntryWhere'],
})


UserBlobEntriesConnectOrCreateFieldInput = TypedDict('UserBlobEntriesConnectOrCreateFieldInput', {
	'where': 'BlobEntryConnectOrCreateWhere',
	'onCreate': 'UserBlobEntriesConnectOrCreateFieldInputOnCreate',
})


UserBlobEntriesConnectOrCreateFieldInputOnCreate = TypedDict('UserBlobEntriesConnectOrCreateFieldInputOnCreate', {
	'node': 'BlobEntryOnCreateInput',
})


UserBlobEntriesCreateFieldInput = TypedDict('UserBlobEntriesCreateFieldInput', {
	'node': 'BlobEntryCreateInput',
})


UserBlobEntriesDeleteFieldInput = TypedDict('UserBlobEntriesDeleteFieldInput', {
	'where': Optional['UserBlobEntriesConnectionWhere'],
	'delete': Optional['BlobEntryDeleteInput'],
})


UserBlobEntriesDisconnectFieldInput = TypedDict('UserBlobEntriesDisconnectFieldInput', {
	'where': Optional['UserBlobEntriesConnectionWhere'],
	'disconnect': Optional['BlobEntryDisconnectInput'],
})


UserBlobEntriesFieldInput = TypedDict('UserBlobEntriesFieldInput', {
	'create': Optional[List['UserBlobEntriesCreateFieldInput']],
	'connect': Optional[List['UserBlobEntriesConnectFieldInput']],
	'connectOrCreate': Optional[List['UserBlobEntriesConnectOrCreateFieldInput']],
})


UserBlobEntriesNodeAggregationWhereInput = TypedDict('UserBlobEntriesNodeAggregationWhereInput', {
	'AND': Optional[List['UserBlobEntriesNodeAggregationWhereInput']],
	'OR': Optional[List['UserBlobEntriesNodeAggregationWhereInput']],
	'NOT': Optional['UserBlobEntriesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'hash_AVERAGE_LENGTH_EQUAL': Optional[float],
	'hash_LONGEST_LENGTH_EQUAL': Optional[int],
	'hash_SHORTEST_LENGTH_EQUAL': Optional[int],
	'hash_AVERAGE_LENGTH_GT': Optional[float],
	'hash_LONGEST_LENGTH_GT': Optional[int],
	'hash_SHORTEST_LENGTH_GT': Optional[int],
	'hash_AVERAGE_LENGTH_GTE': Optional[float],
	'hash_LONGEST_LENGTH_GTE': Optional[int],
	'hash_SHORTEST_LENGTH_GTE': Optional[int],
	'hash_AVERAGE_LENGTH_LT': Optional[float],
	'hash_LONGEST_LENGTH_LT': Optional[int],
	'hash_SHORTEST_LENGTH_LT': Optional[int],
	'hash_AVERAGE_LENGTH_LTE': Optional[float],
	'hash_LONGEST_LENGTH_LTE': Optional[int],
	'hash_SHORTEST_LENGTH_LTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'mimeType_LONGEST_LENGTH_EQUAL': Optional[int],
	'mimeType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'mimeType_AVERAGE_LENGTH_GT': Optional[float],
	'mimeType_LONGEST_LENGTH_GT': Optional[int],
	'mimeType_SHORTEST_LENGTH_GT': Optional[int],
	'mimeType_AVERAGE_LENGTH_GTE': Optional[float],
	'mimeType_LONGEST_LENGTH_GTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_GTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_LT': Optional[float],
	'mimeType_LONGEST_LENGTH_LT': Optional[int],
	'mimeType_SHORTEST_LENGTH_LT': Optional[int],
	'mimeType_AVERAGE_LENGTH_LTE': Optional[float],
	'mimeType_LONGEST_LENGTH_LTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_LTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_EQUAL': Optional[float],
	'blobstore_LONGEST_LENGTH_EQUAL': Optional[int],
	'blobstore_SHORTEST_LENGTH_EQUAL': Optional[int],
	'blobstore_AVERAGE_LENGTH_GT': Optional[float],
	'blobstore_LONGEST_LENGTH_GT': Optional[int],
	'blobstore_SHORTEST_LENGTH_GT': Optional[int],
	'blobstore_AVERAGE_LENGTH_GTE': Optional[float],
	'blobstore_LONGEST_LENGTH_GTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_GTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_LT': Optional[float],
	'blobstore_LONGEST_LENGTH_LT': Optional[int],
	'blobstore_SHORTEST_LENGTH_LT': Optional[int],
	'blobstore_AVERAGE_LENGTH_LTE': Optional[float],
	'blobstore_LONGEST_LENGTH_LTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_LTE': Optional[int],
	'origin_AVERAGE_LENGTH_EQUAL': Optional[float],
	'origin_LONGEST_LENGTH_EQUAL': Optional[int],
	'origin_SHORTEST_LENGTH_EQUAL': Optional[int],
	'origin_AVERAGE_LENGTH_GT': Optional[float],
	'origin_LONGEST_LENGTH_GT': Optional[int],
	'origin_SHORTEST_LENGTH_GT': Optional[int],
	'origin_AVERAGE_LENGTH_GTE': Optional[float],
	'origin_LONGEST_LENGTH_GTE': Optional[int],
	'origin_SHORTEST_LENGTH_GTE': Optional[int],
	'origin_AVERAGE_LENGTH_LT': Optional[float],
	'origin_LONGEST_LENGTH_LT': Optional[int],
	'origin_SHORTEST_LENGTH_LT': Optional[int],
	'origin_AVERAGE_LENGTH_LTE': Optional[float],
	'origin_LONGEST_LENGTH_LTE': Optional[int],
	'origin_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'factorLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GT': Optional[float],
	'factorLabel_LONGEST_LENGTH_GT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_GTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LT': Optional[float],
	'factorLabel_LONGEST_LENGTH_LT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_LTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


UserBlobEntriesUpdateConnectionInput = TypedDict('UserBlobEntriesUpdateConnectionInput', {
	'node': Optional['BlobEntryUpdateInput'],
})


UserBlobEntriesUpdateFieldInput = TypedDict('UserBlobEntriesUpdateFieldInput', {
	'where': Optional['UserBlobEntriesConnectionWhere'],
	'update': Optional['UserBlobEntriesUpdateConnectionInput'],
	'connect': Optional[List['UserBlobEntriesConnectFieldInput']],
	'disconnect': Optional[List['UserBlobEntriesDisconnectFieldInput']],
	'create': Optional[List['UserBlobEntriesCreateFieldInput']],
	'delete': Optional[List['UserBlobEntriesDeleteFieldInput']],
	'connectOrCreate': Optional[List['UserBlobEntriesConnectOrCreateFieldInput']],
})


UserConnectInput = TypedDict('UserConnectInput', {
	'blobEntries': Optional[List['UserBlobEntriesConnectFieldInput']],
	'robots': Optional[List['UserRobotsConnectFieldInput']],
	'maps': Optional[List['UserMapsConnectFieldInput']],
})


UserConnectOrCreateInput = TypedDict('UserConnectOrCreateInput', {
	'blobEntries': Optional[List['UserBlobEntriesConnectOrCreateFieldInput']],
	'robots': Optional[List['UserRobotsConnectOrCreateFieldInput']],
	'maps': Optional[List['UserMapsConnectOrCreateFieldInput']],
})


UserConnectOrCreateWhere = TypedDict('UserConnectOrCreateWhere', {
	'node': 'UserUniqueWhere',
})


UserConnectWhere = TypedDict('UserConnectWhere', {
	'node': 'UserWhere',
})


UserCreateInput = TypedDict('UserCreateInput', {
	'sub': str,
	'givenName': str,
	'familyName': str,
	'status': str,
	'_version': str,
	'permissions': List[str],
	'label': 'EmailAddress',
	'metadata': Optional['Metadata'],
	'lastAuthenticatedTimestamp': Optional['DateTime'],
	'blobEntries': Optional['UserBlobEntriesFieldInput'],
	'robots': Optional['UserRobotsFieldInput'],
	'maps': Optional['UserMapsFieldInput'],
})


UserDeleteInput = TypedDict('UserDeleteInput', {
	'blobEntries': Optional[List['UserBlobEntriesDeleteFieldInput']],
	'robots': Optional[List['UserRobotsDeleteFieldInput']],
	'maps': Optional[List['UserMapsDeleteFieldInput']],
})


UserDisconnectInput = TypedDict('UserDisconnectInput', {
	'blobEntries': Optional[List['UserBlobEntriesDisconnectFieldInput']],
	'robots': Optional[List['UserRobotsDisconnectFieldInput']],
	'maps': Optional[List['UserMapsDisconnectFieldInput']],
})


UserIdCreateInput = TypedDict('UserIdCreateInput', {
	'id': 'UUID',
})


UserIdOptions = TypedDict('UserIdOptions', {
	'sort': Optional[List['UserIdSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


UserIdSort = TypedDict('UserIdSort', {
	'id': Optional['SortDirection'],
})


UserIdUpdateInput = TypedDict('UserIdUpdateInput', {
	'id': Optional['UUID'],
})


UserIdWhere = TypedDict('UserIdWhere', {
	'OR': Optional[List['UserIdWhere']],
	'AND': Optional[List['UserIdWhere']],
	'NOT': Optional['UserIdWhere'],
	'id': Optional['UUID'],
	'id_IN': Optional[List['UUID']],
})


UserMapRoleCreateInput = TypedDict('UserMapRoleCreateInput', {
	'role': str,
})


UserMapRoleSort = TypedDict('UserMapRoleSort', {
	'role': Optional['SortDirection'],
})


UserMapRoleUpdateInput = TypedDict('UserMapRoleUpdateInput', {
	'role': Optional[str],
})


UserMapRoleWhere = TypedDict('UserMapRoleWhere', {
	'OR': Optional[List['UserMapRoleWhere']],
	'AND': Optional[List['UserMapRoleWhere']],
	'NOT': Optional['UserMapRoleWhere'],
	'role': Optional[str],
	'role_IN': Optional[List[str]],
	'role_MATCHES': Optional[str],
	'role_CONTAINS': Optional[str],
	'role_STARTS_WITH': Optional[str],
	'role_ENDS_WITH': Optional[str],
})


UserMapsAggregateInput = TypedDict('UserMapsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['UserMapsAggregateInput']],
	'OR': Optional[List['UserMapsAggregateInput']],
	'NOT': Optional['UserMapsAggregateInput'],
	'node': Optional['UserMapsNodeAggregationWhereInput'],
	'edge': Optional['UserMapsEdgeAggregationWhereInput'],
})


UserMapsConnectFieldInput = TypedDict('UserMapsConnectFieldInput', {
	'where': Optional['MapConnectWhere'],
	'connect': Optional[List['MapConnectInput']],
	'edge': 'UserMapRoleCreateInput',
	'overwrite': bool,
})


UserMapsConnectionSort = TypedDict('UserMapsConnectionSort', {
	'edge': Optional['UserMapRoleSort'],
	'node': Optional['MapSort'],
})


UserMapsConnectionWhere = TypedDict('UserMapsConnectionWhere', {
	'AND': Optional[List['UserMapsConnectionWhere']],
	'OR': Optional[List['UserMapsConnectionWhere']],
	'NOT': Optional['UserMapsConnectionWhere'],
	'edge': Optional['UserMapRoleWhere'],
	'node': Optional['MapWhere'],
})


UserMapsConnectOrCreateFieldInput = TypedDict('UserMapsConnectOrCreateFieldInput', {
	'where': 'MapConnectOrCreateWhere',
	'onCreate': 'UserMapsConnectOrCreateFieldInputOnCreate',
})


UserMapsConnectOrCreateFieldInputOnCreate = TypedDict('UserMapsConnectOrCreateFieldInputOnCreate', {
	'node': 'MapOnCreateInput',
	'edge': 'UserMapRoleCreateInput',
})


UserMapsCreateFieldInput = TypedDict('UserMapsCreateFieldInput', {
	'node': 'MapCreateInput',
	'edge': 'UserMapRoleCreateInput',
})


UserMapsDeleteFieldInput = TypedDict('UserMapsDeleteFieldInput', {
	'where': Optional['UserMapsConnectionWhere'],
	'delete': Optional['MapDeleteInput'],
})


UserMapsDisconnectFieldInput = TypedDict('UserMapsDisconnectFieldInput', {
	'where': Optional['UserMapsConnectionWhere'],
	'disconnect': Optional['MapDisconnectInput'],
})


UserMapsEdgeAggregationWhereInput = TypedDict('UserMapsEdgeAggregationWhereInput', {
	'AND': Optional[List['UserMapsEdgeAggregationWhereInput']],
	'OR': Optional[List['UserMapsEdgeAggregationWhereInput']],
	'NOT': Optional['UserMapsEdgeAggregationWhereInput'],
	'role_AVERAGE_LENGTH_EQUAL': Optional[float],
	'role_LONGEST_LENGTH_EQUAL': Optional[int],
	'role_SHORTEST_LENGTH_EQUAL': Optional[int],
	'role_AVERAGE_LENGTH_GT': Optional[float],
	'role_LONGEST_LENGTH_GT': Optional[int],
	'role_SHORTEST_LENGTH_GT': Optional[int],
	'role_AVERAGE_LENGTH_GTE': Optional[float],
	'role_LONGEST_LENGTH_GTE': Optional[int],
	'role_SHORTEST_LENGTH_GTE': Optional[int],
	'role_AVERAGE_LENGTH_LT': Optional[float],
	'role_LONGEST_LENGTH_LT': Optional[int],
	'role_SHORTEST_LENGTH_LT': Optional[int],
	'role_AVERAGE_LENGTH_LTE': Optional[float],
	'role_LONGEST_LENGTH_LTE': Optional[int],
	'role_SHORTEST_LENGTH_LTE': Optional[int],
})


UserMapsFieldInput = TypedDict('UserMapsFieldInput', {
	'create': Optional[List['UserMapsCreateFieldInput']],
	'connect': Optional[List['UserMapsConnectFieldInput']],
	'connectOrCreate': Optional[List['UserMapsConnectOrCreateFieldInput']],
})


UserMapsNodeAggregationWhereInput = TypedDict('UserMapsNodeAggregationWhereInput', {
	'AND': Optional[List['UserMapsNodeAggregationWhereInput']],
	'OR': Optional[List['UserMapsNodeAggregationWhereInput']],
	'NOT': Optional['UserMapsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'status_AVERAGE_LENGTH_EQUAL': Optional[float],
	'status_LONGEST_LENGTH_EQUAL': Optional[int],
	'status_SHORTEST_LENGTH_EQUAL': Optional[int],
	'status_AVERAGE_LENGTH_GT': Optional[float],
	'status_LONGEST_LENGTH_GT': Optional[int],
	'status_SHORTEST_LENGTH_GT': Optional[int],
	'status_AVERAGE_LENGTH_GTE': Optional[float],
	'status_LONGEST_LENGTH_GTE': Optional[int],
	'status_SHORTEST_LENGTH_GTE': Optional[int],
	'status_AVERAGE_LENGTH_LT': Optional[float],
	'status_LONGEST_LENGTH_LT': Optional[int],
	'status_SHORTEST_LENGTH_LT': Optional[int],
	'status_AVERAGE_LENGTH_LTE': Optional[float],
	'status_LONGEST_LENGTH_LTE': Optional[int],
	'status_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


UserMapsUpdateConnectionInput = TypedDict('UserMapsUpdateConnectionInput', {
	'node': Optional['MapUpdateInput'],
	'edge': Optional['UserMapRoleUpdateInput'],
})


UserMapsUpdateFieldInput = TypedDict('UserMapsUpdateFieldInput', {
	'where': Optional['UserMapsConnectionWhere'],
	'update': Optional['UserMapsUpdateConnectionInput'],
	'connect': Optional[List['UserMapsConnectFieldInput']],
	'disconnect': Optional[List['UserMapsDisconnectFieldInput']],
	'create': Optional[List['UserMapsCreateFieldInput']],
	'delete': Optional[List['UserMapsDeleteFieldInput']],
	'connectOrCreate': Optional[List['UserMapsConnectOrCreateFieldInput']],
})


UserOnCreateInput = TypedDict('UserOnCreateInput', {
	'sub': str,
	'givenName': str,
	'familyName': str,
	'status': str,
	'_version': str,
	'permissions': List[str],
	'label': 'EmailAddress',
	'metadata': Optional['Metadata'],
	'lastAuthenticatedTimestamp': Optional['DateTime'],
})


UserOptions = TypedDict('UserOptions', {
	'sort': Optional[List['UserSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


UserRelationInput = TypedDict('UserRelationInput', {
	'blobEntries': Optional[List['UserBlobEntriesCreateFieldInput']],
	'robots': Optional[List['UserRobotsCreateFieldInput']],
	'maps': Optional[List['UserMapsCreateFieldInput']],
})


UserRobotsAggregateInput = TypedDict('UserRobotsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['UserRobotsAggregateInput']],
	'OR': Optional[List['UserRobotsAggregateInput']],
	'NOT': Optional['UserRobotsAggregateInput'],
	'node': Optional['UserRobotsNodeAggregationWhereInput'],
})


UserRobotsConnectFieldInput = TypedDict('UserRobotsConnectFieldInput', {
	'where': Optional['RobotConnectWhere'],
	'connect': Optional[List['RobotConnectInput']],
	'overwrite': bool,
})


UserRobotsConnectionSort = TypedDict('UserRobotsConnectionSort', {
	'node': Optional['RobotSort'],
})


UserRobotsConnectionWhere = TypedDict('UserRobotsConnectionWhere', {
	'AND': Optional[List['UserRobotsConnectionWhere']],
	'OR': Optional[List['UserRobotsConnectionWhere']],
	'NOT': Optional['UserRobotsConnectionWhere'],
	'node': Optional['RobotWhere'],
})


UserRobotsConnectOrCreateFieldInput = TypedDict('UserRobotsConnectOrCreateFieldInput', {
	'where': 'RobotConnectOrCreateWhere',
	'onCreate': 'UserRobotsConnectOrCreateFieldInputOnCreate',
})


UserRobotsConnectOrCreateFieldInputOnCreate = TypedDict('UserRobotsConnectOrCreateFieldInputOnCreate', {
	'node': 'RobotOnCreateInput',
})


UserRobotsCreateFieldInput = TypedDict('UserRobotsCreateFieldInput', {
	'node': 'RobotCreateInput',
})


UserRobotsDeleteFieldInput = TypedDict('UserRobotsDeleteFieldInput', {
	'where': Optional['UserRobotsConnectionWhere'],
	'delete': Optional['RobotDeleteInput'],
})


UserRobotsDisconnectFieldInput = TypedDict('UserRobotsDisconnectFieldInput', {
	'where': Optional['UserRobotsConnectionWhere'],
	'disconnect': Optional['RobotDisconnectInput'],
})


UserRobotsFieldInput = TypedDict('UserRobotsFieldInput', {
	'create': Optional[List['UserRobotsCreateFieldInput']],
	'connect': Optional[List['UserRobotsConnectFieldInput']],
	'connectOrCreate': Optional[List['UserRobotsConnectOrCreateFieldInput']],
})


UserRobotsNodeAggregationWhereInput = TypedDict('UserRobotsNodeAggregationWhereInput', {
	'AND': Optional[List['UserRobotsNodeAggregationWhereInput']],
	'OR': Optional[List['UserRobotsNodeAggregationWhereInput']],
	'NOT': Optional['UserRobotsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


UserRobotsUpdateConnectionInput = TypedDict('UserRobotsUpdateConnectionInput', {
	'node': Optional['RobotUpdateInput'],
})


UserRobotsUpdateFieldInput = TypedDict('UserRobotsUpdateFieldInput', {
	'where': Optional['UserRobotsConnectionWhere'],
	'update': Optional['UserRobotsUpdateConnectionInput'],
	'connect': Optional[List['UserRobotsConnectFieldInput']],
	'disconnect': Optional[List['UserRobotsDisconnectFieldInput']],
	'create': Optional[List['UserRobotsCreateFieldInput']],
	'delete': Optional[List['UserRobotsDeleteFieldInput']],
	'connectOrCreate': Optional[List['UserRobotsConnectOrCreateFieldInput']],
})


UserSort = TypedDict('UserSort', {
	'id': Optional['SortDirection'],
	'sub': Optional['SortDirection'],
	'givenName': Optional['SortDirection'],
	'familyName': Optional['SortDirection'],
	'status': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'metadata': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
	'lastAuthenticatedTimestamp': Optional['SortDirection'],
})


UserUniqueWhere = TypedDict('UserUniqueWhere', {
	'id': Optional[str],
	'sub': Optional[str],
	'label': Optional['EmailAddress'],
})


UserUpdateInput = TypedDict('UserUpdateInput', {
	'sub': Optional[str],
	'givenName': Optional[str],
	'familyName': Optional[str],
	'status': Optional[str],
	'_version': Optional[str],
	'permissions': Optional[List[str]],
	'label': Optional['EmailAddress'],
	'metadata': Optional['Metadata'],
	'lastAuthenticatedTimestamp': Optional['DateTime'],
	'permissions_POP': Optional[int],
	'permissions_PUSH': Optional[List[str]],
	'blobEntries': Optional[List['UserBlobEntriesUpdateFieldInput']],
	'robots': Optional[List['UserRobotsUpdateFieldInput']],
	'maps': Optional[List['UserMapsUpdateFieldInput']],
})


UserWhere = TypedDict('UserWhere', {
	'OR': Optional[List['UserWhere']],
	'AND': Optional[List['UserWhere']],
	'NOT': Optional['UserWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'sub': Optional[str],
	'sub_IN': Optional[List[str]],
	'sub_MATCHES': Optional[str],
	'sub_CONTAINS': Optional[str],
	'sub_STARTS_WITH': Optional[str],
	'sub_ENDS_WITH': Optional[str],
	'givenName': Optional[str],
	'givenName_IN': Optional[List[str]],
	'givenName_MATCHES': Optional[str],
	'givenName_CONTAINS': Optional[str],
	'givenName_STARTS_WITH': Optional[str],
	'givenName_ENDS_WITH': Optional[str],
	'familyName': Optional[str],
	'familyName_IN': Optional[List[str]],
	'familyName_MATCHES': Optional[str],
	'familyName_CONTAINS': Optional[str],
	'familyName_STARTS_WITH': Optional[str],
	'familyName_ENDS_WITH': Optional[str],
	'status': Optional[str],
	'status_IN': Optional[List[str]],
	'status_MATCHES': Optional[str],
	'status_CONTAINS': Optional[str],
	'status_STARTS_WITH': Optional[str],
	'status_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'permissions': Optional[List[str]],
	'permissions_INCLUDES': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp': Optional['DateTime'],
	'lastAuthenticatedTimestamp_IN': Optional[List['DateTime']],
	'lastAuthenticatedTimestamp_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_GTE': Optional['DateTime'],
	'label': Optional['EmailAddress'],
	'label_IN': Optional[List['EmailAddress']],
	'metadata': Optional['Metadata'],
	'metadata_IN': Optional[List['Metadata']],
	'blobEntriesAggregate': Optional['UserBlobEntriesAggregateInput'],
	'blobEntries_ALL': Optional['BlobEntryWhere'],
	'blobEntries_NONE': Optional['BlobEntryWhere'],
	'blobEntries_SINGLE': Optional['BlobEntryWhere'],
	'blobEntries_SOME': Optional['BlobEntryWhere'],
	'robotsAggregate': Optional['UserRobotsAggregateInput'],
	'robots_ALL': Optional['RobotWhere'],
	'robots_NONE': Optional['RobotWhere'],
	'robots_SINGLE': Optional['RobotWhere'],
	'robots_SOME': Optional['RobotWhere'],
	'mapsAggregate': Optional['UserMapsAggregateInput'],
	'maps_ALL': Optional['MapWhere'],
	'maps_NONE': Optional['MapWhere'],
	'maps_SINGLE': Optional['MapWhere'],
	'maps_SOME': Optional['MapWhere'],
	'blobEntriesConnection_ALL': Optional['UserBlobEntriesConnectionWhere'],
	'blobEntriesConnection_NONE': Optional['UserBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SINGLE': Optional['UserBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SOME': Optional['UserBlobEntriesConnectionWhere'],
	'robotsConnection_ALL': Optional['UserRobotsConnectionWhere'],
	'robotsConnection_NONE': Optional['UserRobotsConnectionWhere'],
	'robotsConnection_SINGLE': Optional['UserRobotsConnectionWhere'],
	'robotsConnection_SOME': Optional['UserRobotsConnectionWhere'],
	'mapsConnection_ALL': Optional['UserMapsConnectionWhere'],
	'mapsConnection_NONE': Optional['UserMapsConnectionWhere'],
	'mapsConnection_SINGLE': Optional['UserMapsConnectionWhere'],
	'mapsConnection_SOME': Optional['UserMapsConnectionWhere'],
})


VariableBlobEntriesAggregateInput = TypedDict('VariableBlobEntriesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['VariableBlobEntriesAggregateInput']],
	'OR': Optional[List['VariableBlobEntriesAggregateInput']],
	'NOT': Optional['VariableBlobEntriesAggregateInput'],
	'node': Optional['VariableBlobEntriesNodeAggregationWhereInput'],
})


VariableBlobEntriesConnectFieldInput = TypedDict('VariableBlobEntriesConnectFieldInput', {
	'where': Optional['BlobEntryConnectWhere'],
	'connect': Optional[List['BlobEntryConnectInput']],
	'overwrite': bool,
})


VariableBlobEntriesConnectionSort = TypedDict('VariableBlobEntriesConnectionSort', {
	'node': Optional['BlobEntrySort'],
})


VariableBlobEntriesConnectionWhere = TypedDict('VariableBlobEntriesConnectionWhere', {
	'AND': Optional[List['VariableBlobEntriesConnectionWhere']],
	'OR': Optional[List['VariableBlobEntriesConnectionWhere']],
	'NOT': Optional['VariableBlobEntriesConnectionWhere'],
	'node': Optional['BlobEntryWhere'],
})


VariableBlobEntriesConnectOrCreateFieldInput = TypedDict('VariableBlobEntriesConnectOrCreateFieldInput', {
	'where': 'BlobEntryConnectOrCreateWhere',
	'onCreate': 'VariableBlobEntriesConnectOrCreateFieldInputOnCreate',
})


VariableBlobEntriesConnectOrCreateFieldInputOnCreate = TypedDict('VariableBlobEntriesConnectOrCreateFieldInputOnCreate', {
	'node': 'BlobEntryOnCreateInput',
})


VariableBlobEntriesCreateFieldInput = TypedDict('VariableBlobEntriesCreateFieldInput', {
	'node': 'BlobEntryCreateInput',
})


VariableBlobEntriesDeleteFieldInput = TypedDict('VariableBlobEntriesDeleteFieldInput', {
	'where': Optional['VariableBlobEntriesConnectionWhere'],
	'delete': Optional['BlobEntryDeleteInput'],
})


VariableBlobEntriesDisconnectFieldInput = TypedDict('VariableBlobEntriesDisconnectFieldInput', {
	'where': Optional['VariableBlobEntriesConnectionWhere'],
	'disconnect': Optional['BlobEntryDisconnectInput'],
})


VariableBlobEntriesFieldInput = TypedDict('VariableBlobEntriesFieldInput', {
	'create': Optional[List['VariableBlobEntriesCreateFieldInput']],
	'connect': Optional[List['VariableBlobEntriesConnectFieldInput']],
	'connectOrCreate': Optional[List['VariableBlobEntriesConnectOrCreateFieldInput']],
})


VariableBlobEntriesNodeAggregationWhereInput = TypedDict('VariableBlobEntriesNodeAggregationWhereInput', {
	'AND': Optional[List['VariableBlobEntriesNodeAggregationWhereInput']],
	'OR': Optional[List['VariableBlobEntriesNodeAggregationWhereInput']],
	'NOT': Optional['VariableBlobEntriesNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'hash_AVERAGE_LENGTH_EQUAL': Optional[float],
	'hash_LONGEST_LENGTH_EQUAL': Optional[int],
	'hash_SHORTEST_LENGTH_EQUAL': Optional[int],
	'hash_AVERAGE_LENGTH_GT': Optional[float],
	'hash_LONGEST_LENGTH_GT': Optional[int],
	'hash_SHORTEST_LENGTH_GT': Optional[int],
	'hash_AVERAGE_LENGTH_GTE': Optional[float],
	'hash_LONGEST_LENGTH_GTE': Optional[int],
	'hash_SHORTEST_LENGTH_GTE': Optional[int],
	'hash_AVERAGE_LENGTH_LT': Optional[float],
	'hash_LONGEST_LENGTH_LT': Optional[int],
	'hash_SHORTEST_LENGTH_LT': Optional[int],
	'hash_AVERAGE_LENGTH_LTE': Optional[float],
	'hash_LONGEST_LENGTH_LTE': Optional[int],
	'hash_SHORTEST_LENGTH_LTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'mimeType_LONGEST_LENGTH_EQUAL': Optional[int],
	'mimeType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'mimeType_AVERAGE_LENGTH_GT': Optional[float],
	'mimeType_LONGEST_LENGTH_GT': Optional[int],
	'mimeType_SHORTEST_LENGTH_GT': Optional[int],
	'mimeType_AVERAGE_LENGTH_GTE': Optional[float],
	'mimeType_LONGEST_LENGTH_GTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_GTE': Optional[int],
	'mimeType_AVERAGE_LENGTH_LT': Optional[float],
	'mimeType_LONGEST_LENGTH_LT': Optional[int],
	'mimeType_SHORTEST_LENGTH_LT': Optional[int],
	'mimeType_AVERAGE_LENGTH_LTE': Optional[float],
	'mimeType_LONGEST_LENGTH_LTE': Optional[int],
	'mimeType_SHORTEST_LENGTH_LTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_EQUAL': Optional[float],
	'blobstore_LONGEST_LENGTH_EQUAL': Optional[int],
	'blobstore_SHORTEST_LENGTH_EQUAL': Optional[int],
	'blobstore_AVERAGE_LENGTH_GT': Optional[float],
	'blobstore_LONGEST_LENGTH_GT': Optional[int],
	'blobstore_SHORTEST_LENGTH_GT': Optional[int],
	'blobstore_AVERAGE_LENGTH_GTE': Optional[float],
	'blobstore_LONGEST_LENGTH_GTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_GTE': Optional[int],
	'blobstore_AVERAGE_LENGTH_LT': Optional[float],
	'blobstore_LONGEST_LENGTH_LT': Optional[int],
	'blobstore_SHORTEST_LENGTH_LT': Optional[int],
	'blobstore_AVERAGE_LENGTH_LTE': Optional[float],
	'blobstore_LONGEST_LENGTH_LTE': Optional[int],
	'blobstore_SHORTEST_LENGTH_LTE': Optional[int],
	'origin_AVERAGE_LENGTH_EQUAL': Optional[float],
	'origin_LONGEST_LENGTH_EQUAL': Optional[int],
	'origin_SHORTEST_LENGTH_EQUAL': Optional[int],
	'origin_AVERAGE_LENGTH_GT': Optional[float],
	'origin_LONGEST_LENGTH_GT': Optional[int],
	'origin_SHORTEST_LENGTH_GT': Optional[int],
	'origin_AVERAGE_LENGTH_GTE': Optional[float],
	'origin_LONGEST_LENGTH_GTE': Optional[int],
	'origin_SHORTEST_LENGTH_GTE': Optional[int],
	'origin_AVERAGE_LENGTH_LT': Optional[float],
	'origin_LONGEST_LENGTH_LT': Optional[int],
	'origin_SHORTEST_LENGTH_LT': Optional[int],
	'origin_AVERAGE_LENGTH_LTE': Optional[float],
	'origin_LONGEST_LENGTH_LTE': Optional[int],
	'origin_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'factorLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GT': Optional[float],
	'factorLabel_LONGEST_LENGTH_GT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_GTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LT': Optional[float],
	'factorLabel_LONGEST_LENGTH_LT': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LT': Optional[int],
	'factorLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'factorLabel_LONGEST_LENGTH_LTE': Optional[int],
	'factorLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


VariableBlobEntriesUpdateConnectionInput = TypedDict('VariableBlobEntriesUpdateConnectionInput', {
	'node': Optional['BlobEntryUpdateInput'],
})


VariableBlobEntriesUpdateFieldInput = TypedDict('VariableBlobEntriesUpdateFieldInput', {
	'where': Optional['VariableBlobEntriesConnectionWhere'],
	'update': Optional['VariableBlobEntriesUpdateConnectionInput'],
	'connect': Optional[List['VariableBlobEntriesConnectFieldInput']],
	'disconnect': Optional[List['VariableBlobEntriesDisconnectFieldInput']],
	'create': Optional[List['VariableBlobEntriesCreateFieldInput']],
	'delete': Optional[List['VariableBlobEntriesDeleteFieldInput']],
	'connectOrCreate': Optional[List['VariableBlobEntriesConnectOrCreateFieldInput']],
})


VariableConnectInput = TypedDict('VariableConnectInput', {
	'ppes': Optional[List['VariablePpesConnectFieldInput']],
	'blobEntries': Optional[List['VariableBlobEntriesConnectFieldInput']],
	'solverData': Optional[List['VariableSolverDataConnectFieldInput']],
	'factors': Optional[List['VariableFactorsConnectFieldInput']],
	'session': Optional['VariableSessionConnectFieldInput'],
})


VariableConnectOrCreateInput = TypedDict('VariableConnectOrCreateInput', {
	'ppes': Optional[List['VariablePpesConnectOrCreateFieldInput']],
	'blobEntries': Optional[List['VariableBlobEntriesConnectOrCreateFieldInput']],
	'solverData': Optional[List['VariableSolverDataConnectOrCreateFieldInput']],
	'factors': Optional[List['VariableFactorsConnectOrCreateFieldInput']],
	'session': Optional['VariableSessionConnectOrCreateFieldInput'],
})


VariableConnectOrCreateWhere = TypedDict('VariableConnectOrCreateWhere', {
	'node': 'VariableUniqueWhere',
})


VariableConnectWhere = TypedDict('VariableConnectWhere', {
	'node': 'VariableWhere',
})


VariableCreateInput = TypedDict('VariableCreateInput', {
	'label': str,
	'nstime': 'BigInt',
	'variableType': str,
	'solvable': int,
	'tags': List[str],
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'metadata': Optional['Metadata'],
	'timestamp': 'DateTime',
	'ppes': Optional['VariablePpesFieldInput'],
	'blobEntries': Optional['VariableBlobEntriesFieldInput'],
	'solverData': Optional['VariableSolverDataFieldInput'],
	'factors': Optional['VariableFactorsFieldInput'],
	'session': Optional['VariableSessionFieldInput'],
})


VariableDeleteInput = TypedDict('VariableDeleteInput', {
	'ppes': Optional[List['VariablePpesDeleteFieldInput']],
	'blobEntries': Optional[List['VariableBlobEntriesDeleteFieldInput']],
	'solverData': Optional[List['VariableSolverDataDeleteFieldInput']],
	'factors': Optional[List['VariableFactorsDeleteFieldInput']],
	'session': Optional['VariableSessionDeleteFieldInput'],
})


VariableDisconnectInput = TypedDict('VariableDisconnectInput', {
	'ppes': Optional[List['VariablePpesDisconnectFieldInput']],
	'blobEntries': Optional[List['VariableBlobEntriesDisconnectFieldInput']],
	'solverData': Optional[List['VariableSolverDataDisconnectFieldInput']],
	'factors': Optional[List['VariableFactorsDisconnectFieldInput']],
	'session': Optional['VariableSessionDisconnectFieldInput'],
})


VariableFactorsAggregateInput = TypedDict('VariableFactorsAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['VariableFactorsAggregateInput']],
	'OR': Optional[List['VariableFactorsAggregateInput']],
	'NOT': Optional['VariableFactorsAggregateInput'],
	'node': Optional['VariableFactorsNodeAggregationWhereInput'],
})


VariableFactorsConnectFieldInput = TypedDict('VariableFactorsConnectFieldInput', {
	'where': Optional['FactorConnectWhere'],
	'connect': Optional[List['FactorConnectInput']],
	'overwrite': bool,
})


VariableFactorsConnectionSort = TypedDict('VariableFactorsConnectionSort', {
	'node': Optional['FactorSort'],
})


VariableFactorsConnectionWhere = TypedDict('VariableFactorsConnectionWhere', {
	'AND': Optional[List['VariableFactorsConnectionWhere']],
	'OR': Optional[List['VariableFactorsConnectionWhere']],
	'NOT': Optional['VariableFactorsConnectionWhere'],
	'node': Optional['FactorWhere'],
})


VariableFactorsConnectOrCreateFieldInput = TypedDict('VariableFactorsConnectOrCreateFieldInput', {
	'where': 'FactorConnectOrCreateWhere',
	'onCreate': 'VariableFactorsConnectOrCreateFieldInputOnCreate',
})


VariableFactorsConnectOrCreateFieldInputOnCreate = TypedDict('VariableFactorsConnectOrCreateFieldInputOnCreate', {
	'node': 'FactorOnCreateInput',
})


VariableFactorsCreateFieldInput = TypedDict('VariableFactorsCreateFieldInput', {
	'node': 'FactorCreateInput',
})


VariableFactorsDeleteFieldInput = TypedDict('VariableFactorsDeleteFieldInput', {
	'where': Optional['VariableFactorsConnectionWhere'],
	'delete': Optional['FactorDeleteInput'],
})


VariableFactorsDisconnectFieldInput = TypedDict('VariableFactorsDisconnectFieldInput', {
	'where': Optional['VariableFactorsConnectionWhere'],
	'disconnect': Optional['FactorDisconnectInput'],
})


VariableFactorsFieldInput = TypedDict('VariableFactorsFieldInput', {
	'create': Optional[List['VariableFactorsCreateFieldInput']],
	'connect': Optional[List['VariableFactorsConnectFieldInput']],
	'connectOrCreate': Optional[List['VariableFactorsConnectOrCreateFieldInput']],
})


VariableFactorsNodeAggregationWhereInput = TypedDict('VariableFactorsNodeAggregationWhereInput', {
	'AND': Optional[List['VariableFactorsNodeAggregationWhereInput']],
	'OR': Optional[List['VariableFactorsNodeAggregationWhereInput']],
	'NOT': Optional['VariableFactorsNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'fnctype_AVERAGE_LENGTH_EQUAL': Optional[float],
	'fnctype_LONGEST_LENGTH_EQUAL': Optional[int],
	'fnctype_SHORTEST_LENGTH_EQUAL': Optional[int],
	'fnctype_AVERAGE_LENGTH_GT': Optional[float],
	'fnctype_LONGEST_LENGTH_GT': Optional[int],
	'fnctype_SHORTEST_LENGTH_GT': Optional[int],
	'fnctype_AVERAGE_LENGTH_GTE': Optional[float],
	'fnctype_LONGEST_LENGTH_GTE': Optional[int],
	'fnctype_SHORTEST_LENGTH_GTE': Optional[int],
	'fnctype_AVERAGE_LENGTH_LT': Optional[float],
	'fnctype_LONGEST_LENGTH_LT': Optional[int],
	'fnctype_SHORTEST_LENGTH_LT': Optional[int],
	'fnctype_AVERAGE_LENGTH_LTE': Optional[float],
	'fnctype_LONGEST_LENGTH_LTE': Optional[int],
	'fnctype_SHORTEST_LENGTH_LTE': Optional[int],
	'data_AVERAGE_LENGTH_EQUAL': Optional[float],
	'data_LONGEST_LENGTH_EQUAL': Optional[int],
	'data_SHORTEST_LENGTH_EQUAL': Optional[int],
	'data_AVERAGE_LENGTH_GT': Optional[float],
	'data_LONGEST_LENGTH_GT': Optional[int],
	'data_SHORTEST_LENGTH_GT': Optional[int],
	'data_AVERAGE_LENGTH_GTE': Optional[float],
	'data_LONGEST_LENGTH_GTE': Optional[int],
	'data_SHORTEST_LENGTH_GTE': Optional[int],
	'data_AVERAGE_LENGTH_LT': Optional[float],
	'data_LONGEST_LENGTH_LT': Optional[int],
	'data_SHORTEST_LENGTH_LT': Optional[int],
	'data_AVERAGE_LENGTH_LTE': Optional[float],
	'data_LONGEST_LENGTH_LTE': Optional[int],
	'data_SHORTEST_LENGTH_LTE': Optional[int],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'solvable_AVERAGE_EQUAL': Optional[float],
	'solvable_MIN_EQUAL': Optional[int],
	'solvable_MAX_EQUAL': Optional[int],
	'solvable_SUM_EQUAL': Optional[int],
	'solvable_AVERAGE_GT': Optional[float],
	'solvable_MIN_GT': Optional[int],
	'solvable_MAX_GT': Optional[int],
	'solvable_SUM_GT': Optional[int],
	'solvable_AVERAGE_GTE': Optional[float],
	'solvable_MIN_GTE': Optional[int],
	'solvable_MAX_GTE': Optional[int],
	'solvable_SUM_GTE': Optional[int],
	'solvable_AVERAGE_LT': Optional[float],
	'solvable_MIN_LT': Optional[int],
	'solvable_MAX_LT': Optional[int],
	'solvable_SUM_LT': Optional[int],
	'solvable_AVERAGE_LTE': Optional[float],
	'solvable_MIN_LTE': Optional[int],
	'solvable_MAX_LTE': Optional[int],
	'solvable_SUM_LTE': Optional[int],
	'nstime_AVERAGE_EQUAL': Optional['BigInt'],
	'nstime_MIN_EQUAL': Optional['BigInt'],
	'nstime_MAX_EQUAL': Optional['BigInt'],
	'nstime_SUM_EQUAL': Optional['BigInt'],
	'nstime_AVERAGE_GT': Optional['BigInt'],
	'nstime_MIN_GT': Optional['BigInt'],
	'nstime_MAX_GT': Optional['BigInt'],
	'nstime_SUM_GT': Optional['BigInt'],
	'nstime_AVERAGE_GTE': Optional['BigInt'],
	'nstime_MIN_GTE': Optional['BigInt'],
	'nstime_MAX_GTE': Optional['BigInt'],
	'nstime_SUM_GTE': Optional['BigInt'],
	'nstime_AVERAGE_LT': Optional['BigInt'],
	'nstime_MIN_LT': Optional['BigInt'],
	'nstime_MAX_LT': Optional['BigInt'],
	'nstime_SUM_LT': Optional['BigInt'],
	'nstime_AVERAGE_LTE': Optional['BigInt'],
	'nstime_MIN_LTE': Optional['BigInt'],
	'nstime_MAX_LTE': Optional['BigInt'],
	'nstime_SUM_LTE': Optional['BigInt'],
	'timestamp_MIN_EQUAL': Optional['DateTime'],
	'timestamp_MAX_EQUAL': Optional['DateTime'],
	'timestamp_MIN_GT': Optional['DateTime'],
	'timestamp_MAX_GT': Optional['DateTime'],
	'timestamp_MIN_GTE': Optional['DateTime'],
	'timestamp_MAX_GTE': Optional['DateTime'],
	'timestamp_MIN_LT': Optional['DateTime'],
	'timestamp_MAX_LT': Optional['DateTime'],
	'timestamp_MIN_LTE': Optional['DateTime'],
	'timestamp_MAX_LTE': Optional['DateTime'],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


VariableFactorsUpdateConnectionInput = TypedDict('VariableFactorsUpdateConnectionInput', {
	'node': Optional['FactorUpdateInput'],
})


VariableFactorsUpdateFieldInput = TypedDict('VariableFactorsUpdateFieldInput', {
	'where': Optional['VariableFactorsConnectionWhere'],
	'update': Optional['VariableFactorsUpdateConnectionInput'],
	'connect': Optional[List['VariableFactorsConnectFieldInput']],
	'disconnect': Optional[List['VariableFactorsDisconnectFieldInput']],
	'create': Optional[List['VariableFactorsCreateFieldInput']],
	'delete': Optional[List['VariableFactorsDeleteFieldInput']],
	'connectOrCreate': Optional[List['VariableFactorsConnectOrCreateFieldInput']],
})


VariableOnCreateInput = TypedDict('VariableOnCreateInput', {
	'label': str,
	'nstime': 'BigInt',
	'variableType': str,
	'solvable': int,
	'tags': List[str],
	'_version': str,
	'userLabel': str,
	'robotLabel': str,
	'sessionLabel': str,
	'metadata': Optional['Metadata'],
	'timestamp': 'DateTime',
})


VariableOptions = TypedDict('VariableOptions', {
	'sort': Optional[List['VariableSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


VariablePpesAggregateInput = TypedDict('VariablePpesAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['VariablePpesAggregateInput']],
	'OR': Optional[List['VariablePpesAggregateInput']],
	'NOT': Optional['VariablePpesAggregateInput'],
	'node': Optional['VariablePpesNodeAggregationWhereInput'],
})


VariablePpesConnectFieldInput = TypedDict('VariablePpesConnectFieldInput', {
	'where': Optional['PPEConnectWhere'],
	'connect': Optional[List['PPEConnectInput']],
	'overwrite': bool,
})


VariablePpesConnectionSort = TypedDict('VariablePpesConnectionSort', {
	'node': Optional['PPESort'],
})


VariablePpesConnectionWhere = TypedDict('VariablePpesConnectionWhere', {
	'AND': Optional[List['VariablePpesConnectionWhere']],
	'OR': Optional[List['VariablePpesConnectionWhere']],
	'NOT': Optional['VariablePpesConnectionWhere'],
	'node': Optional['PPEWhere'],
})


VariablePpesConnectOrCreateFieldInput = TypedDict('VariablePpesConnectOrCreateFieldInput', {
	'where': 'PPEConnectOrCreateWhere',
	'onCreate': 'VariablePpesConnectOrCreateFieldInputOnCreate',
})


VariablePpesConnectOrCreateFieldInputOnCreate = TypedDict('VariablePpesConnectOrCreateFieldInputOnCreate', {
	'node': 'PPEOnCreateInput',
})


VariablePpesCreateFieldInput = TypedDict('VariablePpesCreateFieldInput', {
	'node': 'PPECreateInput',
})


VariablePpesDeleteFieldInput = TypedDict('VariablePpesDeleteFieldInput', {
	'where': Optional['VariablePpesConnectionWhere'],
	'delete': Optional['PPEDeleteInput'],
})


VariablePpesDisconnectFieldInput = TypedDict('VariablePpesDisconnectFieldInput', {
	'where': Optional['VariablePpesConnectionWhere'],
	'disconnect': Optional['PPEDisconnectInput'],
})


VariablePpesFieldInput = TypedDict('VariablePpesFieldInput', {
	'create': Optional[List['VariablePpesCreateFieldInput']],
	'connect': Optional[List['VariablePpesConnectFieldInput']],
	'connectOrCreate': Optional[List['VariablePpesConnectOrCreateFieldInput']],
})


VariablePpesNodeAggregationWhereInput = TypedDict('VariablePpesNodeAggregationWhereInput', {
	'AND': Optional[List['VariablePpesNodeAggregationWhereInput']],
	'OR': Optional[List['VariablePpesNodeAggregationWhereInput']],
	'NOT': Optional['VariablePpesNodeAggregationWhereInput'],
	'_type_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_type_LONGEST_LENGTH_EQUAL': Optional[int],
	'_type_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_type_AVERAGE_LENGTH_GT': Optional[float],
	'_type_LONGEST_LENGTH_GT': Optional[int],
	'_type_SHORTEST_LENGTH_GT': Optional[int],
	'_type_AVERAGE_LENGTH_GTE': Optional[float],
	'_type_LONGEST_LENGTH_GTE': Optional[int],
	'_type_SHORTEST_LENGTH_GTE': Optional[int],
	'_type_AVERAGE_LENGTH_LT': Optional[float],
	'_type_LONGEST_LENGTH_LT': Optional[int],
	'_type_SHORTEST_LENGTH_LT': Optional[int],
	'_type_AVERAGE_LENGTH_LTE': Optional[float],
	'_type_LONGEST_LENGTH_LTE': Optional[int],
	'_type_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


VariablePpesUpdateConnectionInput = TypedDict('VariablePpesUpdateConnectionInput', {
	'node': Optional['PPEUpdateInput'],
})


VariablePpesUpdateFieldInput = TypedDict('VariablePpesUpdateFieldInput', {
	'where': Optional['VariablePpesConnectionWhere'],
	'update': Optional['VariablePpesUpdateConnectionInput'],
	'connect': Optional[List['VariablePpesConnectFieldInput']],
	'disconnect': Optional[List['VariablePpesDisconnectFieldInput']],
	'create': Optional[List['VariablePpesCreateFieldInput']],
	'delete': Optional[List['VariablePpesDeleteFieldInput']],
	'connectOrCreate': Optional[List['VariablePpesConnectOrCreateFieldInput']],
})


VariableRelationInput = TypedDict('VariableRelationInput', {
	'ppes': Optional[List['VariablePpesCreateFieldInput']],
	'blobEntries': Optional[List['VariableBlobEntriesCreateFieldInput']],
	'solverData': Optional[List['VariableSolverDataCreateFieldInput']],
	'factors': Optional[List['VariableFactorsCreateFieldInput']],
	'session': Optional['VariableSessionCreateFieldInput'],
})


VariableSessionAggregateInput = TypedDict('VariableSessionAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['VariableSessionAggregateInput']],
	'OR': Optional[List['VariableSessionAggregateInput']],
	'NOT': Optional['VariableSessionAggregateInput'],
	'node': Optional['VariableSessionNodeAggregationWhereInput'],
})


VariableSessionConnectFieldInput = TypedDict('VariableSessionConnectFieldInput', {
	'where': Optional['SessionConnectWhere'],
	'connect': Optional['SessionConnectInput'],
	'overwrite': bool,
})


VariableSessionConnectionSort = TypedDict('VariableSessionConnectionSort', {
	'node': Optional['SessionSort'],
})


VariableSessionConnectionWhere = TypedDict('VariableSessionConnectionWhere', {
	'AND': Optional[List['VariableSessionConnectionWhere']],
	'OR': Optional[List['VariableSessionConnectionWhere']],
	'NOT': Optional['VariableSessionConnectionWhere'],
	'node': Optional['SessionWhere'],
})


VariableSessionConnectOrCreateFieldInput = TypedDict('VariableSessionConnectOrCreateFieldInput', {
	'where': 'SessionConnectOrCreateWhere',
	'onCreate': 'VariableSessionConnectOrCreateFieldInputOnCreate',
})


VariableSessionConnectOrCreateFieldInputOnCreate = TypedDict('VariableSessionConnectOrCreateFieldInputOnCreate', {
	'node': 'SessionOnCreateInput',
})


VariableSessionCreateFieldInput = TypedDict('VariableSessionCreateFieldInput', {
	'node': 'SessionCreateInput',
})


VariableSessionDeleteFieldInput = TypedDict('VariableSessionDeleteFieldInput', {
	'where': Optional['VariableSessionConnectionWhere'],
	'delete': Optional['SessionDeleteInput'],
})


VariableSessionDisconnectFieldInput = TypedDict('VariableSessionDisconnectFieldInput', {
	'where': Optional['VariableSessionConnectionWhere'],
	'disconnect': Optional['SessionDisconnectInput'],
})


VariableSessionFieldInput = TypedDict('VariableSessionFieldInput', {
	'create': Optional['VariableSessionCreateFieldInput'],
	'connect': Optional['VariableSessionConnectFieldInput'],
	'connectOrCreate': Optional['VariableSessionConnectOrCreateFieldInput'],
})


VariableSessionNodeAggregationWhereInput = TypedDict('VariableSessionNodeAggregationWhereInput', {
	'AND': Optional[List['VariableSessionNodeAggregationWhereInput']],
	'OR': Optional[List['VariableSessionNodeAggregationWhereInput']],
	'NOT': Optional['VariableSessionNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


VariableSessionUpdateConnectionInput = TypedDict('VariableSessionUpdateConnectionInput', {
	'node': Optional['SessionUpdateInput'],
})


VariableSessionUpdateFieldInput = TypedDict('VariableSessionUpdateFieldInput', {
	'where': Optional['VariableSessionConnectionWhere'],
	'update': Optional['VariableSessionUpdateConnectionInput'],
	'connect': Optional['VariableSessionConnectFieldInput'],
	'disconnect': Optional['VariableSessionDisconnectFieldInput'],
	'create': Optional['VariableSessionCreateFieldInput'],
	'delete': Optional['VariableSessionDeleteFieldInput'],
	'connectOrCreate': Optional['VariableSessionConnectOrCreateFieldInput'],
})


VariableSolverDataAggregateInput = TypedDict('VariableSolverDataAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['VariableSolverDataAggregateInput']],
	'OR': Optional[List['VariableSolverDataAggregateInput']],
	'NOT': Optional['VariableSolverDataAggregateInput'],
	'node': Optional['VariableSolverDataNodeAggregationWhereInput'],
})


VariableSolverDataConnectFieldInput = TypedDict('VariableSolverDataConnectFieldInput', {
	'where': Optional['SolverDataConnectWhere'],
	'connect': Optional[List['SolverDataConnectInput']],
	'overwrite': bool,
})


VariableSolverDataConnectionSort = TypedDict('VariableSolverDataConnectionSort', {
	'node': Optional['SolverDataSort'],
})


VariableSolverDataConnectionWhere = TypedDict('VariableSolverDataConnectionWhere', {
	'AND': Optional[List['VariableSolverDataConnectionWhere']],
	'OR': Optional[List['VariableSolverDataConnectionWhere']],
	'NOT': Optional['VariableSolverDataConnectionWhere'],
	'node': Optional['SolverDataWhere'],
})


VariableSolverDataConnectOrCreateFieldInput = TypedDict('VariableSolverDataConnectOrCreateFieldInput', {
	'where': 'SolverDataConnectOrCreateWhere',
	'onCreate': 'VariableSolverDataConnectOrCreateFieldInputOnCreate',
})


VariableSolverDataConnectOrCreateFieldInputOnCreate = TypedDict('VariableSolverDataConnectOrCreateFieldInputOnCreate', {
	'node': 'SolverDataOnCreateInput',
})


VariableSolverDataCreateFieldInput = TypedDict('VariableSolverDataCreateFieldInput', {
	'node': 'SolverDataCreateInput',
})


VariableSolverDataDeleteFieldInput = TypedDict('VariableSolverDataDeleteFieldInput', {
	'where': Optional['VariableSolverDataConnectionWhere'],
	'delete': Optional['SolverDataDeleteInput'],
})


VariableSolverDataDisconnectFieldInput = TypedDict('VariableSolverDataDisconnectFieldInput', {
	'where': Optional['VariableSolverDataConnectionWhere'],
	'disconnect': Optional['SolverDataDisconnectInput'],
})


VariableSolverDataFieldInput = TypedDict('VariableSolverDataFieldInput', {
	'create': Optional[List['VariableSolverDataCreateFieldInput']],
	'connect': Optional[List['VariableSolverDataConnectFieldInput']],
	'connectOrCreate': Optional[List['VariableSolverDataConnectOrCreateFieldInput']],
})


VariableSolverDataNodeAggregationWhereInput = TypedDict('VariableSolverDataNodeAggregationWhereInput', {
	'AND': Optional[List['VariableSolverDataNodeAggregationWhereInput']],
	'OR': Optional[List['VariableSolverDataNodeAggregationWhereInput']],
	'NOT': Optional['VariableSolverDataNodeAggregationWhereInput'],
	'BayesNetVertID_AVERAGE_LENGTH_EQUAL': Optional[float],
	'BayesNetVertID_LONGEST_LENGTH_EQUAL': Optional[int],
	'BayesNetVertID_SHORTEST_LENGTH_EQUAL': Optional[int],
	'BayesNetVertID_AVERAGE_LENGTH_GT': Optional[float],
	'BayesNetVertID_LONGEST_LENGTH_GT': Optional[int],
	'BayesNetVertID_SHORTEST_LENGTH_GT': Optional[int],
	'BayesNetVertID_AVERAGE_LENGTH_GTE': Optional[float],
	'BayesNetVertID_LONGEST_LENGTH_GTE': Optional[int],
	'BayesNetVertID_SHORTEST_LENGTH_GTE': Optional[int],
	'BayesNetVertID_AVERAGE_LENGTH_LT': Optional[float],
	'BayesNetVertID_LONGEST_LENGTH_LT': Optional[int],
	'BayesNetVertID_SHORTEST_LENGTH_LT': Optional[int],
	'BayesNetVertID_AVERAGE_LENGTH_LTE': Optional[float],
	'BayesNetVertID_LONGEST_LENGTH_LTE': Optional[int],
	'BayesNetVertID_SHORTEST_LENGTH_LTE': Optional[int],
	'variableType_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableType_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableType_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableType_AVERAGE_LENGTH_GT': Optional[float],
	'variableType_LONGEST_LENGTH_GT': Optional[int],
	'variableType_SHORTEST_LENGTH_GT': Optional[int],
	'variableType_AVERAGE_LENGTH_GTE': Optional[float],
	'variableType_LONGEST_LENGTH_GTE': Optional[int],
	'variableType_SHORTEST_LENGTH_GTE': Optional[int],
	'variableType_AVERAGE_LENGTH_LT': Optional[float],
	'variableType_LONGEST_LENGTH_LT': Optional[int],
	'variableType_SHORTEST_LENGTH_LT': Optional[int],
	'variableType_AVERAGE_LENGTH_LTE': Optional[float],
	'variableType_LONGEST_LENGTH_LTE': Optional[int],
	'variableType_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'userLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'userLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'userLabel_AVERAGE_LENGTH_GT': Optional[float],
	'userLabel_LONGEST_LENGTH_GT': Optional[int],
	'userLabel_SHORTEST_LENGTH_GT': Optional[int],
	'userLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'userLabel_LONGEST_LENGTH_GTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'userLabel_AVERAGE_LENGTH_LT': Optional[float],
	'userLabel_LONGEST_LENGTH_LT': Optional[int],
	'userLabel_SHORTEST_LENGTH_LT': Optional[int],
	'userLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'userLabel_LONGEST_LENGTH_LTE': Optional[int],
	'userLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'robotLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GT': Optional[float],
	'robotLabel_LONGEST_LENGTH_GT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_GTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LT': Optional[float],
	'robotLabel_LONGEST_LENGTH_LT': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LT': Optional[int],
	'robotLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'robotLabel_LONGEST_LENGTH_LTE': Optional[int],
	'robotLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sessionLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_GTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LT': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LT': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LT': Optional[int],
	'sessionLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'sessionLabel_LONGEST_LENGTH_LTE': Optional[int],
	'sessionLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_EQUAL': Optional[float],
	'variableLabel_LONGEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_SHORTEST_LENGTH_EQUAL': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GT': Optional[float],
	'variableLabel_LONGEST_LENGTH_GT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_GTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_GTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_GTE': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LT': Optional[float],
	'variableLabel_LONGEST_LENGTH_LT': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LT': Optional[int],
	'variableLabel_AVERAGE_LENGTH_LTE': Optional[float],
	'variableLabel_LONGEST_LENGTH_LTE': Optional[int],
	'variableLabel_SHORTEST_LENGTH_LTE': Optional[int],
	'dimbw_AVERAGE_EQUAL': Optional[float],
	'dimbw_MIN_EQUAL': Optional[int],
	'dimbw_MAX_EQUAL': Optional[int],
	'dimbw_SUM_EQUAL': Optional[int],
	'dimbw_AVERAGE_GT': Optional[float],
	'dimbw_MIN_GT': Optional[int],
	'dimbw_MAX_GT': Optional[int],
	'dimbw_SUM_GT': Optional[int],
	'dimbw_AVERAGE_GTE': Optional[float],
	'dimbw_MIN_GTE': Optional[int],
	'dimbw_MAX_GTE': Optional[int],
	'dimbw_SUM_GTE': Optional[int],
	'dimbw_AVERAGE_LT': Optional[float],
	'dimbw_MIN_LT': Optional[int],
	'dimbw_MAX_LT': Optional[int],
	'dimbw_SUM_LT': Optional[int],
	'dimbw_AVERAGE_LTE': Optional[float],
	'dimbw_MIN_LTE': Optional[int],
	'dimbw_MAX_LTE': Optional[int],
	'dimbw_SUM_LTE': Optional[int],
	'dims_AVERAGE_EQUAL': Optional[float],
	'dims_MIN_EQUAL': Optional[int],
	'dims_MAX_EQUAL': Optional[int],
	'dims_SUM_EQUAL': Optional[int],
	'dims_AVERAGE_GT': Optional[float],
	'dims_MIN_GT': Optional[int],
	'dims_MAX_GT': Optional[int],
	'dims_SUM_GT': Optional[int],
	'dims_AVERAGE_GTE': Optional[float],
	'dims_MIN_GTE': Optional[int],
	'dims_MAX_GTE': Optional[int],
	'dims_SUM_GTE': Optional[int],
	'dims_AVERAGE_LT': Optional[float],
	'dims_MIN_LT': Optional[int],
	'dims_MAX_LT': Optional[int],
	'dims_SUM_LT': Optional[int],
	'dims_AVERAGE_LTE': Optional[float],
	'dims_MIN_LTE': Optional[int],
	'dims_MAX_LTE': Optional[int],
	'dims_SUM_LTE': Optional[int],
	'dimval_AVERAGE_EQUAL': Optional[float],
	'dimval_MIN_EQUAL': Optional[int],
	'dimval_MAX_EQUAL': Optional[int],
	'dimval_SUM_EQUAL': Optional[int],
	'dimval_AVERAGE_GT': Optional[float],
	'dimval_MIN_GT': Optional[int],
	'dimval_MAX_GT': Optional[int],
	'dimval_SUM_GT': Optional[int],
	'dimval_AVERAGE_GTE': Optional[float],
	'dimval_MIN_GTE': Optional[int],
	'dimval_MAX_GTE': Optional[int],
	'dimval_SUM_GTE': Optional[int],
	'dimval_AVERAGE_LT': Optional[float],
	'dimval_MIN_LT': Optional[int],
	'dimval_MAX_LT': Optional[int],
	'dimval_SUM_LT': Optional[int],
	'dimval_AVERAGE_LTE': Optional[float],
	'dimval_MIN_LTE': Optional[int],
	'dimval_MAX_LTE': Optional[int],
	'dimval_SUM_LTE': Optional[int],
	'solveInProgress_AVERAGE_EQUAL': Optional[float],
	'solveInProgress_MIN_EQUAL': Optional[int],
	'solveInProgress_MAX_EQUAL': Optional[int],
	'solveInProgress_SUM_EQUAL': Optional[int],
	'solveInProgress_AVERAGE_GT': Optional[float],
	'solveInProgress_MIN_GT': Optional[int],
	'solveInProgress_MAX_GT': Optional[int],
	'solveInProgress_SUM_GT': Optional[int],
	'solveInProgress_AVERAGE_GTE': Optional[float],
	'solveInProgress_MIN_GTE': Optional[int],
	'solveInProgress_MAX_GTE': Optional[int],
	'solveInProgress_SUM_GTE': Optional[int],
	'solveInProgress_AVERAGE_LT': Optional[float],
	'solveInProgress_MIN_LT': Optional[int],
	'solveInProgress_MAX_LT': Optional[int],
	'solveInProgress_SUM_LT': Optional[int],
	'solveInProgress_AVERAGE_LTE': Optional[float],
	'solveInProgress_MIN_LTE': Optional[int],
	'solveInProgress_MAX_LTE': Optional[int],
	'solveInProgress_SUM_LTE': Optional[int],
	'solvedCount_AVERAGE_EQUAL': Optional[float],
	'solvedCount_MIN_EQUAL': Optional[int],
	'solvedCount_MAX_EQUAL': Optional[int],
	'solvedCount_SUM_EQUAL': Optional[int],
	'solvedCount_AVERAGE_GT': Optional[float],
	'solvedCount_MIN_GT': Optional[int],
	'solvedCount_MAX_GT': Optional[int],
	'solvedCount_SUM_GT': Optional[int],
	'solvedCount_AVERAGE_GTE': Optional[float],
	'solvedCount_MIN_GTE': Optional[int],
	'solvedCount_MAX_GTE': Optional[int],
	'solvedCount_SUM_GTE': Optional[int],
	'solvedCount_AVERAGE_LT': Optional[float],
	'solvedCount_MIN_LT': Optional[int],
	'solvedCount_MAX_LT': Optional[int],
	'solvedCount_SUM_LT': Optional[int],
	'solvedCount_AVERAGE_LTE': Optional[float],
	'solvedCount_MIN_LTE': Optional[int],
	'solvedCount_MAX_LTE': Optional[int],
	'solvedCount_SUM_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


VariableSolverDataUpdateConnectionInput = TypedDict('VariableSolverDataUpdateConnectionInput', {
	'node': Optional['SolverDataUpdateInput'],
})


VariableSolverDataUpdateFieldInput = TypedDict('VariableSolverDataUpdateFieldInput', {
	'where': Optional['VariableSolverDataConnectionWhere'],
	'update': Optional['VariableSolverDataUpdateConnectionInput'],
	'connect': Optional[List['VariableSolverDataConnectFieldInput']],
	'disconnect': Optional[List['VariableSolverDataDisconnectFieldInput']],
	'create': Optional[List['VariableSolverDataCreateFieldInput']],
	'delete': Optional[List['VariableSolverDataDeleteFieldInput']],
	'connectOrCreate': Optional[List['VariableSolverDataConnectOrCreateFieldInput']],
})


VariableSort = TypedDict('VariableSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'nstime': Optional['SortDirection'],
	'variableType': Optional['SortDirection'],
	'solvable': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'userLabel': Optional['SortDirection'],
	'robotLabel': Optional['SortDirection'],
	'sessionLabel': Optional['SortDirection'],
	'metadata': Optional['SortDirection'],
	'timestamp': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
	'sessionId': Optional['SortDirection'],
	'robotId': Optional['SortDirection'],
	'userId': Optional['SortDirection'],
})


VariableUniqueWhere = TypedDict('VariableUniqueWhere', {
	'id': Optional[str],
})


VariableUpdateInput = TypedDict('VariableUpdateInput', {
	'label': Optional[str],
	'nstime': Optional['BigInt'],
	'variableType': Optional[str],
	'solvable': Optional[int],
	'tags': Optional[List[str]],
	'_version': Optional[str],
	'userLabel': Optional[str],
	'robotLabel': Optional[str],
	'sessionLabel': Optional[str],
	'metadata': Optional['Metadata'],
	'timestamp': Optional['DateTime'],
	'nstime_INCREMENT': Optional['BigInt'],
	'nstime_DECREMENT': Optional['BigInt'],
	'solvable_INCREMENT': Optional[int],
	'solvable_DECREMENT': Optional[int],
	'tags_POP': Optional[int],
	'tags_PUSH': Optional[List[str]],
	'ppes': Optional[List['VariablePpesUpdateFieldInput']],
	'blobEntries': Optional[List['VariableBlobEntriesUpdateFieldInput']],
	'solverData': Optional[List['VariableSolverDataUpdateFieldInput']],
	'factors': Optional[List['VariableFactorsUpdateFieldInput']],
	'session': Optional['VariableSessionUpdateFieldInput'],
})


VariableWhere = TypedDict('VariableWhere', {
	'OR': Optional[List['VariableWhere']],
	'AND': Optional[List['VariableWhere']],
	'NOT': Optional['VariableWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'nstime': Optional['BigInt'],
	'nstime_IN': Optional[List['BigInt']],
	'nstime_LT': Optional['BigInt'],
	'nstime_LTE': Optional['BigInt'],
	'nstime_GT': Optional['BigInt'],
	'nstime_GTE': Optional['BigInt'],
	'variableType': Optional[str],
	'variableType_IN': Optional[List[str]],
	'variableType_MATCHES': Optional[str],
	'variableType_CONTAINS': Optional[str],
	'variableType_STARTS_WITH': Optional[str],
	'variableType_ENDS_WITH': Optional[str],
	'solvable': Optional[int],
	'solvable_IN': Optional[List[int]],
	'solvable_LT': Optional[int],
	'solvable_LTE': Optional[int],
	'solvable_GT': Optional[int],
	'solvable_GTE': Optional[int],
	'tags': Optional[List[str]],
	'tags_INCLUDES': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'userLabel': Optional[str],
	'userLabel_IN': Optional[List[str]],
	'userLabel_MATCHES': Optional[str],
	'userLabel_CONTAINS': Optional[str],
	'userLabel_STARTS_WITH': Optional[str],
	'userLabel_ENDS_WITH': Optional[str],
	'robotLabel': Optional[str],
	'robotLabel_IN': Optional[List[str]],
	'robotLabel_MATCHES': Optional[str],
	'robotLabel_CONTAINS': Optional[str],
	'robotLabel_STARTS_WITH': Optional[str],
	'robotLabel_ENDS_WITH': Optional[str],
	'sessionLabel': Optional[str],
	'sessionLabel_IN': Optional[List[str]],
	'sessionLabel_MATCHES': Optional[str],
	'sessionLabel_CONTAINS': Optional[str],
	'sessionLabel_STARTS_WITH': Optional[str],
	'sessionLabel_ENDS_WITH': Optional[str],
	'timestamp': Optional['DateTime'],
	'timestamp_IN': Optional[List['DateTime']],
	'timestamp_LT': Optional['DateTime'],
	'timestamp_LTE': Optional['DateTime'],
	'timestamp_GT': Optional['DateTime'],
	'timestamp_GTE': Optional['DateTime'],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'metadata': Optional['Metadata'],
	'metadata_IN': Optional[List['Metadata']],
	'ppesAggregate': Optional['VariablePpesAggregateInput'],
	'ppes_ALL': Optional['PPEWhere'],
	'ppes_NONE': Optional['PPEWhere'],
	'ppes_SINGLE': Optional['PPEWhere'],
	'ppes_SOME': Optional['PPEWhere'],
	'blobEntriesAggregate': Optional['VariableBlobEntriesAggregateInput'],
	'blobEntries_ALL': Optional['BlobEntryWhere'],
	'blobEntries_NONE': Optional['BlobEntryWhere'],
	'blobEntries_SINGLE': Optional['BlobEntryWhere'],
	'blobEntries_SOME': Optional['BlobEntryWhere'],
	'solverDataAggregate': Optional['VariableSolverDataAggregateInput'],
	'solverData_ALL': Optional['SolverDataWhere'],
	'solverData_NONE': Optional['SolverDataWhere'],
	'solverData_SINGLE': Optional['SolverDataWhere'],
	'solverData_SOME': Optional['SolverDataWhere'],
	'factorsAggregate': Optional['VariableFactorsAggregateInput'],
	'factors_ALL': Optional['FactorWhere'],
	'factors_NONE': Optional['FactorWhere'],
	'factors_SINGLE': Optional['FactorWhere'],
	'factors_SOME': Optional['FactorWhere'],
	'sessionAggregate': Optional['VariableSessionAggregateInput'],
	'ppesConnection_ALL': Optional['VariablePpesConnectionWhere'],
	'ppesConnection_NONE': Optional['VariablePpesConnectionWhere'],
	'ppesConnection_SINGLE': Optional['VariablePpesConnectionWhere'],
	'ppesConnection_SOME': Optional['VariablePpesConnectionWhere'],
	'blobEntriesConnection_ALL': Optional['VariableBlobEntriesConnectionWhere'],
	'blobEntriesConnection_NONE': Optional['VariableBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SINGLE': Optional['VariableBlobEntriesConnectionWhere'],
	'blobEntriesConnection_SOME': Optional['VariableBlobEntriesConnectionWhere'],
	'solverDataConnection_ALL': Optional['VariableSolverDataConnectionWhere'],
	'solverDataConnection_NONE': Optional['VariableSolverDataConnectionWhere'],
	'solverDataConnection_SINGLE': Optional['VariableSolverDataConnectionWhere'],
	'solverDataConnection_SOME': Optional['VariableSolverDataConnectionWhere'],
	'factorsConnection_ALL': Optional['VariableFactorsConnectionWhere'],
	'factorsConnection_NONE': Optional['VariableFactorsConnectionWhere'],
	'factorsConnection_SINGLE': Optional['VariableFactorsConnectionWhere'],
	'factorsConnection_SOME': Optional['VariableFactorsConnectionWhere'],
	'sessionConnection': Optional['VariableSessionConnectionWhere'],
})


VisualizationBlobConnectWhere = TypedDict('VisualizationBlobConnectWhere', {
	'node': 'VisualizationBlobWhere',
})


VisualizationBlobCreateInput = TypedDict('VisualizationBlobCreateInput', {
	'hierarchyId': Optional['UUID'],
	'octreeId': Optional['UUID'],
	'metadataId': Optional['UUID'],
})


VisualizationBlobOptions = TypedDict('VisualizationBlobOptions', {
	'sort': Optional[List['VisualizationBlobSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


VisualizationBlobSort = TypedDict('VisualizationBlobSort', {
	'hierarchyId': Optional['SortDirection'],
	'octreeId': Optional['SortDirection'],
	'metadataId': Optional['SortDirection'],
})


VisualizationBlobUpdateInput = TypedDict('VisualizationBlobUpdateInput', {
	'hierarchyId': Optional['UUID'],
	'octreeId': Optional['UUID'],
	'metadataId': Optional['UUID'],
})


VisualizationBlobWhere = TypedDict('VisualizationBlobWhere', {
	'OR': Optional[List['VisualizationBlobWhere']],
	'AND': Optional[List['VisualizationBlobWhere']],
	'NOT': Optional['VisualizationBlobWhere'],
	'hierarchyId': Optional['UUID'],
	'hierarchyId_IN': Optional[List['UUID']],
	'octreeId': Optional['UUID'],
	'octreeId_IN': Optional[List['UUID']],
	'metadataId': Optional['UUID'],
	'metadataId_IN': Optional[List['UUID']],
})


WorkflowConnectInput = TypedDict('WorkflowConnectInput', {
	'createdBy': Optional['WorkflowCreatedByConnectFieldInput'],
	'map': Optional['WorkflowMapConnectFieldInput'],
})


WorkflowConnectOrCreateInput = TypedDict('WorkflowConnectOrCreateInput', {
	'map': Optional['WorkflowMapConnectOrCreateFieldInput'],
})


WorkflowConnectOrCreateWhere = TypedDict('WorkflowConnectOrCreateWhere', {
	'node': 'WorkflowUniqueWhere',
})


WorkflowConnectWhere = TypedDict('WorkflowConnectWhere', {
	'node': 'WorkflowWhere',
})


WorkflowCreatedByAggregateInput = TypedDict('WorkflowCreatedByAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['WorkflowCreatedByAggregateInput']],
	'OR': Optional[List['WorkflowCreatedByAggregateInput']],
	'NOT': Optional['WorkflowCreatedByAggregateInput'],
	'node': Optional['WorkflowCreatedByNodeAggregationWhereInput'],
})


WorkflowCreatedByConnectFieldInput = TypedDict('WorkflowCreatedByConnectFieldInput', {
	'where': Optional['UserConnectWhere'],
	'connect': Optional['UserConnectInput'],
	'overwrite': bool,
})


WorkflowCreatedByConnectionSort = TypedDict('WorkflowCreatedByConnectionSort', {
	'node': Optional['UserSort'],
})


WorkflowCreatedByConnectionWhere = TypedDict('WorkflowCreatedByConnectionWhere', {
	'AND': Optional[List['WorkflowCreatedByConnectionWhere']],
	'OR': Optional[List['WorkflowCreatedByConnectionWhere']],
	'NOT': Optional['WorkflowCreatedByConnectionWhere'],
	'node': Optional['UserWhere'],
})


WorkflowCreatedByConnectOrCreateFieldInputOnCreate = TypedDict('WorkflowCreatedByConnectOrCreateFieldInputOnCreate', {
	'node': 'UserOnCreateInput',
})


WorkflowCreatedByDisconnectFieldInput = TypedDict('WorkflowCreatedByDisconnectFieldInput', {
	'where': Optional['WorkflowCreatedByConnectionWhere'],
	'disconnect': Optional['UserDisconnectInput'],
})


WorkflowCreatedByFieldInput = TypedDict('WorkflowCreatedByFieldInput', {
	'connect': Optional['WorkflowCreatedByConnectFieldInput'],
})


WorkflowCreatedByNodeAggregationWhereInput = TypedDict('WorkflowCreatedByNodeAggregationWhereInput', {
	'AND': Optional[List['WorkflowCreatedByNodeAggregationWhereInput']],
	'OR': Optional[List['WorkflowCreatedByNodeAggregationWhereInput']],
	'NOT': Optional['WorkflowCreatedByNodeAggregationWhereInput'],
	'sub_AVERAGE_LENGTH_EQUAL': Optional[float],
	'sub_LONGEST_LENGTH_EQUAL': Optional[int],
	'sub_SHORTEST_LENGTH_EQUAL': Optional[int],
	'sub_AVERAGE_LENGTH_GT': Optional[float],
	'sub_LONGEST_LENGTH_GT': Optional[int],
	'sub_SHORTEST_LENGTH_GT': Optional[int],
	'sub_AVERAGE_LENGTH_GTE': Optional[float],
	'sub_LONGEST_LENGTH_GTE': Optional[int],
	'sub_SHORTEST_LENGTH_GTE': Optional[int],
	'sub_AVERAGE_LENGTH_LT': Optional[float],
	'sub_LONGEST_LENGTH_LT': Optional[int],
	'sub_SHORTEST_LENGTH_LT': Optional[int],
	'sub_AVERAGE_LENGTH_LTE': Optional[float],
	'sub_LONGEST_LENGTH_LTE': Optional[int],
	'sub_SHORTEST_LENGTH_LTE': Optional[int],
	'givenName_AVERAGE_LENGTH_EQUAL': Optional[float],
	'givenName_LONGEST_LENGTH_EQUAL': Optional[int],
	'givenName_SHORTEST_LENGTH_EQUAL': Optional[int],
	'givenName_AVERAGE_LENGTH_GT': Optional[float],
	'givenName_LONGEST_LENGTH_GT': Optional[int],
	'givenName_SHORTEST_LENGTH_GT': Optional[int],
	'givenName_AVERAGE_LENGTH_GTE': Optional[float],
	'givenName_LONGEST_LENGTH_GTE': Optional[int],
	'givenName_SHORTEST_LENGTH_GTE': Optional[int],
	'givenName_AVERAGE_LENGTH_LT': Optional[float],
	'givenName_LONGEST_LENGTH_LT': Optional[int],
	'givenName_SHORTEST_LENGTH_LT': Optional[int],
	'givenName_AVERAGE_LENGTH_LTE': Optional[float],
	'givenName_LONGEST_LENGTH_LTE': Optional[int],
	'givenName_SHORTEST_LENGTH_LTE': Optional[int],
	'familyName_AVERAGE_LENGTH_EQUAL': Optional[float],
	'familyName_LONGEST_LENGTH_EQUAL': Optional[int],
	'familyName_SHORTEST_LENGTH_EQUAL': Optional[int],
	'familyName_AVERAGE_LENGTH_GT': Optional[float],
	'familyName_LONGEST_LENGTH_GT': Optional[int],
	'familyName_SHORTEST_LENGTH_GT': Optional[int],
	'familyName_AVERAGE_LENGTH_GTE': Optional[float],
	'familyName_LONGEST_LENGTH_GTE': Optional[int],
	'familyName_SHORTEST_LENGTH_GTE': Optional[int],
	'familyName_AVERAGE_LENGTH_LT': Optional[float],
	'familyName_LONGEST_LENGTH_LT': Optional[int],
	'familyName_SHORTEST_LENGTH_LT': Optional[int],
	'familyName_AVERAGE_LENGTH_LTE': Optional[float],
	'familyName_LONGEST_LENGTH_LTE': Optional[int],
	'familyName_SHORTEST_LENGTH_LTE': Optional[int],
	'status_AVERAGE_LENGTH_EQUAL': Optional[float],
	'status_LONGEST_LENGTH_EQUAL': Optional[int],
	'status_SHORTEST_LENGTH_EQUAL': Optional[int],
	'status_AVERAGE_LENGTH_GT': Optional[float],
	'status_LONGEST_LENGTH_GT': Optional[int],
	'status_SHORTEST_LENGTH_GT': Optional[int],
	'status_AVERAGE_LENGTH_GTE': Optional[float],
	'status_LONGEST_LENGTH_GTE': Optional[int],
	'status_SHORTEST_LENGTH_GTE': Optional[int],
	'status_AVERAGE_LENGTH_LT': Optional[float],
	'status_LONGEST_LENGTH_LT': Optional[int],
	'status_SHORTEST_LENGTH_LT': Optional[int],
	'status_AVERAGE_LENGTH_LTE': Optional[float],
	'status_LONGEST_LENGTH_LTE': Optional[int],
	'status_SHORTEST_LENGTH_LTE': Optional[int],
	'_version_AVERAGE_LENGTH_EQUAL': Optional[float],
	'_version_LONGEST_LENGTH_EQUAL': Optional[int],
	'_version_SHORTEST_LENGTH_EQUAL': Optional[int],
	'_version_AVERAGE_LENGTH_GT': Optional[float],
	'_version_LONGEST_LENGTH_GT': Optional[int],
	'_version_SHORTEST_LENGTH_GT': Optional[int],
	'_version_AVERAGE_LENGTH_GTE': Optional[float],
	'_version_LONGEST_LENGTH_GTE': Optional[int],
	'_version_SHORTEST_LENGTH_GTE': Optional[int],
	'_version_AVERAGE_LENGTH_LT': Optional[float],
	'_version_LONGEST_LENGTH_LT': Optional[int],
	'_version_SHORTEST_LENGTH_LT': Optional[int],
	'_version_AVERAGE_LENGTH_LTE': Optional[float],
	'_version_LONGEST_LENGTH_LTE': Optional[int],
	'_version_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastAuthenticatedTimestamp_MAX_LTE': Optional['DateTime'],
})


WorkflowCreateInput = TypedDict('WorkflowCreateInput', {
	'label': str,
	'description': Optional[str],
	'status': str,
	'_type': str,
	'_version': str,
	'data': Optional['B64JSON'],
	'result': Optional['B64JSON'],
	'createdBy': Optional['WorkflowCreatedByFieldInput'],
	'map': Optional['WorkflowMapFieldInput'],
})


WorkflowDeleteInput = TypedDict('WorkflowDeleteInput', {
	'map': Optional['WorkflowMapDeleteFieldInput'],
})


WorkflowDisconnectInput = TypedDict('WorkflowDisconnectInput', {
	'createdBy': Optional['WorkflowCreatedByDisconnectFieldInput'],
	'map': Optional['WorkflowMapDisconnectFieldInput'],
})


WorkflowMapAggregateInput = TypedDict('WorkflowMapAggregateInput', {
	'count': Optional[int],
	'count_LT': Optional[int],
	'count_LTE': Optional[int],
	'count_GT': Optional[int],
	'count_GTE': Optional[int],
	'AND': Optional[List['WorkflowMapAggregateInput']],
	'OR': Optional[List['WorkflowMapAggregateInput']],
	'NOT': Optional['WorkflowMapAggregateInput'],
	'node': Optional['WorkflowMapNodeAggregationWhereInput'],
})


WorkflowMapConnectFieldInput = TypedDict('WorkflowMapConnectFieldInput', {
	'where': Optional['MapConnectWhere'],
	'connect': Optional['MapConnectInput'],
	'overwrite': bool,
})


WorkflowMapConnectionSort = TypedDict('WorkflowMapConnectionSort', {
	'node': Optional['MapSort'],
})


WorkflowMapConnectionWhere = TypedDict('WorkflowMapConnectionWhere', {
	'AND': Optional[List['WorkflowMapConnectionWhere']],
	'OR': Optional[List['WorkflowMapConnectionWhere']],
	'NOT': Optional['WorkflowMapConnectionWhere'],
	'node': Optional['MapWhere'],
})


WorkflowMapConnectOrCreateFieldInput = TypedDict('WorkflowMapConnectOrCreateFieldInput', {
	'where': 'MapConnectOrCreateWhere',
	'onCreate': 'WorkflowMapConnectOrCreateFieldInputOnCreate',
})


WorkflowMapConnectOrCreateFieldInputOnCreate = TypedDict('WorkflowMapConnectOrCreateFieldInputOnCreate', {
	'node': 'MapOnCreateInput',
})


WorkflowMapCreateFieldInput = TypedDict('WorkflowMapCreateFieldInput', {
	'node': 'MapCreateInput',
})


WorkflowMapDeleteFieldInput = TypedDict('WorkflowMapDeleteFieldInput', {
	'where': Optional['WorkflowMapConnectionWhere'],
	'delete': Optional['MapDeleteInput'],
})


WorkflowMapDisconnectFieldInput = TypedDict('WorkflowMapDisconnectFieldInput', {
	'where': Optional['WorkflowMapConnectionWhere'],
	'disconnect': Optional['MapDisconnectInput'],
})


WorkflowMapFieldInput = TypedDict('WorkflowMapFieldInput', {
	'create': Optional['WorkflowMapCreateFieldInput'],
	'connect': Optional['WorkflowMapConnectFieldInput'],
	'connectOrCreate': Optional['WorkflowMapConnectOrCreateFieldInput'],
})


WorkflowMapNodeAggregationWhereInput = TypedDict('WorkflowMapNodeAggregationWhereInput', {
	'AND': Optional[List['WorkflowMapNodeAggregationWhereInput']],
	'OR': Optional[List['WorkflowMapNodeAggregationWhereInput']],
	'NOT': Optional['WorkflowMapNodeAggregationWhereInput'],
	'label_AVERAGE_LENGTH_EQUAL': Optional[float],
	'label_LONGEST_LENGTH_EQUAL': Optional[int],
	'label_SHORTEST_LENGTH_EQUAL': Optional[int],
	'label_AVERAGE_LENGTH_GT': Optional[float],
	'label_LONGEST_LENGTH_GT': Optional[int],
	'label_SHORTEST_LENGTH_GT': Optional[int],
	'label_AVERAGE_LENGTH_GTE': Optional[float],
	'label_LONGEST_LENGTH_GTE': Optional[int],
	'label_SHORTEST_LENGTH_GTE': Optional[int],
	'label_AVERAGE_LENGTH_LT': Optional[float],
	'label_LONGEST_LENGTH_LT': Optional[int],
	'label_SHORTEST_LENGTH_LT': Optional[int],
	'label_AVERAGE_LENGTH_LTE': Optional[float],
	'label_LONGEST_LENGTH_LTE': Optional[int],
	'label_SHORTEST_LENGTH_LTE': Optional[int],
	'description_AVERAGE_LENGTH_EQUAL': Optional[float],
	'description_LONGEST_LENGTH_EQUAL': Optional[int],
	'description_SHORTEST_LENGTH_EQUAL': Optional[int],
	'description_AVERAGE_LENGTH_GT': Optional[float],
	'description_LONGEST_LENGTH_GT': Optional[int],
	'description_SHORTEST_LENGTH_GT': Optional[int],
	'description_AVERAGE_LENGTH_GTE': Optional[float],
	'description_LONGEST_LENGTH_GTE': Optional[int],
	'description_SHORTEST_LENGTH_GTE': Optional[int],
	'description_AVERAGE_LENGTH_LT': Optional[float],
	'description_LONGEST_LENGTH_LT': Optional[int],
	'description_SHORTEST_LENGTH_LT': Optional[int],
	'description_AVERAGE_LENGTH_LTE': Optional[float],
	'description_LONGEST_LENGTH_LTE': Optional[int],
	'description_SHORTEST_LENGTH_LTE': Optional[int],
	'status_AVERAGE_LENGTH_EQUAL': Optional[float],
	'status_LONGEST_LENGTH_EQUAL': Optional[int],
	'status_SHORTEST_LENGTH_EQUAL': Optional[int],
	'status_AVERAGE_LENGTH_GT': Optional[float],
	'status_LONGEST_LENGTH_GT': Optional[int],
	'status_SHORTEST_LENGTH_GT': Optional[int],
	'status_AVERAGE_LENGTH_GTE': Optional[float],
	'status_LONGEST_LENGTH_GTE': Optional[int],
	'status_SHORTEST_LENGTH_GTE': Optional[int],
	'status_AVERAGE_LENGTH_LT': Optional[float],
	'status_LONGEST_LENGTH_LT': Optional[int],
	'status_SHORTEST_LENGTH_LT': Optional[int],
	'status_AVERAGE_LENGTH_LTE': Optional[float],
	'status_LONGEST_LENGTH_LTE': Optional[int],
	'status_SHORTEST_LENGTH_LTE': Optional[int],
	'createdTimestamp_MIN_EQUAL': Optional['DateTime'],
	'createdTimestamp_MAX_EQUAL': Optional['DateTime'],
	'createdTimestamp_MIN_GT': Optional['DateTime'],
	'createdTimestamp_MAX_GT': Optional['DateTime'],
	'createdTimestamp_MIN_GTE': Optional['DateTime'],
	'createdTimestamp_MAX_GTE': Optional['DateTime'],
	'createdTimestamp_MIN_LT': Optional['DateTime'],
	'createdTimestamp_MAX_LT': Optional['DateTime'],
	'createdTimestamp_MIN_LTE': Optional['DateTime'],
	'createdTimestamp_MAX_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_EQUAL': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_MIN_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_MAX_LTE': Optional['DateTime'],
})


WorkflowMapUpdateConnectionInput = TypedDict('WorkflowMapUpdateConnectionInput', {
	'node': Optional['MapUpdateInput'],
})


WorkflowMapUpdateFieldInput = TypedDict('WorkflowMapUpdateFieldInput', {
	'where': Optional['WorkflowMapConnectionWhere'],
	'update': Optional['WorkflowMapUpdateConnectionInput'],
	'connect': Optional['WorkflowMapConnectFieldInput'],
	'disconnect': Optional['WorkflowMapDisconnectFieldInput'],
	'create': Optional['WorkflowMapCreateFieldInput'],
	'delete': Optional['WorkflowMapDeleteFieldInput'],
	'connectOrCreate': Optional['WorkflowMapConnectOrCreateFieldInput'],
})


WorkflowOnCreateInput = TypedDict('WorkflowOnCreateInput', {
	'label': str,
	'description': Optional[str],
	'status': str,
	'_type': str,
	'_version': str,
	'data': Optional['B64JSON'],
	'result': Optional['B64JSON'],
})


WorkflowOptions = TypedDict('WorkflowOptions', {
	'sort': Optional[List['WorkflowSort']],
	'limit': Optional[int],
	'offset': Optional[int],
})


WorkflowRelationInput = TypedDict('WorkflowRelationInput', {
	'map': Optional['WorkflowMapCreateFieldInput'],
})


WorkflowSort = TypedDict('WorkflowSort', {
	'id': Optional['SortDirection'],
	'label': Optional['SortDirection'],
	'description': Optional['SortDirection'],
	'status': Optional['SortDirection'],
	'_type': Optional['SortDirection'],
	'_version': Optional['SortDirection'],
	'data': Optional['SortDirection'],
	'result': Optional['SortDirection'],
	'createdTimestamp': Optional['SortDirection'],
	'lastUpdatedTimestamp': Optional['SortDirection'],
})


WorkflowUniqueWhere = TypedDict('WorkflowUniqueWhere', {
	'id': Optional[str],
})


WorkflowUpdateInput = TypedDict('WorkflowUpdateInput', {
	'label': Optional[str],
	'description': Optional[str],
	'status': Optional[str],
	'_type': Optional[str],
	'_version': Optional[str],
	'data': Optional['B64JSON'],
	'result': Optional['B64JSON'],
	'map': Optional['WorkflowMapUpdateFieldInput'],
})


WorkflowWhere = TypedDict('WorkflowWhere', {
	'OR': Optional[List['WorkflowWhere']],
	'AND': Optional[List['WorkflowWhere']],
	'NOT': Optional['WorkflowWhere'],
	'id': Optional[str],
	'id_IN': Optional[List[str]],
	'id_MATCHES': Optional[str],
	'id_CONTAINS': Optional[str],
	'id_STARTS_WITH': Optional[str],
	'id_ENDS_WITH': Optional[str],
	'label': Optional[str],
	'label_IN': Optional[List[str]],
	'label_MATCHES': Optional[str],
	'label_CONTAINS': Optional[str],
	'label_STARTS_WITH': Optional[str],
	'label_ENDS_WITH': Optional[str],
	'description': Optional[str],
	'description_IN': Optional[List[str]],
	'description_MATCHES': Optional[str],
	'description_CONTAINS': Optional[str],
	'description_STARTS_WITH': Optional[str],
	'description_ENDS_WITH': Optional[str],
	'status': Optional[str],
	'status_IN': Optional[List[str]],
	'status_MATCHES': Optional[str],
	'status_CONTAINS': Optional[str],
	'status_STARTS_WITH': Optional[str],
	'status_ENDS_WITH': Optional[str],
	'_type': Optional[str],
	'_type_IN': Optional[List[str]],
	'_type_MATCHES': Optional[str],
	'_type_CONTAINS': Optional[str],
	'_type_STARTS_WITH': Optional[str],
	'_type_ENDS_WITH': Optional[str],
	'_version': Optional[str],
	'_version_IN': Optional[List[str]],
	'_version_MATCHES': Optional[str],
	'_version_CONTAINS': Optional[str],
	'_version_STARTS_WITH': Optional[str],
	'_version_ENDS_WITH': Optional[str],
	'createdTimestamp': Optional['DateTime'],
	'createdTimestamp_IN': Optional[List['DateTime']],
	'createdTimestamp_LT': Optional['DateTime'],
	'createdTimestamp_LTE': Optional['DateTime'],
	'createdTimestamp_GT': Optional['DateTime'],
	'createdTimestamp_GTE': Optional['DateTime'],
	'lastUpdatedTimestamp': Optional['DateTime'],
	'lastUpdatedTimestamp_IN': Optional[List['DateTime']],
	'lastUpdatedTimestamp_LT': Optional['DateTime'],
	'lastUpdatedTimestamp_LTE': Optional['DateTime'],
	'lastUpdatedTimestamp_GT': Optional['DateTime'],
	'lastUpdatedTimestamp_GTE': Optional['DateTime'],
	'data': Optional['B64JSON'],
	'data_IN': Optional[List['B64JSON']],
	'result': Optional['B64JSON'],
	'result_IN': Optional[List['B64JSON']],
	'createdByAggregate': Optional['WorkflowCreatedByAggregateInput'],
	'mapAggregate': Optional['WorkflowMapAggregateInput'],
	'createdByConnection': Optional['WorkflowCreatedByConnectionWhere'],
	'mapConnection': Optional['WorkflowMapConnectionWhere'],
})


BlobInput = TypedDict('BlobInput', {
	'name': str,
	'size': Optional['BigInt'],
})


CompletedUploadPartInput = TypedDict('CompletedUploadPartInput', {
	'partNumber': int,
	'eTag': Optional[str],
})


CompletedUploadInput = TypedDict('CompletedUploadInput', {
	'uploadId': str,
	'parts': List['CompletedUploadPartInput'],
})


BlobQueryFilter = TypedDict('BlobQueryFilter', {
	'name_CONTAINS': Optional[str],
})


