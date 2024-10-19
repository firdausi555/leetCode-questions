class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        st1=sentence1.split(" ")
        st2=sentence2.split(" ")

        if len(st1)>len(st2):
            st1,st2=st2,st1

        #to check and compare prefix
        i=0
        while i <len(st1) and st1[i]==st2[i]:
            i+=1
        
        #to check and compare suffix
        j=0
        while j<len(st1) and st1[-(j+1)] ==st2[-(j+1)]:
            j+=1

        return i+j >=len(st1)
        