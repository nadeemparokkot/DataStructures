#avoid duplicates and calculate avg
lst=[1,2,2,1,3,4,5]
a=set(lst)
print(a)
lst1=[]
c=1
for i in lst:
    if i not in lst1:
        lst1.append(i)
        c+=1
re=(sum(lst1))/c
print(c)
print(re)
print(lst1)