a = int(input())

def c(num):
    arr = []
    while num != 0:
        arr.append(num%10)
        num = int(num/10)
    if len(arr) <= 2:
        return 1
    h = arr[0] - arr[1]
    for i in range(1, len(arr)-1):
        if arr[i] - arr[i + 1] != h:
            return 0
    return 1

result = 0
for i in range(1, a + 1):
    result += c(i)

print(result)

