class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i in range(len(nums)):
            print(nums[i])
            num = target - nums[i]
            if num in s:
                return [s[num], i]
            else:
                s[nums[i]] = i
        