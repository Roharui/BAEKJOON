a = int(input())
c = 1

for i in range(a):
    for j in range(2):
        for k in range(a):
            if c == 1:
                print("*",end='')
            else:
                print(" ",end='')
            c *= -1
        if a%2 == 0:
            c *= -1
        print()