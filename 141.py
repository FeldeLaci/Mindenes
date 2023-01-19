#LKKT és LNKO

def lkkt(a,b):
    if a>b:
        nsz=a   #nagyobb szám
        ksz=b   #kisebb szám
    else:
        nsz=b
        ksz=a
    osztando=nsz
    while osztando%ksz!=0:   # "!=" --> NEM egyenlő     % --> maradékképzés
        osztando+=nsz     #osztando=osztando+nsz
    return osztando

def lnko(a,b):
    while a!=b:
        if a>b:
            a-=b   # a=a-b
        else:
            b-=a    #b=b-a
    return a

print("Legkisebb közös többszörös és legnagyobb közös osztó meghatásrozása")

elso_szam=int(input("a: "))
masodik_szam=int(input("b: "))

print(f"A két szám legkisebb közös többszöröse: {lkkt(elso_szam,masodik_szam)}")
print(f"A két szám legnagyobb közös osztója: {lnko(elso_szam,masodik_szam)}")