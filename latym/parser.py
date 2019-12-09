from lark import Lark, InlineTransformer
from pathlib import Path

from runtime import Symbol

class LangTransformer(InlineTransformer):
    def start(self, *args): 
        return [Symbol.BEGIN, *args]

    def atom(self,args):
        "Numeros se tornam números, qualquer outro token ou é uma string ou um symbol"
        if(str(args)=='verum'):
            return True
        elif(str(args)=='falsus'):
            return False
        else:
            try:
                return int(args)
            except ValueError:
                try:
                    return float(args)
                except ValueError:
                    if(args.type == 'STRING'):
                        res = str(args)[1:-1]
                        res = res.replace("\\n","\n").replace("\\t","\t").replace("\\","")
                        return res
                    else:    
                        return Symbol(str(args))
        
    def condition(self, *args):
        left, comparsion, right = args
        print('PARSER CONDITION:')
        print(left)
        print(comparsion)
        print(right)
        return [left, Symbol(comparsion) ,right]

    def ifstatement(self, condition, block):
        print('block:')
        print(block)
        print('something else:')       
        print(condition)
        #check = eval(condition)
        return [Symbol.IF, condition, block]

    def op(self,args):
        return Symbol(args)

    def binop(self, left, op, right):
        op = str(op)        
        return [Symbol(op),left, right]  

    def prnthss(self, Rparenthesis, unit, Lparenthesis):
        Rparenthesis = str(Rparenthesis)
        Lparenthesis = str(Lparenthesis)
        return [Symbol(Rparenthesis), unit, Symbol(Lparenthesis)]
                


def parse(src: str):
    return parser.parse(src)

def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """

    path = Path(__file__).parent / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=LangTransformer())
    return grammar

parser = _make_grammar()
