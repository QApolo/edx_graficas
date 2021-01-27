import matplotlib
import numpy as np
import matplotlib.pyplot as plt
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

np.random.seed(19680801)

#data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.savefig("02_coursera.png")
plt.show()


#
first = os.path.abspath("") 
string = os.path.abspath("")
res = string.split(slash)[0:-1]
res = slash.join(res)
try:
    shutil.copy(res+slash+output+"." + l3, first + slash + "02_coursera")
except:
    print("Missing modules...\nTry installing them first and execute again")