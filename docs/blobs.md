## Data `BlobEntry=>Blob`

Additional (large) data attached to variables exist in a few different ways.  The primary method for storing additional large data blobs with a variable, is to look at the `BlobEntry`s associated with a particular variable.  For example:
```python
de = listBlobEntries(client, context, "x0") |> fetch
de .|> s->s["blobLabel"]
# e.g. ["Camera0", "user_calibration", etc.]
```

Data blobs can be fetched via, e.g. using the unique `blobId` of the first `dataEntry` on this variable:
```python
blob = getBlob(client, context, de[1]["blobId"]; checkhash=false)
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

<!-- ```@docs
listBlobEntries
getBlob
``` -->