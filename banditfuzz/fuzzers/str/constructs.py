from ..construct import Construct
import random

class STR_CONCAT(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'str'
        self.sig = [
            'str', 'str',
            'str'
        ]
        self.chainable = True
    def __str__(self):
        return "str.++"
    __repr__ = __str__

class STR_LEN(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'int'
        self.sig = [
            'str',
            'int'
        ]
        self.chainable = False
    def __str__(self):
        return "str.len"
    __repr__ = __str__
class STR_LEX_ORD(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'bool'
        self.sig = [
            'str', 'str',
            'bool'
        ]
        self.chainable = True
    def __str__(self):
        return "str.<"
    __repr__ = __str__
class STR_TO_REG(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'str',
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "str.to_re"
    __repr__ = __str__
class STR_IN_REG(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'bool'
        self.sig = [
            'str', 'reg',
            'bool'
        ]
        self.chainable = False
    def __str__(self):
        return "str.in_re"
    __repr__ = __str__
class STR_NONE(Construct):
    def __init__(self):
        self.arity = 0
        self.type = 'reg'
        self.sig = [
            # no input
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "re.none"
    __repr__ = __str__
class STR_RE_ALL(Construct):
    def __init__(self):
        self.arity = 0
        self.type = 'reg'
        self.sig = [
            #None
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "re.all"
    __repr__ = __str__
class STR_RE_ALLCHAR(Construct):
    def __init__(self):
        self.arity = 0
        self.type = 'reg'
        self.sig = [
            #None
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "re.allchar"
    __repr__ = __str__
class STR_RE_CONCAT(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'reg'
        self.sig = [
            'reg', 'reg'
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.++"
    __repr__ = __str__
class STR_RE_UNION(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'reg'
        self.sig = [
            'reg', 'reg',
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.union"
    __repr__ = __str__
class STR_RE_INTER(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'reg'
        self.sig = [
            'reg', 'reg',
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.inter"
    __repr__ = __str__
class STR_RE_KLEENE(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'reg',
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "re.*"
    __repr__ = __str__
class STR_LEQ(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'bool'
        self.sig = [
            'str', 'str'
            'bool'
        ]
        self.chainable = True
    def __str__(self):
        return "str.<="
    __repr__ = __str__
class STR_AT(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'str'
        self.sig = [
            'str', 'int'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.at"
    __repr__ = __str__
class STR_SUBSTR(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'str'
        self.sig = [
            'str', 'int', 'int'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.substr"
    __repr__ = __str__
class STR_PREFIXOF(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'bool'
        self.sig = [
            'str', 'int', 'int'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.substr"
    __repr__ = __str__
class STR_SUFFIXOF(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'bool'
        self.sig = [
            'str', 'str'
            'bool'
        ]
        self.chainable = False
    def __str__(self):
        return "str.suffixof"
    __repr__ = __str__

class STR_CONTAINS(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'bool'
        self.sig = [
            'str', 'str'
            'bool'
        ]
        self.chainable = False
    def __str__(self):
        return "str.contains"
    __repr__ = __str__

class STR_INDEXOF(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'int'
        self.sig = [
            'str', 'str','int'
            'int'
        ]
        self.chainable = False
    def __str__(self):
        return "str.indexof"
    __repr__ = __str__
class STR_REPLACE(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'str'
        self.sig = [
            'str', 'str','str'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.replace"
    __repr__ = __str__
class STR_REPLACE_ALL(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'str'
        self.sig = [
            'str', 'str','str'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.replace_all"
    __repr__ = __str__
class STR_REPLACE_RE(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'str'
        self.sig = [
            'str', 'reg','str'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.replace_re"
    __repr__ = __str__
class STR_REPLACE_RE_ALL(Construct):
    def __init__(self):
        self.arity = 3
        self.type = 'str'
        self.sig = [
            'str', 'reg','str'
            'str'
        ]
        self.chainable = False
    def __str__(self):
        return "str.replace_re_all"
    __repr__ = __str__
class STR_REG_COMP(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'reg', 
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "re.comp"
    __repr__ = __str__
class STR_REG_DIFF(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'reg'
        self.sig = [
            'reg', 'reg'
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.diff"
    __repr__ = __str__
class STR_REG_COMP(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'reg', 
            'reg'
        ]
        self.chainable = False
    def __str__(self):
        return "re.comp"
    __repr__ = __str__
class STR_REG_DIFF(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'reg'
        self.sig = [
            'reg', 'reg'
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.diff"
    __repr__ = __str__
class STR_REG_OPT(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'reg',
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.opt"
    __repr__ = __str__
class STR_REG_RANGE(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'str', 'str'
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.range"
    __repr__ = __str__
class STR_REG_RANGE(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'str', 'str'
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return "re.range"
    __repr__ = __str__
class STR_RE_LOOP(Construct):
    def __init__(self):
        self.arity = 2
        self.type = 'reg'
        self.sig = [
            'reg', 'reg'
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return f"(_ re.loop {random.randint(0,10**6)} {random.randint(0,10**6)})" #a bit hacky... suggestions?
    __repr__ = __str__
class STR_RE_POW(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'reg'
        self.sig = [
            'reg', 
            'reg'
        ]
        self.chainable = True
    def __str__(self):
        return f"(_ re.^ {random.randint(0,10**6)})" #a bit hacky... suggestions?
    __repr__ = __str__
class STR_IS_DIGIT(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'str'
        self.sig = [
            'str',
            'bool'
        ]
        self.chainable = True
    def __str__(self):
        return "str.is_digit"
    __repr__ = __str__
class STR_TO_CODE(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'int'
        self.sig = [
            'str',
            'int'
        ]
        self.chainable = True
    def __str__(self):
        return "str.to_code"
    __repr__ = __str__
class STR_FROM_CODE(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'str'
        self.sig = [
            'int',
            'str'
        ]
        self.chainable = True
    def __str__(self):
        return "str.from_code"
    __repr__ = __str__
class STR_TO_INT(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'int'
        self.sig = [
            'str',
            'int'
        ]
        self.chainable = True
    def __str__(self):
        return "str.to_int"
    __repr__ = __str__
class STR_FROM_INT(Construct):
    def __init__(self):
        self.arity = 1
        self.type = 'str'
        self.sig = [
            'int',
            'str'
        ]
        self.chainable = True
    def __str__(self):
        return "str.from_int"   
    __repr__ = __str__