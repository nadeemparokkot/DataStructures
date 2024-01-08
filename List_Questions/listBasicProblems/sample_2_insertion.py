lst=[1,2,3]
limit=int(input("Enter limit"))
for i in range(limit):
    values=int(input("Enter values"))
    lst.append(values)
position=int(input("Enter the location for add new value"))
element=int(input("Enter new Value"))
lst.insert(position-1,element)
# i=limit
# while(i>=position):
#     lst[i+1]=lst[i]
#     lst[position]=element
#     i-=1
print(lst)
print(lst[position])