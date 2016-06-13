#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib 
import operator

def plot_linestyles(out_file=None):
	fig, ax = plt.subplots()
	fig.suptitle('Line styles')			# add a centered title to the figure

	linestyles = matplotlib.lines.lineStyles
	'''
	linestyles = {	u'': u'_draw_nothing', 
					u' ': u'_draw_nothing', 
					u'None': u'_draw_nothing', 
					u'--': u'_draw_dashed', 
					u'-.': u'_draw_dash_dot', 
					u'-': u'_draw_solid', 
					u':': u'_draw_dotted'}
	'''

	linestyles_sorted = sorted(linestyles.items(), key=operator.itemgetter(0), reverse=True)

	for idx, (linestyle, s) in enumerate(linestyles_sorted):
		y = [-idx]*5
		ax.plot(y, 	linestyle=linestyle,		# ls, ‘solid’ | ‘dashed’ | ‘dashdot’  |  ‘dotted’ | (offset, on-off-dash-seq) 
												# ls,   '-'	  |    '--'  |    '-.' 	  |     ':'   | 'None' | ' ' | ''
					linewidth=3,				# float value in points
					color='k', label=repr(linestyle).replace('u', ''))


	ax.legend(loc='center left')
	ax.set_axis_off()
	ax.set_xlim(-1.5, 4)
	ax.set_ylim(-idx-0.1, 0.1)

	if out_file:
		plt.savefig(out_file, bbox_inches='tight')
	else:
		plt.show()


def main():
	out_file = 'line_styles.png'
	out_file = None
	plot_linestyles(out_file)


if __name__ == '__main__':
	main()