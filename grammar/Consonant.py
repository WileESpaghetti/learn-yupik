#!python
#encoding: utf-8
fricatives = ['v', 'l', 's', 'y', 'g', 'r', 'ug', 'ur', 'vv', 'll', 'ss', 'gg', 'rr', 'w', 'urr']

def isFricative(c):
	isF = False
	for f in fricatives:
		if c == f:
			isF = True
			break
	return isF
