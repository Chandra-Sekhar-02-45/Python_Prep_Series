m = int(input())
n = int(input())
count = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i == 1 or i == m or j == 1:
            count += 1
            print(count, end=" ")
        elif j == n:
            count += n - 1
            print(count, end=" ")
        else:
            print(" ", end=" ")
    print()
