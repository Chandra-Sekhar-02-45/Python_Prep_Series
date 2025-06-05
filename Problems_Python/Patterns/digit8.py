n = int(input())

for i in range(1, 2 * n + 2):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or j == n or i == (n + 1) or i == (2 * n + 1):
            print("* ", end="")
        else:
            print(" ", end=" ")
    print()

