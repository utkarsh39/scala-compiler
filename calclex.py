# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required

reserved = {
	'if' : 'IF',
	'else' : 'ELSE',
	'for' : 'FOR',
	'while' : 'WHILE',
	'do' : 'DO',
	'break' : 'BREAK',
	'var' : 'VAR',
	'val' : 'VAL',
	'return' : 'RETURN',
	'type' : 'TYPE',
	'import' : 'IMPORT',
	'class' : 'CLASS',
	'private' : 'PRIVATE',
	'protected' : 'PROTECTED',
	'define' : 'DEFINE',
	'null' : 'NULL',
	'object' : 'OBJECT',
	'package' : 'PACKAGE',
	'case' : 'CASE'
}

tokens = [
   'LPAREN', 'RPAREN',
   'BINARY',
   'AROP', 'RELOP','BINOP','LOGOP', 
   'IDENTIFIER',
   'COMMENT','COMMENT_BEGIN','COMMENT_END',
    'STRING','NUMBER'
] + list(reserved.values())


# Regular expression rules for simple tokens
t_BINARY = r'true|false'

t_AROP   = r'[-%+*/]'

t_LPAREN     = r'\('
t_RPAREN     = r'\)'
'''t_'{'     = r'\{'
t_'}'     = r'\}'
t_'['     = r'\['
t_']'     = r'\]'
t_':'     = r'\:'
t_','     = r'\,'
t_';'     = r'\;'
t_'.'     = r'\.'
t_'"'     = r'\"'
'''
t_RELOP = r'==|<=|>=|<|>|!='

t_BINOP = r'&|\||~|<<|>>|>>>'

t_LOGOP = r'&&|!|\|\|'

t_STRING = r'".+"'

t_NUMBER = r'[0-9]+.?[0-9]*E.[+-]?[0-9]*'

def t_IDENTIFIER(t):
 	r'[_a-zA-Z][_a-zA-Z0-9]*'
 	t.type = reserved.get(t.value,'IDENTIFIER')
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

# Test it out
data = '''
3 + 4 * 10
  + -20 *2
  for
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.value)