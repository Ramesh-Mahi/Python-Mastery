#Collections 

#Session 1 

#list - ordered, mutable, allows duplicates, indexed 

numbers = [10, 20, 30, 40]

numbers.append(50)  #O(1)
numbers.insert(1,15)#O(n)
numbers.remove(20)  #O(n)
numbers.pop()
numbers.extend([60, 70])
numbers.sort()
numbers.reverse()

print(numbers)

#Session 2 - Tuples - ordered, immutable, can be dict keys 

coordinates = (10,20)

#used for coordinates, database records, configuration values often fixed and shouldn't changed

#Session 3 - Sets - unordered, mutable, unique values only, very fast memebership

numbers = {1,2,3,4,5}

numbers.add(10) #O(1) in most cases
numbers.remove(2)
numbers.discard(100) #no error 
numbers.union({5,6})
numbers.intersection({2,3,8})
numbers.difference({1,2})

#Session 4 - Dictionaries 

# key - value pair , mutable, keys must be hashable, fast lookups 

#employee.get('salary') 

employee = {
    'name':'Mahi',
    'age':23,
    'role': 'Lead'
}

employee.keys()
employee.values()
employee.items()
employee.update({'city':'Chennai'})
# employee.pop('age')

print(employee.pop('age'))

# #Practice Problems 

# #Problem 1 

numbers = [10,20,30,40]
numbers.append(50)
print(f'Appending 50 {numbers}')
numbers.insert(1, 60)
print(f'Inserting 60 {numbers}')
numbers.remove(10)
print(f'Removing 10 {numbers}')
numbers.reverse()
print(f'Reversing the numbers - {numbers}')

#Problem 2 

list1 = [1,2,2,3,3,4,5,5]
list_new = list(set(list1))
print(list_new)

#Problem 3 

a = {1,2,3,4}

b = {3,4,5,6}

print(f'Common values are {a.intersection(b)}')

#Problem 4 

employee = {
    'name':'Mahi',
    'salary': 5000,
    'age': 23
}

employee['salary'] = 6000
employee.pop('age')
for key, value in employee.items():
    print(f'Keys - {key}; Value - {value}')

#Problem 5

str = 'programming'

from collections import Counter

counts = Counter(str)
print(counts)

#Mini Project

students = {
    101: {'name': 'Mahi', 'marks': 93},
    102: {'name': 'Rahul', 'marks': 88}
}

def add_student(roll, name, marks):
    if roll in students:
        print(f'Student already exists in the db. with the id {roll}')
    else:
        students[roll] = {'name': name, 'marks': marks}
        print(f'Student {name} successfully added')

def update_marks(roll, new_marks):
    if roll in students:
        students[roll] = {'marks':new_marks}
        print(f'Student {roll} successfully added')
    else:
        print(f'Student {roll} not exists')

def delete_student(roll):
    if roll in students:
        del students[roll]
        print(f'Student {roll} successully deleted')
    else:
        print(f'Student {roll} not exists')

def display_all():
    if not students:
        print('No students found')
    else:
        for key, value in students.items():
            print(f'Student - {key} : Name - {value['name']} : Marks - {value['marks']}')

def search(roll):
    if roll not in students:
        print(f'Student not found')
    else:
        print(f'Student - {students[roll]} - Name - {students[roll]['name']} : Marks - {students[roll]['marks']}')

add_student(101, 'M', 333)
update_marks(101, 334)
delete_student(101)
display_all()
search(101)

#Interview Questions
'''
1. list - ordered, mutable and allowed duplicates and indexed [] ; tuple - ordered, immutable, (), can be dict keys
2. We use tuple in a configuration, db records, coordinates where we don't want to change the data once set 
3. sets are faster than lists bez it doesn't have any duplicates and run at O(1) at most cases
4. remove() - it will remove the value from the set ; discard - it will remove the value but even if the value doesn't present then it won't throw any error
5. dict['key'] - it will return the value of that key but if the key doesn't exist then it will throw the error ; dict.get('key') - it is the safe way to get the value of the key 
6. dict keys must be immutable bez we will lose the value of that particular if the value of the key changes
7. List cannot be used as a dict key as its not hashable and list is mutable and we can't have mutable keys
8. list append - O(1) - as we are adding at the end of the list only. no change in the list order
9. set lookup - O(1) - 
10. User profile - dict; shopping cart - list ; unique email address - set; gps coordinates - tuples; conversation history - list
'''

#Mentor challenge

contacts = {
    'Mahi': '22343242',
    'Sam': '2342342'
}

def add_contact(name, mobile):
    if name in contacts:
        return f'User already exists'
    else:
        contacts[name] = mobile

def update_contact(name, mobile):
    if name in contacts:
        contacts[name] = mobile
    else:
        return f'User not exists'

def delete_contact(name):
    if name in contacts:
        del contacts[name] 

def search_contact(name):
    if name in contacts:
        print(f'Name - {name}, mobile - {contacts[name]}')

def display_all():
    for key, value in contacts.items():
        print(f'Name - {key} ; mobile - {value}')


