# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 14:16:39 2026

@author: Promo2A
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/tp2a/Desktop/TP2A/G3/Pinilla-Infante/Reslice of Pinilla-Infante.txt',sep="\t",header=None)
t = (-df[1]+np.max(df[1]) ) / 24
x = (df[0] / 1781  ) * 12.5 * pow((10), -2)

plt.figure()
plt.plot(t,x,',')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title("Parabolic relation distance-time")
plt.grid()
plt.show()
plt.close()
rt = np.sqrt(t)

coef = np.polyfit(rt, x,1)

m, b = coef

rec_fit = m*rt + b

r = np.corrcoef(rt,x)[0,1]
r2= r**2

plt.figure()
plt.scatter(rt,x, label = "Data")
plt.plot(rt,rec_fit,color ="r", label = 'Linear regression')
plt.xlabel('sqrt(t) [sqrt(s)]')
plt.ylabel('x (m)')
plt.title("Linear relation distance-time")
plt.grid()
plt.legend()
plt.show()

print("m =", m)
print("b =", b)



r = 318 * pow(10,-6)
eta = 1.2e-3
gamma = 22.1e-3

pen = np.sqrt(r*gamma*t/eta)


coef2 = np.polyfit(pen, x,1)

m2, b2 = coef2

rec_fit2 = m2*pen + b2

r4 = np.corrcoef(pen,x)[0,1]
r8= r4**2

plt.figure()
plt.scatter(pen,x, label = "Data")
plt.plot(pen,rec_fit2,color ="r", label = 'Linear regression')
plt.xlabel('sqrt(t) [sqrt(s)]')
plt.ylabel('x (m)')
plt.title("Linear relation distance-time")
plt.grid()
plt.legend()
plt.show()
print("m2 =", m2)
print("b2 =", b2)
print("r2 =", r8)
