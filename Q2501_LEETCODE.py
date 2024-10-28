class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans=-1
        hash={}
        nums.sort()
        for i in nums:
            temp=sqrt(i)
            if temp in hash:
                hash[i]=hash[temp]+1
                ans =max(ans,hash[i])
            else:
                hash[i]=1

        return ans