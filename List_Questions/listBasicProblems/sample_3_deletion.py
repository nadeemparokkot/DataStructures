lst=[]
limit=int(input("Enter limit"))
for i in range(limit):
    values=int(input("Enter values"))
    lst.append(values)
print(lst)
n=int(input("1 for to remove element\n2 for to remove position\nplease choose a number"))
if n==1:
    element = int(input("Enter element to delete"))
    lst.remove(element)
else:
    position=int(input("Enter position to delete"))
    lst.pop(position-1)
print("After remove")
print(lst)