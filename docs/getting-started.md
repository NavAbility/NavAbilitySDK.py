# Getting Started

NavAbility fundamentally organizes mapping, localization, and perception data (a.k.a. navigation data) by means of a visual graphical model known as factor graphs.  See the related documentation on [Graph Concepts](https://juliarobotics.org/Caesar.jl/latest/concepts/concepts/) for more information about what factor graphs.

## Free `guest@navability.io` access

A free tier access to NavAbility servers is provided through the user `guest@navability.io`.  To learn more about using the guest user, consider trying the [NavAbility Tutorials](./nvatutorials).

## Privacy and Auth Token

A user specific authentication token is needed whether you are just accessing an existing graph, modifying, adding data, or building a whole new graph directly through the SDK.  At present, the only way to obtain a temporary authentication token is through the [NavAbility App on the "Connect" page][nva-app-auth] (or from the App, use the burger menu top left to access the Connect page).  A user login to NavAbility is needed before an auth token can be provided.  Auth tokens last for 24 hours, and should be kept private to each session or usage.  Do not store or share the token with others.  See below for getting a login if you do not already have one.

## NavAbility App Login

You can login via the [NavAbility App](https://app.navability.io/get-started/introduction/) by clicking on the account menu top right.  Reach out if you have any questions via Slack [![](https://img.shields.io/badge/Invite-Slack-green.svg?style=popout)][slack-invite], emailing us at <info@navability.io>, or [filing specific issues against the SDK][sdk-py].

<a href="https://app.navability.io/edge/connect"><p align="center">
<img src="https://user-images.githubusercontent.com/6412556/218193635-2325bbd1-f82c-4391-8959-8f54b2acdc0a.png" width="240px" border="0" />
</p></a>

## Installing

The NavAbilitySDK can be installed as a usual Python pip package to a virtual environment ([more info venv and pip info here][py-venv-pip]):

```
cd ~/my/working/dir
python3 -m venv venv
source venv/bin/activate
```

and install the package to current active environment (or tosystem global if not in an venv)
```
pip install navabilitysdk
```

Installing from within a Python kernel can also be done using:
```python
# Install a pip package inside a Jupyter kernel
# import sys
# !{sys.executable} -m pip install navabilitysdk
```


# Starting a Python REPL and Importing

To use the NavAbility SDK example in a REPL, together with a [virtual environment][py-venv]
```python
python3 venv /path/to/user/venv
```

Loading the SDK module:
```python
from navability.entities import *
from navability.services import *
from uuid import uuid4
import numpy as np
# import asyncio
```

:::{seealso}
The NavAbility and [Caesar.jl][cjl-docs] design promote distributed factor graph workflows for both edge and cloud usage.  The NavAbilitySDK is part of a larger architecture where both client and server side computations are used.  The rest of this page illustrates usage against the server side data and computations.  Reach out to NavAbility via Slack [![](https://img.shields.io/badge/Invite-Slack-green.svg?style=popout)][slack-invite] or <info@navability.io> for more help.
:::

:::{warning}
Earlier versions of NavAbilitySDK.py had to be started with  `python -m asyncio`, otherwise you'd see `SyntaxError: 'await' outside function`:
```python
# earlier versions of sdk had to be started with asyncio
python3 -m asyncio venv /path/to/user/venv
```
:::


[sdk-py]: https://github.com/NavAbility/NavAbilitySDK.py/issues
[cjl-docs]: https://juliarobotics.org/Caesar.jl/latest/
[slack-invite]: https://join.slack.com/t/caesarjl/shared_invite/zt-ucs06bwg-y2tEbddwX1vR18MASnOLsw
[nva-app-auth]: https://app.navability.io/edge/connect
[py-venv]: https://docs.python.org/dev/library/venv.html
[py-venv-pip]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
