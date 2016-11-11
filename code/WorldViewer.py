from pylab import *
from matplotlib.colors import LinearSegmentedColormap
from Cell2D import Cell2D, Cell2DViewer

class WorldViewer(Cell2DViewer):
    """Generates visualization and animation of the world"""
    vmax = 1
    options = dict(interpolation='none', alpha=0.6, 
                   vmin=0, vmax=vmax)
   
    cmap = plt.get_cmap('YlOrRd')
