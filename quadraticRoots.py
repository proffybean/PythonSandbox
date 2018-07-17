def roots(a,b,c):
    d = (b*b -4*a*c)**(1/2)

    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)

    print(f'root1 = {root1}')
    print(f'root2 = {root2}')

print('Enter a, b, c')
a = float(input('a > '))
b = float(input('b > '))
c = float(input('c > '))

roots(a, b, c)
