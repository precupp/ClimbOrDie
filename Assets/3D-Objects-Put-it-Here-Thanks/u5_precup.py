#######################################################################

#1. Schreiben Sie eine Code, der eine leere Liste erstellt und mit den Zahlen 1 bis 1000 befüllt

###############################  1  #####################################
print("//      U1      //")

emptyToAThousand = []
def oneToAThousand(arr):
    for i in range(1,1001):
        arr.append(i)

oneToAThousand(emptyToAThousand)
print(emptyToAThousand)

#######################################################################

#2. Sortieren Sie eine Liste mit beliebigen Namen alphabetisch. Dafür gibt es in Python bereits eine
#built-in Funktion. Recherchieren und verwenden Sie diese Funktion. Geben Sie das Ergebnis
#auf der Konsole aus

###############################  2  #####################################
print("//      U2      //")

nameList = ["Danny", "Zayn", "Tania", "Maya", "Anna"]
print(nameList)
nameList.sort()
print(nameList)

#######################################################################

#3. Schreiben Sie Code, der das zweite Element einer beliebigen Liste auf der Konsole ausgibt. 

###############################  3  #####################################
print("//      U3      //")

arrRndm1 = ["Danny", "Zayn", "Tania", "Maya", "Anna"]
arrRndm2 = [1, 234, 999, 9679, 44]

def returnPos2(arr):
        if len(arr) >= 2:
             print("Die zweite stelle ist = ", arr[1])
        else:
             print("Du hast keine 2 Stellen im array")


print(arrRndm1)
returnPos2(arrRndm1)
print(arrRndm1)
#
print(arrRndm2)
returnPos2(arrRndm2)
print(arrRndm2)

#######################################################################

#4. Schreiben Sie Code, der den Wert ‘‘apple‘‘ in ‘‘kiwi‘‘ der Liste [‘‘apple‘‘,‘‘banana‘‘,‘‘cherry‘‘] 
# umwandelt.

###############################  4  #####################################
print("//      U4      //")

fruit = ["apple", "banana", "cherry"]

def changeToKiwi(arr):
    if "apple" in arr:
        index = arr.index("apple")
        fruit[index] = "kiwi"

print(fruit)
changeToKiwi(fruit)
print(fruit)

#######################################################################

#5. Schreiben Sie Code, der ‘‘orange‘‘ der Liste [‘‘apple‘‘,‘‘banana‘‘,‘‘cherry‘‘] hinzufügt.

###############################  5  #####################################
print("//      U5      //")


fruits = ["apple", "banana", "cherry"]

print(fruits)

fruits.append("banana")

print(fruits)


#######################################################################

#6. Inventarverwaltung für einen kleinen Laden:
# Du bist verantwortlich für die Inventarverwaltung eines kleinen Ladens. Dein Ziel ist es, ein
# einfaches System zu erstellen, das die verfügbaren Artikel im Lager, deren Mengen und Preise
# erfasst. Dieses System soll es dem Ladenbesitzer ermöglichen, das Inventar effizient zu
# verwalten, indem Artikel hinzugefügt, entfernt, aktualisiert und der Gesamtwert des Lagers
# berechnet werden kann. Du wirst Listen verwenden, um die Details der Artikel zu speichern.

#Aufgabenstellung:
#Überprüfen Sie jede Teilaufgabe auf Ihre Funktionstüchtigkeit, bevor Sie mit der nächsten
#weitermachen.
#1. Definiere eine Inventarliste
#Erstellen Sie ganz oben in ihrer Python-Datei eine Liste namens inventory, in der jeder
#Artikel als Unterliste dargestellt wird (also Listen in einer Liste). Jede Unterliste enthält:
#• Den Namen des Artikels (String),
#• Die Menge auf Lager (Ganzzahl),
#• Den Preis pro Einheit (Fließkommazahl).
#• Fügen Sie zwei Äpfel, eine Banane und drei Orangen hinzu (den Preis können Sie
# #beliebig definieren).
#z.B. inventory = [[„Apfel“,100,0.5],[„Orange”….].

###############################  6  #####################################
print("//      U6      //")

#6.1
print("//      U6.1      //")

inventory = [["Apple",100,0.5],["Banana", 50,0.65], ["Orange", 20,0.33]]  

print(inventory)

#6.2
print("//      U6.2      //")

def list_inventory(arr):
     for i in arr:
          name, amount, price = i
          print(f"Artikelname: {name}, Menge: {amount}, Preis: {price} Euronen ")
          
list_inventory(inventory)

#6.3
print("//      U6.3      //")

def addItem(arr, name, amount, price):
     arr.append([name, amount, price])
     print(f"Ein neues Produkt wurde hinzugefugt:  / {name} /")

addItem(inventory, "Kiwi",1000, 1 )
list_inventory(inventory)

#6.4
print("//      U6.4      //")

def delItem(arr, name):
    for i in arr:
          if i[0].lower() == name.lower():
               arr.remove(i)
               print(f"{name} was deleted from the inventory")
               return
    print("item not found")

delItem(inventory, "BaNaNa")
list_inventory(inventory)

#6.5
print("//      U6.5      //")

def updateItem(arr, name, quantity=None, price=None):
    for item in arr:
        if item[0].lower() == name.lower():  
            if quantity is not None:
                item[1] = quantity 
            if price is not None:
                item[2] = price  
            print(f"{name} wurde geupdated: Menge = {item[1]}, Preis = {item[2]} Euronen")
            return
    print(f"{name} wurde im Inventar nicht gefunden.")

updateItem(inventory, "Apple", quantity=120, price=0.55)

list_inventory(inventory)
 

#6.6
print("//      U6.6      //")

def calcValue(arr):
    totalValue = 0.0 
    for item in arr:
        quantity = item[1]  
        price = item[2]     
        totalValue += quantity * price  
    return totalValue


total_inventory_value = calcValue(inventory)
print(f"Der Gesamtwert des Inventars beträgt: {total_inventory_value} Euronen")



#########################################################################
#a. Füge eine Funktion low_stock_alert() hinzu, die alle Artikel auflistet, deren Bestand
#unter einem bestimmten Schwellenwert liegt. Der Schwellenwert kann als Parameter
#festgelegt werden, damit er bei Bedarf geändert werden kann. Diese Funktion soll
#aufgerufen werden, wenn eine „6“ eingegeben wird.
###############################  7  #####################################

print("//    7.1    //")

def low_stock_alert(arr, sWert):
    for i in arr:
         name, amount, price = i
         if amount < sWert:
              print(f"Du hast nur noch {amount} stueck {name}, bitte neu bestellen!")


low_stock_alert(inventory,21)
list_inventory(inventory)

#########################################################################
#Erstelle eine Funktion search_item(), die nach einem Artikel im Inventar sucht und die
#Details anzeigt, falls der Artikel gefunden wird. Falls nicht, soll eine entsprechende
#Fehlermeldung ausgegeben werden.
###############################  7  #####################################


print("//    7.2    //")

def search_items(arr, productName):
     for i in arr:
          name, amount, price = i
          if name.lower() == productName.lower():
               print(f"Das Produkt wurde gefunden! ({name})")
               print(f"Artikelname: {name}, Menge: {amount}, Preis: {price}")
               return
     print(f"Dein gesuchtes Produkt ({productName}) wurde nicht gefunden!")

search_items(inventory, "kiwi")
search_items(inventory, "kiwio")
