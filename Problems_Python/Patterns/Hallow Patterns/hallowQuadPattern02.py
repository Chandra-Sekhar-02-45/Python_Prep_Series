n = int(input())

for i in range(1, n + 1):
    if i == 1 or i == n:
        for j in range(1, n + 1):
            print(n - j + 1, end=" ")
    else:
        for j in range(1, n + 1):
            if j == 1:
                print(n, end=" ")
            elif j == n:
                print(1, end=" ")
            else:
                print(" ", end=" ")
    print()
