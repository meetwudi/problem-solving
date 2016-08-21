n, m = [int(_) for _ in raw_input().split()]
has_other_color = False
for i in xrange(n):
    colors = raw_input().split()
    for color in colors:
        if color != 'W' and color !='B' and color != 'G':
            has_other_color = True

if has_other_color:
    print '#Color'
else:
    print '#Black&White'
