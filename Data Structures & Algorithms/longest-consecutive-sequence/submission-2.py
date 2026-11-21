class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if len(nums) == 0:
            return 0
        maxL = 1
        for num in s:
            if (num - 1) not in s:
                length = 1
                while (num + length) in s:
                    length += 1
                maxL = max(maxL, length)
        return maxL