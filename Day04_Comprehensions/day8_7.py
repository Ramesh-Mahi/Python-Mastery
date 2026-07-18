# #Session 1 
# #List comprehension 

# numbers = [i for i in range(10)]
# print(numbers)

# #[expression for item in iterable]

# squares = [x*x for x in range(10)]

# evens = [x for x in range(20) if x % 2 == 0]

# names = ['mahi', 'ram', 'sam']

# upper = [names.upper() for name in names]

# matrix = [
#     [1,2],
#     [3,4]
# ]

# flat = [num for row in matrix for num in row]

# print(flat)

# #Dictionary Comprehension

# squares = {}

# for i in range(5):
#     squares[i] = i*i 

# squares = {i:i*i for i in range(5)}

# words = ['apple','banana','cat']

# length = {
#     word:len(word) for word in words
# }


# #Set Comprehension

# unique = {
#     x*x for x in range(10)
# }

# #Session 3 

# #Generator Expression 

# numbers = (
#     x*x for x in range(1000000)
# )

# #Nothing is calculated immediately 
# #It generates values one at a time 
# # () -> this is making this as a generator 

# #enumerate()

# names = ['A', 'B', 'C']

# index = 0 

# for name in names:
#     print(index, name)
#     index += 1 

# for index, name in enumerate(names):
#     print(index, name)

# #zip()
    
# names = ['A', 'B', 'C']
# marks = [90, 80, 70]

# for name, marks in zip(names, marks):
#     print(name, marks)

# #Session 4 

# #map()

# numbers = [1,2,3]

# result = []

# for n in numbers:
#     result.append(n*2)

# result = list(map(lambda x:x*2, numbers))

# #filter

# evens = []

# for n in numbers:
#     if n%2 == 0:
#         evens.append(n)
    
# evens = list(filter(lambda x:x%2 == 0, numbers))

# #any() -> atleast one value is truthy 

# numbers = [0,0,5]

# print(any(numbers))

# #all() -> all the values is truthy or not 

# numbers = [1,3,4]

# print(all(numbers))

# #o/p - True

# #Pratice Problems 

# #Problem 1 - list comprehension 

list1 = [i*i for i in range(1,6)]
print(list1)

#Problem 2 

list2 = ['apple', 'banana','cat']
list_updated = [value.upper() for value in list2]
print(list_updated)

#Problem 3 - dict comprehension 

numbers = [1,2,3,4]

numbers = {x:x*x for x in numbers}

print(numbers)

#Problem 4 - flatten 

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

list_flatten = [num for row in matrix for num in row]
print(list_flatten)

#problem 5 

students=['Mahi','Ram','Sam']
marks = [90, 80, 95]

zipped = list(zip(students, marks))
for i in zipped:
    print(f'{i[0]} -> {i[1]}')

#problem 6
    
fruits = ['Apple','Banana','Orange']
for id, value in enumerate(fruits,start = 1):
    print(f'{id} {value}')

#problem 7
    
list2 = [10, 15, 22, 31, 44]
list_even = list(filter(lambda x:x%2 == 0, list2))
print(list_even)


#problem 8 
list1 = ['10','20','30']
print(list1)
list_mapped = list(map(int,list1))
print(list_mapped)

#problem 9

list1 = [0,0,0,5]
print(any(list1))

list2 = [1,2,3,4]
print(all(list2))


#Mini Project 

employees = [
    {'name':'Mahi','salary':5000},
    {'name':'Ram', 'salary':8000},
    {'name':'Sam','salary':4000}
]

employees_names = [i['name'].upper() for i in employees]
print(employees_names)

employees_bonus = [{'name':employee['name'], 'salary':employee['salary']+(employee['salary']*0.1)}
                   for employee in employees]
print(employees_bonus)

employee_salary = {i['name']:i['salary'] for i in employees}
for key,value in employee_salary.items():
    print(f'{key} -> {value}')

high_earning_employees = [{'name': employee['name'], 'salary': employee['salary']} for employee in employees if employee['salary'] > 5000]
print(high_earning_employees)

for idx, value in enumerate(employees,start=1):
    print(f'{idx}. {value["name"]}')

#INTERVIEW QUESTIONS 
'''
1. list comprehension -> it is a way of performing the list performing in a single line enclosed in [] so that will turn up as a list 
2. list comprehension is faster as it performs the operations element by element. list comprehension - C level optimisation and less overhead compared to normal loop which executes at bytecode evaluation. 
3. list comprehension -> executes all the operations in the function ; generator exp -> enclosed by () and it won't execute everythin at one go. it will execute one instance at a time 
4. map() -> used to map a function to a input (list, dict etc) ; list comprehension -> used to perform a operation in a single of code 
5. filter() -> it compares the condition with a input at runtime; comprehension with if -> 
6. zip() -> it returns the zipped values from the inputs 
7. enumerate returns the id and the value of the iterable object starts from 0 which can be configurable
8. any() -> it will check if we has any one truthy value to return True; all() -> it will check if all the values are truthy to return True
9. generators are used , when we want to execute one at a time and test how it performs instead of executing everything at one go. ex - on infinite processing, streaming data, working with large datasets 
10. generators are memory efficient bez it executes one at a time 

'''

#Mentor Challenge 

def top_students(students):
    return {
        roll: info for roll, info in students.items() if info['marks'] >= 90
    }