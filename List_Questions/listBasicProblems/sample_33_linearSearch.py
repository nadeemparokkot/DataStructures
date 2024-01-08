lst=[]
limit=int(input("Enter a limit"))
for i in range(limit):
    values=int(input(f"Enter {i+1} values"))
    lst.append(values)
print(lst)
element=int(input("Enter the value for search"))
is_found=False
for i in lst:
    if i==element:
        is_found=True
if is_found:
    print("found")
else:
    print("Not found")
