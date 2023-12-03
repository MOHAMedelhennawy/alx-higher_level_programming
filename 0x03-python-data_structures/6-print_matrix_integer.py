#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (j != 2):
                print("{} ".format(matrix[i][j]), end="")
            else:
                print("{}".format(matrix[i][j]), end="")
        print("\n", end="")
