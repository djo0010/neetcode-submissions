class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        res = []
        for i in range(k):
            currMax = float('-inf')
            keyToPop = -1
            for key in counts.keys():
                if counts[key] > currMax:
                    currMax = counts[key]
                    keyToPop = key
            res.append(keyToPop)
            counts.pop(keyToPop)
        return res
            