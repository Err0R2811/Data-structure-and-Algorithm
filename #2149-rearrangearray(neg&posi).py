def arrange(nums):
    n=len(nums)
    res=[0]*n
    pos_idx=0
    neg_idx=1
    for x in nums:
        if x>0:
            res[pos_idx]=x
            pos_idx+=2
        else:
            res[neg_idx]=x
            neg_idx+=2
    return res
# Example usage:
nums = [3, -2, 1, -5, 4, -6]
result = arrange(nums)
print(result)  # Output: [3, -2, 1, -5, 4, -6]
# This function rearranges the array such that positive and negative numbers alternate.