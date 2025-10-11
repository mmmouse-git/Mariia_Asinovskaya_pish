"""Составить логическую функцию, которая опеределяет, 
верно ли, что в заданном числе сумма цифр равна произведению"""

def summ(number):
    result = 0
    while number > 0:
        result = result + number % 10
        number = number // 10
    return result

def mult(number):
    result = 1
    while number > 0:
        result = result * (number % 10)
        number = number // 10
    return result

def f(number):
    if summ(number) == mult(number):
        return True
    else:
        return False
    
print(f(23))