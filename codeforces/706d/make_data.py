import random

n = 200000
nums = []
print(n)
for _ in xrange(n):
    choice = random.randint(0, 16)
    if choice < 10 or len(nums) == 0:
        # insert
        num = random.randint(500000000, 1000000000)
        nums.append(num)
        print('+ {0}'.format(num))
    elif choice < 15:
        # remove
        pos = random.randint(0, len(nums) - 1)
        num = nums.pop(pos)
        print('- {0}'.format(num))
    else:
        mask = random.randint(0, 100)
        print('? {0}'.format(mask))


