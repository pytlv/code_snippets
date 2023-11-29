# Formatter
The logging.Formatter class in Python's logging module allows several placeholders to be used in the format string. Here are some of them:

%(asctime)s: The time when the LogRecord was created, formatted with time.strftime().
%(name)s: The name of the logger used to log the call.
%(levelname)s: The textual representation of the log level (e.g., 'DEBUG', 'INFO').
%(message)s: The logged message text itself.
%(filename)s: The name of the file containing the logging call.
%(funcName)s: The name of the function containing the logging call.
%(lineno)d: The line number in the file where the logging call was made.
%(module)s: The module name portion of the filename.
%(pathname)s: The full pathname of the file containing the logging call.

## create a formatter with time:name:levelname:module:funName:::message


# Time
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
description:

filename: The base file name for the log file.

when: The type of interval at which logs should be rotated ('S', 'M', 'H', 'D', 'W0' to 'W6', 'midnight').

interval: The number of units specified by when between each rotation.

backupCount: The number of backup log files to retain.

encoding (optional): The character encoding for the log file.

delay (optional): If True, file opening is deferred until the first emit() call. This can be useful in certain situations.

utc (optional): If True, the rotation and backup times will be in UTC; if False (default), they will be in the local time zone.

atTime (optional): If specified, the log file will be rotated at the specified time, in the format (hour, minute).

suffix (optional): A string to append to the rotated log file's name. It can include a date/time format, e.g., "%Y%m%d%H%M%S".

when_time (optional): A dictionary mapping weekdays to times for weekly rotation.