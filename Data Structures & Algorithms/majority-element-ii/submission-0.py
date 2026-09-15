class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictionary = defaultdict(int)
        requiredSize = len(nums) // 3
        res = set()

        for num in nums:
            dictionary[num] += 1
            if dictionary[num] > requiredSize:
                res.add(num)
        
        return list(res)