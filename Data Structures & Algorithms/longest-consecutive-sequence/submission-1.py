class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        longest = 0

        for num in nums:
            count = 0
            if num - 1 not in numsSet:
                while num + 1 in numsSet:
                    count += 1
                    num += 1
                longest = max(longest, count + 1)
        return longest