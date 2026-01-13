def maxSubArray(nums):
    max_curr=max_glo=nums[0]
    for i in range(1,len(nums)):
        max_curr=max(nums[i],max_curr+nums[i])
        if max_curr>max_glo:
            max_glo=max_curr
    return max_glo

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
