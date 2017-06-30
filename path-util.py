#!/usr/bin/env python3

'''
Utility to assist in maintaining PATH
'''

# import argparse
import os

__version__ = (0, 1, 0)


# def parse_args():
# 	parser = argparse.ArgumentParser(description=__doc__)

# 	return parser.parse_args()

def main(args):
	print(':'.join([a for a, _ in sorted({y: x for x,y in enumerate(os.environ['PATH'].split(':'))}.items(), key=lambda x: x[1])]))


if __name__=='__main__':
	# main(parse_args())
	main(None)
