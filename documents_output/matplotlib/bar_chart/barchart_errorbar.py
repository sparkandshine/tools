#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib

def autolabel(rects, ax):
    """write the value inside each bar"""
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., height-0.4,
                '%d' % int(height), fontsize=15, ha='center', va='bottom')

def main():
	# plot a barchart with error bar
	fig, ax = plt.subplots()

	legends = ['Q1', 'Q2', 'Q3', 'Q4']
	# 4 groups, generate a random list with `random.sample(range(1, 5), 4)`
	groups = [	[4, 3, 1, 2],	# Q1
				[1, 2, 3, 4],	# Q2
				[3, 1, 2, 4],	# Q3
				[2, 1, 4, 3]]	# Q4

	colors = ['r', 'g', 'b', 'm']

	x = range(len(groups))
	list_rects = list()
	for idx, group in enumerate(groups):
		left = [i+idx*0.2 for i in x]

		rects = plt.bar(left, group, 
						width=0.2, 
						color=colors[idx], 
						yerr=0.1, ecolor='k', capsize=5,
						orientation='vertical')

		list_rects.append(rects)


	# write the value inside each bar 	
	for rects in list_rects:
		autolabel(rects, ax)

	# decoration 
	ax.legend(list_rects, legends, loc='best')

	# set xtick labels
	list_ticklabel = ['2012', '2013', '2014', '2015']
	ax.set_xticks([i+0.4 for i in x])
	ax.set_xticklabels(list_ticklabel)
	ax.set_xlim(0, max(x)+1-0.2)

	# Hide the right and top spines
	ax.spines['left'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(False)

	# Only show ticks on the bottom spine
	ax.xaxis.set_ticks_position('bottom')

	#ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	#ax.set_frame_on(False)
	#ax.axis('off')

	out_file = 'barchart_errorbar.png'
	plt.savefig(out_file)
	plt.show()


if __name__ == '__main__':
	main()
