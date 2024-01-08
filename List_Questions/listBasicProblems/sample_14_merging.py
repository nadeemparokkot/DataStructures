list1 = [12,18,5,6,6]
list2 = [4,6,6,7]
list3=[]
k=0
for i in range(len(list1)+len(list2)):
    if i<len(list1):
        list3.append(list1[i])
    else:
        list3.append(list2[k])
        k += 1
for i in range(len(list3)-1):
    for j in range(i+1,len(list3)):
        if list3[i]>list3[j]:
            list3[i],list3[j]=list3[j],list3[i]
print(list3)