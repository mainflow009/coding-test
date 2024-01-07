class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = True
        answer = []
        for i in candies:
            if i + extraCandies >= maxCandy:
                result = True
            else:
                result = False
            answer.append(result)
            
        return answer
