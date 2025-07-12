class Solution:
    def increasingTriplet(self, nums):
        if len(nums)<3:
            return False 
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            if n <= min1:
                #first min
                min1 = n  
            elif n <= min2:
                #second min
                min2 = n  
            else:
                 # Found third greater than both 
                return True 
        return False  
