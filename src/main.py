from copystatic import copy_refresh
from generate import generate_page

def main():
    copy_refresh("static","public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()

