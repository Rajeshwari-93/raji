inp="0123456789"
ans=0
i="1234"
inp=i.lower()
for i in inp:
    if(i in inp):
        ans+=int(i)
print(ans)