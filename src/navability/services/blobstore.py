import logging
import warnings
import requests
from typing import List

from gql import gql

# from navability.common.queries import (
#     GQL_LISTDATAENTRIES,
# )
# from navability.common.mutations import (
#     GQL_CREATEDOWNLOAD,
#     GQL_CREATEUPLOAD,
#     GQL_COMPLETEUPLOAD_SINGLE,
#     GQL_ADDBLOBENTRY,
# )

from navability.services.loader import GQL_OPERATIONS

from navability.entities.navabilityclient import QueryOptions

from navability.entities.client import Client
from navability.entities.navabilityclient import (
    MutationOptions,
    NavAbilityClient,
    QueryOptions,
)
# from navability.entities.querydetail import QueryDetail
from navability.entities.blob.blobentry import (
    BlobEntry,
    BlobEntrySchema,
)


logger = logging.getLogger(__name__)


## ==================================
## download upload blobs
## ==================================


async def createDownload(
    client: NavAbilityClient,
    userLabel: str,
    blobId: str,
):
    """ Request URLs for data blob download.

    Args:
    client (NavAbilityClient): The NavAbility client for handling requests.
    userId (String): The userId with access to the data.
    blobId (String): The unique blob identifier of the data.
    """
    params = {
        "userLabel": userLabel,
        "blobId": blobId,
    }
    logger.debug(f"Query params: {params}")
    res = await client.mutate(
        MutationOptions(
            GQL_OPERATIONS["MUTATION_CREATEDOWNLOAD"].data,
            params,
        )
    )

    # TODO error checking
    if not 'createDownload' in res:
        raise ValueError('Cannot create download for ', userLabel, " seeking ", blobId)
    return res['createDownload']



async def createUpload(
    client: NavAbilityClient,
    blobLabel: str,
    blobSize: int,
    parts: int = 1,
):
    """ Request URLs for data blob upload.

    Args:
        client (NavAbilityClient): The NavAbility client.
        blobLabel (String): human readable blob label (aka filename).
        filesize (Int): total number of bytes to upload. 
        parts (Int): Split upload into multiple blob parts, 
        FIXME currently only supports parts=1.

    Returns:
        str: The dedicated upload URL
    """
    params = {
        "blobLabel": blobLabel,
        "blobSize": blobSize,
        "parts": parts
    }
    logger.debug(f"Query params: {params}")
    res = await client.mutate(
        MutationOptions(
            gql(GQL_CREATEUPLOAD),
            params,
        )
    )
    # TODO error handling
    return res['createUpload']


async def getBlob(
    client: NavAbilityClient,
    user: str,
    blobId: str,
):
    """ If the user has access, retrieve the identified blob of bytes.

    Args:
        client (NavAbilityClient): The NavAbility client for handling requests.
        userId (String): The userId with access to the data.
        blobId (String): The unique blob identifier of the data.

    Returns:
        data: coroutine with data blob content
    """
    url = await createDownload(client, user, blobId)
    resp = requests.get(url)
    return resp.content


async def completeUploadSingle(
    client: NavAbilityClient,
    blobId: str,
    uploadId: str,
    eTag: str,
):
    #
    params = {
        "blobId": blobId,
        "uploadId": uploadId,
        "eTag": eTag
    }
    logger.debug(f"Query params: {params}")
    res = await client.mutate(
        MutationOptions(
            gql(GQL_COMPLETEUPLOAD_SINGLE),
            params,
        )
    )
    # TODO error handling
    return res['completeUpload']


async def addBlob(
    client: Client,
    blobLabel: str,
    blob
):
    """Push a data blob to user and get a unique identifier back.

    Args:
        client (NavAbilityClient): The NavAbility client for handling requests.
        blobLabel (str): Human readable label for the blob (aka filename).
        blob (bytes): Actual data blob as a chunk of data.

    Returns:
        blobId (String): The unique blob identifier of the data.
    """
    blobSize = len(blob)
    upd = await createUpload(client, blobLabel, blobSize)
    url = upd['parts'][0]['url']
    uploadId = upd['uploadId']
    blobId = upd['file']['id']
    
    headers = {
        'Content-Length': str(blobSize),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        'Connection': 'keep-alive'
    }

    # do the upload
    r = requests.put(url, data=blob, headers=headers)
    
    # Extract eTag
    eTag = r.headers['eTag']

    # close out the upload
    res = await completeUploadSingle(client, blobId, uploadId, eTag)

    return blobId
