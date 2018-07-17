def multi_tables(a):
    for i in range(1,11):
        print(f'{a} x {i} = {a*i}')

a = float(input('enter number > '))
multi_tables(int(a))