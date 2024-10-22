import numpy as np


def remontee(A, B):
    # Résolution d'un système triangulaire supérieur
    m = len(B)
    X = [0] * m
    X[m - 1] = B[m - 1] / A[m - 1][m - 1]
    for i in range(m - 2, -1, -1):
        somme = 0
        for j in range(i + 1, m):
            somme += A[i][j] * X[j]
        X[i] = (B[i] - somme) / A[i][i]
    return X


def descente(A, B):
    # Résolution d'un système triangulaire inférieur
    m = len(B)
    X = [0] * m
    X[0] = B[0] / A[0][0]
    for i in range(1, m):
        somme = 0
        for j in range(i):
            somme += A[i][j] * X[j]
        X[i] = (B[i] - somme) / A[i][i]
    return X


def gauss_seidel(A, B):
    # Méthode de Gauss-Seidel pour résoudre un système linéaire
    X = np.array([0, 0, 0, 0])
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    precision_souhaitee = 10e-6
    erreur = []

    while np.linalg.norm(A @ X - B) > precision_souhaitee:
        X = np.linalg.inv(D - L) @ U @ X + np.linalg.inv(D - L) @ B
        erreur.append(np.linalg.norm(A @ X - B))

    # print(X)
    # plt.plot(erreur)
    # plt.show()
    # print(A @ X)  # on tombe bien sur B
    return X, erreur


def newton_raphson(f, df):
    # Méthode de Newton-Raphson pour une équation non linéaire
    x = 0
    k = 0
    precision_souhaitee = 10e-6
    while np.linalg.norm(f(x)) > precision_souhaitee:
        x = x - f(x) / df(x)
        k += 1

    # print(x)
    # print(f(x))
    # print(k)
    return x


def newton_raphson_system(f, j, tol=1e-6, max_iter=100):
    # Méthode de Newton-Raphson pour un système d'équations non linéaires
    x = np.array([1, 4])

    for k in range(8):
        X_av = x
        x = x - np.linalg.inv(j(x)) @ f(x)
        print(
            'x = ' + str(X_av[0]) + ' , y = ' + str(X_av[1]) + ' et la norme = ' + str(
                np.linalg.norm(x - X_av)) + ' pour k = ' + str(k))
