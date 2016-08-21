def adj(node, edges, e_next, e_target, e_length):
    edge = edges[node]
    while edge is not None:
        yield e_target[edge], e_length[edge]
        edge = e_next[edge]

class Solution(object):
    def build_graph(self, n, m, k):
        num_edges = m * 2
        edges = [None] * (n + 1)
        e_length = [None] * num_edges
        e_next = [None] * num_edges
        e_target = [None] * num_edges
        latest_edge_id = 0
        storages = []

        def add_edge(x, y, length, edges, e_next, e_target, e_length, latest_edge_id):
            head = edges[x]
            edges[x] = latest_edge_id
            e_next[edges[x]] = head
            e_target[edges[x]] = y
            e_length[edges[x]] = length
            return latest_edge_id + 1

        for i in xrange(m):
            x, y, length = [int(_) for _ in raw_input().split()]
            latest_edge_id = add_edge(x, y, length, edges, e_next, e_target, e_length, latest_edge_id)
            latest_edge_id = add_edge(y, x, length, edges, e_next, e_target, e_length, latest_edge_id)

        storages = [int(_) for _ in raw_input().split()]

        return edges, e_length, e_next, e_target, storages


    def spfa(self, n, edges, e_next, e_target, e_length, storages):
        answer = float('inf')
        storages_set = set(storages)
        for storage in storages:
            for adj_node, length in adj(storage, edges, e_next, e_target, e_length):
                if adj_node in storages_set:
                    continue
                answer = min(answer, length)
        return -1 if answer == float('inf') else answer


    def run(self):
        n, m, k = [int(_) for _ in raw_input().split()]
        if k == 0:
            print -1
        else:
            edges, e_length, e_next, e_target, storages = self.build_graph(n, m, k)
            result = self.spfa(n + 1, edges, e_next, e_target, e_length, storages)
            print result

if __name__ == '__main__':
    Solution().run()
