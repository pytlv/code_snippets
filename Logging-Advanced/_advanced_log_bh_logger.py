import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

'''
2023-11-29
Ideally, the script should have two loggers:
1. "regular" root logger. prints to time rotating file (10 second
    resulting in each run a new log file, including (copy text from chat)
    


2. HTML logger:
    - time rotation as above
    - propagte false (so it won't send it up)
    - with tags (check custom class)
    - supposed to work from within a function smart_log

def greet(name: str, greeting: str = 'Hello') -> None:


smart_log
    if any of the args or kwargs is a dataframe:
    log_df(
        df, console = True, csv: bool = False, level: str = 'DEBUG', max_rows = None,
         dtypes = False, info = true)
        
        if config.df.html = true
            log_html.level(df.to_html)
                note; max_rows
            if dtypes 
                find the function name to print dtypes as table
            if info
                pandas.DataFrame.info verbose



'''
outputs_folder = os.path.dirname(os.path.abspath(__file__)) + os.sep + '_outputs'
print(outputs_folder)

'''
1st logger = 
 - prints to an appended file
 - prints to console
 - does not rotate 

 Handler2 = with different formatter
'''
file_name = 'logger1_h1.log'
log_file = os.path.join(outputs_folder, file_name)

#1 - create logger
logger1 = logging.getLogger('root')
#2 - set logger level
logger1.setLevel(logging.DEBUG)
#3 - create formatter
formatter1 = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
# 2023-11-29 09:55:22,807:logger1:This is a debug message
#4 - create handler
file_handler1 = logging.FileHandler(log_file)
file_handler1.setFormatter(formatter1)
# file_handler1.setLevel(logging.DEBUG)
del file_name, log_file
#5 - add handler to logger
stream_handler1 = logging.StreamHandler()
stream_handler1.setFormatter(formatter1)

logger1.addHandler(file_handler1)
logger1.addHandler(stream_handler1)
logger1.propagate = True
logger1.debug('This is a debug message')
############################# Logger 2
#1 - create logger
#2 - set logger level
#3 - create formatter
#4 - handler - set output
#5 - create handler
#6 - handler - set formatter
#7 - handler - set level
#8 - add handler to logger
#9 - test logger
logger2 = logging.getLogger('logger2') #1
logger2.setLevel(logging.DEBUG) #2 
formatter2 = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(funcName)s:::%(message)s')#3
# 4 - handler - set output
file_name = 'logger2_h2.HTML'
log_file = os.path.join(outputs_folder, file_name)
#5 - create handler
file_handler2 = logging.FileHandler(log_file)
#6 - handler - set formatter
file_handler2.setFormatter(formatter2)
#7 - handler - set level
file_handler2.setLevel(logging.DEBUG)
#8 - add handler to logger
logger2.addHandler(file_handler2)
logger2.addHandler(stream_handler1)
del file_name, log_file


############################## HANDLER 3 - TIME
# 4 - handler - set output
file_name = 'logger2_h3_rot.HTML'
log_file = os.path.join(outputs_folder,'time_rotation', file_name)
#5 - create handler
handler3_time = TimedRotatingFileHandler(log_file, when='s', interval=1, backupCount=5)
del file_name, log_file

handler3_time.setFormatter(formatter2)
handler3_time.setLevel(logging.DEBUG)
logger2.addHandler(handler3_time)

#9 - test logger
logger2.debug('This is a debug message for logger2')

