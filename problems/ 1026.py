lst = []
for i in range(3):
    lst.append(input())
a = sorted(list(map(int, lst[1].split(" "))), reverse=True)
b = sorted(list(map(int, lst[2].split(" "))))
result = 0
for i in range(len(a)):
    result += (a[i] * b[i])
print(result)