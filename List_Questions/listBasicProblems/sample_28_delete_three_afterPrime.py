lst=[10,9,5,18,16,7,12]

for i in range(len(lst)):
    is_prime = True
    for j in range(2,lst[i]):
        if lst[i]%j==0:
            is_prime=False
            break
    if not is_prime:
        lst.pop(i+1)
        lst.pop(i + 1)
        lst.pop(i + 1)
        break
print(lst)




