stack = []

for _ in range(int(input())):
  x = int(input())

  if x == 0:
    if len(stack) != 0:
      stack.pop()
  else:
    stack.append(x)

print(sum(stack))