lst=[]
limit=int(input("Enter limit"))
for i in range(limit):
    values=int(input("Enter values"))
    lst.append(values)
print(lst)
lar=lst[0]
second_lar=None
for i in lst[1:]:
    if i!=lar: #for would not come same lar b number
        if i > lar:
            second_lar = lar
            lar = i
        elif second_lar is None or i > second_lar:
            second_lar = i
print("Second Largest",second_lar)