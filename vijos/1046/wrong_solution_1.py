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
        for i in xrange(self.n):
            for j in xrange(self.n):
                if i == j:
                    continue
                chosen_k = None
                for k in xrange(self.n):
                    if self.adj[i][k] is None or self.adj[k][j] is None:
                        continue
                    if self.adj[i][j] is None or self.adj[i][k] + self.adj[k][j] < self.adj[i][j]:
                        self.adj[i][j] = self.adj[j][i] = self.adj[i][k] + self.adj[k][j]
                        chosen_k = k
                if chosen_k is None:
                    continue
                for t in xrange(self.n):
                    if t in [i, j, chosen_k]:
                        continue
                    if self.adj[i][t] is None or self.adj[j][t] is None:
                        continue
                    ans = min(ans, self.adj[i][j] + self.adj[i][t] + self.adj[j][t])
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
