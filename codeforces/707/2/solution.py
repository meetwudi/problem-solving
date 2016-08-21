n = int(raw_input())

if n < 3:
    print -1
elif n % 2 != 0:
    c = ((n ** 2) + 1) / 2
    b = c - 1
    print c, b
else:
    c = (n ** 2) / 4 + 1
    b = c - 2
    print c, b
