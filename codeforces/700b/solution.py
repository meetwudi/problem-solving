import math


def readline_ints(delta=0):
    return [int(i) + delta for i in raw_input().split()]

def accumulate(node, prev, targets, usts, k):
    answer = 0
    n_usts = 0

    for target in targets[node]:
        if (target == prev):
            continue
        answer_target, n_usts_target = accumulate(target, node, targets, usts, k)
        answer += answer_target
        answer += min(n_usts_target, 2 * k - n_usts_target)
        n_usts += n_usts_target

    if node in usts:
        n_usts += 1

    return (answer, n_usts, )


n, k = readline_ints()
usts = set(readline_ints(delta=-1)) # universities
targets = [None] * n
n_usts = [0] * n

for i in xrange(n):
    targets[i] = []

for _ in xrange(n - 1):
    x, y = readline_ints(delta=-1)
    targets[x].append(y)
    targets[y].append(x)

answer, _ = accumulate(0, prev=-1, targets=targets, usts=usts, k=k)
print(answer)

