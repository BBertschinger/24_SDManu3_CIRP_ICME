import pandas as pd
import matplotlib.pyplot as plt

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
lam_y = np.cos(y)

plt.plot(lam_x,lam_y, color='lightcoral', linestyle ='dashed', label = 'No Diffusor 470nm')
#plt.plot(w470[:,0],w470[:,1], color='orangered', label = 'With Diffusor 470nm')
plt.plot(n595[:,0],n595[:,1], color='lightgreen', linestyle ='dashed', label = 'No Diffusor')
plt.plot(w595[:,0],w595[:,1], color='green', label =  'With Diffusor')
plt.legend()
plt.ylabel('Normalized Intensity [DN]')
plt.xlabel("Angle [$deg^{\circ}$]")
plt.suptitle('Scattering Profile - Diffusor Tip')
plt.show()