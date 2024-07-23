num=int(input("enter a number"))
a=int(math.sqrt(num))
b=0
for i in range(2,a):
     if a%i==0:
    b=b+1
    if b==0:
 print(a,"is a prime number")
 print(a,"is not a prime number")