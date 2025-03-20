
import math

#----------------------1-------------------------#

## Adding two numbers

add1 = 1

add2 = 1

addSum = add1 + add2

print("#-----1.1-----#")
print("")
print(add1, " + ", add2," = ", addSum)
print("")
## Subtracting two numbers

sub1 = 10

sub2 = 3

subSum = sub1 - sub2

print("#-----1.2-----#")
print("")
print(sub1," - ", sub2," = ", subSum)
print("")

## Multiplying two numbers

mult1 = 10

mult2 = 3

multSum = mult1 * mult2

print("#-----1.3-----#")
print("")
print(mult1," x ", mult2," = ", multSum)
print("")

## Dividing two numbers

div1 = 10

div2 = 2

divSum = div1 / div2 

print("#-----1.4-----#")
print("")
print(div1," / ", div2," = ", divSum)
print("")
print("")
print("")
#####################################################################

#----------------------2-------------------------#

lengthA = 2
lengthA_negative = lengthA * -1

lengthB = 5
lengthB_negative = lengthB * -1


lengthC = 8
lengthC_negative = lengthC * -1


print(lengthA_negative)
print((lengthA_negative)**2 *-1)


pythagorasSumC = math.sqrt(lengthA**2 + lengthB**2)


pythagorasSumB = math.sqrt(lengthA_negative**2 *-1 + lengthC**2)


pythagorasSumA = math.sqrt(lengthB_negative**2 *-1 + lengthC**2)


print("#-----2.1-----#")
print("")
print("-a^2 + b^2 = c^2")
print(lengthA,"^2 + ", lengthB,"^2  = ", pythagorasSumC)
print("")



print("#-----2.2-----#")
print("")
print("a^2 + c^2 = b^2")
print(lengthA_negative,"^2 + ", lengthC,"^2  = ", pythagorasSumB)
print("")



print("#-----2.3-----#")
print("")
print("-b^2 + c^2 = a^2")
print(lengthB_negative,"^2 + ", lengthC,"^2  = ", pythagorasSumA)
print("")

#####################################################################
#----------------------3-------------------------#
print("#-----3-----#")
print("")
print("")
print("")

print("enter a number: ")
num = int(input())

if 50 < num < 100:
    print(num, " liegt zwischen 50 und 100")

elif num == 50:
    print(num, " IST 50 ")

elif num == 100:
    print(num, " IST 100 ")

else:
    print(num, " liegt NICHT zwischen 50 und 100")

#####################################################################
#----------------------4-------------------------#
print("#-----4-----#")
print("")
print("")
print("")



print("enter a number: ")
num = int(input())

if num % 7  == 0:
    print(num, " IST ein vielfaches von 7")

elif num % 9 == 0:
    print(num, " IST ein vielfaches von 9")

else:
    print(num, " ist KEIN vielfaches von 7 oder 9")
#####################################################################
#----------------------5-------------------------#

print("#-----5-----#")
print("")
print("")
print("")



print("Gib deine eingabe in C° an: ")
impC = float(input())

varF = (impC * 1.8) +32

print(impC, "C° ist ",varF,"F° ")

##
print("")
print("")
print("")

print("Gib deine eingabe in F° an: ")
impF = float(input())

varC = (impF-32) / 1.8

print(impF, "F° ist ",varC,"C° ")


