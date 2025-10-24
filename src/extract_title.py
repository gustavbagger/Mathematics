import re

def extract_title(markdown):
    lines = markdown.split("\n")
    matches = list()
    for line in lines:
        matches.extend(re.findall(r"^#([^#].*)",line))
    try:
        return matches[0].strip()
    except:
        raise Exception("Error: no header")

