lst=[]
limit=int(input("Enter a limit"))
for i in range(limit):
    values=int(input(f"Enter {i+1} values"))
    lst.append(values)
lst.sort()
print(lst)
low=0
upper=len(lst)-1
is_found=False
element=int(input("Enter a element for search"))
while(low<upper):
    mid = low + upper // 2
    if element>lst[mid]:
        low=mid+1
    elif element<lst[mid]:
        upper=mid-1
    elif element==lst[mid]:
        is_found=True
        break
if is_found:
    print("element is found")
else:
    print("not found")