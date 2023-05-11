import numpy as np

def LSM(t, y, degree):
    N = len(t)
    phi = np.zeros((N-1,2*degree))
    for i in range(N-1):
        for j in range(degree):
            if i - j <= 0:
                phi[i][j] = 0
            else:
                phi[i][j] = -y[i-j]
    for i in range(N-1):
        for j in range(degree,2*degree):
            if i + degree - j <= 0:
                phi[i][j] = 0
            else:
                phi[i][j] = 1
    Y = y[1:N]
    B = np.dot(phi.T,Y)
    A = np.dot(phi.T,phi)
    x = np.linalg.solve(A,B)
    return x