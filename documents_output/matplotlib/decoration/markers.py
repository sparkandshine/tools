from __future__ import division

import matplotlib.pyplot as plt
import matplotlib
import math
import operator

import matplotlib.cm as cm

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def plot_all_marks(out_file):
	"""plot all possible markers"""
	fig, axarr = plt.subplots(2, 2)
	fig.suptitle('All possible markers in Matplotlib')			# Add a centered title to the figure

	markers = matplotlib.lines.Line2D.markers 	# all possiable markers, 35
	group_size = int(math.ceil(len(markers)/4))
	list_marker_s = sorted(markers.items(), key=operator.itemgetter(1))	# sorted by description
	
	for idx_chunk, l in enumerate(chunks(list_marker_s, group_size)):
		# for each group
		i, j = divmod(idx_chunk, 2)
		for idx, (marker, s) in enumerate(l):
			y = [-idx]*5
			label = ' : '.join([repr(marker).replace('u', ''), s])
			axarr[i, j].plot(y, 'o', 	marker=marker, 
										markeredgecolor='k',		# mec 
										markerfacecolor='b', 		# mfc 
										markerfacecoloralt='r',		# mfcalt, set the alternate marker face color
										markeredgewidth=1.0,		# mew, float value in points
										fillstyle='none',			# fillstyles = ('full', 'left', 'right', 'bottom', 'top', 'none') 
										markevery=None,				# [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
										markersize=8, label=label)

			axarr[i, j].set_axis_off()
			axarr[i, j].legend(loc='center left')
			axarr[i, j].set_xlim(-4, 5)
			axarr[i, j].set_ylim(-group_size, 1)
			axarr[i, j].legend(loc='center left')
			#axarr[i, j].imshow(y, cmap=cm.jet)

	plt.annotate('Produced by Spark & Shine (sparkandshine.net)', 
				xy=(0,0), xytext=(0, -9), xycoords='axes fraction', textcoords='offset points', horizontalalignment='right', va='top')

	# http://matplotlib.org/users/tight_layout_guide.html#tight-layout-guide
	plt.tight_layout()

	if out_file:
		plt.savefig(out_file, bbox_inches='tight')
	else:
		plt.show()


def plot_filled_markers(out_file):
	"""plot filled markers"""
	fig, ax = plt.subplots()
	fig.suptitle('Filled markers in Matplotlib')			# Add a centered title to the figure

	filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd')
	
	for idx, marker in enumerate(filled_markers):
		y = [-idx]*5
		ax.plot(y, 'o', marker=marker, 
						markeredgecolor='k',		# mec 
						markerfacecolor='b', 		# mfc 
						markerfacecoloralt='r',		# mfcalt, set the alternate marker face color
						markeredgewidth=1.0,		# mew, float value in points
						fillstyle='none',			# fillstyles = ('full', 'left', 'right', 'bottom', 'top', 'none') 
						markevery=None,				# [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
						markersize=8, label=repr(marker).replace('u', ''))

	ax.legend(loc='center left')
	ax.set_axis_off()
	ax.set_xlim(-2, 5)
	ax.set_ylim(-len(filled_markers), 1)

	if out_file:
		plt.savefig(out_file, bbox_inches='tight')
	else:
		plt.show()

def main():
	# plot filled markers
	out_file = 'filled_markers.png'
	plot_filled_markers(out_file)

	# plot all markers
	out_file = 'all_marks.png'
	plot_all_marks(out_file)


if __name__ == '__main__':
	main()