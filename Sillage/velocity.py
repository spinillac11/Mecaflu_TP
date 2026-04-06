import numpy as np
import matplotlib.pyplot as plt

X = np.zeros(25)
Y = np.array([5.0,4.9,4.8,4.7,4.6,4.5,4.1,3.7,3.3,2.5,2.1,1.3,0.9,0.8,0.7,0.6,0.5,0.4])
V = np.array([0.0028,0.0046,0.0060,0.0072, 0.0082,  0.0090,0.0112,0.0121,0.0124, 0.0126,0.0126, 0.0123 , 0.0107, 0.0099, 0.0089, 0.0076, 0.0060, 0.0041 ])
Err = np.array([9.0381e-04,2.3510e-04,4.0381e-04,1.7897e-04,1.8586e-04, 1.8753e-04,1.4024e-04,1.1729e-04, 2.4746e-04, 3.0833e-04,2.1374e-04, 2.4457e-04, 1.5154e-04, 1.5960e-04, 1.1831e-04, 1.4012e-04, 3.2961e-04, 6.5440e-04 ])


plt.figure()
plt.scatter(Y, V, c = 'r')
plt.errorbar(Y, V, Err)
plt.grid()
plt.xlabel('distance cm')
plt.ylabel('velocity m/s')
plt.title("Velocitys' profile before the obstacle")
plt.show()

Y2 = np.arange(5.0, 0.4, -0.2)
V2 = np.array([0.0032,0.0069, 0.0096,0.0116, 0.0129,0.0139,0.0141,0.0137, 0.0123,0.0097,  0.0074,0.0060, 0.0055,0.0058, 0.0068,0.0091, 0.0121,0.0142, 0.0150,0.0148, 0.0140, 0.0121 ,0.0092])
Err2 = np.array([7.7725e-04,2.6586e-04, 4.4937e-04,2.6231e-04, 1.3065e-04,3.3448e-04,2.1486e-04,1.6386e-04, 1.4245e-04,4.2212e-04, 3.1659e-04,3.4967e-04, 4.0979e-04,2.7447e-04, 2.9779e-04,2.6483e-04,2.0251e-04, 1.2630e-04, 3.1861e-04,1.0763e-04, 1.4517e-04,2.5575e-04 ,2.3514e-04])

plt.figure()
plt.scatter(Y2, V2, c = 'r')
plt.errorbar(Y2, V2, Err2)
plt.grid()
plt.xlabel('distance cm')
plt.ylabel('velocity m/s')
plt.title("Velocitys' profile after the obstacle")
plt.show()


#Debit
Y = Y*pow(10,-2)
Y2 = Y2*pow(10,-2)
H = 0.05
Q1 = -np.trapezoid(V, Y)*H*pow(100,3)
Q2 = -np.trapezoid(V2, Y2)*H*pow(100,3)

err = np.abs(Q1-Q2)*100/Q2

print("Debit avant:", Q1)
print("Debit apres:", Q2)
print("Error:", err)



#Force de traine

U2 = V*V
rho = 1000 #kg/m3
U2_2 = V2*V2
h = 0.005
Ft = (np.trapezoid(U2_2,Y2) - np.trapezoid(U2,Y))
Um2 =( np.mean(V2)* np.mean(V2) + np.mean(V)* np.mean(V))/2
Cx = 2*Ft/(h* Um2)
print(Cx)
# vitesse vs frequency

# --- Datos de entrada ---
h_plaque = 0.005  # Altura de la placa en metros (5 mm)
Q_max = 90        # Caudal máximo en cm3/s
debit_porcentaje = np.array([35, 40, 48, 55, 60, 65, 70, 75])
v_moyen = np.array([0.0170, 0.0193, 0.0226, 0.0252, 0.0267, 0.0279, 0.0294, 0.0313])
T = np.array([2.6500, 2.2561, 1.8667, 1.6000, 1.4047, 1.2733, 1.1543, 1.1374])

# --- Cálculos ---
debit_reel = (debit_porcentaje / 100) * Q_max  # Caudal en cm3/s
freq = 1 / T                                   # Frecuencia en Hz
strouhal = (freq * h_plaque) / v_moyen        # Número de Strouhal (adimensional)

# --- Gráficos en Francés ---
plt.figure(figsize=(12, 5))

# 1. Fréquence vs Débit
plt.subplot(1, 2, 1)
plt.plot(debit_reel, freq, 'bo-', label='Mesures')
plt.xlabel('Débit réel $Q$ ($cm^3/s$)')
plt.ylabel('Fréquence $f$ ($Hz$)')
plt.title('Fréquence d\'oscillation vs Débit')
plt.grid(True, linestyle='--')

# 2. Nombre de Strouhal vs Vitesse
plt.subplot(1, 2, 2)
plt.plot(v_moyen, strouhal, 'rs-', label='$S_t$ expérimental')
plt.axhline(y=0.15, color='k', linestyle='--', label='$S_t$ théorique plaque (~0.15)')
plt.xlabel('Vitesse moyenne $U$ ($m/s$)')
plt.ylabel('Nombre de Strouhal $S_t$')
plt.title('Adimensionnement du sillage (Strouhal)')
plt.ylim(0, 0.3)
plt.legend()
plt.grid(True, linestyle='--')

plt.tight_layout()
plt.show()

print(f"Strouhal moyen mesuré : {np.mean(strouhal):.3f}")