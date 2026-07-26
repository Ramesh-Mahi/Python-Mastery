#context and context manager

#session 1 
#practice problem 1 
# with open('student.txt','w') as file:
#     file.write(f'Student 1 - Mahi')
#     file.write(f'Student 2 - Ram')
#     file.write(f'Student 3 - Sudip')

# with open('student.txt','r') as file:
#     result = file.read()
#     print(result)

#session 2 
#compared to try/finally -> with is preferred as its cleaner, safer, automatic memory release, exception safe, avoids memory leaks

#session 3 
#build your own context manager 
    
class FileLogger:
    def __enter__(self):
        print('Logger Started')
        return self 
    
    def logger(self, message):
        print(f'LOG: {message}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Logger Closed')

with FileLogger() as file:
    file.logger('Hello')

#session 4 
#contextlib.contextmanager
    
from contextlib import contextmanager

@contextmanager
def timer():
    print('Start')
    yield 'db_connection' # this is where the 'with' block's code runs
    print('End')

with timer():
    print('Processing')

#practice problem 3 
    
@contextmanager
def database_connection():
    print('Opening Database')
    yield 
    print('Closing Database')

with database_connection():
    print('Running Queries')

#session 5 
#handling exceptions 

class Demo:
    def __enter__(self):
        print('Started')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print('Cleaning')
        return False

# with Demo():
#     raise ValueError('Oops')

#session 6

#multiple context managers 

# with open('a.txt') as a, open('b.txt') as b:
#     print(a.read())
#     print(b.read())

#session 7 

#real AI 
    
# with DatabaseConnection():

#     logs = fetch_logs()

#     incidents = fetch_incident()

#     embeddings = build_embeddings(logs)

#     save_embeddings()

#practice problems 

#problem 1 
    
with open('log.txt', 'w') as file:
    file.write('incident1 - network issue') 

with open('log.txt', 'r') as file:
    result = file.read()

#problem 2 
import json 

incident_data = {
    'incident_number': 'INC001',
    'status': 'Open',
    'priority': 'Critical',
    'decription': 'Network connect failed'
}

with open('incident.json', 'w') as file:
    json.dump(incident_data, file, indent=4)

with open('incidents.json', 'r') as file:
    result = json.load(file)


#problem 3 

class FileLogger:
    def __init__(self, filename):
        self.filname = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'a')
        self.file.write('--Log Session started--')
        print('Starting')
        return self.file
    
    def logger(self, message):
        print(f'logging the message {message}')
    def __exit__(self):
        print('Exiting..')

with FileLogger() as file:
    file.logger('HELLO')

#problem 4 

from contextlib import contextmanager
import time

@contextmanager
def Timer():
    print('Started')
    start_time = time.time()
    yield
    end_time = time.time()
    print('Ended')
    print(f'Execution Time - {end_time - start_time:.4f}s')

with Timer():
    pass

#problem 5 

class FileLogger:
    def __enter__(self):
        print('Starting')
        return self 
    
    def logger(self, message):
        print(f'logging the message {message}')
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Exiting..')

with FileLogger() as file:
    file.logger('HELLO')

#problem 6

with open('file1.txt') as a, open('file2.txt') as b:
    print(a.read())
    print(b.read())

#Mini project 
#AI log processing context manager

class LogSession:
    def __enter__(self):
        print('Connecting to LogScale')
        return self 
    
    def fetch_logs(self):
        print('Printing Logs')
        return ['ERROR Database Timeout', 'INFO User Login', 'CRITICAL Disk Failure']
    
    def filter_errors(self, errors):
        return [error for error in errors if error.startswith('ERROR') of error.startswith('CRITICAL')]
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Closing Connection...')
        if exc_type:
            print('Logging exception .. {exc_type}')
        return False

with LogSession() as logs:

    data = logs.fetch_logs()

    filtered = logs.filter_errors(data)

    print(filtered)

#Mentor Challenge

class RCAAgent:
    def __enter__(self):
        print('Connecting to .. \n Servicenow \n Dynatrace \n LogScale')
        self.incidents = None 
        self.logs = None
        self.metrics = None 
        return self
    
    def fetch_incidents(self):
        self.incidents = ['INC001', 'INC002', 'INC003']
        return self.incidents
    
    def fetch_logs(self):
        self.logs = ['Error database timeout', 'INFO user login', 'CRITICAL disk failure']
        return self.logs
    
    def fetch_metrics(self):
        self.metrics = {'db_connection': 100, 'db_connection_max':100}
        return self.metrics
    
    def generate_summary(self):
        summary = {
            'root_cause': 'Database connection failure',
            'confidence': '99',
            'recommendation':'increase pool size'
        }
        return summary
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is not None:
            print(f'Error occured - {exc_type}')
        return False

with RCAAgent() as agent:

    logs = agent.fetch_logs()

    incidents = agent.fetch_incidents()

    metrics = agent.fetch_metrics()

    report = agent.generate_summary()

#Interview questions 
'''
1. context manager -> it takes care automatic setup and cleanup behaviour withing the block of code with the keyword 'with'. it eliminates the exception and auto release or cleanup the resources even when a exception occured or normally return
2. with -> its used to take care of the auto closing the file / process even when a exception occurred in the mid code
3. try/finally and with -> both solves the same problem but with is more modern and flexible. with is built on top of the try/finally
4. __enter__ -> runs automatically whenever the with block starts and return the value to the with block
__exit__ -> runs automatically whenever the with block ends and safely handles the cleanup
5. __exit__ -> pass 3 arguments - exc_type - expection class; exc_value - expection instance ; exc_tb - exception traceback
6. if __exit__ returns True then it will supress the exception and it won't propagate the exception to the main function
7. we should create custom context managers - when we need to handle the setup and cleanup automatically, handle the exceptions better, cordinated connects/disconnect across multiple tools
8. @contextmanager is a type of decorator from contextlib and it used to do the same startup and cleanup without the __enter__ and __exit__ and it gives yield to pass the control to the base function
9. context managers examples - File I/O, database connects and disconnects, API connections, Thread locks
10. used in tool integrations like Servicenow, Logscale, elastic 

'''

    

