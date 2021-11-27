#PW generator skapad av Johan I
#Imports random
import random

#funktion för att blanda om bokstäver och nummer
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return''.join(tempList)

#Genererar bokstäver och nummer.
Uppercaseletter1 = chr(random.randint(65,90)) # Genererar en stor random bokstav emellan A-Z
Uppercaseletter2 = chr(random.randint(65,90)) # Genererar en stor random bokstav emellan A-Z
Uppercaseletter3 = chr(random.randint(65,90)) # Genererar en stor random bokstav emellan A-Z
lowercaseletter1 = chr(random.randint(97,122)) # Genererar en liten random bokstav emellan A-Z
lowercaseletter2 = chr(random.randint(97,122)) # Genererar en liten random bokstav emellan A-Z
lowercaseletter3 = chr(random.randint(97,122)) # Genererar en liten random bokstav emellan A-Z
number1 = chr(random.randint(48,57)) # Genererar ett random nummer emellan 0-9
number2 = chr(random.randint(48,57)) # Genererar ett random nummer emellan 0-9

#Skapar variablen password med alla nummer och bokstäver sedan 
#shufflar vi om ordningen av de random genererade tecknen.
password = Uppercaseletter1, Uppercaseletter2, Uppercaseletter3, lowercaseletter1, lowercaseletter2, lowercaseletter3, number1, number2
password = shuffle(password)

#Skriver ut lösenordet.
print(password)

with open('PW.txt', 'w', newline='') as f:
    f.writelines(password)
