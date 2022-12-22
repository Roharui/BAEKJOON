arr = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    c = list(map(int, i.split(" ")))
    avg = sum(c[1:])/c[0]
    aaa = sum([int(i > avg) for i in c[1:]]) / c[0]
    print('{0:0.3f}%'.format(aaa * 100))
