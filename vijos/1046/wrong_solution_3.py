class Solution(object):
    def __init__(self):
        self.adj = [[[]]]
        self.n = None

    def run(self):
        if not self.read():
            return False
        self.solve()
        return True

    def solve(self):
        ans = float('inf')
        for k in xrange(self.n):
            updates = [[None for _ in xrange(self.n)] for _ in xrange(self.n)]
            for i in xrange(self.n):
                for j in xrange(self.n):
                    if self.adj[k][i][k] is None or self.adj[k][k][j] is None:
                        continue
                    new_dist = self.adj[k][i][k] + self.adj[k][k][j]
                    if updates[i][j] is None or updates[i][j] > new_dist:
                        updates[i][j] = new_dist

            for i in xrange(k):
                for j in xrange(i):
                    if updates[i][j] is not None and self.adj[k][i][k] is not None and self.adj[i][k][j] is not None:
                        ans = min(ans, updates[i][j] + self.adj[k][i][k] + self.adj[i][k][j])

            for i in xrange(self.n):
                for j in xrange(self.n):
                    self.adj[k + 1][i][j] = self.adj[k][i][j]
                    if updates[i][j] is None:
                        continue
                    if self.adj[k + 1][i][j] is None or self.adj[k + 1][i][j] > updates[i][j]:
                        self.adj[k + 1][i][j] = updates[i][j]


        if ans == float('inf'):
            print('No solution.')
        else:
            print ans

    def read(self):
        first_line = raw_input()
        if not first_line:
            return False

        n, m = [int(_) for _ in first_line.split()]
        self.n = n
        self.adj = [[[None for _ in xrange(n)] for _ in xrange(n)] for _ in xrange(n + 1)]
        for i in xrange(n):
            self.adj[0][i][i] = 0
        for _ in xrange(m):
            x, y, d = [int(_) for _ in raw_input().split()]
            x -= 1
            y -= 1
            if self.adj[0][x][y] is None or self.adj[0][x][y] > d:
                self.adj[0][x][y] = d
                self.adj[0][y][x] = d
        return True

if __name__ == '__main__':
    while True:
        if not Solution().run():
            break
