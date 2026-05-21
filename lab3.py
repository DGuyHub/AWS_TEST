myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))


Num1 = int(input("Enter NO.1: "))
Num2 = int(input("Enter NO.2: "))
Num3: int = Num1 + Num2
print("Total:" + str(Num1) + " + " + str(Num2) + " = " + str(Num3))