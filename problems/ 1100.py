lst = []
for i in range(8):
    lst.append(input())
result = 0
for num1, i in enumerate(lst):
    for num2, j in enumerate(i):
        if (num1 + num2)%2 == 0 and j == 'F':
            result += 1
print(result)