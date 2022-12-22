
arr = []
for i in range(int(input())):
    h, w, n = map(int, input().split(' '))
    x = n%h
    if x == 0:
        x = h
    y = int((n - x)/h) + 1

    arr.append(f'{x}{y:02}')

for i in arr:
    print(i)