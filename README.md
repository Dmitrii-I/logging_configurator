# logging_configurator
[![Tests status badge](https://github.com/Dmitrii-I/logging_configurator/workflows/tests/badge.svg?branch=master)](https://github.com/Dmitrii-I/logging_configurator/actions?query=workflow%3Atests)
[![PyPI version](https://badge.fury.io/py/logging-configurator.svg)](https://badge.fury.io/py/logging-configurator)

Configure logging with one line (not counting the import).

## Installation

```
pip install logging_configurator
```

## Examples

### Log using defaults: INFO to stdout/stderr

```
from logging_configurator import configure_logging
configure_logging()
```

### Log to a file and to stdout/stderr

```
from logging_configurator import configure_logging
configure_logging(path="foo.log", stdout_and_stderr=True)
```

### Log to a file, delete contents first

```
from logging_configurator import configure_logging
configure_logging(path="foo.log", append=False)
```

## Publishing to PyPI

```
git checkout <tag>
python -m build
twine check dist/*
twine upload dist/*
git checkout master
```
