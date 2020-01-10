class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]

