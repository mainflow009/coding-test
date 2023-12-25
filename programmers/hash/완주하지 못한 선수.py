def solution(participant, completion):
    hDict = {}
    sumHash = 0
    for i in participant:
        hDict[hash(i)] = i
        sumHash += hash(i)
        
    for j in completion:
        sumHash -= hash(j)
        
    return hDict [sumHash]
