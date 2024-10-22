import json
import re
import pysubs2

WORDS = {}

def load_json(jname):
	try:
		global WORDS
		print("Loading ", jname)
		f = open(jname)
		data = json.load(f)
		WORDS = data
		return True
	except Exception as e:
		return False


def modifySubs(subfile):
	try:
		subs = pysubs2.load(subfile,encoding='utf-8')
		nfilename = "[Delocalized] "+subfile
		for nl, line in enumerate(subs):
			for k,v in WORDS.items():
				line.text = re.sub(k, v, line.text, flags=re.I)
		subs.save(nfilename)
		return nfilename
	except Exception as e:
		print(e)
		return False

def modify_subs_py(subfile, jsonf):
    try:
        if jsonf:
            load_json(jsonf)
        unlocfile = modifySubs(subfile)
        return unlocfile
    except Exception as e:
        print(e)
        return False