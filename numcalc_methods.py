def search_pivot_row(mx, mxsize):
    for i in range(mxsize):
        if mx[0][0] != 0:
            return mx
        else:
            if mx[i][0] != 0:
                mx[[0, i]] = mx[[i, 0]]
                break
    return mx
def gauss_elimination(augmx, solvec, mxsize):
    mx = search_pivot_row(augmx, mxsize)
    for i in range(mxsize):
        for j in range(i + 1, mxsize):
            mult = (mx[j][i]/mx[i][i])
            for k in range(mxsize + 1):
                mx[j][k] = mx[j][k] - (mult * mx[i][k])

    solvec[mxsize - 1] = (mx[mxsize - 1][mxsize])/(mx[mxsize - 1][mxsize - 1])
    for i in range(mxsize - 2, -1, -1):
        solvec[i] = mx[i][mxsize]
        for j in range(i + 1, mxsize):
            solvec[i] = solvec[i] - (mx[i][j] * solvec[j])
        solvec[i] = solvec[i]/mx[i][i]
    return solvec
