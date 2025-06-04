s = int(input())
n = int(input())
count = (n * (n + 1) // 2) + s - 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == j or j == n:
            print(count, end=" ")
            count -= 1
        elif j < i:
            print("  ", end="")
        else:
            print(" ", end=" ")
            count -= 1
    print()

