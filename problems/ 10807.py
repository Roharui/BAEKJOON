input()

x = map(int, input().split(" "))

n = int(input())

print(sum([1 for i in x if i == n]))