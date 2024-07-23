a=int(input())
b=int(input())
for i in range(a,b+1):
    if (i%400==0):
       print(i,end="")
    elif(i%400 and i%100)!=0:
        print(i,end=" ")