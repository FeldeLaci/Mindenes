#Abszolút érték meghatározása (manuális módon

def abszolutertek(number):    # a zárójelben formális paraméter, amit megkap a híváskor
    if number<0:
        number=number*-1
    return number             # a függvény visszatérési értéke

szam=int(input("Kérem adjon meg egy egész számot: "))

print(f"A szám abszolút értéke: {abszolutertek(szam)}")  #zárójelben a "szam" változó az aktuális paraméter
# print(f"A szám abszolút értéke: {abszolutertek(-10)}")
# print(f"A szám abszolút értéke: {abszolutertek(-34)}")
# print(f"A szám abszolút értéke: {abszolutertek(54)}")