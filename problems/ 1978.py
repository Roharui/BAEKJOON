input()
arr = list(map(int, input().split(" ")))

def ispn(num):
    if num == 1:
        return 0
    for i in range(2, num):
        if num%i == 0:
            return 0
    return 1

result = 0
for i in arr:
    result += ispn(i)
print(result)