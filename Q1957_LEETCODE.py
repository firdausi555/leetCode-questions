class Solution:
    def makeFancyString(self, s: str):
        res=""
        i=0
        while i<len(s):
            if i<len(s)-3 and s[i]==s[i+1]==s[i+2]:
                res+=s[i]
                res+=s[i+1]
                i+=3
                if i==len(s)-1:
                    return res

            else:
                res+=s[i]
                i+=1
        return res


obj=Solution()
obj.makeFancyString(s= "aaa")