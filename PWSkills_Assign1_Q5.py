#Declare 2 numbers
a=1620
b=3

cnt=0

#loop while the modulus is zero
while a%b==0:
    cnt+=1
    a=a/b

print("The number ", a, "is divisible ",cnt," times.")

