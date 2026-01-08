# def missing(nums):
#     n=len(nums)
#     for i in range(n):
#         if i not in nums:
#             return i
#     return n
    
# print(missing([3,0,1]))

def missingNo(nums):
    n=len(nums)
    t_sum=(n*(n+1)/2)
    a_sum=0
    for i in range(n):
        a_sum+=nums[i]
    return int(t_sum-a_sum)

print(missingNo([3,0,1]))



