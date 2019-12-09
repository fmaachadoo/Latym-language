class Symbol:
    """
    Representa um símbolo Lisp.
    Diferentemente de strings, símbolos com o mesmo valor possuem a mesma identidade.
    """

    data : str
    CACHE = {}

    def __new__(cls, data):
        if isinstance(data, Symbol):
            return data
        try:
            return cls.CACHE[data]
        except KeyError:
            cls.CACHE[data] = new = super().__new__(cls)
            new._data = data
            return new

    def __str__(self):
        return self._data

    def __repr__(self):
        return self._data

    def __hash__(self):
        return id(self._data)

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self._data == other._data
        return NotImplemented


# Formas especiais
'''
Symbol.QUOTE = Symbol('quote')
Symbol.LET = Symbol('let')
'''
Symbol.IF = Symbol('si')
Symbol.VAR = Symbol('aequipar')
'''
Symbol.LAMBDA = Symbol('lambda')
Symbol.DEFINE = Symbol('define')
'''
Symbol.BEGIN = Symbol('begin')


# Funções úteis
'''
Symbol.LIST = Symbol('list')
'''
Symbol.ADD = Symbol('adde')
Symbol.SUB = Symbol('minuas')
Symbol.MUL = Symbol('multiplica')
Symbol.DIV = Symbol('divide')
Symbol.MOD = Symbol('recide')
Symbol.PRT = Symbol('posthac die')
Symbol.MNQ = Symbol('minus quam')
Symbol.MAQ = Symbol('maior quam')
Symbol.PRINT = Symbol('inprimo')
Symbol.STR = Symbol('scriptum')


class _Var:
    def __getattr__(self, attr):
        return Symbol(attr)

    def __repr__(self):
        return 'var'

var = _Var()