inp="hello------wor----ld"
inp1=''
count=0
for i in inp:
    if(ord(i)==45):
        count+=1
    else:
        inp1+=i
print('-'*count+inp1)