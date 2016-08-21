import math
import fractions

def is_square_num(gg):
    return abs(math.pow(math.sqrt(gg), 2) - gg) < 1e-6

n = 10000
exists = set()
for i in xrange(1, n):
    for j in xrange(i, n):
        k = int(math.pow(i, 2) + math.pow(j, 2))
        if not is_square_num(k):
            continue
        gcd = fractions.gcd(k, fractions.gcd(i, j))
        tup = (i / gcd, j / gcd, k / gcd)
        if tup not in exists:
            exists.add(tup)
            print tup

