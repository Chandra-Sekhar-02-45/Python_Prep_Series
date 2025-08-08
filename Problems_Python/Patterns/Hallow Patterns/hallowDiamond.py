# Take the number of rows for the Hallow Diamond
n = int(input("Enter the number of levels (n): "))

# Upper half of the pattern
for i in range(1, n + 1):
    row = ""
    space = " " * (4 * (i - 1))  # Middle space increases with each row

    if i == 1:
        # First row: 2n stars with no gap
        print("* " * (2 * n))
    else:
        # Stars on both sides with growing space in middle
        stars = "* " * (n - i + 1)
        row = stars + space + stars
        print(row)

# Lower half of the pattern
for i in range(1, n + 1):
    row = ""
    space = " " * (4 * (n - i))  # Middle space decreases with each row

    if i == n:
        # Last row: 2n stars again
        print("* " * (2 * n))
    else:
        # Stars on both sides with shrinking space in middle
        stars = "* " * i
        row = stars + space + stars
        print(row)
