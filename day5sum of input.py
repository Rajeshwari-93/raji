inp="hello world"
ans=""
for i in inp:
    if(i not in ans):
        ans+=i
        sum+=1
print("sum of ans",sum)