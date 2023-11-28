
import logging
import os

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

script_folder = os.path.dirname(os.path.abspath(__file__))
print("Script folder:", script_folder)

file_name = os.path.join(script_folder, "test.log")

logging.basicConfig(filename=file_name, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


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
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)

logging.debug(f'Add: {num_1} + {num_2} = {add_result}')
print(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logging.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logging.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logging.debug(f'Div: {num_1} / {num_2} = {div_result}')
