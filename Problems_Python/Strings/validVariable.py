#  Check if a String is a Valid Python Identifier (Without Using isidentifier())

s = input("Enter a variable: ")
flag = True

# Loop through each character in the string
for i in range(len(s)):
    # Check if the character is a valid letter, digit, or underscore
    valid = (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57) or (ord(s[i]) == 95)

    # Conditions that make the string invalid:
    # 1. Starts with a digit
    # 2. Contains a space
    # 3. Contains any character that is not valid

    if (ord(s[0]) >= 48 and ord(s[0]) <= 57) or s[i] == " " or not valid:
        flag = False
        break

# Output the result
print(flag)
