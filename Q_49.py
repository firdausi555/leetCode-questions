class Solution:
    def groupAnagrams(self, strs):
        mpp = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            mpp[sorted_word].append(word)
        # print(mpp)
        return list(mpp.values())
