from pprint import pprint
from parser import parse
from runtime import eval, env

if __name__ == "__main__":
    from pprint import pprint

    src = "<not empty>"
    while src:
        src = input("Latym> ")
        if src:
            pprint(parse(src))

