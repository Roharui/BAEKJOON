arr = list(map(int, input().split(" ")))

num = min(arr)

while True:
    c = 0
    for i in arr:
        if num%i == 0:
            c += 1
    if c >= 3:
        break
    num += 1
print(num)
