import numpy as np
from scipy.optimize import minimize
m = 1
c = 1
e = 1
h = 2*np.pi
n3 = 0


def chain(s, lamb, mu, n, chi):
    p = chi/(2*lamb)
    nu = mu + lamb ** 2 + (1 - p) * (n + 1 + 2 * lamb) + 2 * lamb * n
    u = -(2 * s ** 2 + 2 * s * (2 * lamb + n + 1 - p) + nu) / ((s + 1) * (s + n + 1))
    v = -((s - p + 1 + n)*(s - p))/((s + 2)*(s + n +2))
    if s < 500:
        #print(s, ' --- ', u + v/chain(v = 1, u = 1, s = s + 1))
        return u + v/chain(s = s + 1, lamb = lamb, mu = mu, n = n, chi = chi)
    else:
        #print(s, ' --- ', u + v)
        return u + v


def spec(x):
    return chain(0, x[0], x[1], 0, x[2])**2

spectrum = []
R = np.arange(0.1, 5, 0.1)
r_0 = 3
E_0 = -0.91
lamb_0 = np.sqrt(-r_0**2/2 * E_0)
chi_0 = 2 * r_0
mu_0 = -1.67
x0 = np.array([lamb_0, mu_0, chi_0])
x0 = [1.496662954709576, -0.8262574411126102, 3.999999999999999]

res = minimize(spec, x0, method = 'nelder-mead')
print(res.x)
R = res.x[2]/2
E = -res.x[0]**2*2/R**2
#print("Расстояние:", R, "Энергия:", E + 1/R)

#for a in spectrum:
#    print(a[1]/2, -8*a[0]**2/a[1]**2 + 2/a[1], '---', a)




#print(chain(v_0, u_0, s_0))