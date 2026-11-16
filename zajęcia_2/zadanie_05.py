liczba_punktow = float(input("Podaj liczba punktow: "))
if liczba_punktow >= 10:
    print("Zaliczone")
else:
    print("Niezaliczone")
brakuje = 10 - liczba_punktow
print(f"Brakuje {brakuje} punktów")