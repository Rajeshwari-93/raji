str1='aeiou'
str2='qwrtypsdfghjklzxcvbnm'
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)