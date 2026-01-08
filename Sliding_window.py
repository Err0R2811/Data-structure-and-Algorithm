def slid_win(arr,k):
    win_sum =0 
    max_sum =0
    for i in range(k):
        win_sum=win_sum+arr[i]
    
    max_sum=win_sum

    for i in range(k,len(arr)):
        win_sum=win_sum-arr[i-k]+arr[i]
        max_sum=max(win_sum,max_sum)
    return max_sum

k=4
arr=[1,2,3,4,5,6,7,8,9,10]
print(slid_win(arr,k))

#LEETCODE SOLUTION
"""
problem no. 643. Maximum Average Subarray I 
class Solution(object):
    def findMaxAverage(self, nums, k):
        # """
        # :type nums: List[int]
        # :type k: int
        # :rtype: float
        """
        win_sum = 0
     
        for i in range(k):
            win_sum+=nums[i]
        
        max_sum=win_sum
        
        for i in range(k,len(nums)):
            win_sum=win_sum-nums[i-k]+nums[i]
            max_sum=max(win_sum,max_sum)
        return max_sum / float(k)"""


