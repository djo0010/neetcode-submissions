class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        currProduct = 1
        for i in range(len(nums)):  
            res[i] = currProduct
            currProduct *= nums[i]
        currProduct = nums[len(nums) - 1]
        for j in range(len(nums) - 2, -1, -1):
            res[j] *= currProduct
            currProduct *= nums[j]
        return res
        
