matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""
matrix= [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]

matrix=[[5]]
"""


def matrix_diagonal_add(matrix):
    length = len(matrix)
    primary_diagonal=0
    secondary_diagonal=0

    for i in range(length):
        if i==0:
            print(matrix[i][i])
        primary_diagonal+=matrix[i][i]
        secondary_diagonal+=matrix[i][length-i-1]
        print(primary_diagonal,secondary_diagonal)
    print(primary_diagonal+secondary_diagonal)
    if length % 2 == 1:
        mid_val = length//2
        print(primary_diagonal+secondary_diagonal-matrix[mid_val][mid_val])




matrix_diagonal_add(matrix)