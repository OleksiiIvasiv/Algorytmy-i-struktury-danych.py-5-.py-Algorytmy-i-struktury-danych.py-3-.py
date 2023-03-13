n = int(input("Podaj ilość wierszy: "))
m = int(input("Podaj ilość kolumn: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        val = int(input(f"Podaj element [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

for row in matrix:
    min_val = min(row)
    min_index = row.index(min_val)
    if min_index != 0:
        row[0], row[min_index] = row[min_index], row[0]

print("Wynik:")
for row in matrix:
    print(row)