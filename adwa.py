#For ciklus tartomány bejárására

for i in range(6):      #0-5-ig vesz fel értékeket
    print(i)

for i in range(2,11,2):      #2-10-ig vesz fel értékeket 2-es lépésközzel
    print(i)

gyumolcsok=["alma","körte","szilva","dinnye","cseresznye","barack"]
print(gyumolcsok[3]) #3-as indexű, azaz a 4. elem
print("\n\n")
for i in range(0,len(gyumolcsok),1):
    print(f"{i+1}. {gyumolcsok[i]}")

#For ciklus teljes bejárásra (string, lista, stb.)

for item in "Valami szöveg...":
    print(item,end="  ") #betűk egymás mellé 2db szóközzel elválasztva
print("\n")
for item in gyumolcsok:
    print(item)