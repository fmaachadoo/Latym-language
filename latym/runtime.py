import math
import operator as op
from collections import ChainMap
from types import MappingProxyType

from symbol import Symbol

def eval(x, env=None):
    """
    Avalia as expressões no ambiente de execução dado.
    """

    # Cria ambiente padrão, caso o usuário não passe o argumento opcional "env"
    if env is None:
        env = ChainMap({}, global_env)
    # Avalia tipos atômicos
    if isinstance(x, Symbol):
        return env[x]
    elif isinstance(x, (int, float, bool, str)):
        return x

    head, *args = x

    if head == Symbol.PRINT:        
        for a in args:
            for b in a:
                print( eval(b,env))
                            
        return None

    if head == Symbol.STR:        
        return str(args)

    if head == Symbol.BOOL:
        atom, *rest = args
        if atom=='verum':
            return True
        else:
            return False

    if head == Symbol.IF:
        comparsion, block = args
        if(str(comparsion)=='verum'):
            return eval(block,env)
        elif(str(comparsion)=='falsus'):
            return None
        left, comparsion_type, right = comparsion        

        #As proximas duas linhas foram para realizar o eval novamente dos atomos presentes
        #Para que se alguma variavel especial for usada, não haja comparação de Symbol com int por exemplo
        left = eval(left,env)
        right = eval(right,env)

        if(str(comparsion_type)=='maior quam'):
            proceed =  left > right
        elif(str(comparsion_type)=='minus quam'):
            proceed = left < right
        elif(str(comparsion_type)=='aequalis'):
            proceed = left == right
        elif(str(comparsion_type)=='maior quam que aequalis'):
            proceed = left >= right
        elif(str(comparsion_type)=='minus quam que aequalis'):
            proceed = left <= right
        else:
            raise SyntaxError

        if(proceed):
            return eval(block,env)
        else:
            return None

    if head == Symbol.VAR:
        name, expr = args
        env[name]= eval(expr, env)

    if head == Symbol.PRT:
        x.pop(0)
        head, *args = x
        z = head
        ##print(z)
        y = eval(z,env)
        return eval(y,env)

    ##BINOP OPERATIONS
    if head  == Symbol.ADD:
        op, x, y = x
        return eval(x,env) + eval (y,env)
    elif head == Symbol.SUB:        
        op, x, y = x
        return eval(x,env) - eval (y,env)
    elif head == Symbol.MUL:
        op, x, y = x
        return eval(x,env) * eval(y,env)
    elif head == Symbol.DIV:
        op, x, y = x
        return eval(x,env) / eval(y,env)
    elif head == Symbol.MOD:
        op, x, y = x
        return eval(x,env) % eval(y,env)


    else:
        args = map(eval, args, [env]*len(args))
        args = list(args)
        return env[head](*args)


def env(*args, **kwargs):
    """
    Retorna um ambiente de execução que pode ser aproveitado pela função
    eval().
    Aceita um dicionário como argumento posicional opcional. Argumentos nomeados
    são salvos como atribuições de variáveis.
    Ambiente padrão
    >>> env()
    {...}
        
    Acrescenta algumas variáveis explicitamente
    >>> env(x=1, y=2)
    {x: 1, y: 2, ...}
        
    Passa um dicionário com variáveis adicionais
    >>> d = {Symbol('x'): 1, Symbol('y'): 2}
    >>> env(d)
    {x: 1, y: 2, ...}
    """

    kwargs = {Symbol(k): v for k, v in kwargs.items()}
    if len(args) > 1:
        raise TypeError('accepts zero or one positional arguments')
    elif len(args):
        if any(not isinstance(x, Symbol) for x in args[0]):
            raise ValueError('keys in a environment must be Symbols')
        args[0].update(kwargs)
        return ChainMap(args[0], global_env)
    return ChainMap(kwargs, global_env)

def _make_global_env():
    """
    Retorna dicionário fechado para escrita relacionando o nome das variáveis aos
    respectivos valores.
    """

    dic = {
        **vars(math), # sin, cos, sqrt, pi, ...
        'adde':op.add, 
        'minuas':op.sub, 
        'multiplica':op.mul, 
        'divide':op.truediv, 
        'maior quam':op.gt, 
        'minus quam':op.lt, 
        'maior quam vel aequalis':op.ge, 
        'minus quam vel aequalis':op.le, 
        'aequipar':op.eq, 
        'absoluta':     abs,
        'symbol?': lambda x: isinstance(x, Symbol),
    }
    return MappingProxyType({Symbol(k): v for k, v in dic.items()})

global_env = _make_global_env() 
