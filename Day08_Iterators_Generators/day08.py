#iterator 

#iterable -> anything that we can loop over

#list, tuple, set, dict, string 

# numbers = [10,20,30]

# for number in numbers:
#     print(number)

#Iterator -> an iterator remembers where it currently is 
    
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

#practice problem1 

employees = ['Ram', 'Sam','Mahi']

iterator = iter(employees)
print(next(iterator))
print(next(iterator))


#Generator Functions

# def numbers():
#     return [1,2,3,4,5]

def numbers():
    yield 1
    yield 2 
    yield 3 
    yield 4
    yield 5

for number in numbers():
    print(number)

#practice problem 2 
    
def generate_even_numbers(n):
    for i in range(1, n+1):
        yield i * 2 
print(generate_even_numbers(1)) # it prints the generator address
for number in generate_even_numbers(10):
    print(number) # it prints the value 

#practice problem 3 

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a 
        a, b = b, a + b 

for number in fibonacci(10):
    print(number)

#session 3 
#generator expression 
    
# squares = []

# for i in range(10):
#     squares.append(i*i)

print('\n')
squares = (i*i for i in range(10))


print(squares) # it will print the address
for value in squares:
    print(value) # it will print the value

# practice problem 4 
print('\n')
cubes = (i*i*i for i in range(5))

for value in cubes:
    print(value)

#itertools 
print('\n')
from itertools import count 

for i in count(10):
    if i == 15:
        break
    print(i)

from itertools import cycle

colors = cycle(['Red', 'Blue'])

for _ in range(5):
    print(next(colors))

from itertools import repeat

for value in repeat('AI', 3):
    print(value)

from itertools import chain

a = [1,2]
b = [3,4]

print(list(chain(a,b)))

from itertools import islice

numbers = range(100)

print(list(islice(numbers, 10)))


#problem 5 

Employee_IDs = [101,102,103,104]
Incident_IDs = ['INC001', 'INC002', 'INC003']
Ticket_IDs = ['001','002','003']

print(list(chain(Employee_IDs, Incident_IDs, Ticket_IDs)))

#Session 5 

with open('logs.txt') as f:
    logs = f.readlines()

with open('logs.txt') as f:
    for line in f:
        print(line)

#Mini Project 
#Log Streaming Simulator
        
def read_logs(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line 
    except FileNotFoundError as e:
        print(f'The file - {filename} does not exists')
    

for log in read_logs('logs.txt'):

    print(f'Processing - {log}')

    if 'ERROR' in log:
        print('Critical Error found')

#Bonus Challenge 
        
import time

def incident_stream():

    raw_events = [
        {'incident_id':101, 'severity':'Critical'},
        {'incident_id':102, 'severity': 'Low'},
        {'incident_id':103, 'severity': 'Medium'},
        {'incident_id':104, 'severity': 'Low'},
        {'incident_id':105, 'severity': 'Critical'}
    ]

    for event in raw_events:
        time.sleep(0.4) #delay of 4ms
        yield event
    
def critical_incidents(stream):

    for event in stream:
        if event['severity'] == 'Critical':
            yield event

if __name__ == '__main__':
    print('AI Event processing Pipelines')
    print('Connecting to upstream')

    raw_stream_source = incident_stream()
    filtered_source = critical_incidents(raw_stream_source)

    for alert in filtered_source:
        print(f'AI alert - Action Requied')
        print(f' Incident ID - {alert["incident_id"]}')
        print(f' Severity - {alert["severity"]}')
        print('-' * 40)
    

'''
Interview Questions:
1. Iterable - Its the object through which we can iterate over like - list, dict, string etc
2. iterator - It remembers where it currently points in the object like iter(words) and we use next() to iterate over to the next iteration 
3. iterable and iterator - iterable is the object through which we can iterate over and iterator is used to remember where it points in the iterable object
4. iter() - returns an iterator object from an iterable 
5. next() - returns the next item from an iterator. If not items remain, it raises StopIteration.
6. generator - it uses a lazy evaluation and saves the memory. if we run a normal function then it will execute and store the values in the memory and generator will store the object address only and only executes one at a time through yield keyword
7. return - it will end the loop and return the complete values back from the function
yield - it will return only one value at a time and it will pause the loop and it will resume for the next instance
8. generators will only hold one value at a time in the memory and it will throws away and it keep the next instance in the memory so it saves a lot of memory in RAM
9. Generator expression - () - it has a next() under the hood.
list comprehension - [] - it will execute the complete loop and stores the values in the memory and the generator expression - it will just store the object memory and it will execute only when we explicitly executes the loop
10. itertools - count(), cycle(), islice(), repeat(), chain()
'''

#Mentor challenge 

def read_logs(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                yield line 
    except FileNotFoundError as e:
        print(f'The log file - {filename} does not exist')
    
def filter_rca_logs(log_stream):

    metrics = {'critical_count':0}

    for line in log_stream:

        if 'CRITICAL' in line or 'ERROR' in line:
            if 'CRITICAL' in line:
                metrics['critical_count'] += 1
            
            yield line, metrics['critical_count']
import os 

def run_rca_analysis(input_file, output_file):

    if not os.path.exists(input_file):
        print(f'Error: Input log file {input_file} not found')
        return
    
    print(f'RCA Agent intitialized')
    final_critical_counts = 0 

    raw_stream = read_logs(input_file)
    filtered_logs = filter_rca_logs(raw_stream)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for log_line, current_critical_counts in filtered_logs:
            out_file.write(log_line)
            final_critical_counts = current_critical_counts
    
if __name__ == '__main__':

    input_log = 'app.log'
    output_log = 'rca.txt'

    run_rca_analysis(input_log, output_log)


