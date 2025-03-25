class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=float('-inf')
        pre=1
        suf=1
        for i in range(len(nums)):
            #if we encounter 0 in between we have to initialise the pre and suf to 1
            if pre==0:pre=1
            if suf==0:suf=1

            pre=pre*nums[i]
            suf=suf*nums[len(nums)-i-1]

            res=max(res,max(pre,suf))
        return res
