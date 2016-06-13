#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib

def plot_single_letter_colors(out_file=None):
	"""plot single letter colors"""
	fig, ax = plt.subplots()
	fig.suptitle('Built-in colors in Matplotlib')

	#colors = matplotlib.colors.ColorConverter.colors.keys() 	# [u'c', u'b', u'w', u'g', u'y', u'k', u'r', u'm']
	#colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
	colors = [('b', 'blue'), ('g', 'green'), ('r', 'red'), ('c', 'cyan'), ('m', 'magenta'), ('y', 'yellow'), ('k', 'black'), ('w', 'white')]

	for idx, (c, s) in enumerate(colors):
		label = ' : '.join([repr(c).replace('u', ''), s])
		y = [-idx]*8
		ax.plot(y, color=c, linestyle='-', marker='o', label=label)

	ax.legend(loc='center left')
	ax.set_axis_off()
	ax.set_xlim(-4, idx-1+0.1)
	ax.set_ylim(-idx-0.1, 0.1)

	if out_file:
		fig.savefig(out_file, bbox_inches='tight')
	else:
		plt.show() 

def main():
	# plot built-in colors
	out_file = 'single_letter_colors.png' 
	plot_single_letter_colors(out_file)

if __name__ == '__main__':
	main()