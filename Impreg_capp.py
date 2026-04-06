#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:47:12 2026

@author: promo2a
"""

import numpy as np
import matplotlib.pyplot as plt

R=np.array([235,320,429,595])
h=np.array([24,17,12,9])
H = h* pow(10,-3)
R= R * pow(10,-6)


coef = np.polyfit(1/R, H,1)

m, b = coef

rec_fit = m*1/R + b

r = np.corrcoef(1/R,H)[0,1]
r2= r**2

plt.scatter(1/R, H)
plt.plot(1/R,rec_fit, label = 'Reg lineel')
plt.xlabel("1/R  [1/m]")
plt.ylabel("Hauteur [m]")
plt.title("Hauteur vs 1/R ")
plt.grid()
plt.show()

print("m =", m)
print("b =", b)

gamma = 3871 * m

print("gamma =", gamma)
print("R2 =", r2)