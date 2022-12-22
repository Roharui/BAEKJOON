a, b = map(int, input().split(" "))

def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

g = GCD(a,b)

print(g, (a*b)//g)   #60