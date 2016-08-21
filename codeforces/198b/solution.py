def adj(node, edges, e_next, e_target):
    edge = edges[node]
    while edge is not None:
        yield e_target[edge]
        edge = e_next[edge]

class Solution(object):
    def build_graph(self, n, k, walls):
        flatten_n = 2 * n
        max_edges = flatten_n * 5
        latest_edge_id = 0
        edges = [None] * flatten_n
        e_next = [None] * max_edges
        e_target = [None] * max_edges
        wall = walls[0] + walls[1]

        def add_edge(x, y, edges, e_next, e_target, latest_edge_id):
            head = edges[x]
            edges[x] = latest_edge_id
            e_next[edges[x]] = head
            e_target[edges[x]] = y
            return latest_edge_id + 1

        for i in xrange(flatten_n):
            if wall[i] == 'X':
                continue
            if (i < n and i > 0) or (i < 2 * n and i > n):
                if wall[i - 1] == '-':
                    latest_edge_id = add_edge(i, i - 1, edges, e_next, e_target, latest_edge_id)
            if (i % n) + 1 < n and wall[i + 1] == '-':
                latest_edge_id = add_edge(i, i + 1, edges, e_next, e_target, latest_edge_id)
            if (i % n) + k < n and wall[(i + k + n) % (2 * n)] == '-':
                latest_edge_id = add_edge(i, (i + k + n) % (2 * n), edges, e_next, e_target, latest_edge_id)
        return flatten_n, max_edges, edges, e_next, e_target, wall

    def calc_game_points(self, n, k, walls):
        flatten_n = 2 * n
        wall = walls[0] + walls[1]
        is_game_point = [False] * flatten_n
        i = n - 1
        while wall[i] == '-' and i >= 0:
            is_game_point[i] = True
            i -= 1
        i = 2 * n - 1
        while wall[i] == '-' and i >= n:
            is_game_point[i] = True
            i -= 1
        for i in xrange(max(0, n - k), n):
            if wall[i] == '-':
                is_game_point[i] = True
        for i in xrange(max(n, 2 * n - k), 2 * n):
            if wall[i] == '-':
                is_game_point[i] = True
        return is_game_point

    def spfa(self, n, flatten_n, k, edges, e_next, e_target, is_game_point):
        dist = [float('inf')] * flatten_n
        start_node = 0
        dist[start_node] = 0
        queue_size = flatten_n * 2
        nodes_to_relax = [None] * queue_size
        head = 0
        tail = 0
        nodes_to_relax[tail] = start_node
        tail += 1
        in_nodes_to_relax = set([start_node])

        while head < tail:
            current = nodes_to_relax[head]
            head += 1
            head %= queue_size
            in_nodes_to_relax.remove(current)
            if is_game_point[current]:
                return True
            for adj_node in adj(current, edges, e_next, e_target):
                if dist[current] + 1 < (adj_node % n) + 1 and dist[current] + 1 < dist[adj_node]:
                    dist[adj_node] = dist[current] + 1
                    if adj_node not in in_nodes_to_relax:
                        nodes_to_relax[tail] = adj_node
                        tail += 1
                        tail %= queue_size
                        in_nodes_to_relax.add(adj_node)
        return False

    def read(self):
        n, k = [int(_) for _ in raw_input().split()]
        walls = [raw_input(), raw_input(), ]
        return n, k, walls

    def run(self):
        n, k, walls = self.read()
        flatten_n, max_edges, edges, e_next, e_target, wall = self.build_graph(n, k, walls)
        is_game_point = self.calc_game_points(n, k, walls)
        result = self.spfa(n, flatten_n, k, edges, e_next, e_target, is_game_point)
        print 'YES' if result else 'NO'

if __name__ == '__main__':
    Solution().run()
