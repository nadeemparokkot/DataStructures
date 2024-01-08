lst=[]
n=int(input("Enter a limit"))
for i in range(n):
    values=int(input("Enter values"))
    lst.append(values)
print(lst)
smallest=lst[0]
second_sma=None
for i in lst[1:]:
    if i<smallest:
        second_sma=smallest
        smallest=i
    elif second_sma is None or i<second_sma:
        second_sma=i
print(second_sma)
