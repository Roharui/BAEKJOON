import sys

a = int(sys.stdin.readline().strip())

for i in range(a):
  print(sum(map(int, sys.stdin.readline().strip().split(" "))))