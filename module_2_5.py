def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append([value, value])

    print(matrix)

get_matrix(5, 2, 3)