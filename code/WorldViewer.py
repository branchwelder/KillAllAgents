from pylab import *
from Cell2D import Cell2D, Cell2DViewer

class WorldViewer(Cell2DViewer):
	"""Generates visualization and animation of the world"""
	options = dict(interpolation='none', alpha=0.6, 
		vmin=0)
	cmap = plt.get_cmap('YlOrRd')
