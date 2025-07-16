# Program to convert a CamelCase string to snake_case

a = input("Enter a CamelCase string: ")                    # Read the input string
count = 0                                                  # Counter to track uppercase letters
row = ""                                                   # Resulting snake_case string

for i in a:
    if i.isupper() and count == 0:                         # First uppercase letter
        row += i.lower()                                   # Convert to lowercase
        count += 1
    elif i.isupper() and count > 0:                        # Subsequent uppercase letters
        row += "_" + i.lower()                             # Add underscore before lowercase letter
        count += 1
    elif i == " ":                                         # Skip spaces
        continue
    else:
        row += i                                           # Add other characters as is

print(row)                                                  # Print the final snake_case string
