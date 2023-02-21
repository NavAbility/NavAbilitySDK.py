# Data `BlobEntry=>Blob`

## Getting BlobEntries

Additional (large) data attached to variables exist in a few different ways.  The primary method for storing additional large data blobs with a variable, is to look at the `BlobEntry`s associated with a particular variable.  For example:
```python
entries = await listBlobEntries(client, context, "x0") |> fetch
# human friendly labels
print([en.label for en in entries])
# e.g. ['Camera0', 'UserCalib', 'GPS', 'JoystickCmds']

# machine friendly system wide unique identifier
print([en.id for en in entries])
```

:::{tip}
`Blob`s are separate from `BlobEntry`s.  Various nodes on the graph can have any number of `BlobEntry`s (including duplicates), but the user does not necessary have the need to pull the bandwidth heavy blobs across all parts of the system network.
:::

Data blobs can be fetched via, e.g. using the unique `id` (or `blobId`) of from a `BlobEntry`:
```python
blob = await getBlob(client, context, entries[1].id]; checkhash=false)
# b'{"latitude":41.7325,"altitude":2.211,"header":{"stamp":{"secs":1670378554,"nsecs":000624417},"seq":91,"frame_id":"gps","_type":"ROS1/std_msgs/Header"},"status":{"status":0,"service":1},"position_covariance":[0.265225,0.0,0.0,0.0,0.265225,0.0,0.0,0.0,0.556516],"longitude":-49.946944,"_type":"ROS1/sensor_msgs/NavSatFix","position_covariance_type":2}'
```

Data blobs are provided in binary format.  A blob can be associated via any number of `BlobEntry`s across multiple graph nodes, sessions, or robots.  `BlobEntry` also stores a hash value to ensure data consistency which must correspond to the stored hash upon retrieval.  The check can be skipped as indicated by the option in the function call above.


:::{tip}
A blob is owned by a `user` and only accessible by other users if allowed via approved roles or permissions.
:::

:::{tip}
All `blobId`s are unique across the entire distributed system and are immutable.
:::

## Adding BlobEntries

Blobs can be linked to any variable (future node) in the graph.  This is easily done by adding a BlobEntry:
```python
res = await addBlobEntry(client, context, 'x12', entries[1].id, entries[1].label, len(blob), entries[1].mimeType)
```

:::{tip}
More ubiqitous use of `blob` size was recently introduced to `BlobEntry` and will be unified with less user input as part of SDKs v0.6 upgrades.
:::

## BlobEntry Structure

To simplify many different requirements, a `BlobEntry` has the following field structure:
```
{
  id: UUID
  label: string
  description: string
  blobstore: string
  hash: string
  mimeType: string
  origin: string

  ## planned future fields
  # blobId: UUID
  # originId: UUID
  # createdTimestamp: datetime
  # size: int
  # metadata: string
}
```

See [Tutorial 5 from ICRA 2022 for a more indepth example of working with data blobs](https://app.navability.io/get-started/tutorials/icra-5-marineexample).


<!-- ```@docs
listBlobEntries
getBlob
``` -->