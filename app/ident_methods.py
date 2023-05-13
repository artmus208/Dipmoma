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
    # TODO:
    # [ ]: Распарсить массив коэффициентов x на коэфф. числ. и знамен.
    x = np.linalg.solve(A,B)
    x = x.tolist()
    x.insert(0, 1)
    x.insert(degree+1, 0)
    num = x[degree+1:] 
    den = x[:degree+1]
    return num, den