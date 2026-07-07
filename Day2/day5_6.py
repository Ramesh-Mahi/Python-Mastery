# def greet(name='user'):
#     print(f'hello {name}')

# greet('Ram')

# greet()

# def add (a,b):
#     return a + b 

# result = add(10, 20)
# print(result)

# def employee(name, age):
#     print(name, age)

# employee(age= 20, name = 'ram')

# Session 2 *args and **kwargs

# *args = Unknown number of arguments to be passed - passed as tuples 
# **kwargs = Unknown number of keyword arguments to be passed - passed as dict

def numbers(*number):
    print(number)
    print(type(number))

numbers(1,3,4,5)
numbers(10,20,30,)

def employee(**details):
    print(details)
    print(type(details))

employee(name='mahi', age = 23, city='mumbai')

def total(*numbers):
    sum = 0 

    for number in numbers:
        sum += number 

    return sum

print(total(1,2,3,4,5))

def demo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

demo(
    1,
    2,
    3,
    4,
    name="Mahi",
    role="Lead"
)


#Variable scope 
def demo():
    x = 10 
    print(x)

demo()

x = 100

def demo():
    x = 10
    print(x)

demo()
print(x)

#Practice Problems
#Problem 1 

#Area of a rectangle 

def area(length, width):
    return length*width

print(area(3,3))

#Problem 2 

def largest(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num3:
        return num2 
    else:
        return num3 

print(largest(10,8,6))

#Problem 3 

def avgerage(*args):
    return sum(args)/len(args)

print(avgerage(1,2,3,4,5))

#Problem 4 

def student(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} - > {value}')

student(name = 'mahi', age = 25, marks = 88)
student(name = 'ram', age = 33, marks = 44)

#Problem 5 

def calculator(a,b,operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b 
    elif operation == '/':
        if b == 0:
            return 'Error: Division by zero'
        return a / b 
    elif operation == '%':
        return a % b
    elif operation == '//':
        if b == 0:
            return 'Error: Division by zero'
        return a // b
    elif operation == '**':
        return a ** b 
    else:
        raise ValueError
    
        return 'Invalid Operation'
def calculator(a,b,operation):
    operations = {'+': a + b,
                  '-': a - b,
                  '*': a * b,
                  '/': a / b,
                  '&': a & b,
                  '//': a//b,
                  '**': a**b}
    return operations[operation]


print(calculator(10,20,'+'))

#Mini Project 

#Functions defined 

def calculate_bonus(basic_salary, bonus_amount):
    return bonus_amount

def calculate_tax(basic_salary, tax):
    return basic_salary * (tax/100)

def calculate_net_salary(basic_salary, bonus, tax):
    return basic_salary + bonus - tax 

def display_employee(name, basic_salary, bonus, tax, net_salary):
    print(f'--- Employee Paystub: {name} ---')
    print(f'Basic Salary: ${basic_salary:.2f}')
    print(f'Bonus       : ${bonus:.2f}')
    print(f'Tax Deducted: ${tax:.2f}')
    print(f'---------------------')
    print(f'Net Salary  : {net_salary:.2f}')
    print('--------------------------')

emp_name = 'Jane'
emp_basic = 5000.00
emp_bonus = 500
emp_tax_pct = 15

bonus = calculate_bonus(emp_basic, emp_bonus)
tax = calculate_tax(emp_basic, emp_tax_pct)
net_salary = calculate_net_salary(emp_basic, bonus, tax)

display_employee(emp_name, emp_basic, bonus, tax, net_salary)

#Interview questions 
"""
1. Function is a DRY concept - don't repear yourself, instead we use the function to reuse the part of code again and again
2. we use functions to avoid repeating the code again and again. we use functions when we want to divide the full program into sub modules so that module can be called or used when needed.
3. parameter -> variables defined in the function definition and argument -> the actual values passed in the function calling 
4. return -> it returns the values from the function ; print -> it will just print the values in it. 
5. if a function has no return then it won't return anything. 
6. defaults arguments is used to assign the value of those arguments when no actual is passed in the function and it used to avoid the runtime errors
7. *args -> used to get the values when we don't know the number of inputs and it will return it as tuple
8. **kwargs -> used to get the key-value pairs and it will return as dict 
9. variable scope -> it is the scope where the value of the variable valids upto. 
10. one is local and global and local variable value valids inside the local scope and global variable valids all over the program
11. excessive use of global is bad practice -> bez it breaks encapsulation, introduces hidden dependencies and other unpredicable side effects.
"""

#Mentor Problem

def calculator(a,b,operation):

    operations = {
        '+': lambda x, y : x + y,
        '-': lambda x, y : x - y,
        '*': lambda x, y : x * y,
        '/': lambda x, y : x / y,
        '%': lambda x, y : x % y,
        '**': lambda x, y : x ** y,
        '//': lambda x, y : x // y 
    }

    if operation not in operations:
        raise ValueError(f'Unsupported operation {operation}')
    
    if operation in ('//', '/','%') and b == 0:
        raise ZeroDivisionError('Division by zero')
    
    return operations[operation](a,b)

print(calculator(10,2,'*'))