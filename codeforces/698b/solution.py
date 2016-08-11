import itertools
import sys


def readline_int(delta=0):
    return [int(i) + delta for i in raw_input().split()]

class Solution(object):
    def find(self, ident, fa):
        root = ident
        while fa[root] != root:
            root = fa[root]
        cursor = ident
        while cursor != root:
            fa_cursor = fa[cursor]
            fa[cursor] = root
            cursor = fa_cursor
        return root

    def merge(self, ident_child, ident_father, fa):
        fa_child = self.find(ident_child, fa)
        fa_father = self.find(ident_father, fa)
        fa[fa_child] = fa_father

    def solve(self):
        n = self.n
        p = self.p
        issues = []
        roots = []
        fa = [i for i in xrange(n)]

        for current in xrange(n):
            parent = p[current]
            if parent == current:
                roots.append(current)
                continue

            parent_set_id = self.find(parent, fa)
            if parent_set_id == current:
                issues.append(current)
                continue

            self.merge(current, parent, fa)

        root = None
        changes = 0
        if len(roots) > 0:
            root = roots[0]
            changes = len(roots) + len(issues) - 1
        elif len(roots) == 0:
            root = roots[0] if len(roots) > 0 else issues[0]
            changes = len(roots) + len(issues)

        for ident in itertools.chain(roots, issues):
            p[ident] = root

        return (changes, p, )

    def read_data(self):
        self.n = readline_int()[0]
        self.p = readline_int(delta=-1) # make sure to restore index while printing result

    def print_result(self, result):
        changes, p = result
        print(changes)
        for idx, parent in enumerate(p):
            sys.stdout.write(str(parent + 1))
            if idx != len(p) - 1:
                sys.stdout.write(' ')
        sys.stdout.write('\n')


    def run(self):
        self.read_data()
        result = self.solve()
        self.print_result(result)

if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1], 'r')
    print('Redirect stdin to {0}'.format(sys.argv[1]))

Solution().run()

