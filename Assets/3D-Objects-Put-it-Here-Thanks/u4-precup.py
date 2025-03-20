arr = [30, 13042, 189, 8005, 782, 109, 2, 118]

#Schreiben Sie eine Funktion, die den höchsten Wert einer Liste aus Zahlen zurückgibt.
###############################  1  #####################################

def highestNumber(arr):
    maxZahl = arr[0]
    for i in arr:
        if maxZahl < i:
            maxZahl = i
    print("DIe höchste nummer aus deinem array: ", maxZahl)

highestNumber(arr)

#######################################################################

#Schreiben Sie eine Funktion, die den Mittelwert von in der Konsole eingegebenen Zahlen
#zurückgibt.

###############################  2  #####################################

def mittelwertCalc():
    num = []  

    while True:  
        eingabe = input("Gib eine Zahl ein und schreib 'done' wenn du fertig bist: ")
        
        if eingabe.lower() == "done":  
            break  
        try:
            zahl = int(eingabe)
            num.append(zahl) #zuweisung 
        except ValueError:
            print("Bitte gib eine Zahl ein du kek!")  

    if num:  # Liste nicht leer 
        mittelwert = sum(num) / len(num)  
        print("Der Mittelwert ist:", mittelwert)
    else:
        print("Du hast keine Zahlen eingegeben du kek")


mittelwertCalc()
    

#######################################################################

#Schreiben Sie eine Funktion, die zurückgibt, ob sich ein Name (soll in der Konsole eingegeben
#werden), in einer von Ihnen definierten Liste an Namen befindet. Befindet sich der Name nicht
#in der Liste, soll ein False auf der Konsole ausgegeben werden. Befindet sich der Name in der
#Liste, soll ein True ausgegeben werden

###############################  4  #####################################


 
def checkName(arr):
    isTrue = False
    eingabe = input("Gib einen namen ein: ")

    for i in arr:
        if eingabe == i:
            isTrue = True
            break
 
    if isTrue == True:
        print("Der gesuchte Name WURDE in der Datebank gefuden")
    elif isTrue == False:
        print("Der Name wurde NICHT in der Datenbank gefunden")

arrString = ["Kevin", "Abdul", "Muhammad", "Turko", "Din", "Simon"]
   
checkName(arrString)    


#######################################################################

#Schreiben Sie eine Funktion, die alle geraden Zahlen zwischen zwei als Parameter
#übergebenen Zahlen auf die Konsole ausgibt. Nutzen Sie eine void-function, d.h. Ihre Funktion
#benötigt kein return Statement.

###############################  3  #####################################

def inputTwoNum(a, b):
    print("Deine gerade Zahlen zwischen ",a, " und ", b)
    for i in range(a, b+1): 
        if i % 2 == 0:
            print(" ", i)

inputTwoNum(2,10)

#######################################################################

#Schreiben Sie eine Funktion, die die Summe aller Zahlen bis zu einem Maximalwert, der über
#die Konsole eingegeben wird, berechnet und zurückgibt. Z.B. Nutzer*in gibt 3 ein, das Ergebnis
#der Funktion ist 6 (1 + 2 + 3)

###############################  5  #####################################

def sumNumbers():
    count = 0
    inputData = int(input("Gib eine Zahl die du fancy Summieren willst"))
    for i in range(1, inputData + 1):
        count += i

    print("Die Summe von ",inputData," betraegt  ", count)

sumNumbers()

#######################################################################

#Schreiben Sie eine void-Funktion, die die Elemente der Liste an Zahlen (10, 20, 30, 40, 50) in
#umgekehrter Reihenfolge (50, 40, 30, 20, 10) auf der Konsole ausgibt. Diese Funktion soll mit
#Listen unterschiedlicher Länge und mit unterschiedlichen Zahlen funktionieren. Sie können die
#einzelnen Elemente der Liste über []-Klammern referenzieren, z.B. list_of_numbers[0] ergibt
#die Zahl 10, list_of_numbers[2] ergibt die Zahl 30.

###############################  6  #####################################

sortElement = [10,20,30,40,50,60,70,80,90,100]


def bubble_sort(arr):
     for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] < arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


bubble_sort(sortElement)
print("Sorted list")
print(sortElement)


#######################################################################

#Bonusaufgabe: Schreiben Sie eine void-Funktion, die folgendes Muster auf die Konsole ausgibt:

#Damit die print-Funktion nicht immer automatisch einen Zeilenumbruch einfügt, können Sie
#den Parameter end übergeben, z.B. print(a_random_number, end = ‘‘ ‘‘). Eine neue Zeile
#können Sie über eine print-Funktion ohne Parameter einfügen, d.h. print().

###############################  7  #####################################

def numberPattern():
    for i in range(5, 0, -1):  
        for j in range(i, 0, -1):  
            print(j, end=" ")
        print("")  

numberPattern()




############################

test123 = float('inf')
if test123 > 100000000:
    print(True)
else:
    print(False)
##########################
test321 = float('-inf')
if test321 < -100000000:
    print(True)
else:
    print(False)