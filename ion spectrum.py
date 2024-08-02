#подключение нужных библиотек и пакетов
import numpy as np
from scipy.optimize import minimize

#функция значнни цепной дроби
def chain(s, lamb, mu, n, chi):
    p = chi/(2*lamb)
    nu = mu + lamb ** 2 + (1 - p) * (n + 1 + 2 * lamb) + 2 * lamb * n
    u = -(2 * s ** 2 + 2 * s * (2 * lamb + n + 1 - p) + nu) / ((s + 1) * (s + n + 1))
    v = -((s - p + 1 + n)*(s - p))/((s + 2)*(s + n +2))
    if s < 500: #300 итераций в дроби
        return u + v/chain(s = s + 1, lamb = lamb, mu = mu, n = n, chi = chi)
    else:
        return u + v


def spec(x):
    return chain(0, x[0], x[1], 0, x[2])**2


#определение примерной энергии уровней
mass = []
n3 = 0
R = np.arange(0.4, 4, 0.1)  # диапазон расстояний между ядрами
E = np.arange(-1.5, -0.4, 0.01)  # диапазон энергий электрона
for r_i in R:
    chi_i = 2*r_i
    for E_j in E:
        lamb_ij = np.sqrt(-0.5 * r_i**2 * E_j)
        mu_ij = -1/3 * lamb_ij ** 2 - 2/135 * lamb_ij ** 4 - 4/8505 * lamb_ij ** 6 + 16/13395375 * lamb_ij ** 8
        p_ij = chi_i/(2 * lamb_ij)
        nu = mu_ij + lamb_ij ** 2 + (1 - p_ij) * (n3 + 1 + 2 * lamb_ij) + 2 * lamb_ij * n3
        if np.abs(chain(0, lamb_ij, mu_ij, n3, chi_i)) < 0.05:
            mass.append([r_i, E_j, mu_ij, np.abs(chain(0, lamb_ij, mu_ij, n3, chi_i))])

#for a in mass:
#     print(a[0], '---', 1/a[0] + a[1], a[2], a[3])


mins = list()
sorted_mass = list()
for el in sorted(mass, key = lambda x: (x[0], x[3])):
    if el[0] not in mins:
        sorted_mass.append(el)
        mins.append(el[0])

#for x in sorted_mass:
#    #print(a[0], '---', 1 / a[0] + a[1], a[2], a[3])
#    a = [np.sqrt(-x[0]**2*x[1]/2), x[2], 2*x[0]]
#    print(a)


s = 1
for x in sorted_mass:
    lamb = np.sqrt(-x[0]**2*x[1]/2)
    chi = 2*x[0]
    mu = x[2]
    x0 = np.array([lamb, mu, chi])
    res = minimize(spec, x0, method='nelder-mead')
    R = res.x[2]/2
    E = -res.x[0]**2*2/R**2
    print(R, E + 1/R)
    s += 1





