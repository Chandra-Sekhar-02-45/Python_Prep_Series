# Defination
# An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits in the number.

# Taught On Approach:
            # Input the upper limit n:
            # Start a loop from 1 to n:
            # Convert number to string:
            # Count the length of numbers (k):
            # Initialize a sum variable (temp_sum):
            # Loop through each digit in the number:
            # Raise the digit to the power of k:
            # Add the result to the sum variable:
            # If the sum is equal to the original number, it’s an Armstrong number.


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    a = str(i)
    k = len(a)
    temp_sum = 0
    for j in a:
        temp_sum += int(j) ** k
    if temp_sum == i:
        print(i)

