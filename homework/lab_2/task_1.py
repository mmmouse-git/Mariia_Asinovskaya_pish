def f(x):
    if x < 2 and x >= -2:
        return x*x
    elif x>= 2:
        return x*x + 4*x + 5
    else:
        return 4
    

print(f(1))
print(f(2))
print(f(-3))