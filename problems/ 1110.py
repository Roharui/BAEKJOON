a = int(input())
aa = a
t = int(aa/10)
o = aa%10
aa = o * 10 + (t + o)%10
num = 1
while aa != a:
    t = int(aa/10)
    o = aa%10
    aa = o * 10 + (t + o)%10
    num += 1
print(num)