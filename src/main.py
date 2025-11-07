from copy_static_to_main import copy_and_override
from generate_page import generate_page, generate_pages_recursive
import sys

def main():
    copy_and_override("static","docs")
    generate_pages_recursive("content/","template.html","docs/",basepath=sys.argv[1])
main()