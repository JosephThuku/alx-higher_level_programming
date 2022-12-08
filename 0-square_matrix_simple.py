#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Iterate over the elements of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Compute the square of each element and store it in the new matrix
            new_matrix[i][j] = matrix[i][j] ** 2

    # Return the new matrix
    return new_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squared_matrix = square_matrix_simple(matrix)
print(squared_matrix)

# squared_matrix should now be [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
