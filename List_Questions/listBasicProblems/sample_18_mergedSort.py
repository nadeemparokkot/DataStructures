lst1 = [2, 4, 5, 6]
lst2 = [5, 3, 9, 1]
merged_list=[]
for i in range((len(lst1)+len(lst2))//2):
    merged_list.append(lst1[i])
    merged_list.append(lst2[i])
print(merged_list)