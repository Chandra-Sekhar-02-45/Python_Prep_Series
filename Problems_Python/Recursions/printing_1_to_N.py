# Question: Print numbers from 1 to n using recursion.
#
# Constraints:
# 1 <= n <= 10^4

def printN(i, n):
    # Base case: stop when i exceeds n
    if i > n:
        return

    # Print current number
    print(i)

    # Recursive call for the next number
    printN(i + 1, n)


# --- Main driver code ---
# Asking user for input
n = int(input("Enter n: "))

# Start recursion from 1
printN(1, n)

"""
Time Complexity: O(n)
    - Each number from 1 to n is printed once.
Space Complexity: O(n)
    - Due to recursive function calls in the call stack.

Optimization:
    - Use an iterative loop (for/while) to reduce space complexity to O(1).
"""
