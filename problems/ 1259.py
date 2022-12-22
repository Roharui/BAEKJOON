x = []

while True:
  i = input()
  if i == "0": break
  x.append(i)

for i in x:
  print("yes" if i == i[::-1] else "no")