import sys
n = 200000
print(n)

for i in xrange(n - 1):
    sys.stdout.write(str(i + 2))
    sys.stdout.write(' ')
sys.stdout.write('1\n')
