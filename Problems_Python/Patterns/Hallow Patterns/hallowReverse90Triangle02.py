n = int(input())
count = (n * (n + 1)) // 2

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        if i == 1 or j == 1 or j == (n - i + 1):
            print(count, end=" ")
        else:
            print(" ", end=" ")
        count -= 1
    print()
