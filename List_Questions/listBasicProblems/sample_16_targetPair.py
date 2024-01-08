lst=[]
limit=int(input("Enter a limit "))
for i in range(limit):
    values=int(input(f"Enter {i+1} values "))
    lst.append(values)
print(lst)
target=int(input("which number is ur target"))
for i in range(limit-1):
    for j in range(i+1,limit):
        data=lst[i]+lst[j]
        if data==target:
            print(lst[i],lst[j])