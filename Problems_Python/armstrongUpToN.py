# Defination
# An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits in the number.

# Taught On Approach:

n = int(input("Enter a number: "))     # Input the upper limit n:

for i in range(1, n + 1):              # Start a loop from 1 to n:
    a = str(i)                         # Convert number to string:
    k = len(a)                         # Count the length of numbers (k):
    temp_sum = 0                       # Initialize a sum variable (temp_sum):
    for j in a:                        # Loop through each digit in the string a, which represents the number.
        temp_sum += int(j) ** k        # Raise the digit to the power of k & Add the result to the sum variable:
                
    if temp_sum == i:                  # If the sum is equal to the original number, it’s an Armstrong number.
        print(i)

