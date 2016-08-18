import copy


class Solution(object):
    def __init__(self):
        self.adj = [[]]
        self.n = None

    def run(self):
        if not self.read():
            return False
        self.solve()
        return True

    def solve(self):
        ans = float('inf')
        dp = copy.deepcopy(self.adj)
        for k in xrange(self.n):
            for i in xrange(k):
                for j in xrange(i + 1, k):
                    if all([self.adj[i][k] is not None,
                        self.adj[k][j] is not None,
                        dp[i][j] is not None, ]):
                        ans = min(ans, self.adj[i][k] + self.adj[k][j] + dp[i][j])
            for i in xrange(self.n):
                for j in xrange(self.n):
                    if dp[i][k] is None or dp[k][j] is None:
                        continue
                    if dp[i][j] is None or dp[i][j] > dp[i][k] + dp[k][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]

        if ans == float('inf'):
            print('No solution.')
        else:
            print(ans)

    def read(self):
        first_line = raw_input()
        if not first_line:
            return False

        n, m = [int(_) for _ in first_line.split()]
        self.n = n
        self.adj = [[None for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n):
            self.adj[i][i] = 0
        for _ in xrange(m):
            x, y, d = [int(_) for _ in raw_input().split()]
            x -= 1
            y -= 1
            if self.adj[x][y] is None or self.adj[x][y] > d:
                self.adj[x][y] = d
                self.adj[y][x] = d
        return True

if __name__ == '__main__':
    while True:
        if not Solution().run():
            break
