def czy_zawiera(tablica, szukana_wartosc):
    for x in tablica:
        if x == szukana_wartosc:
            return True
    return False

tablica = input("Wprowadź tablicę oddzieloną przecinkami (przykład: 1,2,3,4): ")
tablica = tablica.split(",")
tablica = [int(x) for x in tablica]

szukana_wartosc = int(input("Wpisz szukaną wartość: "))

if czy_zawiera(tablica, szukana_wartosc):
    print("Wartość jest zawarta w tablicy")
else:
    print("Wartość nie jest zawarta w tablicy")