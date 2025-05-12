n = int(input())

for i in range(n):
    for j in range(n):
        print("* ", end="") # Print '* ' without newline
    print()                   # After each row, move to next line
