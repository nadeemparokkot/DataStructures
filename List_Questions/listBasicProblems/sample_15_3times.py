# Find array elements that occur exactly three times
lst=[]
limit=int(input("Enter a limit "))
for i in range(limit):
    values=int(input(f"Enter {i+1} values "))
    lst.append(values)
print(lst)
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

for i in dic:
    if dic[i]>=3:
        print(i)


