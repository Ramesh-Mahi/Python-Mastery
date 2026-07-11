# #OOP

# #Session 1 
# #Classes and Objects

# #Class -> Blueprint ; object -> actual thing 

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary

# emp = Employee('Mahi', 5000)

# print(emp.name)

# #self -> refers to the current object 


# #Session 2 

# #Methods

# class Employee:
#     company = 'OpenAI'            #class variable 
#     def __init__(self, name):
#         self.name = name        # instance varible 
#     def greet(self):
#         print(f'Hello {self.name}')

# emp = Employee('Mahi')
# emp.greet()


# #Inheritance 

# class Animal: #Parent 
#     def speak (self):
#         print('Animal speaks')

# class Dog(Animal): #Child 
#     pass

# #Method Overriding 

# class Animal:
#     def speak(self):
#         print('Animal')

# class Dog(Animal):
#     def speak(self):
#         print('Bark')

# dog = Dog()
# dog.speak()

# #super()

# class Animal:
#     def __init__(self, name):
#         self.name = name 

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed 

# #Session 4 
        
# class Employee:

#     company = 'ABC'

#     @classmethod
    
#     def get_company(cls):
#         return cls.company 
    
# Employee.get_company()


# #Static Method 

# class Math:

#     @staticmethod

#     def add(a,b):
#         return a+b 

# #str()
    
# class Employee:
#     def __str__(self):
#         return f'{self.name}'

#Pratice Problems 
    
#Problem 1 
    
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f'Name {self.name}, age {self.age}, marks {self.marks}')


student = Student('Mahi', 35, 55)
student.display()

    
#problem 2 

class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
    def area(self):
        return f'Area = {self.length * self.width}'
    def perimeter(self):
        return f'Perimeter = {2 * (self.length + self.width)}'

rectangle = Rectangle(5, 2)
print(rectangle.area())
print(rectangle.perimeter())

#problem 3 

class BankAccount:
    def __init__(self, main_balance, amount):
        self.main_balance = main_balance
        self.amount = amount 
    def deposit(self):
        self.main_balance += self.amount
        return f'{self.amount} amount deposited. main_balance - {self.main_balance + self.amount}'
    def withdraw(self):
        self.main_balance -= self.amount
        return f'{self.amount} amount withdrawn. main_balance - {self.main_balance - self.amount}'

    def check_balance(self):
        return f'main_balance = {self.main_balance}'


account = BankAccount(20000,400)

print(account.deposit())
print(account.withdraw())
print(account.check_balance())

#problem 4 

#inheritance 

class Vehicle:
    def __init__(self, name):
        self.name = name 

    def start(self):
        print('Vehicle started')

class Car(Vehicle):
    def __init__(self,name) -> None:
        super().__init__(name)

    def start(self): #problem 5 
        print('vehicle started in Car')
    
    def drive(self):
        print('Vehicle Driving now..')

car = Car('Maruthi')
car.start()
car.drive()

class Employee:
    company = 'Facebook'

    def __init__(self):
        pass

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        return cls.company

    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            print(f'{number} is a even number')
        else:
            print(f'{number} is not a even number')

emp = Employee()
emp.is_even(2)
print(f'Company changed - {emp.change_company("Whatsapp")}')

#problem 9

class Student:
    def __init__(self, name):
        self.name = name 
    def __str__(self):
        return f'Student name is {self.name}'
    def __repr__(self):
        return f'Student = {self.name}'

student = Student('Mahi')
print(student)
print(repr(student))
#str -> informal, useful for users 
#repr -> formal and more details of the variables and the methods and useful for the developers 

#Mini Project 

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
            print(f'The book - {self.title} is not availabe')
            return False
    
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
            print(f'No book found matching - {search_title}')

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
book2.borrow()
book2.borrow()
book2.return_book()

my_library.search_book('hobbit')
my_library.search_book('The Matrix')

#Interview Questions 
'''
1. OOP - object oriented programming is a programming paradim that organizes the code around the data(objects) rather than the logic or operations. Instead of writing code as a long list of sequential instructions, you break the program into independent, modular building blocks that interact with each other
it has Inheritance, Polymorphism, Encapsulation, Abstraction
2. Class - it is a blueprint or template. It has the attributes and methods that that object can have but it doesn't have actual values itself
Object - it is a concrete instance build from the blueprint and it lives in the computer memory and actually holds the values 
3. self - it represents the specific instance of the object that is currently calling the method. 
Python needs a way to understand what object's data is being modified or looked after. So by convention, we use self keyword.
4. __init__() - it is a constructor and automatically called when we create an object from the class. the primary role is to accept the arguments and initialize the object's initial values (instance variables)
5. instance varible -> it gets created inside the __init__ function and the values are temporary inside the block only
class varible -> it gets created inside in the class and the values are valid all over the class 
6. Inheritance - it means to inherit the properties of the base class (parent) to a derived class (student) and the derived class can use the attributes and methods of the base class along with its own new functionalities 
7. method overriding -> it means allowing different classes to have the same method name but unique code funtionalities 
8. @classmethod - it used to define or modify the class attributes and variables by using cls keyword 
@staticmethod - it doesn't have any cls or self keyword and it works like a independent fucntion but its present inside the class
9. super() - its a built in proxy function that returns the temporary object of the parent class and allowing the child class to use the parent's attributes and methods
it normally present in the __init__ function of the child class 
10. __str__() - its a dunder method (special method) used to change the default behaviour of the str function. 
normally it used to provide better output for users to show what does the code do in that fucntion/class
ex: if you print(obj) norally it will print the memory location of the obj but if we change the str function to show the functionality of that class. it will print that instead. 


'''

#Mentor Challenge 

# class Incident:
# #attributes - incident_id, timestamp, service_name, alert_message, status, raw_logs 
# #methods - update_status(), attach_logs(logs)

# class LogParser:
# #attributes - log_source 
# #methods - fetch_logs_by_window, filter_anomalies 
    
# class KnowledgeBase:
# #attributes - kb_source_path
# #method - get_runbook
# class LLMClient:
# #attributes - model_name, temperature, api_key
# #methods - generate_rca 
# class RCARepo
# #attributes - report_id, associated_incident_id, executive_summary, root_cause, confidence_score, action_items
# #methods - export_to_markdown()
