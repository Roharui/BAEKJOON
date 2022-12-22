a = input()
result = [-1] * 26
for i in a:
    result[ord(i) - 97] = a.index(i)
for i in result:
    print(i, end=' ')