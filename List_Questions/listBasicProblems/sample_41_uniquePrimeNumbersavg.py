lst=[10,9,7,7,5,17,11,11]
dic={}
lstn=[]
for num in range(len(lst)):

    for i in range(2,lst[num]):
        if lst[num]%i==0:
            break
    else:
        lstn.append(lst[num])

if lstn:
    for i in lstn:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    print(dic)
else:
    print("noPrime")

print("Unique primes")
for i in dic:
    if dic[i]==1:
        print(i)