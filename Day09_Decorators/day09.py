#session 1 

#functions are first class objects
#python consider functions as variables 

#practice problem 1 

def multiply(x):
    return x * 2 

def execute(func,n):
    return func(n)

print(execute(multiply, 10))

#session 2 
#closures 

def outer(message):

    def inner():
        print(message)
    
    return inner

hello = outer('Hello') #here it will return only the inner
hello()

#practice problem 2 

def power(expontent):

    def inner(base):
        return base ** expontent

    return inner 

square = power(2)
cube = power(3)

print(square(5))
print(cube(5))

#session 3 

#basic decorator 
def decorator(func):

    def wrapper():
        print('Before')

        func()

        print('After')

    return wrapper

@decorator
def greet():
    print('Hello')

#practice problem3 
    
def uppercase(func):

    def wrapper(*args, **kwags):
        result = func(*args, **kwags)
        return result.upper()
    return wrapper

@uppercase
def greet(word):
    return word
    

print(greet('hello world'))

#Session 4 
#Decorators with Arguments 

#practice problem 4 

import time 
from functools import wraps

def timer(func):
    
    @wraps(func)

    def wrapper(*args, **kwags):
        start_time = time.time()
        result = func(*args, **kwags)
        end_time = time.time()
        return  end_time - start_time
    
    return wrapper

@timer
def greet():
    time.sleep(3)
    print('Test Print')

print(greet())
print(greet.__name__)

#Session 5 
#functools.wraps 

#session 6 
#multiple decorators 

# @timer
# @logger
# def calculate():
#     pass

#order of execution - timer -> logger -> calculate() -> logger() -> timer()

#session 7 
#caching 

from functools import lru_cache 
#lru = least recently used cache will get evicted if the max limit is reached

@lru_cache(maxsize=10)

def fibonacci(n):
    if n < 2:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

#practice problems 
#problem 1

def square(value):
    return value * value

def operation(func, value):
    return func(value)

print(operation(square, 3))

#problem 2 

#discount(percent)

def discount(percent):
    
    def apply_discount(price):
        return price - (price * percent / 100)
   
    return apply_discount

ten_percent = discount(10)
print(ten_percent(500))

#problem 3 

def uppercase(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() 
    
    return wrapper

@uppercase
def operation(value):
    return value

print(operation('hello world abc'))

#problem 4 

def timer(func):
    
    @wraps(func)
    def wrapper(*args, **kwags):
        start_time = time.time()
        result = func(*args, **kwags)
        time.sleep(1)
        end_time = time.time()
        return end_time - start_time
    return wrapper

@timer
def calculate():
    return 0

print(calculate())

#problem 5 

def logger(func):
    @wraps(func)

    def wrapper(*args, **kwags):
        print(f'Calling function {func.__name__}()')
        result = func(*args, **kwags)
        print(f'Finished function {func.__name__}()')
        return result
    return wrapper

@logger
def addition(var1, var2):
    return var1 + var2 

print(addition(3,4))

#problem 6

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        print(f'Calling the functions {func.__name__}()')
        result = func(*args, **kwags)
        print(f'Finished function {func.__name__}()')
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        start = time.time()
        result = func(*args, **kwags)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f}s')
        return result
    return wrapper

@logger
@timer
def addition(var1, var2):
    time.sleep(0.5)
    return var1 + var2

addition(2,3)

#problem 7 

from functools import lru_cache
def fibonacci_no_cache(n):
    if n < 2: 
        return n 
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

@lru_cache(maxsize=20)
def fibonnacci(n):
    if n < 2:
        return n 
    
    return fibonacci(n-1) + fibonacci(n-2)


start = time.time()
print(fibonacci(20))
end = time.time()

print(f'With lru cache - {end - start}')

start = time.time()
print(fibonacci_no_cache(20))
end = time.time()

print(f'Without cache - {end - start}')


#mini project
#employee audit system 
from datetime import datetime
import time

def audit(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        result = func(*args, **kwags)
        timestamp = datetime.now()
        print(f'Employee added')
        print(f'Timestamp - {time.time()}')
        print(f'Function Name - {func.__name__}')
        return result
    return wrapper

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        start_time = time.time()
        result = func(*args, **kwags)
        end_time = time.time()
        print(f'The execution time - {end - start:.4f}s')
        return result
    return wrapper

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        if kwags.get('role') != 'admin':
            print('Permission Denied')
            return None
        return func(*args, **kwags)
    return wrapper


@audit
@execution_time
def add_employee(name):
    time.sleep(0.3) #simulate db write/ work
    print(f'Adding employee: {name}')

@admin_only
def delete_employee(emp_id, role = None):
    print(f'Employee {emp_id} deleted')

add_employee('Mahi')
print()
delete_employee(101, role= 'admin')
delete_employee(102, role='user')

#Interview Questions 

'''
1. first-class functions - A language has first class functions when the function can be treated like any other values: assigned to variables, stored in data structues and passed as arguments and returned from other functions without any special syntax
2. closure - is a function that remembers the varibles from the enclosing scope, even after the enclosing scope has finished executing 
3. decorator - A function that takes another function as input and wraps it with extra behaviour and returns new function without modiying the existing function
4. why decorators - cross cutting behaviour. to reuse the code in each function by avoiding the duplicates and it follow DRY - dont repeat yourself
5. decorators - it has function as an argument ; wraps it with the wrapper func which can add the extra functionalities ; every decorator is implemented using a closure but not all decorators are closures
closure - any parameter can be a argument ; used to remember only the variables of the enclosing scope ; 
6. *args **kwargs - we can have n number of positional or keyword arguments without dealing with any key not found error
7. functools.wraps - normally when we use the wrapper in decorators, it will show as wrapper for the inner function name but using wraps will show the corresponding correct function name which is using the decorator. It copies the metadata from the original function onto the wrapper function so the decorated function doesn't lose its identity
8. lru_cache - this is a special decorator function where it will cache the return result of the function and will use it whenever required without the recomputation
9. we should avoid caching - when we need the unique data everytime like generating live time, fetch stock prices and memory is a concern as it consume a significant memory for storing the data. 
checking permissions, live inventory counts, 
10. real world uses of decorators - web frameworks like @app.route('/users') and @app.get('/details')
Authentication / Authorization - @login_required, @admin_only 
Caching - @lru_cache() -> 
logging - @logger, @audit
performance monitoring - @timer
retry logic - @retry
'''

#Mentor challenges
#build an AI Tool Execution Framework 
# fast api -> @app.get()
# flask -> @app.route()
# pytest -> @pytest.fixture
# dataclasses -> @dataclass 
# Pydantic -> @field_validator
import random
#----------------------
#     Log Execution
#----------------------

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        print(f'Tool 1: {func.__name__}')
        print(f'Fetching the logs..')
        result = func(*args, **kwags)
        print(f'The logs fetched succesfully')
        return result
    return wrapper

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        start_time = time.time()
        result = func(*args, **kwags)
        end_time = time.time()
        print(f'The execution time taken - {end_time - start_time:.4f}s')
        return result
    return wrapper

def retry(max_attempts=3): # Layer 1 -> the factory
    def decorator(func):   # layer 2 -> the actual decorator
        @wraps(func)
        def wrapper(*args, **kwags): # layer 3 -> the wrapper 
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwags)
                except Exception as e:
                    print(f'Attempted {retry}/{max_attempts}....failed: {e}')
                    if attempt == max_attempts:
                        print(f'Maximum retries exceeded..')
                        raise 
        return wrapper
    return decorator

def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwags):
        if kwags.get('role') != 'admin':
            print(f'The user does not have the required permission to authenticate')
            return None
        return func(*args, **kwags)
    return wrapper

#simulating the tool and llm calling steps 

def read_logs():
    print(' -> Reading the logs from Elastic/Logscale')
    time.sleep(0.2)
    return ['Error: Connection timeout', 'Warn: retrying connection', 'Error: connection failed']

def call_llm(log_data):
    print('Calling the LLM for RCA')
    time.sleep(0.3)

    if random.random() < 0.5:
        raise ConnectionError('LLM endpoint timed out')
    return 'Root Cause: Intermittent network timeout on the connection exhausion'


#the decorated pipeline 

@authorize
@retry(3)
@measure_time
@log_execution
def analyze_incident(role=None):
    logs = read_logs()
    summary = call_llm(logs)
    print(f'-> RCA Summary - {summary}')
    return summary

#tests 
print('Attempting test as admin')
analyze_incident(role='admin')

print('Attempting test as Non-admin')
analyze_incident(role='user')


    
        

