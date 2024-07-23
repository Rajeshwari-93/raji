my_list=list(map(int,input().split()))
choice=int(input("enter"))
if(choice==1):
    my_list.append(32)
    print(f"append list is {my_list}")
elif(choice==2):
    my_list.pop()
    print(f"pop list is{my_list}")
elif(choice==3):
    my_list.sort()
    print(f"sort list is{my_list}")
elif(choice==4):
    print(f"length of the list is{len(my_list)}")
else:
    print("good morning")





