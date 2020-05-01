import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt

def vytvor_objekty(objekty, barva):
    vertices = []
    codes = []
    for objekt in objekty:
        objekt = preved_body_na_tuples(objekt)
        delka = len(objekt) - 1
        codes += [Path.MOVETO] + [Path.LINETO]*delka + [Path.CLOSEPOLY]
        objekt.append((0, 0))
        vertices += objekt

    vertices = np.array(vertices, float)
    path = Path(vertices, codes)

    return PathPatch(path, facecolor='None', edgecolor=barva)


def preved_body_na_tuples(objekt):
    tuples = []
    for bod in objekt:
        tuples.append((bod.x, bod.y))
    return tuples

# funkce pro vykreslovani objektu v mape
def vykreslovani_objektu(puvodni_objekty, konvexni_objekty, trasa, zacatecni_bod, koncovy_bod):

    puvodni_objekty_pathpatch = vytvor_objekty(puvodni_objekty, 'green')
    konvexni_objekty_pathpatch = vytvor_objekty(konvexni_objekty, 'red')

    trasa_pathpatch = vykresli_trasu(trasa)

    fig, ax = plt.subplots()
    ax.add_patch(puvodni_objekty_pathpatch)
    ax.add_patch(konvexni_objekty_pathpatch)
    ax.add_patch(trasa_pathpatch)
    ax.plot(zacatecni_bod.x, zacatecni_bod.y, 'ro')
    ax.plot(koncovy_bod.x, koncovy_bod.y, 'ro')

    ax.set_title('A compound path')

    ax.autoscale_view()

    plt.show()

# funkce pro vykreslovani zacatecniho a koncoveho bodu trasy robota
def vykresli_bod(bodik):
    X = bodik[0]
    Y = bodik[1]
    plt.plot([X], [Y], 'ro')
    plt.show()

# funkce pro vykreslovani trasy
def vykresli_trasu(trasicka):
    vertices = []
    codes = []
    delka = len(trasicka) - 1
    codes += [Path.MOVETO] + [Path.LINETO] * delka
    vertices += preved_body_na_tuples(trasicka)

    vertices = np.array(vertices, float)
    path = Path(vertices, codes)

    pathpatch = PathPatch(path, facecolor='None', edgecolor='blue')
    return pathpatch
