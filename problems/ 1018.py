n, m = map(int, input().split(" "))

n_, m_ = n - 7, m - 7

x = [input() for _ in range(n)]
boardX = list("WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW")
boardY = list("BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB")

result = 64

for i in range(n_):
  for j in range(m_):
    r = ""
    for k in range(8):
      r += x[i + k][j:j+8]
    
    xr = sum([1 for b1, b2 in zip(boardX, r) if b1 != b2])
    yr = sum([1 for b1, b2 in zip(boardY, r) if b1 != b2])

    result = min(xr, yr, result)

print(result)