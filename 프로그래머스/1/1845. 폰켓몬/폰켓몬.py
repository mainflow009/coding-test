def solution(nums):
    hDict = {}
    for i in nums:
        hDict[i] = 1
        
    if len(nums)//2 <= len(hDict):
        return len(nums) // 2
    return len(hDict)