import logging
import advanced_employee
import os

# what getLogger() does is it creates a logger object with the name of the module
# that it's called from. So in this case, it's going to be the name of the script
# that we're running. So in this case, it's going to be advanced_log_sample.
# So we're going to get a logger object with the name of advanced_log_sample.
# in the debugger, you'll see that the logger object has a name of __main__?
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a formatter - this is the format that we want our log messages to be in
# this is the same format that we used in the basic logging sample
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# create a file handler
script_folder = os.path.dirname(os.path.abspath(__file__))
print("Script folder:", script_folder)
file_name = 'sample.log'
log_file = os.path.join(script_folder, file_name)

# create a file handler and set the level to DEBUG - a FileHandler is a handler
# that writes to a file. So we're going to write to the sample.log file.
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# create an HTML file handler and set the level to DEBUG
html_file_name = 'sample.html'
html_log_file = os.path.join(script_folder, html_file_name)
'''
GitHub Copilot: The active selection is a Python class named `HTMLFileHandler` that inherits from the `logging.FileHandler` class. This class is part of Python's built-in logging module, which provides a flexible framework for EMITTING log messages from Python programs.

The `HTMLFileHandler` class overrides the `emit` method from the `FileHandler` class. The `emit` method is responsible for processing a log record by formatting it and writing it to the appropriate destination.

In the overridden `emit` method, the log record is first formatted into a string by calling `self.format(record)`. The `format` method is inherited from the `FileHandler` class and it uses the formatter specified for this handler to convert the record into a string.

Then, the method opens the file specified by `self.baseFilename` in append mode ('a'). This means that new log messages will be added at the end of the file, rather than overwriting the existing content.

Finally, the formatted log message is written to the file, enclosed in `<p>` HTML tags. This suggests that the log file is intended to be viewed in a web browser. The `\n` at the end of the string ensures that each log message appears on a new line in the HTML file.
'''
class HTMLFileHandler(logging.FileHandler):
    def emit(self, record):
        msg = self.format(record)
        with open(self.baseFilename, 'a') as f:
            f.write(f'<p>{msg}</p>\n')

html_file_handler = HTMLFileHandler(html_log_file)
html_file_handler.setLevel(logging.DEBUG)
html_file_handler.setFormatter(formatter)

# StreamHandler is a handler that writes to a stream. So in this case, we're
# going to write to the console. 
# another way to write to the console is
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# This configuration writes to three different places
logger.addHandler(file_handler)
logger.addHandler(html_file_handler)
logger.addHandler(stream_handler)

# This configuration writes to the console and the html_log.html file
# html_logger = logging.getLogger('html_logger')
# html_logger.setLevel(logging.DEBUG)
# html_logger.addHandler(html_file_handler)
# logger.addHandler(stream_handler)




def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
