import math


print('test, is it running?')

def formatting():
    print("")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("")
    


formatting()

print("Gib die erste nummer ein!")
num1 = input()

print("gib die zweite nummer ein")
num2 = input()

def addNum(num1, num2):
    sum = int(num1) + int(num2)
    return sum

def subNum(num1, num2):
    sum = int(num1) - int(num2)
    return sum

def multNum(num1, num2):
    sum = int(num1) * int(num2)
    return sum

def divNum(num1, num2):
    sum = int(num1) / int(num2)
    return sum

formatting()    
addSol = print(num1, " + ", num2, " = " ,addNum(num1, num2))
formatting()

subSol = print(num1, " - ", num2, " = ", subNum(num1, num2))
formatting()

multSol = print(num1, " * ", num2, " = ",multNum(num1, num2))
formatting()

divSol = print(num1, " / ",num2," = ",divNum(num1, num2))
formatting()



formatting()



def dritte_seite(a, b, is_hypotenuse=False):
    if is_hypotenuse:
        if a >= b:
            raise ValueError("Die Hypotenuse muss die laengste Seite sein!!!")
        return math.sqrt(b**2 - a**2)
    else:
         return math.sqrt(a**2 + b**2)

seite1 = float(input("Geben Sie die Länge der ersten Seite ein: "))
seite2 = float(input("Geben Sie die Länge der zweiten Seite ein: "))
hypo_check = input("Ist die zweite Seite die Hypotenuse? (y/n): ").strip().lower()

is_hypotenuse = (hypo_check == "y")

ergebnis = dritte_seite(seite1, seite2, is_hypotenuse)
print(f"Die Länge der fehlenden Seite ist: {ergebnis}")


def isBetween(x):
    if x >= 100:
        print("die Zahl is groesser wie 100. Deine Zahl: ", x)
    elif x <= 50:
        print("die Zahl is kleiner wie 50. Deine Zahl: ", x)
    else:
        print("die Zahl is zwischen 50 und 100. Deine Zahl: ", x)

formatting()
numBetween = float(input("Gib eine zahl ein!: "))
sumBetween = isBetween(numBetween)


def isModolo(num):
    if num % 11  == 0:
        print(num, " IST ein vielfaches von 11")

    elif num % 13 == 0:
        print(num, " IST ein vielfaches von 13")

    else:
        print(num, " ist KEIN vielfaches von 11 oder 13")


numModolo = int(input("ist es ein vielfaches von 11 oder 13?"))

isModolo(numModolo)


def bubble_sort(arr):
     for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

arr = [30, 13042, 189, 8005, 782, 109, 2, 118]

bubble_sort(arr)
formatting()
print("Sorted list")
print(arr)
formatting()
print("die groesste zahl ist: ", arr[-1])


def inputTwoNum(a, b):
    print("Deine gerade Zahlen zwischen ",a, " und ", b)
    for i in range(a, b+1): 
        if i % 2 == 0:
            print(" ", i)


inputTwoNum(2,10)
    

def faktoriell():
    count = 1
    inputData = int(input("Gib eine Zahl die du Faktoriell berechnen willst"))
    for i in range(1, inputData + 1):
        count *= i

    print("Die Fakultaet von ",inputData," betraegt  ", count)


faktoriell()
