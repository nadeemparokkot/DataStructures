lst = [1,2,3,7,2,1,5,6,4,8,5,4]
# new_lst=set(lst)
# print(new_lst)
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
if not new_lst:
    print("list is empty")
else:
    print("list is not empty")