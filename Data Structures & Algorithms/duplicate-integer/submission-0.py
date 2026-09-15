class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevNums = {}
        for i in nums:
            if i in prevNums:
                return True
            else:
                prevNums[i] = 1
        return False