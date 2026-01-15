z = int(input('Введите первое число '))
b = int(input('Введите второе число '))
f = input('Выберите операцию: * / - + ')
k = 0
if f == '*':
    k = z * b
    print(k)
elif f == '+':
    k = z + b
    print(k)
elif f == '-':
    k = z - b
    print(k)
elif f == '/':
    k = z / b
    print(k)
