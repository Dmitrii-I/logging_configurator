# logging_configurator
[![Tests status badge](https://github.com/Dmitrii-I/logging_configurator/workflows/tests/badge.svg?branch=master)](https://github.com/Dmitrii-I/logging_configurator/actions?query=workflow%3Atests)
[![PyPI version](https://badge.fury.io/py/logging-configurator.svg)](https://badge.fury.io/py/logging-configurator)

Configure logging with one line (not counting the import).


Configure logging using defaults (log INFO to stdout/stderr, but not to a log file):
```
from logging_configurator import configure_logging
configure_logging()
```

Logging to a file and to stdout/stderr:
```
from logging_configurator import configure_logging
configure_logging(path="foo.log", stdout_and_stderr=True)
```

Log to a file and if file exists, delete its contents first:
```
from logging_configurator import configure_logging
configure_logging(path="foo.log", append=False)
```
