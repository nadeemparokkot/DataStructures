nums = [1,5,0,3,5]
new=[]
small=nums[0]
#any and or
#any only have one condition and only check condition True or False
#or have two condition
c=0
while any(num!=0 for num in nums):
    for i in nums[1:]:
        if i < small and i != 0:
            small = i
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i]-=small
    c+=1
    # for i in nums:
    #     if i != 0:
    #         new.append(i - small)
    #     else:
    #         new.append(i)
print(c)



# first cheythath

# nums = [11,5,0,3,0,13,25]
# small=nums[0]

# for num in nums:
#     for i in nums[1:]:
#         if i < small and i != 0:
#             small = i
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[i]-=small
#     print(nums)
# print(nums)


