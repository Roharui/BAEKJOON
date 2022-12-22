arr = []
result = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    c = list(filter(lambda x: bool(len(x)), i.split("X")))
    an = 0
    for j in c:
        an += sum(list(range(1, len(j) + 1)))
    result.append(an)
for i in result:
    print(i)        