import os
import sys
import glob
import argparse

from subdeloc_tools.modules.merger import Merger

parser = argparse.ArgumentParser(description='Mux or Demux MKV files')
parser.add_argument('--p', dest='print', action=argparse.BooleanOptionalAction,
				   help='Print language indexes')
parser.add_argument('--mux', dest='mux', action=argparse.BooleanOptionalAction, required=not '--p' in sys.argv,
				   help='Mux or demux operation')
parser.add_argument('--m', dest='multi', action=argparse.BooleanOptionalAction, default=False,
				   help='If multiple files will be affected')
parser.add_argument('--f', dest='folder', type=str, action="store", default=False,
				   help='Folder to save')
parser.add_argument('--s', dest='subtitle', type=str, action="store", default=False, required='--mux' in sys.argv,
				   help='Subtitle file to append')
parser.add_argument('--i', dest='input', type=str, action="store", default=False, required='--mux' in sys.argv,
				   help='Input MKV filename')
parser.add_argument('--idx', dest='index', type=int, action="store", default=-1,
				   help='Index of the subtitle to extract')

path = './Extracted'
merger = Merger()

def generate_subs_params(sfiles):
	try:
		params = []
		for i in sfiles:
			params = params + ["-map", "0:s:"+str(i)]
		return params
	except Exception as e:
		print(e)
		return False

def generate_params(filename):
	try:
		sfiles = merger.get_kept_subs()
		newfilename = path+os.sep+filename + '.mkv'

		subparams = generate_subs_params(sfiles)

		ads = ["-metadata:s:s:{}".format(len(sfiles)), "language=eng", "-metadata:s:s:{}".format(len(sfiles)), "handler_name=English", "-metadata:s:s:{}".format(len(sfiles)), "title=Appended", "-max_interleave_delta", "0", "-disposition:s:0", "0", "-disposition:s:{}".format(len(sfiles)), "default", newfilename]
		return (subparams, ads)
	except Exception as e:
		print(e)
		return []

def print_indexes(multi, file:str=""):
	if multi:
		files = glob.glob('*.mkv')
		for f in files:
			print("----------------------------------------------------------------------------------------")
			merger.set_file(f)
			print(f)
			merger.print_language_indexes()
			print("----------------------------------------------------------------------------------------")
	else:
		print("----------------------------------------------------------------------------------------")
		merger.set_file(file)
		print(file)
		merger.print_language_indexes()
		print("----------------------------------------------------------------------------------------")

def extract(file:str, path:str, index:int=-1):
	merger.set_file(file)
	fname = file.split(".")[0]
	ext = ".txt"

	if index>-1:
		streams = merger.get_streams()
		codec_name = streams["streams"][index]['codec_name']
		if codec_name == "ass":
			ext = ".ass"
		elif codec_name == "subrip":
			ext = ".srt"
		else:
			ext = ".txt"
		merger.demux(file, index, path+os.sep+fname+ext)
	else:
		streams = merger.get_streams()
		for i in streams["streams"]:
			if i["codec_type"] == "subtitle":
				if i["codec_name"] == "ass":
					ext = ".ass"
				elif i["codec_name"] == "subrip":
					ext = ".srt"
				else:
					ext = ".txt"
				merger.demux(file, i["index"], path+os.sep+fname+"_"+str(i["index"])+ext)

	return

def append(file:str, subtitle:str, path:str):
	merger.set_file(file)
	fname = file.split(".")[0]

	params = generate_params(fname)
	r = merger.mux(file, subtitle, params)
	return r

def main():
	global path
	args = parser.parse_args()

	if args.print:
		print_indexes(args.multi, args.input)
		return

	if args.folder:
		path = args.folder

	if not path.startswith("./"):
		path = "./"+path

	if not os.path.exists(path):
		os.mkdir(path)

	if args.mux:
		print("Muxxing...")
		append(args.input, args.subtitle, path)
	else:
		print("Demuxxing...")
		if args.multi:
			files = glob.glob('*.mkv')
			for f in files:
				extract(f, path)
		else:
			if args.input:
				extract(args.input, path, args.index)

if __name__ == '__main__':
	main()
