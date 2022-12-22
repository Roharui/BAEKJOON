x = int(input())

c = 0
r = 0

while x != c:
  r += 1
  while str(r).find("666") < 0: r += 1
  c += 1

print(r)