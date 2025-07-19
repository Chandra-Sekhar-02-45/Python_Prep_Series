# Problem: Given an NxN matrix, calculate the sum of a submatrix from (i, j) to (k, l)

n = int(input("Enter the size of the square matrix (n): "))                    # Input matrix size
i, j, k, l = map(int, input("Enter i, j, k, l (submatrix boundaries): ").split())  # Input submatrix corners

matrix = []                                                                   # Initialize matrix
print("Enter the matrix row by row:")
for row_num in range(n):
    row = list(map(int, input().split()))                  # Input row
    matrix.append(row)                                                       # Append to matrix

# Optional: print the matrix for confirmation
print("\nMatrix:")
for row in matrix:
    print(row)

# Optional: print submatrix boundaries
print(f"\nSubmatrix boundaries: From ({i}, {j}) to ({k}, {l})")

sumS = 0                                                                      # Initialize sum
for x in range(i, k + 1):                                                    # Iterate from row i to k
    for y in range(j, l + 1):                                                # Iterate from col j to l
        sumS += matrix[x][y]                                                 # Add matrix element to sum

print(f"\nSum of the selected submatrix: {sumS}")                            # Output final result
