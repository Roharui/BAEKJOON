arr = []
while True:
    a = input()
    if a == "0 0":
        break
    arr.append(a)
for i in arr:
    a, b = list(map(int, i.split(" ")))
    print(a + b)