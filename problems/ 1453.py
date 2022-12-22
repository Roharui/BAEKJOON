input()
arr = list(map(int, input().split(" ")))
result = 0
lst = []
for i in arr:
    if i in lst:
        result += 1
    else:
        lst.append(i)
print(result)