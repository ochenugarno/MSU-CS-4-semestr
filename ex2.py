import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftshift

def f(z):
    return np.cos(z + 1) * np.exp(-z**2/100)

#def g(z):
#    return f(z + 30)


stepT = 200/1024
netT = np.arange(-100, -100 + 200//stepT * stepT, stepT)
f_np = fftshift(fft(fftshift(f(netT))))
stepW = np.pi/100
netW = np.arange(-len(netT)/2 * stepW, len(netT)/2 * stepW, stepW)

f_numb = 0
#for i in range(0, len(netT) - 1):
#    re = stepT * f(netT[i]) * np.cos(netW*netT[i])
#    im = -stepT * f(netT[i]) * np.sin(netW*netT[i])
#    f_numb += re + 1j * im

for i in range(0, len(netT) - 1):
    f_numb += f(netT[i]) * np.exp(-1j*netW*netT[i])


g_np = np.exp(1j * netW * 30)*f_np
g_numb = np.exp(1j * netW * 30)*f_numb

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.set_xlabel('w')
ax1.set_ylabel('Re(f_)')
ax1.plot(netW, f_np.real, color = 'red')
ax1.plot(netW, f_numb.real, "--", color = 'blue')

ax2.set_xlabel('w')
ax2.set_ylabel('Im(f_)')
ax2.plot(netW, f_np.imag, color = 'red')
ax2.plot(netW, f_numb.imag, "--", color = 'blue')

ax3.set_xlabel('t')
ax3.set_ylabel('f')
ax3.plot(netT, f(netT), color = 'red')

ax4.set_xlabel('t')
ax4.set_ylabel('g')
ax4.plot(netT, fftshift(ifft(fftshift(g_np))),  color = 'red')
ax4.plot(netT, fftshift(ifft(fftshift(g_numb))), "--", color = 'blue')
plt.show()


