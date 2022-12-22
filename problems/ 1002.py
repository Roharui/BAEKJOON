lst = []
for i in range(int(input())):
    lst.append(input())
for i in lst:
    arr = [int(j) for j in i.split(" ")]
    x1, y1, r1, x2, y2, r2 = arr
    rsum = r1 + r2
    rsub = abs(r1 - r2)
    x = abs(x1 - x2) ** 2
    y = abs(y1 - y2) ** 2
    rr = (x + y) ** 0.5
    if rr == 0 and r1 == r2:
        print(-1)
    elif rsub < rr and rr < rsum:
        print(2)
    elif rr == rsum or rr == rsub:
        print(1)
    elif rr > rsum or rr < rsub:
        print(0)
    else:
        print(2)