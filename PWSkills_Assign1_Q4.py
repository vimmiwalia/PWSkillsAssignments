# Declaring a list

randomList=['a', 2, 3.4,'b',"subString",'d','e']
randomList.append([100,200,300])


#Iterating in a loop

#While loop

i=0
y=0
lenOfSubString=len(randomList[7])
#Store length of the list
lenOfList=len(randomList)

while i<lenOfList:
    print("The data type is", type(randomList[i]), " | The element is : ", randomList[i])
    if i==7:
        while y<lenOfSubString:
            print("The data type is", type(randomList[7][y]), " | The element is : ", randomList[7][y])
            y+=1
    i+=1

#For loop
y=0
for ele in randomList:
    print("The data type is", type(ele), " | The element is : ", ele)
    if randomList.index(ele)==7:
        while y<lenOfSubString:
            print("The data type is", type(randomList[7][y]), " | The element is : ", randomList[7][y])
            y+=1
    