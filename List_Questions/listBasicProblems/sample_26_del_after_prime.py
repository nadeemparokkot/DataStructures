# Delete two elements after occurrence of a prime numbe
lst=[10,9,7,12,14,5]
for num in range(len(lst)):
    for i in range(2,lst[num]):
        if lst[num]%i==0:
            break
    else:
        lst.pop(num+1)
        lst.pop(num+1)
        print(lst)
        break

