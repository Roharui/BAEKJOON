a,b = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
result = []

for i in arr:
    for j in arr:
        for k in arr:
            if b < i + j + k or i == j or i == k or j == k : continue
            if b == i + j + k: print(b); exit()
            result.append(i + j + k)
print(max(result))