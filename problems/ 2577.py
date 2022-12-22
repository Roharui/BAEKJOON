a = 1
result = []
r = [0] * 10
for i in range(3):
    a *= int(input())
while a != 0:
    result.append(a%10)
    a = int(a/10)
for i in result:
    r[i] += 1
for i in r:
    print(i)