n = int(input("Wprowadź rozmiar tablicy: "))
arr = []

for i in range(n):
    val = int(input("Wprowadź element tablicy: "))
    arr.append(val)

min_val = arr[0]

for i in range(1, n):
    if arr[i] < min_val:
        min_val = arr[i]

print("Minimalna wartość: ", min_val)