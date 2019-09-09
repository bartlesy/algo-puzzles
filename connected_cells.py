def dfs(matrix, i, j, cur_num):
    for i in range(2):
        for j in range(2):
            if (i + j) == 0:
                continue
        if matrix[i][j]:
            cur_num[0] += 1
            matrix[i][j] = 0
            dfs(matrix, i + 1, j, cur_num)
            dfs(matrix, i, j + 1, cur_num)
            dfs(matrix, i + 1, j + 1, cur_num)
    return


def connectedCell(matrix):
    cur_num = [0]
    dfs(matrix, 0, 0, cur_num)
    return cur_num[0]


print(connectedCell([[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0, 0]]))
