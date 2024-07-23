inp='ABC'
char=''
n=0
for i in inp:
    n=ord(i)
    char+=chr(n+4*6-1)
print(char)
