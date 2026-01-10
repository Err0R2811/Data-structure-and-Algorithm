def twosums(nums,target):
    seen = {}
    for i in range(len(nums)):
        search = target - nums[i]
        if search in seen:
            return [seen[search], i]
        seen[nums[i]] = i
    return []
print(twosums([2,7,11,15],9))