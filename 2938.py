class Solution:
    def minimumSteps(self, s):
        l=0
        res=0
        for r in range(len(s)):
            if s[r]=="0":
                res+=(r-l) #swapping here refer sc 
                l+=1
        return res
        
obj=Solution()
obj.minimumSteps(s= "100")