import click
from pprint import pprint
from parser import parse as parse_src
from runtime import eval, env
#from . import __version__ as version

'''
    from pprint import pprint
    e = env()
    src = "<not empty>"
    while src:
        src = input("Latym> ")
        if src:
            ast = parse(src)
            ##pprint(ast)
            
            try:
                print(eval(ast, e))
            except Exception as exc:                
                print(exc.__class__.__name__, exc)
'''
@click.command()
@click.argument('file', type=click.File(), required=False)
@click.option('--parse', '-p', is_flag=True)
def main(file, parse):
    from pprint import pprint
    e = env()
    if file is None:
        src = "<not empty>"
        while src:
            src = input("Latym> ")
            if src:
                ast = parse_src(src)
                ##pprint(ast)
                
                try:
                    print(eval(ast, e))
                except Exception as exc:                
                    print(exc.__class__.__name__, exc)
    else:
        ast = parse_src(file.read())
        value = eval(ast,env())
        
            


if __name__ == "__main__":
    main()