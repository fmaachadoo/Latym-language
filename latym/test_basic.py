from parser import parse as parse_src
from runtime import eval, env, Symbol
run = lambda src, env=None: eval(parse_src(src), env)


e = env()

class TestLanguage:
    def test_numbers(self):
        assert eval(parse_src('42'),e) == 42
        assert eval(parse_src('3.14'),e) == 3.14
        assert eval(parse_src('-3.14'),e) == -3.14

    def test_atomic(self):
        assert eval(parse_src('verum'),e) is True
        assert eval(parse_src('falsus'),e) is False
        assert parse_src('adde') == Symbol('adde')

    def test_strings(self):
        assert eval(parse_src('"foobar"'),e) == "foobar"
        assert eval(parse_src('"foo bar"'),e) == "foo bar"
        assert eval(parse_src('"esse é um teste"'),e) == "esse é um teste"

    def test_math(self):
        assert eval(parse_src('2 adde 2'),e) == 4
        assert eval(parse_src('2 minuas 2'),e) == 0
        assert eval(parse_src('3 multiplica 2'),e) == 6
        assert eval(parse_src('2 divide 2'),e) == 1
        assert eval(parse_src('2 recide 2'),e) == 0
    
    def test_math_composto(self):
        assert eval(parse_src('2 minuas 2 adde 3 adde 4'),e) == -7
        assert eval(parse_src('2 multiplica 2 minuas 3'),e) == -2
        assert eval(parse_src('posthac die 2 minuas 2 usque huc adde 99'),e) == 99
        assert eval(parse_src('posthac die posthac die 2 adde 2 usque huc minuas 8 usque huc multiplica 4'),e) == -16

    def test_var_assign(self):
        eval(parse_src('imperium aequipar 20'),e)
        eval(parse_src('mundi aequipar 10'),e)
        assert eval(parse_src('imperium'),e) == 20
        assert eval(parse_src('imperium adde 30'),e) == 50
        assert eval(parse_src('mundi adde 30'),e) == 40
        assert eval(parse_src('imperium adde mundi'),e) == 30
        eval(parse_src('imperium aequipar mundi'),e)
        assert eval(parse_src('imperium'),e) == 10

    def test_if(self):
        assert eval(parse_src('si 10 maior quam 2 fac sic 3 adde 3 cis'),e) == 6
        assert eval(parse_src('si 10 minus quam 20 fac sic 3 adde 10 cis'),e) == 13
        
        
        
        
       
       