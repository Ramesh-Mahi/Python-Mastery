# a = 100 
# b = a 

# print(id(a))
# print(id(b))

# a = [1,2]

# b = a 

# b.append(3)

# print(a)
# print(b)

# a = "abc"

# b = a

# b = b + "d"

# print(a)
# print(b)

# a = {"name":"John"}

# b = a

# b["age"] = 25

# print(a)

# x = (1,2)

# print(type(x))

a = 5 
b = 5.3 

str1 = 'hello'
list1 = [1,2,3,4]
print (id(list1))
list1.append(5)
print(id(list1))

print(id(str1))
str1 = str1 + 'world'
print(id(str))
dict1 = {'s.no':1, 'name':'Ram'}
tup1 = (2,3,5,6)
set1 = {1, 2,3,5}

print(a, type(a), id(a))
print(str1, type(str1), id(str1))
print(set1, type(set1), id(set1))

#Interview Questions
"""
1. id() -> it displays the memory of the object 
2. Python pass-by-reference - as the variable doesn't store value. it stores the memory reference to the object
3. list saves and modifies the values in the same list (same memory reference) and tuple is immutable and it saves the values in a new tuple (different memory reference)
4. a = b -> means both a and b will have the same memory reference 
5. because both would point to the same memory reference so changing one will reflect in the other
6. == -> it will check for the value contents whether both values are same and is -> it checks whether both objects points to the same memory address
7. strings immutable -> as it stores the values in a new string in the different memory reference and it can't modify the already existing string
8. everything is an object in python. list, string, set etc...
"""

a = 256
b = 256

print(a == b)

a = [1,2]

b = a

c = a.copy()

print(a is b)

print(a is c)

print(a == c)