"""Task DZ"""
while True:
    try:
        num_1 = float(input('Enter first number: '))
        num_2 = float(input('Enter second number: '))
        res = num_1 / num_2
    except ZeroDivisionError:
        print('division by 0')
        continue
    except ValueError:
        print(f'Dividing a "int" and a "str"')
        break
    else:
        print(res)
        break
