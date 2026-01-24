class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Step 1: find break point
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: if no break point, reverse entire array
        if i == -1:
            nums.reverse()
            return
        
        # Step 3: find element just greater than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Step 4: swap
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5: reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
# Example usage:
solution = Solution()
nums = [1, 2, 3]
solution.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
