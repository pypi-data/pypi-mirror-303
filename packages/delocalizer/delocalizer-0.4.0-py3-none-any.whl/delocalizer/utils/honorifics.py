import pysubs2
import json
import re
import os
from grouping import group_lines_by_time

class HonorificFixer:
    def __init__(self, hfile:str=None, bfile:str=None, tfile:str=None):
        self.honorific_file = hfile
        self.base_file = bfile
        self.tokens_file = tfile
        self.ACCEPTED_STYLES = ["Subtitle", "Regular", "Alt"]
        self.TOKENS = []
        self.HONOR = {
            "kun": [],
            "chan": [],
            "senpai": [],
            "sensei": ["Teacher", "Master", "Doctor", "Professor"],
            "dono": [],
            "san": ["Mr.", "Ms.", "Miss", "Mister"],
            "sama": ["Lady", "Lord", "Sir", "Ma'am"],
            "nee": ["Big sis", "Sis"],
            "onee": ["Big sis", "Sis"],
            "neechan": ["Big sis", "Sis"],
            "oneechan": ["Big sis", "Sis"],
            "neesan": ["Big sis", "Sis"],
            "oneesan": ["Big sis", "Sis"],
            "nii": ["Big bro", "Bro"],
            "onii": ["Big sis", "Sis"],
            "niichan": ["Big sis", "Sis"],
            "oniichan": ["Big sis", "Sis"],
            "niisan": ["Big sis", "Sis"],
            "oniisan": ["Big sis", "Sis"]
        }

    def load_json(self, name):
        f = open(name, encoding="utf-8")
        jfile = json.load(f)

        return jfile

    def save_result(self, result, name):
        with open(name, "w", encoding="utf8") as output:
            json.dump(result, output, ensure_ascii=False, indent=2)

    def load_subs(self, file):
        subs = pysubs2.load(file, encoding="utf-8")

        return subs

    def compare_styles(self, style: str):
        for i in self.ACCEPTED_STYLES:
            if style.startswith(i):
                return True
        return False

    def find_exact_name_in_string(self, name, string):
        pattern = r"\b" + re.escape(name) + r"\b"
        return bool(re.search(pattern, string, flags=re.I))

    def check_tokens(self, text):
        for i in self.TOKENS:
            if self.find_exact_name_in_string(i, text):
                return True
        return False

    def sanitize_string(self, string):
        # Match substrings enclosed in {}
        pattern = r"\{([^{}]*)\}"

        # Replace all occurrences of the pattern using the replace function
        result = re.sub(pattern, " ", string)
        result = re.sub(r"\\.", " ", result)
        return result

    def reduce_subs(self, subs):
        lines = []
        for i in subs:
            for j in i["lines"]["honor"]:
                if self.check_tokens(j["text"]):
                    lines.append(i)
                    break

        return lines

    def tokenize(self, words):
        tokens = list()
        for i in words:
            for j in i.split(" "):
                tokens.append(j)

        return set(tokens)

    # Compare subs
    def compare_subs(self, subs):
        notpaireds = []
        result = {}
        for i in subs:
            pairs,notpaired = self.find_matching_pairs(i["lines"]["honor"], i["lines"]["whonor"])
            notpaireds += notpaired
            #if len(i["honor"]) == 1:
            for i,j in pairs:
                for h in self.search_tokens(i["text"]):
                    if "-" in h:
                        name = self.clean_left(h.split("-")[-2])
                        honorific = self.clean_right(h.split("-")[-1])

                        new_word = name+"-"+honorific

                        if not new_word in j["text"]:
                            j["text"] = self.replace_word(name, new_word, j["text"])
                            j["text"] = self.replace_english_honorifics(j["text"])
                            result[j["nl"]] = j

        return result,notpaireds

    def find_matching_pairs(self, list1, list2):
        paired = []
        pairs = []
        not_paired = []

        # Create a set of words for quick lookup
        words_set = set(self.TOKENS)

        # Sort the lists by the 'order' field
        list1.sort(key=lambda x: x['nl'])
        list2.sort(key=lambda x: x['nl'])

        # Iterate over the lists to find matching pairs
        for item1 in list1:
            item1_text = item1['text']
            matched_word = None
            for word in words_set:
                pattern = r"\b" + re.escape(word) + r"\b"
                if re.search(pattern, item1_text):
                    matched_word = word
                    break
            if matched_word is None:
                continue
                #not_paired.append(item1)
            else:
                matched = False
                for item2 in list2:
                    if item2 not in paired:
                        item2_text = item2['text']
                        pattern = r"\b" + re.escape(matched_word) + r"\b"
                        if re.search(pattern, item2_text):
                            paired.append(item1)
                            paired.append(item2)
                            pairs.append([item1, item2])
                            matched = True
                            break
                if not matched:
                    not_paired.append(item1)

        # for item2 in list2:
        #     if item2 not in paired:
        #         not_paired.append(item2)

        return pairs, not_paired

    def search_tokens(self, text):
        for i in text.split(" "):
            if self.check_tokens(i):
                yield i

    def clean_left(self, word):
        r = ""
        for i in word[::-1]:
            if i.isalpha():
                r += i
            else:
                break

        return r[::-1]

    def clean_right(self, word):
        r = ""
        for i in word:
            if i.isalpha():
                r += i
            else:
                break

        return r

    def replace_word(self, k,v, text):
        return re.sub(k, v, text, flags=re.I)

    def replace_english_honorifics(self, text, honorific=""):
        honorifics = ["Mr.", "Ms.", "Miss", "Mister", "Lady", "Lord", "Big sis", "Big bro"]
        for i in honorifics:
            text = self.replace_word(i, "", text)

        return text

    def modify_subs(self, subfile, changes, name):
        try:
            nfilename = "Modified_"+name
            print(nfilename)
            for nl, line in enumerate(subfile):
                if nl in changes.keys():
                    print("Changing:",line.text,"for",changes[nl]["text"])
                    line.text = changes[nl]["text"].strip()
            subfile.save(nfilename)
            return nfilename
        except Exception as e:
            print(e)
            return False

    def format_milliseconds(self, milliseconds):
        seconds = milliseconds // 1000
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def print_not_paired(self, notpaired):
        for i in notpaired:
            for h in self.search_tokens(i["text"]):
                if "-" in h:
                    print(self.format_milliseconds(i["start"]), i["text"])
                    break

    def main(self):
        print("Start")
        os.chdir('../Subs')
        jfile = self.load_json("./"+self.tokens_file)
        self.TOKENS = self.tokenize(jfile)
        filename_es = self.honorific_file
        filename_en = self.base_file

        subs_en = self.load_subs("./"+filename_en)

        subs_es = self.load_subs("./"+filename_es)

        # First to send the file with honorifics
        grouped = group_lines_by_time(subs_es, subs_en)
        reduced = self.reduce_subs(grouped)

        changes, nps = self.compare_subs(reduced)
        self.print_not_paired(nps)
        if changes:
            self.modify_subs(subs_en, changes, filename_en)

if __name__ == '__main__':
    honor = HonorificFixer("[DantalianSubs] Mato Seihei no Slave - 07.ass", "[EMBER] Mato Seihei no Slave - 07.ass", "mato.json")
    honor.main()