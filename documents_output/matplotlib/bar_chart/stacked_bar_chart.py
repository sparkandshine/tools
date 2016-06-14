#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def main():
	# plot a stacked bar char
	fig, ax = plt.subplots()

	A = [3, 1, 2, 4]
	B = [2, 1, 4, 3]

	x = range(4)
	ax.bar(x, A, color = 'b', label='A')
	ax.bar(x, B, color = 'g', bottom=A, label='B')

	ax.legend(loc='best')
	ax.axis('off')

	out_file = 'stacked_bar_chart.png'
	plt.savefig(out_file)

	plt.show()

if __name__ == '__main__':
	main()