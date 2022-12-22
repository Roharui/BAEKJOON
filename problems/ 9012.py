def V_input():
    result = []
    for _ in range(int(input())):
        tmp = input()
        result.append(tmp)
    return result

v = V_input()

for i in v:
    h = []
    for j in i:
        if not h: h.append(j); continue
        if h[-1] == '(' and j == ')': h.pop()
        else: h.append(j)

    if len(h) != 0: print('NO')
    else : print('YES')