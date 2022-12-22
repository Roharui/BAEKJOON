a = input().upper()

arr = []
for i in set(a):
    tmp = [i, 0]
    for j in a:
        if i == j:
            tmp[1] += 1
    arr.append(tmp)

arr = sorted(arr, key=lambda x: x[1], reverse=True)
if len(arr) >= 2 and arr[0][1] == arr[1][1]:
    print("?")
else:
    print(arr[0][0])