# Developer Notes

## Developer install:
```
cd NavAbilitySDK.py
pip install -e .
```

## Docs Dependencies

```
pip install -r docs/requirements.txt
```

Docs can easily be built locally and/or viewed using the Makefile
```
make docs
make docs_firefox
```

The latter also builds the docs.

## Release to PyPi

Have login credentials and push access to pypi.org.

Run
```
make release
```

Do manual release tag on Github.com/NavAbility/NavAbilitySDK.py.