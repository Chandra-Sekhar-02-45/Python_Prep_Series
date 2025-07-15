# Program to find the maximum number in a list of integers

n = int(input("Enter the number of elements: "))          # Input total number of elements
arr = list(map(int, input("Enter the numbers: ").split()))  # Read the list of integers

num = arr[0]                                              # Assume the first element is the maximum

for i in arr:                                             # Loop through all elements in the array
    if i > num:                                           # If current element is greater than current max
        num = i                                           # Update the maximum value

print(num)                                                # Print the maximum value
