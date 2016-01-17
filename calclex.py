# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from collections import defaultdict
# List of token names.   This is always required

reserved = {
	'if' : 'KEYWORD_IF',
	'else' : 'KEYWORD_ELSE',
	'for' : 'KEYWORD_FOR',
	'while' : 'KEYWORD_WHILE',
	'do' : 'KEYWORD_DO',
	'break' : 'KEYWORD_BREAK',
	'var' : 'KEYWORD_VAR',
	'val' : 'KEYWORD_VAL',
	'return' : 'KEYWORD_RETURN',
	'type' : 'KEYWORD_TYPE',
	'import' : 'KEYWORD_IMPORT',
	'class' : 'KEYWORD_CLASS',
	'private' : 'KEYWORD_PRIVATE',
	'protected' : 'KEYWORD_PROTECTED',
	'define' : 'KEYWORD_DEFINE',
	'null' : 'KEYWORD_NULL',
	'object' : 'KEYWORD_OBJECT',
	'package' : 'KEYWORD_PACKAGE',
	'case' : 'KEYWORD_CASE',

	'println' : 'KEYWORD_PRINTLN',
	'print' : 'KEYWORD_PRINT',
	'main' : 'KEYWORD_MAIN',
	'Array' : 'KEYWORD_ARRAY',
	'def' : 'KEYWORD_DEF',
	'args' : 'KEYWORD_ARGS',
	'String': 'KEYWORD_STRING'
}

tokens = [
   'LPAREN', 'RPAREN','BLOCKBEGIN','BLOCKEND',
   'LBRAC','RBRAC',
   'COLON','COMMA','TERMINATOR','INST','STRINGID',
   'BINARY',
   'AROP', 'RELOP','BINOP','LOGOP','ASOP',
   'IDENTIFIER',
   'COMMENT','COMMENT_BEGIN','COMMENT_END',
    'STRING','NUMBER'
] + list(reserved.values())


# Regular expression rules for simple tokens
t_BINARY = r'true|false'

t_AROP   = r'[-%+*/]'
t_ASOP = r'='
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_BLOCKBEGIN     = r'\{'
t_BLOCKEND     = r'\}'
t_LBRAC   = r'\['
t_RBRAC     = r'\]'
t_COLON     = r'\:'
t_COMMA     = r'\,'
t_TERMINATOR     = r'\;'
t_INST     = r'\.'
t_STRINGID     = r'\"'

t_RELOP = r'==|<=|>=|<|>|!='

t_BINOP = r'&|\||~|<<|>>|>>>'

t_LOGOP = r'&&|!|\|\|'

t_STRING = r'".+"'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t							

''' Number definition modified '''

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
object Test {
   def main(args: Array[String]) {
      var x = 10;

      if( x < 20 ){
         println("This is if statement");
      }
   }
}
'''

# Give the lexer some input
lexer.input(data)

d = {}
e = defaultdict(list)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    if(tok.type in d):
    	d[tok.type] = d[tok.type]+1
    else:
    	d[tok.type] = 1

    e[tok.type].append(tok.value)

for k in d.keys():
	e[k] = set(e[k])

for k in d.keys():
	print k,d[k],e[k]
