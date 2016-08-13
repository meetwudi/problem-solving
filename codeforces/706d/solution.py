import sys
import math


def get_bit(num, position, wide = 1):
    """
        get_bit(0b00001, 1) == 1
        get_bit(0b00010, 2) == 1
    """
    return (num >> (position - wide)) & ((1 << wide) - 1)


class DNode(object):
    def __init__(self, count=0, bits_group=1):
        self.childs = [None] * (1 << bits_group)
        self.count = count
        self.num = None

    @property
    def valid(self):
        return self.count > 0


class DTree(object):
    def __init__(self):
        self.DIGIT_LEN = 30
        self.BITS_GROUP = 5
        self.root = DNode(bits_group=self.BITS_GROUP)

    def num_exists(self, num):
        current_node = self.root
        for i in xrange(self.DIGIT_LEN, 0, -self.BITS_GROUP):
            digit = get_bit(num, i, self.BITS_GROUP)
            if current_node.childs[digit] is None or not current_node.childs[digit].valid:
                return False
            current_node = current_node.childs[digit]
        return True

    def insert(self, num):
        current_node = self.root
        current_node.count += 1
        for i in xrange(self.DIGIT_LEN, 0, -self.BITS_GROUP):
            digit = get_bit(num, i, self.BITS_GROUP)
            if current_node.childs[digit] is None:
                current_node.childs[digit] = DNode(bits_group=self.BITS_GROUP)
            current_node = current_node.childs[digit]
            current_node.count += 1

    def remove(self, num):
        current_node = self.root
        current_node.count -= 1
        for i in xrange(self.DIGIT_LEN, 0, -self.BITS_GROUP):
            digit = get_bit(num, i, self.BITS_GROUP)
            next_node = current_node.childs[digit]
            next_node.count -= 1
            current_node = next_node

    def find_max(self, mask):
        current_node = self.root
        num = 0
        for i in xrange(self.DIGIT_LEN, 0, -self.BITS_GROUP):
            digit_mask = get_bit(mask, i, self.BITS_GROUP)
            for masked_trial in xrange((1 << self.BITS_GROUP) - 1, -1, -1):
                trial = masked_trial ^ digit_mask
                if (current_node.childs[trial] is not None and
                        current_node.childs[trial].valid):
                    num = (num << self.BITS_GROUP) + masked_trial
                    current_node = current_node.childs[trial]
                    break
        return num


class Solution(object):
    def run(self):
        tree = DTree()
        tree.insert(0)
        n = int(raw_input())
        for _ in xrange(n):
            op, num = raw_input().split()
            num = int(num)
            if op == '+':
                tree.insert(num)
            if op == '-':
                tree.remove(num)
            if op == '?':
                print(tree.find_max(num))


class Test(object):
    def run_test(self):
        self.test_insert()
        self.test_remove()
        self.test_find_max()

    def test_insert(self):
        tree = DTree()
        tree.insert(10)
        tree.insert(9)
        assert tree.num_exists(10)
        assert tree.num_exists(9)
        print('test_insert passed')

    def test_remove(self):
        tree = DTree()
        assert not tree.num_exists(10)
        tree.insert(10)
        assert tree.num_exists(10)
        tree.remove(10)
        assert not tree.num_exists(10)
        print('test_remove passed')

    def test_find_max(self):
        tree = DTree()
        tree.insert(3)
        tree.insert(0)
        assert tree.find_max(3) == 3
        print('test_find_max passed')

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'profile':
        import cProfile
        cProfile.run('Solution().run()')
    elif len(sys.argv) == 2 and sys.argv[1] == 'test':
        Test().run_test()
    else:
        Solution().run()

