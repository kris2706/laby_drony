cena_sztuki = float(input("Podaj cenę jednej sztuki: "))
liczba_sztuk = int(input("Podaj liczbę sztuk: "))
cena = round(liczba_sztuk * cena_sztuki, 2)
print(f"Cena: {cena} zł")
