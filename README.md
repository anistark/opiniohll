# Opinio Delivery Python SDK


![version](https://img.shields.io/github/tag/anistark/opiniohll.svg) ![license](https://img.shields.io/github/license/anistark/opiniohll.svg) ![python_versions](https://img.shields.io/pypi/pyversions/opiniohll.svg) [![pypi](https://img.shields.io/pypi/v/opiniohll.svg)](https://pypi.python.org/pypi/opiniohll)


## Installation Instruction

```
pip install opiniohll
```

## Usage

#### Import Package

```
from OpinioDelivery import OpinioDelivery
```

#### Initialise

```
OpinioDelivery(ACCESS_KEY, SECRET_KEY, sandbox=True, debug=True)
```

ACCESS__KEY and SECRET_KEY can be found from Opinio partner model.
sandbox and debug are optional fields.
By default, production is accessed.

Example :

```
OpinioDelivery(ACCESS_KEY, SECRET_KEY)
```


Rest Api are in [documentation](http://deliver.opinioapp.com/api/docs)

### [Wiki](https://github.com/anistark/opiniohll/wiki)

