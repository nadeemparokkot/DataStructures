lst=[]
limit=int(input("Enter a limit "))
for i in range(limit):
    values=int(input(f"Enter {i+1} values "))
    lst.append(values)
print(lst)
#user defined
for i in range(limit-1):
    for j in range(i+1,limit):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]

print(lst)

#inbuilt-funtion
lst.sort()
print("#inbuilt-funtion",lst)