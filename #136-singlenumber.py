# def sin_num(nums):
    
#     for i in range(len(nums)):
#         count=0
#         for j in range(len(nums)):
#             if nums[i]==nums[j]:
#                 count+=1
#         if count==1:
#             return nums[i]
def sin_num(nums):
    result=0
    for i in range(len(nums)):
        result=result^nums[i]
    return result
print(sin_num([4,1,2,1,2]))