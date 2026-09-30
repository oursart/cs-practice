max_temp = int(input('Введите порог в градусах цельсия: '))
n = int(input('Введите количество записей: '))
errors = 0
max_value = 0
lst = []

for i in range(n):
    t = input('Введите температуру в градусах цельсия: ')
    if t == 'error':
        errors += 1
        continue
    t = float(t)
    if t > max_temp:
        max_value += 1
    lst.append(t)


