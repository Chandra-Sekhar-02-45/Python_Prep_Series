# Question: Print numbers from n down to 1 using recursion.
#
# Constraints:
# 1 <= n <= 10^4

def printN(n):
    # Base case: when n reaches 0, stop recursion
    if n == 0:
        return

    # Print current number
    print(n)

    # Recursive call with smaller value
    printN(n - 1)


# --- Main driver code ---
# Asking user for input
n = int(input("Enter n: "))

# Start recursion
printN(n)

"""
Time Complexity: O(n)
    - Each number is printed once.
Space Complexity: O(n)
    - Recursive calls add up to n frames in the call stack.

Optimization:
    - Iterative approach (using a loop) reduces space to O(1).
"""
