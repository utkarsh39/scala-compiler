# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'FOR','WHILE','IF','ELSE','DO','BREAK',
   'TRUE','FALSE',
   'TYPE','VAR','VAL',
   'RETURN',   'IMPORT',   'CLASS',  'DEFINE', 'PRIVATE', 'PROTECTED','NULL',   'CASE',   'OBJECT','PACKAGE',
   'PLUS',   'MINUS',   'TIMES',   'DIVIDE', 'MOD',  
   '(',')','{','}', '[',']', ':'  , ',' ,'.'  ,';'  , '"'
   'IDENTIFIER',
   'EQ','LEQ','GEQ','LESS','GREATER','NEQ',
   'AND','OR','COMPLEMENT', 'XOR','LSHIFT','RSHIFT','RRSHIFT',
   'LAND','LOR','LNOT',
   'COMMENT','COMMENT_BEGIN','COMMENT_END',
    'STRING','NUMBER'
) # += Constanst int decimal real

# Regular expression rules for simple tokens
t_FOR     = r'for'
t_WHILE   = r'while'
t_IF      = r'if'
t_ELSE    = r'else'
t_DO      = r'do'
t_BREAK   = r'break'

t_TRUE    = r'true'
t_FALSE   = r'false'

t_TYPE    = r'type'
t_VAR     = r'var'
t_VAL     = r'val'
t_RETURN  = r'return'
t_IMPORT  = r'import'
t_CLASS   = r'class'
t_DEFINE  = r'define'
t_PRIVATE = r'private'
t_PROTECTED = r'protected'
t_NULL      = r'null'
t_CASE      = r'case'
t_OBJECT    = r'object'
t_PACKAGE   = r'package'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'\%'  ##


t_'('     = r'\('
t_')'     = r'\)'
t_'{'     = r'\{'
t_'}'     = r'\}'
t_'['     = r'\['
t_']'     = r'\]'
t_':'     = r'\:'
t_','     = r'\,'
t_';'     = r'\;'
t_'.'     = r'\.'
t_'"'     = r'\"'

t_EQ  = r'=='
t_LEQ = r'<='
t_GEQ = r'>='
t_LESS = r'<' 
t_GREATER = r'>'
t_NEQ = r'!='

t_AND = r'&' 
t_OR = r'|'
t_COMPLEMENT = r'~'
t_XOR = 'r^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_RRSHIFT = 'r>>>'

t_LAND = r'&'
t_LOR = r'||'
t_LNOT = r'!'

t_COMMENT = r'//'
t_COMMENT_BEGIN = r'/*'
t_COMMENT_END = r'*/'

t_STRING = r""
t_NUMBER = r'[0-9]+.?[0-9]*E.[+-]?[0-9]*'   #2.

t_IDENTIFIER = r'[_a-zA-Z][_a-zA-Z0-9]*'



# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()