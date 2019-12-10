from lark import Lark, InlineTransformer
from pathlib import Path
from runtime import Symbol

class LangTransformer(InlineTransformer):
    def start(self, *args): 
        return [Symbol.BEGIN, *args]
   
    #Definir o tipo int da gramática
    int = int

    #Definir o tipo float da gramática
    float = float

    def boolean(self, booleana):
        return [Symbol.BOOL, booleana]
    
    def string(self, text):
        return [Symbol.STR, str(text)]
    
    def name(self, name):
        return Symbol(name)
    
    def var(self, *args):
        name, value = args
        return [Symbol.VAR, name, value]

    def condition(self, *args):
        left, comparsion, right = args
        return [left, Symbol(comparsion) ,right]

    def ifstatement(self, condition, block):
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
                
    def inprimo(self,*args):
        l_parenthesis, *itens, r_parenthesis = args
        if(str(l_parenthesis)=='posthac die') and str(r_parenthesis)=='usque huc':
            return[Symbol.PRINT, itens]
        else:
            raise SyntaxError   


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
