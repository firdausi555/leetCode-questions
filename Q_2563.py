class Solution:
    def helper(self,target,nums):
        count=0
        low=0
        high=len(nums)-1
        while low<=high:
            if nums[low]+nums[high]<target:
                count+=high-low
                low+=1
            else:
                high-=1

        return count

    def countFairPairs(self, nums, lower, upper):
        nums=sorted(nums)
        return self.helper(upper+1,nums)-self.helper(lower,nums)
        
