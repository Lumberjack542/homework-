def degree(d):
    n = 0
    str1 = ''
    for i in range(1, 1000000):
        str1 += str(i) + " "
    str1 = str1.split()
    for i in str1:
        c = 0

        for j in i:
            c += int(j) ** d
        if c == int(i):
            n += int(i)
    return n - 1


deg = int(input('enter degree:'))

print(degree(deg))
