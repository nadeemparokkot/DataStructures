#Write a program to separate prime and non-prime numbers in separate arrays
lst=[]
limit=int(input("Enter a limit"))
for i in range(limit):
    values=int(input(f"Enter {i+1} value"))
    lst.append(values)
print(lst)
nonPrime=[]
prime=[]
is_prime=True
for num in lst:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            nonPrime.append(num)
            break

    else:
       prime.append(num)

print("Prime Numbers",prime)
print("NonPrime Numbers",nonPrime)