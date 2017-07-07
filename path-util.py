#!/usr/bin/env python3

'''
Utility to assist in maintaining PATH
'''

import argparse
import os

__version__ = (0, 2, 0)


def parse_args():
	parser = argparse.ArgumentParser(prog='path-util', description=__doc__)

	parser.add_argument('-V', '--version', action='version', version='%(prog)s {}'.format('.'.join(map(str, __version__))))

	existing_path_meg = parser.add_mutually_exclusive_group()
	existing_path_meg.add_argument('--include-existing-path', action='store_true', default=True)
	existing_path_meg.add_argument('--exclude-existing-path', action='store_false', dest='include_existing_path')

	parser.add_argument('--existing_path_type', default='bash', choices=('bash',))

	pathd_meg = parser.add_mutually_exclusive_group()
	pathd_meg.add_argument('--include-pathd', action='store_true', default=True)
	pathd_meg.add_argument('--exclude-pathd', action='store_true', dest='include_pathd')

	parser.add_argument('--pathd-dir', default='~/path.d')

	subparsers = parser.add_subparsers()
	output_bash_parser = subparsers.add_parser('output-bash')
	output_bash_parser.set_default(func=encode_bash_path)

	return parser.parse_args()

def parse_bash(bash_path):
	pass

def parse_pathd(pathd_directory=None):
	pass

def encode_bash_path(paths):
	pass

def main(args):
	paths = []

	if args.include_existing_path:
		if args.existing_path_type == 'bash':
			paths += parse_bash(os.environ['PATH'])

	if args.include_pathd:
		paths += parse_pathd(os.path.expandvars(os.path.expanduser(args.pathd_dir)))

	args.func(paths)

	#print(':'.join([a for a, _ in sorted({y: x for x,y in enumerate(os.environ['PATH'].split(':'))}.items(), key=lambda x: x[1])]))


if __name__=='__main__':
	main(parse_args())
