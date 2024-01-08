lst = [10, 12, 0, 3, 0, 4, 15]

# non_zero=[i for i in lst if i != 0 ]
# zero_element=[i for i in lst if i ==0]
# newlst=zero_element+non_zero
# print(newlst)
zero_lst=[]
non_zero=[]
for i in lst:
  if i==0:
    zero_lst.append(i)
  else:
    non_zero.append(i)
new_lst=zero_lst+non_zero
print(new_lst)

