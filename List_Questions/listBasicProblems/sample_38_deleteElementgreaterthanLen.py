# Write a program to count the frequency of each element of an array. Delete the element if frequency is greater than half the size of array
lst=[2,9,5,8,2,2,2,2]
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
new_dict = [key for key, value in dic.items() if value <len(lst)/2]  # Removes odd-valued keys
print(new_dict)
# print(max(dic.values()))
# maxValue=max(dic.values())
# for key,val in dic.items():
#     if val==maxValue:
#         print(key)

