n=5
k=3
arr=[9,2,5,3,7]
ans=0
for i in range(n-k+1):
    sub_arr=arr[i:i+k]
    print("find thescore for sum sub arr",sub_arr)
    sum=0
    for i in range(1,k+1):
        sum+=sub_arr[ind-1]
        print("sum is",sum)
    print("score is:",sum)
    if sum>ans:
        ans=sum
    print(ans)
