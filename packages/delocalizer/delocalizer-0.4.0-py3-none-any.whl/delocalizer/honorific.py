import os
import glob
import argparse

from subdeloc_tools.subtools import SubTools
from subdeloc_tools.modules import pairsubs
from subdeloc_tools.modules import honorific_fixer

parser = argparse.ArgumentParser(description='Modify a subtitle track to make a delocalized version from a JSON file.')
parser.add_argument('--f', dest='folder', type=str, action="store", default=False,
				   help='Folder to save')
parser.add_argument('--ref', dest='reference', type=str, action="store", default=False, required=True,
				   help='Reference subtitle in Japanese')
parser.add_argument('--i', dest='input', type=str, action="store", default=False, required=True,
				   help='Original subtitle')
parser.add_argument('--n', dest='names', type=str, action="store", default=False, required=True,
				   help='Names file')
parser.add_argument('--tokens', dest='tokens', action=argparse.BooleanOptionalAction,
				   help='If active check by tokens instead of japanese reference')
parser.add_argument('--honor', dest='honorifics', type=str, action="store", default=False,
				   help='Honorifics file')
parser.add_argument('--o', dest='output', type=str, action="store", default=False,
				   help='Output name')

path = './Honorifics'
output_name = False

def fix_honorifics(sub, ref, names, honorifics="./honorifics.json", notokens=True):
	fname = sub.split(".")[0]
	on = output_name if output_name else "[Fixed]"+fname+".ass"
	st = SubTools(sub, ref, names, honorifics, on, jap_ref=notokens)
	return st.main()

def main():
	global path
	global output_name
	args = parser.parse_args()
	toks = True

	if args.folder:
		path = args.folder

	if args.output:
		output_name = args.output

	if not path.startswith("./"):
		path = "./"+path

	if not os.path.exists(path):
		os.mkdir(path)

	if args.tokens:
		toks = False

	fix_honorifics(args.input, args.reference, args.names, args.honorifics, toks)

	

if __name__ == '__main__':
	main()
