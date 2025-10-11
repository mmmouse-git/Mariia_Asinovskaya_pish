"""
Составить функцию, которая опеределяте наибольший общий делитель двух чисел nod(a, b)
"""

def nod(a, b):
   a = abs(a)
   b = abs(b)
   if a > b:
     d = b
   elif a < b:
      d = a
   else:
    return a
   
   for i in reversed(range(1, d+1)):
        if a % i == 0 and b % i == 0:
            return i


print(nod(6, 15))
print(nod(77, 49))
print(nod(29, 17))

