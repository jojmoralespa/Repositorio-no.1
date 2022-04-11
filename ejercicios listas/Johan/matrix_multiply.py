

def matrix_multiply(mat_a , mat_b):
    mat_result = []
    if len(mat_a[0]) == len(mat_b):
        for i in range(len(mat_a)):
            product = 0
            for j in range(len(mat_b)):
                product +=  mat_a[i][j]*mat_b[j][i]
                



