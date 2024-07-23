number=int(input("enter a number"))
if(number%2==0 and number>0):
    print("number is even and positive")
elif(number%2==0 and number<0):
    print("number is even and negative")
elif(number%2!=0 and number>0):
print("number is odd and positive")
else:
print("number is odd and negative")