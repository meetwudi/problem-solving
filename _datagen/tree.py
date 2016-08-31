# This script generates a tree
#
# Usage: tree.py n
#
# Args
# n: Number of nodes in the tree. A tree with n nodes has exactly n - 1 edges. Nodes are numbered from 0 to n - 1.
#

import sys
import random
import argparse


class TreeGen(object):
    def __init__(self, n, weighted, base=0):
        self.base = base
        self.n = n
        self.weighted = weighted

    def generate(self):
        nodes = range(self.n)
        random.shuffle(nodes)

        edges = []
        for ch_idx in xrange(1, self.n):
            parent_idx = random.randint(0, ch_idx - 1)
            if self.weighted:
                weight = random.randint(0, 100)
                edges.append((ch_idx, parent_idx, weight,))
            else:
                edges.append((ch_idx, parent_idx, ))

        return edges

    def print_tree(self, edges):
        print(self.n)
        for edge in edges:
            if self.weighted:
                print("{0} {1} {2}".format(edge[0], edge[1], edge[2]))
            else:
                print("{0} {1}".format(edge[0], edge[1]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate a nice tree.")
    parser.add_argument("n", type=int, help="Number of nodes")
    parser.add_argument("--weighted", type=bool, help="Is three weighted", default=False)
    args = parser.parse_args()

    gen = TreeGen(
        n=int(args.n),
        weighted=args.weighted)
    gen.print_tree(gen.generate())

