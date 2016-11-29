from pylab import *
from Cell2D import Cell2D, Cell2DViewer

from matplotlib.colors import LinearSegmentedColormap

def make_cmap(color_dict, vmax=None, name='mycmap'):
	"""Makes a custom color map.

	color_dict: map from numbers to colors
	vmax: high end of the range,
	name: string name for map

	If vmax is None, uses the max value from color_dict

	returns: pyplot color map
	"""
	if vmax is None:
		vmax = max(color_dict.keys())

	colors = [(value/vmax, color) for value, color in color_dict.items()]

	cmap = LinearSegmentedColormap.from_list(name, colors)

	return cmap

class WorldViewer(Cell2DViewer):
	"""Generates visualization and animation of the world"""
	options = dict(interpolation='none', alpha=0.6,
		vmin=0, vmax=2)

	colors = ['#7fc97f','#beaed4','#fdc086','#ffff99','#386cb0']
	cmap = make_cmap({0:'white', 1:colors[2], 2:colors[4]})
