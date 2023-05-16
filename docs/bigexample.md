# Full Example

## SDK.py v0.6 Example

```python
from navability.entities import *
from navability.services import *
from uuid import uuid4
import numpy as np
# import asyncio


userLabel = "guest@navability.io"
robotLabel = "TestRobot"
sessionLabel = "TestHex"

# for private (non-guest) use, get a token after login at app.navability.io, Connect page.
auth_token = ''

fgclient = DFGClient(userLabel, robotLabel, sessionLabel, auth_token=auth_token)

variables = listVariables(fgclient)
# variables = await listVariablesAsync(fgclient)

# get one of the variables from the graph
x1 = getVariable(fgclient, 'x1')
# xl1 = await getVariableAsync(fgclient, 'x1')
print('The tags on this variable are', x1.tags)

# which blob entries (list of labels) are there on this variable
be_labels = listBlobEntries(fgclient, "x1")
# be_labels = await listBlobEntriesAsync(fgclient, "x1")

# fetch fetch one of the blob entries (note not the blob itself yet)
entry = getBlobEntry(fgclient, "x1", be_labels[0])

## fetch binary data blob from one of the blobstores
store = NavAbilityBlobStore(fgclient.client, userLabel)
blob = getBlob(store, str(entry.blobId))
# blob = await getBlobAsync(store, entry.id)

## which neighbors does this variable have
x1_nei = listNeighbors(fgclient, 'x1')

## which factors are there
fcts = listFactors(fgclient)

## get a specific factor
fc = getFactor(fgclient, 'x1x2f1')
```
