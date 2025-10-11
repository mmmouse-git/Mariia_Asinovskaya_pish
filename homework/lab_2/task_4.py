'''Составить функцию, которая определяет сумму цифр в числе'''

def summ(number):
    result = 0
    while number > 0:
        result = result + number % 10
        number = number // 10
    return result


print(summ(123))
print(summ(1234))
