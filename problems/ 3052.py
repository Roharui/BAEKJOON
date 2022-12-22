arr = []
result = []
for i in range(10):
    arr.append(int(input()))
arr = list(map(lambda x: x%42, arr))
print(len(set(arr)))
