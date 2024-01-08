# qn: Find the element that appears more than n/2 times in the array.
lst = [1, 2, 2, 3, 2, 2, 4, 2]
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for i,pos in dic.items():
    if pos>len(lst)//2:
        print("Element is",i)