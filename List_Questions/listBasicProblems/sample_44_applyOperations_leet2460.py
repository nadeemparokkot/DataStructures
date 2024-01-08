nums =[847,847,0,0,0,399,416,416,879,879,206,206,206,272]
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        nums[i]*=2
        nums[i+1]=0
print(nums)
# for i in range(len(nums)-1):
#     if nums[i]==0:
#         nums[i],nums[i+1]=nums[i+1],nums[i]
# zeros=nums.count(0)
# print(zeros)
zeros=[i for i in nums if i==0]
nums=[i for i in nums if i!=0]
print(nums+zeros)