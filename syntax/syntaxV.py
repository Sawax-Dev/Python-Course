""" Dictionary in python """
#syntax
myDictionary = {
    "Colombia": "Bogotá", #The country is a key for the search
    "Francia": "Paris",
    "Estados Unidos": "Washington",
    "Mosqueteros": 3
}
print(myDictionary["Colombia"])

#Add elements to myDictionary.
myDictionary["Italia"] = "Roma"

#Edit value in myDictionary
myDictionary["Venezuela"] = "Maracaibo" #Wrong value
myDictionary["Venezuela"] = "Caracas"

#Delete value in myDictionary.
del (myDictionary["Venezuela"])
print(myDictionary)

#Keys with a tuple in dictionary.
myTuple = ("Colombia", "Francia", "España")
myOtherDictionary = {
    myTuple[0]: "Bogotá",
    myTuple[1]: "Paris",
    myTuple[2]: "Madrid" 
}
print(myOtherDictionary)

#Tuple in dictionary.
aDictionary = {
    23: "Jordan",
    "Mosqueteros": 3,
    "Nombre": "Brian",
    "Edades": (15, 16, 17, 18)
}
print(aDictionary)

#Save dictionary in other dictionary.
primaryDictionary = {
    "Serie": "Riverdale",
    "temporadas": {
        "num": (1, 2, 3, 4) #A dictionary in other dictionary with a tuple.
    }
}
print(primaryDictionary)

#Unite dictionarys.
dictionary1 = {"Hola": "Mundo"}
dictionary2 = {"Cómo": "Están"}
dictionary1.update(dictionary2)
print(dictionary1)

#Dictionary keys.
print(myDictionary.keys())

#Dictionary values.
print(myDictionary.values())

#Dictionary lenght
print(len(myDictionary))