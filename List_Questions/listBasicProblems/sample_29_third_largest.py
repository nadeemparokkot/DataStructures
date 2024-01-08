lst=[10,42,12,1,5,13,56]
lar=lst[0]
sec_lar=None
third_lar=None
for i in lst[1:]:
    if i>lar:
        third_lar=sec_lar
        sec_lar=lar
        lar=i
    elif sec_lar is None or i>sec_lar:
        third_lar=sec_lar
        sec_lar=i
    elif third_lar is None or i>third_lar:
        third_lar=i

print(lar)
print(sec_lar)
print(third_lar)