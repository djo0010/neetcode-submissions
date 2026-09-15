class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):
            if i >= len(candidates) or sum(subset) > target:
                if sum(subset) == target and sorted(subset) not in res:
                    res.append(sorted(subset.copy()))
                return

            subset.append(candidates[i])
            dfs(i+1)

            subset.pop()

            dfs(i + 1)
        
        dfs(0)
    
        return res