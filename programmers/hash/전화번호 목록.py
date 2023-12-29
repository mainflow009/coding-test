def solution(phone_book):
    hashmap = {}
    for pNum in phone_book:
        hashmap[pNum] = 1
        
    for pNum in phone_book:
        temp = ""
        for num in pNum:
            temp += num
            if temp in hashmap and temp != pNum:
                return False
    return True
