import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Constantes físicas (unidades SI)
rho = 1000  # Densidad del agua (kg/m^3)
sigma = 0.072  # Tensión superficial del agua (N/m) [cite: 21, 49]

# Datos extraídos (Muestra representativa de las imágenes)
# Nota: Velocidad en mm/s -> m/s (/1000), Radios en mm -> m (/1000)
data = {
    "Petri": {
        "R0": np.array([3.18, 3.06, 2.69, 2.84, 2.52, 3.33, 2.98, 2.76, 2.63, 2.56, 3.01, 2.26, 3.63,4.85, 4.04, 4.21, 4.25, 3.93]) / 2000,
        "v": np.array([1420, 1576, 1696, 2372, 2036, 2444, 1172, 1412, 1656, 1816, 2056, 2088, 1000, 1648, 1720, 1908, 2132, 2108]) / 1000,
        "Rmax": np.array([9.02, 8.89, 11.27, 12.36, 10.61, 14.41, 7.9, 9.35, 10.26, 10.43, 12.7, 10.71, 9.95, 15.73, 16.09, 17.7, 19.39, 17.71]) / 2000,
        "t_etale": np.array([0.0035, 0.004, 0.004, 0.004, 0.0035, 0.004, 0.0035, 0.004, 0.0035, 0.003, 0.004, 0.0035, 0.005, 0.0065, 0.0055, 0.006, 0.0055, 0.0055])
    },
    "Hydropho": {
        "R0": np.array([2.81, 2.69, 3.27, 3.41, 3.32, 2.54, 2.45, 2.92, 2.64, 2.94, 2.85, 2.44, 4.55, 4.6, 3.7]) / 2000,
        "v": np.array([952, 960, 1192, 1212, 1444, 652, 636, 980, 1036, 1220, 1388, 1180, 460, 440, 636]) / 1000,
        "Rmax": np.array([6.31, 7.5, 9.14, 10.24, 10.1, 4.29, 4.8, 6.67, 6.81, 8.28, 9.17, 8.1, 7.75, 8.15, 9.44]) / 2000,
        "t_etale": np.array([0.004, 0.0045, 0.0045, 0.004, 0.0045, 0.003, 0.0035, 0.004, 0.0035, 0.0035, 0.004, 0.0045, 0.0055, 0.006, 0.006]),
        "t_rebote": np.array([0.019, 0.019, 0.018, 0.0265, 0.0175, 0.016, 0.0165, 0.018, 0.016, 0.0165, 0.017, 0.015, 0.026, 0.026, 0.025])
    },
    "Verre": {
        "R0": np.array([3.05, 2.86, 2.75, 2.93, 2.73, 2.77, 2.58, 2.5, 2.56, 2.42, 2.44, 2.58, 2.43, 4.11, 4.06, 3.69, 3.98, 3.99, 4.03, 4.07]) / 2000,
        "v": np.array([1812, 1920, 2148, 2360, 2596, 2604, 1244, 1572, 1924, 2044, 2292, 2440, 2516, 1196, 1552, 1740, 1984, 2264, 2548, 2716]) / 1000,
        "Rmax": np.array([10.21, 10.56, 11.17, 12.18, 12.21, 12.39, 6.76, 8.12, 8.64, 9.48, 9.93, 10.94, 10.38, 10.44, 14.02, 14.48, 16.23, 17.46, 17.86, 18.3]) / 2000,
        "t_etale": np.array([0.004, 0.004, 0.0035, 0.0035, 0.0035, 0.003, 0.0035, 0.0035, 0.0035, 0.003, 0.003, 0.003, 0.004, 0.0055, 0.0065, 0.0055, 0.0055, 0.006, 0.0055, 0.0055])
    }
}

# 1. Gráficas de Etalement Máximo: (Rmax/R0)^2 vs sqrt(Weber)
for surf, val in data.items():
    R0, v, Rmax = val["R0"], val["v"], val["Rmax"]
    We = (rho * v**2 * R0) / sigma
    x = np.sqrt(We)
    y = (Rmax / R0)**2
    
    # Ajuste lineal
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label='Datos Experimentales')
    plt.plot(x, slope*x + intercept, color='red', 
             label=f'Ajuste: y = {slope:.2f}x + {intercept:.2f} (R²={r_value**2:.2f})')
    plt.xlabel(r'$\sqrt{We}$')
    plt.ylabel(r'$(R_{max}/R_0)^2$')
    plt.title(f'Etalement Máximo - Superficie: {surf}')
    plt.legend()
    plt.grid(True)
    plt.show()

# 2. Gráficas de Tiempo de Etalement: t_etale vs R0^(3/2)
for surf, val in data.items():
    R0 = val["R0"]
    t_etale = val["t_etale"]
    x = R0**(1.5)
    y = t_etale
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label='Datos Experimentales', color='green')
    plt.plot(x, slope*x + intercept, color='black', 
             label=f'Ajuste Lineal (R²={r_value**2:.2f})')
    plt.xlabel(r'$R_0^{3/2}$ ($m^{1.5}$)')
    plt.ylabel(r'$t_{etale}$ (s)')
    plt.title(f'Tiempo de Etalement - Superficie: {surf}')
    plt.legend()
    plt.grid(True)
    plt.show()

# 3. Tiempo de Rebote (Solo para Superficie Hidrofóbica): t_rebote vs R0^(3/2)
surf_h = "Hydropho"
R0_h = data[surf_h]["R0"]
t_rebote = data[surf_h]["t_rebote"]
x_h = R0_h**(1.5)
y_h = t_rebote

slope, intercept, r_value, p_value, std_err = stats.linregress(x_h, y_h)

plt.figure(figsize=(8, 5))
plt.scatter(x_h, y_h, color='blue', label='Datos Experimentales')
plt.plot(x_h, slope*x_h + intercept, color='orange', 
         label=f'Ajuste Lineal (R²={r_value**2:.2f})')
plt.xlabel(r'$R_0^{3/2}$ ($m^{1.5}$)')
plt.ylabel(r'$t_{rebote}$ (s)')
plt.title('Tiempo de Rebote - Superficie Hidrofóbica')
plt.legend()
plt.grid(True)
plt.show()