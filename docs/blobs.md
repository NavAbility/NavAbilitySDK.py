# Data `BlobEntry=>Blob`

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
# [0x2e, 0x45, ..., 0x2b] # length 1225 bytes
```

Data blobs are provided in binary format (i.e. `::Vector{UInt8}`).  A blob can be associated via any number of `BlobEntry`s across multiple graph nodes, sessions, or robots.  `BlobEntry` also stores a hash value to ensure data consistency which must correspond to teh stored hash upon retrieval.  The check can be skipped as indicated by the option in the function call above.

See [Tutorial 5 from ICRA 2022 for a more indepth example of working with data blobs](https://app.navability.io/get-started/tutorials/icra-5-marineexample).


:::{tip}
A blob is owned by a `user` and only accessible by other users if allowed via approved roles or permissions.
:::

:::{tip}
All `blobId`s are unique across the entire distributed system and are immutable.
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
  # createdTimestamp: datetime
  # size: int
}
```


<!-- ```@docs
listBlobEntries
getBlob
``` -->