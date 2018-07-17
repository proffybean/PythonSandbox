from fractions import Fraction

try:
    a = float(input('enter a float>'))
except ValueError:
    print('you entered an invalid number')