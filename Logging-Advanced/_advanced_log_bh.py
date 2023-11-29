import logging
import os
from _advanced_log_bh_logger import logger1, formatter1, outputs_folder

'''
2023-11-28 Barak BH todo:
    done
        add a main function
        add a function that logs using the html_logger
        add a function that logs using the logger1
add a safe_print function that prints to the console
add a function that logs to html 
'''


################################################################################
# create an HTML file handler and set the level to DEBUG
html_file_name = 'sample.html'
html_log_file = os.path.join(outputs_folder, html_file_name)
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
html_file_handler.setFormatter(formatter1)


################################################################################
# create a logger object with the name of barak_logger
html_logger2 = logging.getLogger('barak_logger')
html_logger2.setLevel(logging.DEBUG)
# create a file handler
file_name = 'html_logger2.html'
html_logger2_file = os.path.join(outputs_folder, file_name) 
html_logger2_handler = logging.FileHandler(html_logger2_file)
html_logger2_handler.setFormatter(formatter1)
html_logger2_handler.setLevel(logging.DEBUG)

html_logger2.addHandler(html_logger2_handler) # writes to sample.html


# logger.addHandler(stream_handler)

# html_logger = logging.getLogger('html_logger')

def print_existing_loggers():
    print("Existing loggers:")
    loggers = logging.Logger.manager.loggerDict
    for logger in loggers:
        print(logger)
    print("End of existing loggers")



def add(x, y):
    """Add Function"""
    return x + y


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

def log_using_logger1():
    num_1 = 10
    num_2 = 0

    add_result = add(num_1, num_2)
    logger1.debug('logger - Add: {} + {} = {}'.format(num_1, num_2, add_result))    

    # div_result = divide(num_1, num_2)
    # logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

def log_using_html_logger2():
    num_1 = 10
    num_2 = 0

    add_result = add(num_1, num_2)
    html_logger2.debug('logger - Add: {} + {} = {}'.format(num_1, num_2, add_result))    

def main():
    print_existing_loggers()
    log_using_logger1()
    log_using_html_logger2()
    

if __name__ == "__main__":
    main()
