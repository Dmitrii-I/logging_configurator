# 0.1.0
* Function `configure_logging(path, log_level, append, stdout)` provides quick and easy way to confgure logging.

# 1.0.0
* Logging of exception traceback and log levels ERROR, CRITICAL, and WARNING is now done to `stderr` instead of `stdout`. As a result the signature of `confgiure_logging()` changed. The parameter `stdout` has been renamed to `stdout_and_stderr`.

# 1.0.1
* Declare the package to be compliant with PEP 561 by including py.typed file. PEP 561 compliance means the package has annotated its objects with type info.

# 2.0.0
* Upgrade minmum required Python version from 3.6 to 3.7 because 3.6 reached end-of-life. See official Python [website](https://www.python.org/downloads) for currently active versions.
