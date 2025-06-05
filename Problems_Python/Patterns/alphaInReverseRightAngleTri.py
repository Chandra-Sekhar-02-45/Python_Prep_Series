n = int(input())
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, n + 1):
    row = ""
    for j in range(n - i + 1):
        row += string[j] + " "
    print(row)
