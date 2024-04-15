import pandas as pd
import matplotlib.pyplot as plt

dynErrorGP = pd.read_csv ('dynErrorGP.txt')
dynErrorGP = dynErrorGP.values

dynErrorMeasurement = pd.read_csv ('dynErrorMeasurement.txt')
dynErrorMeasurement = dynErrorMeasurement.values

#plt.plot(n470[:,0],n470[:,1], color='lightcoral', linestyle ='dashed', label = 'No Diffusor 470nm')
#plt.plot(w470[:,0],w470[:,1], color='orangered', label = 'With Diffusor 470nm')

#lam_x = np.linspace(-90.0, 90.0, num=200)
#lam_y = np.cos(y)

plt.figure(figsize=(7,4))
plt.plot(dynErrorGP[:,0], dynErrorGP[:,1], color='#009682', label = 'GP')
plt.plot(dynErrorMeasurement[:,0],dynErrorMeasurement[:,1], color='#eeb70d', label = 'Measurement')
plt.grid(True)
plt.legend()
plt.ylabel('$e$ in deg$^{\circ}$')
plt.xlabel('$t$ in s')
#plt.suptitle('Scattering Profile - Diffusor Tip')
plt.show()