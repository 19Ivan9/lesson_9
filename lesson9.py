def oops():
    my_list = [1, 23, 4, 5, 6, 6]
    i = 0
    while i <= len(my_list) + 1:
        print(my_list[i])
        i += 1


def for_oops():
    try:
        oops()
    except IndexError:
        print('Index err')


def accept(a, b):
    try:
        return print(a ** 2 / b)
    except TypeError:
        print('Unacceptable value!')
    except ZeroDivisionError:
        print('Cannot be divided by zero!')


if __name__ == '__main__':
    print('tack1:')
    for_oops()

    print('tack2:')
    num1 = int(input('Enter the first number:'))
    num2 = input('Enter the second number:')
    accept(num1, num2)
