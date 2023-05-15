# Data `BlobEntry=>Blob`

Many `BlobEntry`s from various location can all reference the same large and heavy binary data `Blob`.  Furthermore, this system allows a distributed usage over a large networked system.

:::{tip}
`Blob`s are separate from `BlobEntry`s.  Various nodes on the graph can have any number of `BlobEntry`s (including duplicates), but the user does not necessary have the need to pull the bandwidth heavy blobs across all parts of the system network.
:::

## What is a `BlobEntry`

Additional (large) data attached to variables exist in a few different ways.  The primary method for storing additional large data as a `Blob`, however, a blob just "barcoded" binary blob.  we use `BlobEntry`s to organize, find, share, distribute, make available and useful across the divergent network how a `Blob` is associated with the graph.

A blob entry is small about of structed data that holds reference information to find an actual binary blob which is possibly a massive amount of data.

### Listing BlobEntries on a Node

The `list` verb is purposefully limited to just returning a list of labels (i.e. `List[string]`), and therefore the following call only returns the labels of `BlobEntry`s attached a particular node (variable, session, robot, etc.):
```python
ent_labels = listBlobEntries(fgclient, 'x0')
# ent_labels = await listBlobEntriesAsync(fgclient, 'x0')

# human friendly labels
print('Human friendly BlobEntry labels on x0 are', ent_labels)
# e.g. ['LEFTCAM_1002', 'LEFTCAM_1003', 'UserCalib', 'GPS', 'JoystickCmds']
```

```{eval-rst}
.. autofunction:: navability.services.listBlobEntries
.. autofunction:: navability.services.listBlobEntriesAsync
```

### Getting a `BlobEntry`

Using the human friendly label from the `listBlobEntries` above, we can fetch the `BlobEntry`
```python
entry = getBlobEntry(fgclient, 'LEFTCAM_1002')
# entry = await getBlobEntryAsync(fgclient, 'LEFTCAM_1002')
```

The entry object is well structured
```{eval-rst}
.. autoclass:: navability.entities.BlobEntry
```

## Getting the associated `Blob`

A binary `Blob` is basically just a "barcoded" piece of data that can be associated (via individual `BlobEntry`s) multiple times across multiple graph nodes, sessions, or robots.

Data blobs can be fetched via, e.g. using the unique `.blobId` as primary (or `.originId` as secondary) reference.  Also note that the blob itself may also be replicated across any number of blob stores, depending on the application:
```python
blob = getBlob(fgclient, entry.blobId]; checkhash=false) # legacy versions did not use .hash check
# blob = await getBlobAsync(fgclient, entry.blobId]; checkhash=false)
```

The blob contains binary information, for example this `mimeType = application/octet-stream/json; _type=ROS.sensor_msgs.NavSatFix`:
```
b'{"latitude":41.7325,"altitude":2.211,"header":{"stamp":{"secs":1670378554,"nsecs":000624417},"seq":91,"frame_id":"gps","_type":"ROS1/std_msgs/Header"},"status":{"status":0,"service":1},"position_covariance":[0.265225,0.0,0.0,0.0,0.265225,0.0,0.0,0.0,0.556516],"longitude":-49.946944,"_type":"ROS1/sensor_msgs/NavSatFix","position_covariance_type":2}'
```

:::{tip}
Depending on the blob store, it may also be possible to retrieve a blob using the `.originId` rather than `.blobId`.
:::

:::{tip}
A blob is owned by a `user` and only accessible by other users if allowed via approved roles or permissions.
:::

:::{tip}
`BlobEntry.hash` helps ensure data consistency by rehasing the retrieved blob binary data itself.
:::

## Adding BlobEntries

:::{warning}
Adding `Blob` or `BlobEntry`s from the Python SDK are under construction and expected to be part of the v0.6.1 release.  This functionality has already been released with the JuliaLang SDK.
:::

Blobs can be linked to any variable (future node) in the graph.  This is easily done by adding a BlobEntry:
```python
res = addBlobEntry(fgclient, 'x12', entries[1].id, entries[1].label, len(blob), entries[1].mimeType)
# res = await addBlobEntryAsync(fgclient, 'x12', entries[1].id, entries[1].label, len(blob), entries[1].mimeType)
```

## Adding New Blobs

It is also possible to push data blobs:
```python
client = NavAbilityHttpsClient()
blobId = await addBlob(fgclient.client, "testimage.png", imgblob)
```

Remember to add at least one BlobEntry somewhere in your session so that you might find it again in the future, see `addBlobEntry` above.

:::{eval-rst}
.. autofunction:: navability.entities.NavAbilityHttpsClient
:::

:::{seealso}
See [Tutorial 5 from ICRA 2022 for a more in-depth example of working with data blobs](sdkpynb:python/navability-sdk/icra-5-marineexample).
:::
