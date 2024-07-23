#print all the vowels followed by consonants
inp=input()
str1='aeiou'
str2='qwrtypsdfghjklzxcvbnm'
ans=""
for i in inp:
    if(i  in str1):
        ans=ans+i
for i in inp:
    if(i in str2):
        ans=ans+i
print(*ans)