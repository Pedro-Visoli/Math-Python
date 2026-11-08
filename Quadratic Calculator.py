import math
a = int(input('Set the coefficient A: '))
b = int(input('set the coefficient B: '))
c = int(input('Set the coefficient C: '))
if a == 0:
    print('The coefficient A cannot be 0 in a quadratic equation, try again.')
    breakpoint()
else:
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('It will end in a complex number, try again.')
        breakpoint()
    else:
        B1 = (-b + math.sqrt(D)) / (2 * a)
        B2 = (-b - math.sqrt(D)) / (2 * a)
        print(f'Result: X1: {B1}, X2: {B2}')
