class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        numsSeen = set()
        for num in nums:
            if num not in numsSeen:
                nums[i] = num
                i += 1
                numsSeen.add(num)

        return len(numsSeen)