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

print()
print(f'Пришло записей: {n}')
print(f'Количество ошибок: {errors}')
print(f'Записей больше порога: {max_value}')
print(f'Максимальное значение: {round(max(lst), 1)}')
print(f'Среднее значение: {round((sum(lst) / len(lst)), 1)}')


