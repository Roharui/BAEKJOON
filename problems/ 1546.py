input()
a = list(map(int, input().split(" ")))

mx = max(a)

c = list(map(lambda x: x/mx*100, a))
print(round(sum(c)/len(c), 6))