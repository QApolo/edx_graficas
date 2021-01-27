import matplotlib.pyplot as plt
import os
import shutil
import numpy as np

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

if __name__ == '__main__':
        # Data for plotting
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('A tale of 2 subplots')

    ax1.plot(x1, y1, 'o-')
    ax1.set_ylabel('Damped oscillation')

    ax2.plot(x2, y2, '.-')
    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('Undamped')

    plt.savefig("01_coursera.png")
    plt.show()
    #
    first = os.path.abspath("") 
    string = os.path.abspath("")
    res = string.split(slash)[0:-1]
    res = slash.join(res)
    try:
        shutil.copy(res+slash+output+"." + l3, first + slash + "01_coursera")
    except:
        print("Missing modules...\nTry installing them first and execute again")