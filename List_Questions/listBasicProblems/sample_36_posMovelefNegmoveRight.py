lst=[]
neg=[]
pos=[]

limit=int(input("Enter a limit"))
for i in range(limit):
    values=int(input(f"Enter {i+1} value"))
    lst.append(values)
print(lst)
for i in lst:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
negPos=pos+neg
print(negPos)
        