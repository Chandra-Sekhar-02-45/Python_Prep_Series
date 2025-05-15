m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))
count = 0

for i in range(m) :
    for j in range(n) :
        count += 1
        print(count , end = " ")
    print()


