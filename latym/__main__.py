from pprint import pprint
from parser import parse
from runtime import eval, env

if __name__ == "__main__":
    from pprint import pprint

    src = "<not empty>"
    while src:
        src = input("Latym> ")
        if src:
            ast = parse(src)
            #pprint(ast)
            
            try:
                print(eval(ast, env))
            except Exception as exc:                
                print(exc.__class__.__name__, exc)


