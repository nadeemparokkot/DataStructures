lst=[]
limit=int(input("Enter limit"))
for i in range(limit):
    values=int(input("Enter values"))
    lst.append(values)
print(lst)
print("After Reverse")
print(lst[::-1])
print("reverse adjacent")
for i in range(0,len(lst),2):
    if i + 1 < len(lst): #this for odd numbers
     lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)
#method 2
#last element would not read
# lst=[10,20,30,40,50]
# for i in range(0,len(lst)-1,2):
#     lst[i],lst[i+1]=lst[i+1],lst[i]
# print(lst)