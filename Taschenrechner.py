print ("Taschenrechner")
    
zahl1 = int(input("Gib die 1. Zahl an   "))

zahl2 = int(input("Gib die 2. Zahl an   "))

rechenart = input ("+,-,*,/")

if rechenart == "+":
    Ergebnis = zahl1+zahl2
    print (Ergebnis)

if rechenart == "-":
    Ergebnis = zahl1-zahl2
    print (Ergebnis)

if rechenart == "*":
    Ergebnis = zahl1*zahl2
    print (Ergebnis)

if rechenart == "/":
    Ergebnis = zahl1/zahl2
    print (Ergebnis)