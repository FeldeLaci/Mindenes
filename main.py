#Változók kezelése (1 soros komment)
"""
Ez 
egy 
több soros komment
"""

print('ez "egy" szöveg')
print("ez 'egy' szöveg")
print("ez \"egy\" szöveg")
print('ez \'egy\' szöveg')

a=2
b=3
c=a+b
print(a+b)
print(c)
print("c = "+str(c)) #a c változót át kell konvertálni karakterlánc (string) típusra
print(f"c változó értéke = {c}")
print("c értéke=",c)
print(a,'+',b,'=',c)
print(f"{a} + {b} = {c}")

#------------------------------------------------------------------------------------
#Változó név szabályok

#1péter - nem kezdődhet számmal!!!
#péter neve - nem lehet benne szóköz!!!
#peters'name - nem lehet benne speciális karakter sem, csak a-z vagy A-Z vagy 0-9 és _
péter1=23 # ez jó!!
péter_neve="Péter" # ez is jó!

# case sensitive - nagy betűk és a kis betűk különbözőek!!
# "A" nem ugyan az mint az "a" / Alma nem ugyan az mint alma

#olyan változónevet kell választani ami utal annak tartalmára
#asd - TILOS!!
a=10
b=321.34
c="körte"
d=True

print(a)
print(type(a))

#Változó nevek használata jó példa:

#Autók adatai (típus, tulajdonos, stb)

autó_típus="Audi"
autó_tulajdonos="Gipsz Jakab"   #snake case

autóTípus="Skoda"   #camel case

AutóTípus="BMW" #Pascal case

#-----------------------------------------------------------------------------------
print("3. feladat:")
print("\tKérem adjon meg egy számot!")
print("\n\n\t\tSzám=")          #"\t" kapcsoló --> 1 db tabulátor
                                #"\n" kapcsoló --> 1 db soremelés 