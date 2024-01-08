# Find average of prime numbers numbers in an array
lst=[10,9,7,12,14,5]
i=0
c=0
sum=0
while(i<len(lst)): #u can use here for looop also while anenki i=0 i++ seperate kodkkanam
    flag = 0
    for j in range(2,lst[i]):
        if lst[i]%j==0:
            flag=1
            break
    if flag==0:
        sum=sum+lst[i]
        print(lst[i])
        c+=1
    i+=1
if c>0:
    avg=sum/c
    print(c)
    print(sum)
    print("Average is :",avg)
else:
    print("No prime numbers")