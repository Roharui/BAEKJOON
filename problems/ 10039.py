lst = [int(input()) for _ in range(5)]
c = []
for i in lst:
    if i < 40:
        c.append(40)
    else:
        c.append(i)
print(int(sum(c)/len(c)))