five = 0; three = 0
a = int(input())
aa = a
while True:
    if aa < five * 5:
        break
    five += 1
while aa - (five * 5) - (three * 3) != 0:
    if five == 0:
        five = -1
        three = 0
        break
    five -= 1
    while aa > five * 5 + three * 3:
        three += 1
print(five + three)
