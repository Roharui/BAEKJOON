arr = []
for i in range(int(input())):
    arr.append(input())
for num, i in enumerate(arr):
    a, b = list(map(int, i.split(" ")))
    print(f"Case #{num + 1}: {a} + {b} = {a+b}")