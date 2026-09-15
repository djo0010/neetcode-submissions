class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 2
        dp[1] = 3

            

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        print(dp)

        return dp[n - 2]
    # 1 + 1 = 2
    # 2 = 2

    # 1 + 1 + 1 = 3
    # 1 + 2 = 3
    # 2 + 1 = 3

    # 1 + 1 + 1 + 1 = 4
    # 1 + 1 + 2 = 4
    # 1 + 2 + 1 = 4
    # 2 + 1 + 1 = 4
    # 2 + 2 = 4
        