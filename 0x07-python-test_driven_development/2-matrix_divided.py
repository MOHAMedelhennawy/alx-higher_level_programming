#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Matrix Divided.

    Args:
    matrix: the origan matrix
    div: the number to divide by

    Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: Each row of the matrix must have the same size
    TypeError: div must be a number
    ZeroDivisionError: division by zero

    Return: a new matrix
    """
    new_matrix = []

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(row / div, 2) for row in col] for col in matrix]
