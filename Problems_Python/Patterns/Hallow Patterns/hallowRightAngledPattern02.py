n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == n:
            print(n - j + 1, end=" ")
        elif i + j == n + 1:
            print(i, end=" ")
        elif j == n:
            print(1, end=" ")
        else:
            print(" ", end=" ")
    print()
