inputs = []

while True:
  x = list(map(int, input().split(" ")))
  if sum(x) <= 0: break
  inputs.append(x)

for i in inputs:
  c = max(i)
  i.remove(c)
  a, b = i
  if a ** 2 + b ** 2 == c ** 2:
    print("right")
  else:
    print("wrong")