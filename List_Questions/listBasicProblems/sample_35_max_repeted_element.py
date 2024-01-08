lst=[2,4,3,2,3,3,3,2,4,5,6,3,3]
is_repeated=False
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
print(max(dic.values()))
max_count = max(dic.values())
for key,val in dic.items():
    if val==max_count:
        print("max repeated value",key)
        break


