import sys
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument()
if len(sys.argv[1:]) == 0:
	parser.print_help()
	parser.exit()
args = parser.parse_args()