stack = []
cmds = []

for i in range(int(input())):
  cmds.append(input())

for i in cmds:
  ip = i.split(" ")
  cmd = ip[0]
  if cmd == "push":
    stack.append(ip[1])
  elif cmd == "pop":
    if len(stack) == 0: print(-1)
    else: print(stack.pop())
  elif cmd == "top":
    if len(stack) == 0: print(-1)
    else: print(stack[-1])
  elif cmd == "size":
    print(len(stack))
  elif cmd == "empty":
    print(int(len(stack) == 0))