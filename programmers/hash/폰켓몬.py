def solution(nums):
    hDict = {}
    for i in nums:
        hDict[i] = 1 # duplicate check

    if len(nums) // 2 <= len(hDict) :
        return len(nums) // 2

    return len(hDict)
