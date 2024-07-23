#remove all the brackets from the given algebraic expression
inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93):
        pass
    else:
        print(i,end="")
print()