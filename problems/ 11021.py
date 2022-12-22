lst = []
for i in range(int(input())):
    lst.append(input())
for num, i in enumerate(lst):
    a, b = list(map(int, i.split(" ")))
    print(f"Case #{num+1}: {a+b}")