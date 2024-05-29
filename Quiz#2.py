def mul_matrices(A, B):
    
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    mat_res = [[0] * p for x in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                mat_res[i][j] += A[i][k] * B[k][j]

    return mat_res