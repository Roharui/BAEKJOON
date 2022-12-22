arr = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    a, b = list(map(int, i.split(" ")))
    print(a + b)