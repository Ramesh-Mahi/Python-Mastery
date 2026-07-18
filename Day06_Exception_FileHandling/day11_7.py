#Session 1 
a, b = 10, 0

try:
    print(a/b)

except ZeroDivisionError:
    print('Cannot divide by zero')

try:
    value = int(input())

except ValueError:
    print('Invalid number')

except KeyboardInterrupt:
    print('Cancelled')

#Catch all
except Exception as e:
    print(e)

else: # runs only if no exception occcured 
    print(result) 

finally: #always executes no matter what 
    print('Close DB')

#Session 2 
    
def set_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    
    return age 

#Custom Exception 

class InvalidSalaryError(Exception):
    pass

if salary < 0:
    raise InvalidSalaryError('Invalid salary')


#Session 3 

file = open('sample.txt', 'r')
print(file.read())
file.close()

with open('sample.txt','r') as file: #no need of file.close() here 
    print(file.read())

with open('sample.txt', 'w') as file:
    file.write('Hello')

#append 
with open('sample.txt','a') as file:
    file.write('\n New line')

#read line by line 
with open('sample.txt') as file:
    for line in file:
        print(line.strip())

Session 4 
JSON

import json 
employee = {
    'name' : 'mahi',
    'salary': 3000
}

json_data = json.dumps(employee)

print(json_data)
print(type(json_data))
obj = json.loads(json_data)
print(obj)
print(type(obj))

with open('employee.json', 'w') as file:
    json.dump(employee, file, indent = 4)


#csv 
    
import csv 

with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Name', 'Salary'])

    writer.writerow(['Mahi',50000])

with open('employees.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#Logging 
        
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Application started')
logging.warning('Disk space low')
logging.error('Database failed')

#Practice problems 

#problem 1 

a, b = 10, 0 
try:
    c = a / b 
except ZeroDivisionError as e:
    print(e)


#problem 2 
try:
    number = int(input('Enter a number '))
    print('The input is valid')
except ValueError as e:
    print(e)

#problem 3 

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError
        else:
            balance -= amount
            print(f'Amount - {amount} withdrawn; Current Balance - {balance}')
    except ValueError as e :
        print(e)

withdraw(1000, 10000)

#problem 4

def InvalidMarksError(Exception):
    print(f'Marks are either above 100 or less than 0')

marks = int(input('enter the marks'))

if marks > 100 or marks < 0:
    raise InvalidMarksError
else:
    print('Entered marks are good')

#problem 5 
    
with open('student.txt', 'w') as file:
    file.write('Mahi\n90')

with open('student.txt', 'r') as file:
    content = file.read()

print(content)

with open('student.txt', 'a') as file:
    file.write('\nRam\n80')

with open('student.txt','r') as file:
    content = file.read()

print(content)

#problem 7 
import json 

employee = {
    'name' : 'Mahi',
    'city' : 'Chennai'
}

contents = json.dumps(employee)
print(type(contents))
obj = json.loads(contents)

print(obj) 
#dumps and loads - would serialize the dict into JSON and deserialize the JSON into dict
#dump and load - would dump the dict into a physical json and read from the physical json back

with open('employee.json','w') as file:
    json.dump(employee, file, indent=4)

with open('employee.json','r') as file:
    content = json.load(file)

#problem 8
import csv
with open('employees.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Salary'])
    writer.writerow(['Mahi',5000])
    writer.writerow(['Ram',6000])

with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)

#problem 9
#configure logging 

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler() #for sending the details to console
file_handler = logging.FileHandler('app.log') # for saving the logs in a file 

console_handler.setLevel(logging.INFO)
file_handler.set_name(logging.ERROR)

clean_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
detailed_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')

console_handler.setFormatter(clean_formatter)
file_handler.setFormatter(detailed_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info('This shows up only in the console')
logger.critical('this shows in both console and app.log file')

#Mini project 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class IncidentReader:
    def read_log():
        try:
            with open('app.logs', 'r') as file:
                content = file.read()
        except FileNotFoundError as e:
            return e

    def read_json():
        try:
            with open('incident.json', 'r') as file:
                content = json.load(file)
        except FileNotFoundError as e :
            return e
    
    def rca_analyser():
        #we supposed to have the logic for checking the different anamolies amoung different tools here
        return 
    
    def write_json():
        try:
            with open('rca_report.json', 'w') as file:
                json.dump(rca_report, file, indent= 4)
        except json.JSONDecodeError as e:
            logger.error()
            return e

    def save_summary(report):
        try:
            with open('rca_summary.txt', 'w') as file:
                file.write(report)
        except:
            return f'Not able to save the RCA report'
    

#Interview Questions
'''
1. syntax errors - it occurs during the code development and can be rectified before running the code. Exceptions are error that occur during the runtime of the execution depending on the dynamic values/conditions
2. try - it is the block where we need to keep the code that may trigger the exception. 
except - it is the block that will execute when an exception occured
else - it will get executed only when the exception didn't occur
finally - irrespective of whether the exception executes or not, finally will get executed 
3. with - provides the flexibility for the user to open and perform the operation on the file and no need to put the close() here
4. raise - it will create a exception and show it as a error to the user ; return - it will just return the values from the function to the user
5. custom exceptions - User can create custom exceptions which can be used to handle very specific exceptions for the situations 
6. json.load() -> it will deserializes the json to dict (python) from a physical json file
json.loads() -> it deserializes the str based json to dict without any physical file
7. json.dump() -> it serializes the dict to json as a physical json file 
json.dumps() -> it serializes the str to json without a physical json file 
8. csv.reader() -> this is used to read the csv file; we need to extract the values from the index locations and moving any data will create problem
csv.DictReader() -> here the first row is considered as the header and it will have the data in the dict key - values pair and we can easy extract using the key from the dict
9. production code uses logging() module bez it provides the categorisation on the level of issues , it has target flexibility and context string where in we show see the metadata from the details to understand the issues immediately
10. finally -> we use finally to execute some critical cleanup tasks that cannot be avoided under any circumstances
like, closing database connections or network sockets
releasing threads or processor hardware execution locks 
deleting temporary file scraps from the local drive 

'''

#Mentor Challenge 
class BookNotAvailableError(Exception):
    #trying to borrow a book which is already been borrowed out 
    pass
class BookNotFoundError(Exception):
    #trying to find a book which is not present in the library itself 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f'Successfully borrowed the book.. {self.title}')
            return True
        else:
            raise BookNotAvailableError(f'{self.title} is available to borrow')
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f'Successfully returned the book - {self.title}')
            return True
        else:
            print(f'Notice: {self.title} is already available in the system')
            return False
        
    def display(self):
        status = 'Available' if self.available else 'Borrowed'
        print(f'Title - {self.title}, Author - {self.author}, Status - {status}')


class Library():

    def __init__(self):
        self.books = [] # Internal storage list for book object
    
    def add_book(self, book_obj):
        if isinstance(book_obj, Book):
            self.books.append(book_obj)
            print(f'Library: Added {book_obj.title} to the catalog')
        else:
            print('Error: Only valid book instances can be added ')
    
    def show_books(self):
        if not self.books:
            print('No Books in the catalog')
        else:
            print('Library Books ------')
            for book in self.books:
                book.display()
            print('-----------------')
    
    def search_book(self, search_title):
        print(f'\n Searching for the book - {search_title}')
        found = False 

        for book in self.books:
            if book.title.lower() == search_title.lower():
                book.display()
                found = True
        if not found:
            raise BookNotFoundError(f'The Book is not found')

#Testing 
            
#initializing the library 
my_library = Library()

#create some books 
book1 = Book('The Hobbit', 'J R R')
book2 = Book('Wings of fire', 'Dr. APJ')
book3 = Book('To Kill a Mockingbird', 'Harper Lee')

#adding books to the library 

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.show_books()

#borrowing and returning the operations 
try:
    book2.borrow()
except BookNotAvailableError as e:
    print(e)

book2.borrow()
book2.return_book()

try:
    my_library.search_book('hobbit')
except BookNotFoundError as e:
    print(e) 

try:
    my_library.search_book('The Matrix')
except BookNotFoundError as e:
    print(e) 