import pysubs2
import argparse
import json
import glob
import os
from .utils.lambda_fetch import get_data

cyenv = os.getenv("CYENV", 'true').lower() in ('true', '1') #os.getenv('CYENV')

if cyenv:
    from modify_subs import overwrite_subs as modify_subs_py
else:
    from .md_subs import modify_subs_py
from subdeloc_tools.modules.merger import Merger

class Delocalizer:

    def __init__(self):
        self.LANGUAGES = ["eng", "spa"]
        self.ERRORS = []
        self.index = 0
        self.language = "eng"
        self.keep_subs = False
        self.nomux = False
        self.wordsfile = None
        self.file = None
        self.subfile = None
        self.merger = Merger()

    def modify_subs(self, f):
        try:
            name = modify_subs_py(str(f), str(self.wordsfile))
            if name:
                return name
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def shift_subs(self, delta):
        try:
            subs1 = pysubs2.load(self.file, encoding="utf-8")
            subs1.shift(s=delta)
            msub = "m_" + self.file
            subs1.save(msub)

            return msub
        except Exception as e:
            print(e)
            return False

    def prepare_data(self, args):
        try:
            if args.words:
                lambda_url = os.getenv("JSONLAMBDA", False)
                if lambda_url:
                    words = get_data(lambda_url)
                    self.wordsfile = words
                else:
                    raise Exception("No Lambda url in environment")
            else:
                if args.jfile:
                    self.wordsfile = args.jfile
                else:
                    raise Exception("No JSON file indicated")
            if args.language:
                if args.language in LANGUAGES:
                    self.language = args.language
            if args.index and args.index > 0:
                self.index = args.index
            if args.keep_subs:
                self.keep_subs = True
            if args.nomux:
                self.nomux = True

            return True
        except Exception as e:
            print(e)
            return False

    def print_errors(self):
        try:
            if len(ERRORS) > 0:
                print("There were errors:")
                for i in ERRORS:
                    print("-", i)
            else:
                print("No errors")
        except Exception as e:
            print(e)

    def get_index(self):
        try:
            streams = self.merger.get_streams()
            index = self.merger.get_language_index(self.language, selected_index=self.index)

            return index
        except Exception as e:
            print(e)
            return -1

    def generate_subs_params(self, sfiles):
        try:
            params = []
            for i in sfiles:
                params = params + ["-map", "0:s:"+str(i)]
            return params
        except Exception as e:
            print(e)
            return False

    def generate_params(self):
        try:
            sfiles = self.merger.get_kept_subs()
            filename = os.path.splitext(self.file)[0]
            newfilename = "."+os.sep+"Finished"+os.sep+filename + '.mkv'

            subparams = self.generate_subs_params(sfiles)

            ads = ["-metadata:s:s:{}".format(len(sfiles)), "language=eng", "-metadata:s:s:{}".format(len(sfiles)), "handler_name=English", "-metadata:s:s:{}".format(len(sfiles)), "title=Unlocalized", "-max_interleave_delta", "0", "-disposition:s:0", "0", "-disposition:s:{}".format(len(sfiles)), "default", newfilename]
            return (subparams, ads)
        except Exception as e:
            print(e)
            return []

    def clean_files(self, file, f):
        try:
            if not self.keep_subs:
                os.remove(file)
            else:
                newfilename = "."+os.sep+"Subs"+os.sep+f.split(".")[0] + '.' + file.split(".")[1]
                os.rename(file, newfilename)

            return True
        except Exception as e:
            print(e)
            return False

    def delocalize(self, f):
        try:
            index = -1
            print("Extracting: ", f)
            # Initial tasks
            self.file = f
            self.merger.set_file(f)
            index = self.get_index()

            if index > -1:
                print("Subtitles found at", index)
                if self.merger.codec_name == "ass":
                    outputf = "subfile.ass"
                elif self.merger.codec_name == "subrip":
                    outputf = "subfile.srt"
                else:
                    raise Exception("Subtitle codec not recognized")
                    
                self.subfile = self.merger.demux(self.file, index, outputf)
                if self.subfile:
                    print("Delocalizing...")
                    unloc_sub = self.modify_subs(self.subfile)
                    # For reference
                    # word_json = self.get_replace_file(self.subfile)
                    # unloc_sub = self.replace_words(word_json)

                    if unloc_sub:
                        # Remove sub file and Mux unlocalized
                        os.remove(self.subfile)
                        if self.nomux:
                            self.clean_files(unloc_sub, f)
                        else:
                            print("Muxxing with file:", unloc_sub)
                            params = self.generate_params()
                            print("params", params)
                            r = self.merger.mux(f, unloc_sub, params)
                            if r:
                                #Clean
                                self.clean_files(unloc_sub, f)
                            else:
                                print("Failed to mux sub!")
                                self.ERRORS.append(str(self.file))
                    else:
                        print("Failed to modify subs!")
                        self.ERRORS.append(str(self.file))
                else:
                    print("Failed to extract Subtitle!")
                    self.ERRORS.append(str(self.file))
            else:
                print("Subtitles not found!")
                self.ERRORS.append(str(self.file))
            return True
        except Exception as e:
            print(e)
            return False

    def delocalize_all(self):
        try:
            files = glob.glob('*.mkv')
            for f in files:
                status = self.delocalize(f)
            return True
        except Exception as e:
            print(e)
            return False