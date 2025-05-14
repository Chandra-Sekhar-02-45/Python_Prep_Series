n = int(input("Enter the number of rows for the star pyramid: "))

for i in range(n):
    sp = " " * (n - i - 1)
    print(sp, end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()
