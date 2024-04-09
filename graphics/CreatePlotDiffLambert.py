import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

n470 = pd.read_csv ('NoDiffusor_470.txt')
n470 = n470.values

n595 = pd.read_csv ('NoDiffusor_595.txt')
n595 = n595.values

w470 = pd.read_csv ('wDiffusor_470.txt')
w470 = w470.values

w595 = pd.read_csv ('wDiffusor_595.txt')
w595 = w595.values

#plt.plot(n470[:,0],n470[:,1], color='lightcoral', linestyle ='dashed', label = 'No Diffusor 470nm')
#plt.plot(w470[:,0],w470[:,1], color='orangered', label = 'With Diffusor 470nm')


lam_x = np.linspace(-90.0, 90.0, num=200)
lamc_x = np.linspace(-180.0, 180.0, num=400)
lam_y = np.cos(np.radians(lam_x))
lamc_y = lamc_x*0.0+1.0

cnst_x = np.linspace(-105.0, 105.0, num=200)

plt.plot(lamc_x,lamc_y, color='orangered', linestyle ='-', label = r'LED - Surface Emitter [$ \gamma$ ]')
plt.plot(lamc_x, lamc_y, color='plum', linestyle ='--', label = r'Fibre Diffuser Tip [$\beta$]')
plt.plot(w595[:,0],w595[:,1], color='blueviolet', linestyle ='-', label = r'Fibre Diffuser Tip [$\alpha, \gamma$]')
plt.plot(lam_x,lam_y, color='coral', linestyle ='-', label = r'LED - Surface Emitter [$ \alpha,\beta$ ]')
plt.legend()
plt.ylabel('Normalized Intensity [DN]')
plt.xlabel("Angle [$deg^{\circ}$]")
plt.grid(True)
#plt.suptitle('Scattering Profile - Diffusor Tip')
plt.show()