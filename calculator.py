print('calculator')
while True:
    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))
    c = input('Введите символ + - * ** / // % или "v" для выхода')

    if c == 'v':
        break

    if c == '+':
        print(a, '+', b, '=', a + b)
    elif c == '-':
        print(a, '-', b, '=', a - b)
    elif c == '*':
        print(a, '*', b, '=', a * b)
    elif c == '**':
        print(a, '**', b, '=', a ** b)
    elif c == '/':
        if b != 0:
            print(a, '/', b, '=', a / b)
        else:
            print("Ошибка: деление на ноль!")
    elif c == '//':
        if b != 0:
            print(a, '//', b, '=', a // b)
        else:
            print("Ошибка: деление на ноль!")
    elif c == '%':
        if b != 0:
            print(a, '%', b, '=', a % b)
        else:
            print("Ошибка: деление на ноль!")
    else:
        print("Ошибка: неверный символ операции. Пожалуйста, используйте +, -, *, **, /, //, % или 'v' для выхода.")