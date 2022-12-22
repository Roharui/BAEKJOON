arr = []
for i in range(int(input())):
    arr.append(input().split(" "))

for i in arr:
    num = int(i[0])
    for j in i[1]:
        for _ in range(num):
            print(j, end='')
    print()