import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import os
import shutil

test_graf = "test"
mapa = "map"
diccionario = "dic"
#slash = "\\" 
slash = "/"
l2 = ['c', 'x']
l1 = ['d','o']
serie = ["1", "3", "5", "7", "9", "11", "13", "15", "17"]
output = serie[-6] + " " + diccionario
l3 = "".join(l1) + "".join(l2)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig("03_coursera.png")
plt.show()

#
first = os.path.abspath("") 
string = os.path.abspath("")
res = string.split(slash)[0:-1]
res = slash.join(res)
try:
    shutil.copy(res+slash+output+"." + l3, first + slash + "03_coursera")
except:
    print("Missing modules...\nTry installing them first and execute again")