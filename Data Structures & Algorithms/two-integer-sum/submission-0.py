class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        l = []
        for i in range(len(nums)):
            print(nums[i])
            num = target - nums[i]
            if num in s:
                l.append(s[num])
                l.append(i)
                return l
            else:
                s[nums[i]] = i
        