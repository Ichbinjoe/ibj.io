
# This is a really stupid text template engine. Please don't laugh too much :(

import os
import re

try:
    os.makedirs("public")
except:
    pass

input_lines = []
with open("index.html") as r:
    input_lines = r.readlines()

with open("public/index.html", "w") as f:
    for line in input_lines:
        match = re.search("^\s*\{\{(.+)\}\}$", line)
        if match:
            with open(match[1]) as content:
                f.write(content.read())
        else:
            f.write(line)


with open("resume.pdf", "rb") as r:
    with open("public/resume.pdf", "wb") as w:
        w.write(r.read())
