def solution(clothes):
    hashmap = {}
    for cloth, ctype in clothes:
        hashmap[ctype] = hashmap.get(ctype, 0) + 1
    # {'headgear':2, 'eyewear':1}
    result = 1
    for ctype in hashmap:
        result *= (hashmap[ctype] + 1)
        
    return result - 1
    
