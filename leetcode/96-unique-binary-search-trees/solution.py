class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1, 1]
        for i in xrange(2, n + 1):
            ans.append(0)
            for j in xrange(0, i):
                ans[i] += ans[j] * ans[i - j - 1]
        return ans[n]
