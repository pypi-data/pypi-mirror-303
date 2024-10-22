import numpy as np


# GAUSS - SEIDEL

def gauss_seidel(A, B, X, precision_souhaitee=10e-6):
    # A = np.array([[-6, 1, -1, 0], [1, 4, 0, 1], [-1, 0, -6, 2], [0, 1, 2, 6]])
    # B = np.array([-3, 9, -2, 0])
    # X = np.array([0, 0, 0, 0])

    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    erreur = []

    while np.linalg.norm(A @ X - B) > precision_souhaitee:
        X = np.linalg.inv(D - L) @ U @ X + np.linalg.inv(D - L) @ B
        erreur.append(np.linalg.norm(A @ X - B))

    # print(X)
    # plt.plot(erreur)
    # plt.show()
    # print(A @ X)  # on tombe bien sur B
    return X, erreur


# NEWTON - RAPHSON

def newton_raphson(f, f_prime, x, precision_souhaitee=10e-6):
    # def f(x):
    #     return x ** 3 - 2 * x - 5
    #
    # def f_prime(x):
    #     return 3 * x ** 2 - 2
    #

    x = 0
    k = 0

    while np.linalg.norm(f(x)) > precision_souhaitee:
        x = x - f(x) / f_prime(x)
        k += 1

    # print(x)
    # print(f(x))
    # print(k)
    return x, f(x), k


# NEWTON - RAPHSON Ã  2 inconnus

def newton_raphson_2(f, Jf, X, precision_souhaitee=10e-6):
    # X = np.array([1, 4])
    #
    # def f(X):
    #     return np.array([X[0] ** 2 - X[0] + X[1] ** 2, X[0] ** 2 - X[1] ** 2 - X[1]])
    #
    # def Jf(X):
    #     return np.array([[2 * X[0] - 1, 2 * X[1]], [2 * X[0], -2 * X[1] - 1]])
    #
    # X = np.array([1, 4])

    for k in range(8):
        X_av = X
        X = X - np.linalg.inv(Jf(X)) @ f(X)
        print(
            'x = ' + str(X_av[0]) + ' , y = ' + str(X_av[1]) + ' et la norme = ' + str(
                np.linalg.norm(X - X_av)) + ' pour k = ' + str(k))

    return X
