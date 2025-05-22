n = int(input())
count = 5

for i in range(n):
    if i == 0:
        sp = " " * (n - i - 1)
        print(sp + str(count) + " ")
    elif i == (n - 1):
        for j in range(5, 5 + n):
            print(j, end=" ")
    else:
        sp = " " * (n - i - 1)
        hsp = " " * 2 * (i - 1)
        count += 1
        print(sp + "5 " + hsp + str(int(count)))

