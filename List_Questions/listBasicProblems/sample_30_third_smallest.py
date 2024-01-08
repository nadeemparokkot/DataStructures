lst=[10,42,12,1,5,13,56,2]
#10,8,6,7,20,30,
small=lst[0]
sec_small=None
third_small=None
for i in lst[1:]:
    if i<small:
        third_small=sec_small
        sec_small=small
        small=i
    elif sec_small is None or i<sec_small:
        third_small=sec_small
        sec_small=i
    elif third_small is None or i<third_small:
        third_small=i
print("Small",small)
print("Second small",sec_small)
print("Third small",third_small)