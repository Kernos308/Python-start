import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np 

cmaps = [ 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','YlOrBr', 'YlOrRd', 
'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

fig = plt.figure()
for a in range(5):
    m = np.random.randint(len(cmaps))
    ax=fig.add_subplot(3,2,a+1, projection = '3d')
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x** 2 + y** 2)
    z = np.sin(r)
    surf = ax.plot_surface(x, y, z, cmap = cmaps[m],
    linewidth = 0, antialiased = False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(2))
plt.show()