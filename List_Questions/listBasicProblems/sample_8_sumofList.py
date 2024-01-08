lst=[]
limit=int(input("Enter a limit "))
for i in range(limit):
    values=int(input(f"Enter {i+1} values "))
    lst.append(values)
print(lst)

# inbuilt function
lstSum=sum(lst)
print("inbuilt function",lstSum)

# userDefined function
def sum():
    sum=0
    for i in lst:
        sum=sum+i
    print("userDefined function")
    print("Sum of the list :",sum)
sum()

