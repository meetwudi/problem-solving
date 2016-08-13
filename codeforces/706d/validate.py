n = int(raw_input())
nums = [0]
for _ in xrange(n):
    op, num = raw_input().split()
    num = int(num)
    if op == '+':
        nums.append(num)
    if op == '-':
        chosen = None
        for idx, idx_num in enumerate(nums):
            if idx_num == num:
                chosen = idx
                break
        nums.pop(chosen)
    if op == '?':
        max_xor = nums[0] ^ num
        for idx_num in nums:
            max_xor = max(max_xor, idx_num ^ num)
        print(max_xor)

