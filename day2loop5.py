#you are given with a comma separated natural numbers 1to10 print only even numbers
my_list=list(map(int,input().split()))
count_even=0
count_odd=0
for i in range(len(my_list)):
    if(my_list[i]%2==0):
         count_even+=1
    