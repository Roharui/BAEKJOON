h, m = list(map(int, input().split(" ")))
m -= 45
if m < 0:
    m = 60 - abs(m)
    h -= 1
if h < 0:
    h = 23
print(f'{h} {m}')