import json
import numpy as np
from control.matlab import *
import matplotlib.pyplot as plt


class GradientIdentification():
    def __init__(self, x, y, init_params, KMAX = 100) -> None:
        # data load:
        self.t = x
        self.h = y
        self.size = len(self.h)
        self.state = round(np.mean(self.h[int(0.2*self.size): ]))
        # coeffs load:
        self.num = init_params[ :len(init_params)//2]
        self.den = init_params[len(init_params)//2: ]
        self.numDim = len(self.num)
        self.denDim = len(self.den)
        self.X = np.concatenate([self.num, self.den])
        self.J = np.zeros(len(self.X))
        # log data
        self.kmax = KMAX
        self.currentK = None
        self.currentEps = None
        self.k = 0

    def GraphOut(self,graphs,title='График',filename = 'График', name='untitled', folder = ''):
        plt.figure(1)
        plt.title(title)
        for graph in graphs:
            plt.plot(graph[0], graph[1],label=graph[2])
        plt.legend()
        plt.grid()
        plt.show()
        return
    
    def MakeCoefs(self, _X):
        n = np.zeros(self.numDim)
        d = np.zeros(self.denDim)
        for i in range(self.numDim):
            n[i] = _X[i]
        for i in range(self.denDim):
            d[i] = _X[self.numDim + i]
        return n, d

    def MakeModel(self, _X):
        numm, denn = self.MakeCoefs(_X)
        sys_ = tf(numm, denn)
        return sys_        

    def StepResponseData(self, _X):
        sys_ = self.MakeModel(_X)
        t = np.linspace(0,self.t[-1],self.size)
        yM, t = step(sys_, T=t)
        return t, yM 

    def I(self,_X):
        t, yM = self.StepResponseData(_X)   
        return  (yM-self.h) @ (yM-self.h)

    def Gradient(self):
        eps = 1e-6
        Xi = np.copy(self.X)
        gr = np.zeros(len(Xi))
        for i in range(len(Xi)):
            if Xi[i] == 0:
                dx = eps
            else:
                dx = 0.001 * abs(Xi[i])
            Xi[i] += dx
            f1 = self.I(Xi)
            Xi[i] -= 2 * dx
            f2 = self.I(Xi)
            gr[i] = (f1 - f2) / (dx + dx)
            Xi[i] += dx
        return gr

    def f1(self, alpha):
        Xi = np.copy(self.X)
        for i in range(len(Xi)):
            Xi[i] = Xi[i] + alpha*(-self.J[i])
        return self.I(Xi)

    def min_fun_split(self, a, b):
        xi = 0
        k_max = 250
        
        ai = a
        bi = b
        l = (b - a)*0.01
        #print('L = ', l)
        while(abs(bi-ai)>=l and k_max > 0):
            dx = (bi-ai)*0.001
            
            pi = ((ai + bi) - dx) * 0.5
            qi = ((ai + bi) + dx) * 0.5
            
            fp = self.f1(pi)
            fq = self.f1(qi)
            
            if(fp < fq):
                bi = qi
            else:
                ai = pi
            k_max = k_max - 1
        xi = (ai+bi) / 2.0
        return xi

    def GetMinimization(self):
        I0 = self.I(self.X)
        eps = 0.001 * I0
        kmax = self.kmax
        epsCurrent = 1
        a = -10
        b = 10 
        self.J = self.Gradient()
        for i in range(len(self.X)):
            if self.J[i] != 0:
                alf1 = -self.X[i] / self.J[i]
                alf2 = 0.5 * self.X[i]/self.J[i]
                a1 = min(alf1, alf2)
                b1 = max(alf1, alf2)
                a = max(a, a1)
                b = min(b,b1)
        step = self.min_fun_split(a,b)
        
        self.X = self.X - step * self.J
        epsCurrent = self.I(self.X)/I0
        self.k += 1
        self.currentEps = epsCurrent
        
        x2, y2 = self.StepResponseData(self.X)
        error = self.I(self.X)
        model = self.MakeModel(self.X)
                
        data = {
            'x2': x2.tolist(),
            'y2': y2.tolist(),
            'error': error,
            'tf_formula': model._repr_latex_()
        }
        
        if self.k > self.kmax:
            return
        
        yield 'data: {}\n\n'.format(json.dumps(data))
        
    def Info(self,tM=None, hM=None):
        self.GraphOut([[self.t,self.h,'Задание'],[tM,hM, 'Модель']])
        print('Вычисление завершено за ', self.currentK, ' иттераций')
        print('Ошибка относительно задания ', self.currentEps*100, ' %')
        print('Числитель ', self.MakeCoefs(self.X)[0])
        print('Знаменатель ',  self.MakeCoefs(self.X)[1])
        print('Значение функционала ', self.I(self.X))    

if __name__ == '__main__':
    print("ЗАПУСК НЕ КАК МОДУЛЯ")
    file_path = "test_data/time_value.txt"
    x, y = np.loadtxt(file_path, delimiter=',', unpack=True)
    k = int(input("Введите максимальное кол-во итераций: "))
    Tparam = 0.05
    xi = 1.0
    # Последний коэффициент в числителе д.б. равен установившемуся значению ПХ  
    numerator = [0.0000001, 0.0000001, 2] # b1 b2 b3
    # Последний коэффициент в знаменателе д.б. равен одному
    denumerator = [0.000001, Tparam**2, 2*xi*Tparam, 1] # a0 a1 a2 a3
    
    m = GradientIdentification(x, y, numerator+denumerator, KMAX = k)
    print(m.num, m.den)
    print("============Start Minim=============")
    for i in range(k):
        next(m.GetMinimization())
    coeffs = next(m.GetMinimization())
    t,y = m.StepResponseData(coeffs)
    # m.Info(t, y)



