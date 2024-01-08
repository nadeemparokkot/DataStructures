# Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
nums=[1,3,6,10,12,15]
lst=[]
c=0
for i in nums:
    if i%2==0 and i%3==0:
        c+=1
        lst.append(i)
if c>0:
    avg = sum(lst) / c
    print(lst)
    print(avg)
else:
    print("There is no single number that satisfies the requirement ")