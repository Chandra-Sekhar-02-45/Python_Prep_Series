n = int(input())

for i in range(1, n + 1):
    sp = " " * (n - i)
    if i == 1:
        print(sp + "1")
    else:
        row = sp + "1" + " " * (2 * i - 3) + str(i)
        print(row)

for i in range(1, n):
    sp = " " * i
    if i == n - 1:
        print(sp + "1")
    else:
        row = sp + "1" + " " * (2 * (n - i - 1) - 1) + str(n - i)
        print(row)
