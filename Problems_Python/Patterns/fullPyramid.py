n = int(input())

for i in range(1, n + 1):
    count = 1
    if i == 1:
        sp = " " * (n - 1)
        print(sp + "1")
    else:
        sp = " " * (n - i)
        print(sp, end="")
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()




