import random
myList=[]

#Add 25 random numbers to the list
i=0
while i<25:
    myList.append(random.randint(1,3000))
    i+=1

print(myList)

#Verify if the list items are divisible by 3

for ele in myList:
    if ele%3==0:
        print("Item : ", ele, "is divisible by 3")
    else:
        print("Item : ", ele, "is not divisible by 3")