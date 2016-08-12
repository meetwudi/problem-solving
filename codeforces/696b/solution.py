import sys


def readline_int(delta=0, is_list=False):
    result = [int(i) + delta for i in raw_input().split()]
    if len(result) == 1 and not is_list:
        return result[0]
    return result

def print_list(l):
    len_l = len(l)
    for idx, item in enumerate(l):
        sys.stdout.write(str(item))
        if idx != len_l - 1:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

class Solution(object):
    def prepare(self):
        self.n = readline_int()
        if self.n == 1:
            return False
        self.p = readline_int(delta=-1, is_list=True)
        self.p.insert(0, -1)
        self.childs = [None] * self.n
        self.result = [0] * self.n
        self.treesize = [1] * self.n
        for i in xrange(self.n):
            self.childs[i] = []
        for idx, parent in enumerate(self.p[1:]):
            self.childs[parent].append(idx + 1)
        return True

    def calc_treesize(self):
        stack = [self.ROOT]
        cursor = 0
        while cursor < len(stack):
            current = stack[cursor]
            cursor += 1
            for child in self.childs[current]:
                stack.append(child)
        cursor -= 1
        while cursor >= 0:
            current = stack[cursor]
            cursor -= 1
            parent = self.p[current]
            if parent != -1:
                self.treesize[parent] += self.treesize[current]

    def calc_result(self, current):
        parent = self.p[current]
        siblings_sizesum = self.treesize[parent] - 1 - self.treesize[current]
        siblings_count = len(self.childs[parent]) - 1
        parent_expectation = self.result[parent]
        result_current = (siblings_sizesum + 2 * parent_expectation) / 2.0 + 1.0
        return result_current

    def solve(self):
        self.result[self.ROOT] = 1.0
        stack = [_ for _ in self.childs[self.ROOT]]
        cursor = 0
        while cursor < len(stack):
            current = stack[cursor]
            cursor += 1
            self.result[current] = self.calc_result(current)
            for child in self.childs[current]:
                stack.append(child)

    def run(self):
        self.ROOT = 0

        if not self.prepare():
            return print_list([1.0])
        self.calc_treesize()
        self.solve()
        print_list(self.result)

if __name__ == '__main__':
    Solution().run()

