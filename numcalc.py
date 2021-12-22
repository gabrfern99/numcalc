import numpy as np
import numcalc_methods


def get_matrix(nmx):

    init_augmx = np.zeros((nmx, nmx + 1))
    init_solvec = np.zeros(nmx)

    print("Enter augmented matrix coefficients: ")
    for i in range(nmx):
        for j in range(nmx + 1):
            init_augmx[i][j] = float(input(f"a[{str(i)}][{str(j)}] = "))

    return init_augmx, init_solvec


if __name__ == "__main__":
    try:
        nmx = int(input("Enter number of unknowns: "))
    except Exception:
        pass
    init_augmx, init_solvec = get_matrix(nmx)
    print("Applying gauss elimination")
    solvec = numcalc_methods.gauss_elimination(init_augmx, init_solvec, nmx)
    print("The solution vector is: ")
    for i in range(nmx):
        print(f"x{i} = {solvec[i]:.2f}")
