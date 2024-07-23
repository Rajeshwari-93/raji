str=['a','e','i','o','u']
consonants='rsdghjklnqwrtypzxcvbnm'
count=0
count1=0
inp=input()
for i in inp:
    if(i  in str):
        count+=1
print(count)
for i in inp:
    if(i in consonants):
        count1+=1
print(count1)