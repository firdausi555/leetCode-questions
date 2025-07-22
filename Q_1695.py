class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        current_sum = 0
        ans = 0
        
        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            current_sum += nums[right]
            seen.add(nums[right])
            ans = max(ans, current_sum)
        
        return ans
