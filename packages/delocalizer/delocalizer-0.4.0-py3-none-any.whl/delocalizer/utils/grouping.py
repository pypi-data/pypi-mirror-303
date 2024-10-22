import pysubs2
import json
import re

def load_ass(file_path):
    try:
        subs = pysubs2.load(file_path)
        return subs
    except Exception as e:
        print(f"Error loading file '{file_path}': {e}")
        return None

def intersect(t1, t2):
    if (t1[0] == t2[1] or t1[1] == t2[0]) and (t1[0] != t2[1] or t1[1] != t2[0]):
        return False
    if t1[0] > t2[1] or t2[0] > t1[1]:
        return False
    return True

def generate_item(interval):
    return {
        "interval": interval,
        "nls": [],
        "lines": {"honor":[], "whonor":[]}
    }

def sanitize_string(string):
    # Match substrings enclosed in {}
    pattern = r"\{([^{}]*)\}"

    # Replace all occurrences of the pattern using the replace function
    result = re.sub(pattern, " ", string)
    result = re.sub(r"\\.", " ", result)
    return result

def group_lines_by_time(sub1, sub2):
    intervals = []
    sub_pivot = sub2
    current = 0
    for nl,line in enumerate(sub1):
        if line.type == "Dialogue":
            interval_key = (line.start, line.end)
            line_text = sanitize_string(line.text)
            # Initialize element
            if len(intervals) == 0:
                intervals.append(generate_item(interval_key))
                intervals[-1]["lines"]["honor"].append({"nl":nl, "text":line_text, "start":line.start})
                intervals[-1]["nls"].append(nl)
            else:
                if intersect(interval_key, intervals[-1]["interval"]):
                    intervals[-1]["lines"]["honor"].append({"nl":nl, "text":line_text, "start":line.start})
                    intervals[-1]["nls"].append(nl)
                    intervals[-1]["interval"] = (intervals[-1]["interval"][0], line.end)
                else:
                    intervals.append(generate_item(interval_key))
                    intervals[-1]["lines"]["honor"].append({"nl":nl, "text":line_text, "start":line.start})
                    intervals[-1]["nls"].append(nl)

            # Check intersections
            for nl2,line2 in enumerate(sub_pivot):
                second_interval = (line2.start, line2.end)
                line_text2 = sanitize_string(line2.text)
                #print("Comparing with:",line2.text)
                if intersect(intervals[-1]["interval"], second_interval):
                    intervals[-1]["lines"]["whonor"].append({"nl":current+nl2, "text":line_text2})
                else:
                    if line2.end > line.start:
                        sub_pivot = sub_pivot[nl2:]
                        current = nl2+current
                        break
                    else:
                        continue
        else:
            continue
    return intervals