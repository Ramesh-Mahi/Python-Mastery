def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multify(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b