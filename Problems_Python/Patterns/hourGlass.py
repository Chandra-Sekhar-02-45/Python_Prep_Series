# Program to print an hourglass or double-triangle star pattern of height n

n = int(input("Enter the height of the pattern (n): "))         # Read the height of the pattern

# Upper inverted triangle
for i in range(1, n + 1):
    star = "* " * (n - i + 1)                                   # Create stars decreasing each row
    space = " " * (i - 1)                                       # Leading spaces increase each row
    row = space + star                                          # Combine spaces and stars
    print(row)                                                  # Print the row

# Lower normal triangle
for i in range(1, n):
    star = "* " * (i + 1)                                       # Create stars increasing each row
    space = " " * (n - i - 1)                                   # Leading spaces decrease each row
    row = space + star                                          # Combine spaces and stars
    print(row)                                                  # Print the row
