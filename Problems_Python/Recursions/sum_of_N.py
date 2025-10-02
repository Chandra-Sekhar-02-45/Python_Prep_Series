# Question: Find the sum of first n natural numbers using recursion.
#
# Constraints:
# 1 <= n <= 10^4

def sumN(n, total):
    # Base case: when n reaches 0, return accumulated sum
    if n <= 0:
        return total

    # Add current n to total
    total += n

    # Recursive call with smaller n
    return sumN(n - 1, total)


# --- Main driver code ---
n = int(input("Enter n: "))
print("Sum of first", n, "natural numbers is:", sumN(n, 0))

"""
Time Complexity: O(n)
    - Each number from n → 1 is processed once.
Space Complexity: O(n)
    - Due to recursive call stack of depth n.

Mathematical Optimization:
    - Formula = n * (n + 1) // 2
    - This gives O(1) time and O(1) space.
"""
