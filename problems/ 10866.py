stack = []
cmds = []

for i in range(int(input())):
  cmds.append(input())

for i in cmds:
  ip = i.split(" ")
  cmd = ip[0]
  if cmd == "push_back":
    stack.append(ip[1])
  if cmd == "push_front":
    stack.insert(0, ip[1])
  elif cmd == "pop_front":
    if len(stack) == 0: print(-1)
    else: print(stack.pop(0))
  elif cmd == "pop_back":
    if len(stack) == 0: print(-1)
    else: print(stack.pop())
  elif cmd == "front":
    if len(stack) == 0: print(-1)
    else: print(stack[0])
  elif cmd == "back":
    if len(stack) == 0: print(-1)
    else: print(stack[-1])
  elif cmd == "size":
    print(len(stack))
  elif cmd == "empty":
    print(int(len(stack) == 0))