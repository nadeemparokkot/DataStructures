lst=[]
limit=int(input("Enter a limit "))
for i in range(limit):
    values=int(input(f"Enter {i+1} values "))
    lst.append(values)
print(lst)
element=int(input("Enter a element to fetch index"))
pos=0
for i in lst:
    pos+=1
    if i==element:
        print(f"index of {element} is ",pos)
        break
