#Százalék számítás (hányan mennek át az alapvizsgán)

def atmentTanulokSzazaleka(osszesTanuloDb,bukottTanuloDb):
    szazalek=(1-bukottTanuloDb/osszesTanuloDb)*100
    return szazalek

osszes=-1 
while osszes<1:             #a feltételben a rossz esetek vannak (ekkor kér be újra)
    osszes=int(input("Összes tanuló száma: "))

bukott=-1
while bukott<0 or bukott>osszes: #ha bukott negatív VAGY több mint az összes vizsgázó, akkor újra bekérjük
    bukott=int(input("Bukott tanulók száma:"))

szazalek=atmentTanulokSzazaleka(osszes,bukott)
print(f"A tanulók {szazalek} %-a ment át a vizsgán.")