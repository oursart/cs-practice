from tablestats import *

name = input().strip()

with open(name, encoding="utf-8") as table:
    rows = read_rows(table)

print(len(rows))

counts = count_types(rows)
print(len(counts))

minutes = total_minutes(rows, "ошибка")
print(minutes)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))