# Take the input for number of levels
n = int(input("Enter the number of levels (n): "))

# Start with ASCII value of 'A'
m = ord('A')

# Top half of the pattern (including the middle row)
for i in range(1, n + 1):
    space = " " * (n - i)  # Leading spaces

    if i == 1:
        # First row has only one letter (A)
        print(space + chr(m))
    else:
        m += 1  # Move to next alphabet
        inner_space = " " * ((2 * i) - 3)  # Space between two letters
        print(space + chr(m) + inner_space + chr(m))

# Bottom half of the pattern
for i in range(1, n):
    space = " " * i  # Leading spaces
    m -= 1  # Go back to previous alphabet

    if i == (n - 1):
        # Last row has only one letter
        print(space + chr(m))
    else:
        inner_space = " " * (2 * (n - i - 1) - 1)  # Inner space
        print(space + chr(m) + inner_space + chr(m))
