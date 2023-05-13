# For mutable objects you can change the value of the  object without changing the object’s identity
# Example of mutable obejcts are lists, sets and dictionary

#Declare a list and show it is mutable
myList=[1,2,3]
print("The date type is : ", type(myList), "The items are : ", myList)
myList[1]=100
print("The date type is : ", type(myList), "The items after update are : ", myList)
myList.append(20)
print("The date type is : ", type(myList), "The items after update are : ", myList)
myList.extend([500, 600,500])
print("The date type is : ", type(myList), "The items after update are : ", myList)

print("###################################################################")
#Declare a set and show it is mutable
mySet={4,10,25}
print("The date type is : ", type(mySet), "The items are : ", mySet)
mySet.add(40)
print("The date type is : ", type(mySet), "The items after update are : ", mySet)
mySet.update(myList)
print("The date type is : ", type(mySet), "The items after update are : ", mySet)
mySet.discard(600)
print("The date type is : ", type(mySet), "The items after update are : ", mySet)

print("###################################################################")

#Declare a dictionary and show it is mutable
myDict={}
myDict["Red"]=1
myDict["Green"]=2
myDict["Blue"]=3

print("The date type is : ", type(myDict), "The items are : ", myDict)
myDict["Blue"]=0
print("The date type is : ", type(myDict), "The items after update are : ", myDict)
myDict["Orange"]=5
print("The date type is : ", type(myDict), "The items after update are : ", myDict)
del myDict["Blue"]
print("The date type is : ", type(myDict), "The items after update are : ", myDict)

print("###################################################################")
print("###################################################################")

# Immutable objects cannot be modified or changed once it is created
# Example of immutable obejcts are tuples and strings

#Declare a String and show it is immutable
# myStr1="Hello"
# print(myStr1)
# print(myStr1[0])
# myStr1[0]="h"
# print(myStr1)

#Declare a tuple and show it is immutable
myTup=(1,2,3)
print(myTup)
print(myTup[0])
myTup[0]=100
print(myTup)





