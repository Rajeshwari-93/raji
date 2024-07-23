my_list=list(map(int,input().split()))
sum=0
avg=0
n=0
for i in range(len(my_list)):
    sum+=my_list[i]
    n+=1
avg=sum/n
print(avg)