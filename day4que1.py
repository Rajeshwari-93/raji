my_list=list(map(int,input().split()))
peak elements=[]
for i in range (1,len(my_list)-1):
    if(my_list[i]>my_list[i-1]and my_list>my_list[i+1]):
    peak_elements.append(my_list)
print("peak_elemnts")
                                                                     