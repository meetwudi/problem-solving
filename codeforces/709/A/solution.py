import math

n, b, d = [int(_) for _ in raw_input().split()]
ans = 0
accu = 0

a = [int(_) for _ in raw_input().split()]
for i in xrange(n):
    if a[i] > b:
        continue
    accu += a[i]
    if accu > d:
        accu = 0
        ans += 1

print(ans)

