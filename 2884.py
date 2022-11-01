h, m = map(int, input().split())

if m - 45 < 0:
    m = (60 + m) - 45
    h -= 1

elif m - 45 >= 0:
    m -= 45

if h < 0:
    h += 24

print(h, m)