a=23
b=2
lcm=a*b
while b!=0:
    a,b=b,a*b//2
print("LCM of two numbers:",b)