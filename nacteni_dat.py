
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt

vertices = []
codes = []

codes = [Path.MOVETO] + [Path.LINETO]*5 + [Path.CLOSEPOLY]
# *5 - pocet bodu -1 - neco s len()-1?
vertices = [(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9), (0, 0)]
# musi se vsude pridat koncovy bod (0, 0), bo potrebuje stabilni zazemi (jako kdokoliv jiny na Zemi)

codes += [Path.MOVETO] + [Path.LINETO]*10 + [Path.CLOSEPOLY]
vertices += [(51.7, 52.0), (54.4, 22.8), (43.8, 7.9), (34.7, 10.2), (32.2, 17.4), (23.2, 11.1), (15.6, 17.4), (22.2, 42.3), (37.1, 27.2), (44.4, 30.4), (41.6, 37.4), (0, 0)]

codes += [Path.MOVETO] + [Path.LINETO]*4 + [Path.CLOSEPOLY]
vertices += [(63.4, 45.1), (88.0, 54.9), (72.6, 20.6), (65.7, 27.7), (63.4, 45.1), (0, 0)]

codes += [Path.MOVETO] + [Path.LINETO]*6 + [Path.CLOSEPOLY]
vertices += [(47.3, 81.2), (58.5, 77.4), (62.8, 86.3), (88.2, 86.3), (71.1, 60.5), (66.2, 75.2), (51.7, 68.8), (0, 0)]


vertices = np.array(vertices, float)
path = Path(vertices, codes)

pathpatch = PathPatch(path, facecolor='None', edgecolor='green')

fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A compound path')

ax.autoscale_view()

plt.show()