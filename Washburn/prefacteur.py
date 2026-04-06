import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Données extraites de l'image
h = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13]) # en mm
t = np.array([12.6, 17.5, 23.8, 32.7, 47.8, 72.2, 94.0, 124.0, 459.0]) # en s
x2 = h**2 # Carré de la hauteur en mm²

# Sélection des premiers points pour le régime linéaire (5 à 8 mm)
h_lin = h[:4]
t_lin = t[:4]
slope, intercept, r_value, _, _ = stats.linregress(t_lin, h_lin**2)

# Calcul du rayon des pores (r)
# Pente m convertie en m²/s (1 mm² = 1e-6 m²)
m_m2s = slope * 1e-6
gamma = 0.0223 # N/m (éthanol)
eta = 0.0012   # Pa.s (éthanol)
r_m = (2 * eta * m_m2s) / gamma
r_um = r_m * 1e6 # Conversion en micromètres

# Graphique
plt.figure(figsize=(10, 6))
plt.scatter(t, x2, color='blue', label='Données expérimentales')
plt.plot(t_lin, slope * t_lin + intercept, color='red', linestyle='--', label='Régime de Washburn (linéaire)')
plt.title("Loi de Washburn : Ascension de l'éthanol dans le papier")
plt.xlabel("Temps t (s)")
plt.ylabel("Carré de la hauteur x² (mm²)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.savefig('analyse_washburn.png')

print(f"m = {slope:.4e}")
print(f"R2 = {r_value**2:.3f}")
print(f"Taille de pore: {r_um:.2f} µm")
