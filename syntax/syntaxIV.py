""" Tuples in Python """
#Syntax
myTuple = ("Brian",1,2,3)

#Converts.
myArray = list(myTuple) #list is converted a tupla in array
print(myArray[0])

otherTuple = tuple(myArray) #tuple is converted a list in tuple
print(otherTuple[0])
if ("Brian" in otherTuple): #If exist "Brian" in tuple, in return true or false.
    print(f"Hi!! How are you? {otherTuple[0]}")
    
#Method count: number of elements that exist with the same value.
print(otherTuple.count(1))

#Method len: number of elements in tuple.
print(len(otherTuple))

#tuple unpacked.
myDateTuple = ("Brian", 3, 7, 2004)
name, month, day, year = myDateTuple
print(name)
print(day)
print(month)
print(year)