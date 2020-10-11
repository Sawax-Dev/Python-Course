""" Lists or arrays in python """
#syntax
myList = ["Brian", "Santi", "Marlon"]

#Array
myResult = myList[0:3] #Toma los elementos del 0 hasta el 3
print(f"My name's in the list is: {myResult}")

#Add an elements in my array.
myList.append("Claudia") #Adding an element to final. 
myList.insert(2, "Lola") #It's adding an element where I specified.
myList.extend(["María", "Juan", "Martina"]) #Adding some elements in the list.
myList.remove("Martina") #Remove a specified element.
print(myList[:]) #Printing all objects.
print(myList.index("Santi")) #Function index is return index number in the list.
print("Brian" in myList) #In specified if exist "Brian" in my list (this return true or false)

#My program with lists and functions.
def list(value):
    listSpace = []
    listSpace.extend([value])
    #print(f"Haz insertado el dato: {value} en la posición {position}")
    print(f"Haz insertado el dato: {listSpace[:]} en la posición: {listSpace.index(value)}")
print(list(input("Por favor, escribe el dato que quieres insertar: ")))