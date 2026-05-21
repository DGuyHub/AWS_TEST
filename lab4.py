myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))


print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)


myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple",
  "Roberta" : "Watermelon"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(list(myFavoriteFruitDictionary.items())[0])
print(list(myFavoriteFruitDictionary.keys())[0])
print(list(myFavoriteFruitDictionary.values())[0])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print(myFavoriteFruitDictionary["Roberta"])