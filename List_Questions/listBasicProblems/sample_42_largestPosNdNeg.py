# lst=[-1,2,-3,3]
def findMaxK(nums):
    nums = sorted(nums, reverse=True)
    s = set(nums)
    for i in range(len(nums)):
        if 0 - nums[i] in s:
            return (nums[i])
    return(-1)
lst = [-1,10,-3,3,6,7,-7,1]
re=findMaxK(lst)
print(re)
# lar=max(lst)
# lst=sorted(lst,reverse=True)
# print(lst)
# s=set(lst)
# print(s)
# for i in lst:
#     if i==-lar:
#         print(lar)
#         break
# else:
#     print("No larger positive exist with its neg"),