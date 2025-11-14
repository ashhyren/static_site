import sys

from copystatic import copy_refresh
from generate import generate_pages_recursive

static = "static"
public = "public"
template = "template.html"
content = "content"
docs = "docs"

basepath = "/"
if len(sys.argv)>1:
    basepath = sys.argv[1]

def main():
    copy_refresh(static,docs)
    generate_pages_recursive(content, template, docs, basepath)

main()

