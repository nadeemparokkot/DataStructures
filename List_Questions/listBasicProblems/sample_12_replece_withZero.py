lst=[]
limit=int(input("Enter a limit "))
for i in range(limit):
    values=int(input(f"Enter {i+1} values "))
    lst.append(values)
print(lst)
for i in range(len(lst)):
    if lst[i]<0:
        lst[i]=0

print(lst)
