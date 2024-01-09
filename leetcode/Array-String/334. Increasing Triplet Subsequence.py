class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
    
        i = float('inf') #set infinity, opposite '0'
        j = float('inf')

        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        # i = 2/ i = 1/ j = 4/ i = 0/ j = 4 / return True
        return False
        
