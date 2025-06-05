n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n or i == 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, n):
    for j in range(1, n + 1):
        if i == n - 1 or j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


