from copy_static_to_main import copy_and_override
from generate_page import generate_page

def main():
    copy_and_override("static","public")
    generate_page("content/index.md","template.html","public/index.html")
    generate_page("content/blog/glorfindel/index.md","template.html","public/blog/glorfindel/index.html")
    generate_page("content/blog/majesty/index.md","template.html","public/blog/majesty/index.html")
    generate_page("content/blog/tom/index.md","template.html","public/blog/tom/index.html")
main()