import LEXER
import re
import os
import sys
from backpatch import *
import ply.yacc as yacc

tokens = LEXER.tokens
START = ['ProgramStructure']

parser = yacc.yacc()

#ERROR
def p_error(p):
  
    flag=-1;

    print("Syntax error at '%s'" % p.value),
    print('\t Error: {}'.format(p))

    while 1:
        tok = yacc.token()             # Get the next token
        if not tok:
            flag=1
            break
        if tok.type == 'STATE_END': 
            flag=0
            break

    if flag==0:
        yacc.errok()
        return tok
    else:
        yacc.restart()


f = open(sys.argv[1],"r")
code_full = f.read()
f.close()

node = parser.parse(code_full)
emit(['exit', '0'])

for i in range(1,len(TAC)):
	print i,
	for j in range(len(TAC[i])):
		print TAC[i][j],
	print
