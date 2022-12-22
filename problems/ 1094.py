x = int(input())
stick = [64]
trash = []
while sum(stick) != x:
    s = stick.pop(stick.index(min(stick)))
    stick.append(int(s/2))
    trash.append(int(s/2))
    if x > sum(stick):
        stick.append(trash.pop(trash.index(min(trash))))
print(len(stick))