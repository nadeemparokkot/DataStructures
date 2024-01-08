lst=[]
n=int(input("Enter a limit"))
for i in range(n):
    values=int(input("Enter values"))
    lst.append(values)
print(lst)
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)