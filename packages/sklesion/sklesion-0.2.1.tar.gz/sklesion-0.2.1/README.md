# SkinLesionClassifier - A Keras Model for Diagnosing Skin Lesions

>[***NOTE:*** Python 3.11 was used in this project.]

## Publish package to [PyPI](https://pypi.org/) (so that anyone may install it using `pip`)

> [***NOTE:*** The steps below assume that a PyPI account and an API Token had already
> been created and configured (the configuration file corresponds to `~/.pypirc`). Be
> sure to update the package version in the argument `version` at file `setup.py`.]

In the folder where this very file is found, create a virtual environment, activate it,
and install the required packages ([`twine`](https://pypi.org/project/twine/) and [`wheel`](https://pypi.org/project/wheel/)). You may
use `venv` for this: 

```powershell
Remove-Item  -Recurse -Force ".venv"
python -m venv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```

Create distribution files:

```powershell
Remove-Item -Recurse -Force "dist"
python setup.py sdist bdist_wheel
```

These will then be found in the `dist/` directory.

Upload package to PyPI using [`twine`](https://pypi.org/project/twine/):

```powershell
twine upload dist/*
```

The now public project may be accessed through the URL https://pypi.org/project/sklesion/ .


The package may then be installed by anyone through the command

```powershell
pip install sklesion
```
