lst=[9,5,4,8,4,1,6,3,7,1,7,9,9]
freq={}
for i in lst:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)
new_dict = [key for key,value in freq.items() if value %2==0]
print(new_dict)
# for i in freq:
#     print(i)
#     if freq[i]%2==0:
#         print(freq[i])

