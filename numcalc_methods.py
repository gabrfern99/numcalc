def gauss_elimination(augmx, solvec, mxsize):
    for i in range(mxsize):
        if augmx[i][i] == 0:
            break
        for j in range(i + 1, mxsize):
            mult = (augmx[j][i]/augmx[i][i])
            for k in range(mxsize + 1):
                augmx[j][k] = augmx[j][k] - (mult * augmx[i][k])

    solvec[mxsize - 1] = (augmx[mxsize - 1][mxsize])/(augmx[mxsize - 1][mxsize - 1])
    for i in range(mxsize - 2, -1, -1):
        solvec[i] = augmx[i][mxsize]
        for j in range(i + 1, mxsize):
            solvec[i] = solvec[i] - (augmx[i][j] * solvec[j])
        solvec[i] = solvec[i]/augmx[i][i]

    return solvec
