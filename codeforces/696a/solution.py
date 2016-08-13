import sys
import math


def count_of_bits(num):
    #return int(math.floor(math.log(num) / math.log(2))) + 1
    return len(bin(num))

def is_binary_presentation_prefix(prefix, num):
    if prefix > num:
        return False
    len_prefix = count_of_bits(prefix)
    len_num = count_of_bits(num)
    return (num >> (len_num - len_prefix)) == prefix

def make_path(u, v):
    current = u
    path = []
    while not is_binary_presentation_prefix(current, v):
        path.append(current)
        current = current >> 1
    path.append(current)

    current = v
    path_rev = []
    while not is_binary_presentation_prefix(current, u):
        path_rev.append(current)
        current = current >> 1
    path_rev.reverse()

    return path + path_rev

def process(inp, prices):
    if inp[0] == 1:
        # add weight
        op, u, v, w = inp
        path = make_path(u, v)
        for i in xrange(len(path) - 1):
            ends = sorted([path[i], path[i + 1]])
            key = str('-'.join([str(_) for _ in ends]))
            if key in prices:
                prices[key] += w
            else:
                prices[key] = w
    if inp[0] == 2:
        op, u, v = inp
        path = make_path(u, v)
        ans = 0
        for i in xrange(len(path) - 1):
            ends = sorted([path[i], path[i + 1]])
            key = str('-'.join([str(_) for _ in ends]))
            ans += prices[key] if key in prices else 0
        print(ans)

# Testing
DEBUG = len(sys.argv) >= 2 and sys.argv[1] == 'debug'
def d(msg):
    global DEBUG
    if DEBUG:
        print(msg)
if DEBUG:
    assert count_of_bits(4) == 3
    assert count_of_bits(8) == 4
    assert count_of_bits(15) == 4
    assert count_of_bits(16) == 5
    assert is_binary_presentation_prefix(1, 4)
    assert is_binary_presentation_prefix(3, 12)
    assert not is_binary_presentation_prefix(3, 4)
    assert make_path(3, 4) == [3, 1, 2, 4]
    assert make_path(6, 4) == [6, 3, 1, 2, 4]
    assert make_path(4, 4) == [4]
    assert make_path(4, 1) == [4, 2, 1]
    d('test passed')


n = int(raw_input())
prices = {}
for _ in xrange(n):
    inp = [int(_) for _ in raw_input().split()]
    process(inp, prices)
