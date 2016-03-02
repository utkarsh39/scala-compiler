import LEXER
import re
import os
import sys
from Ass import *
import ply.yacc as yacc

tokens = LEXER.tokens

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

def printnodes(current_node,file):
		if (len(current_node.children)==0):
			return;
		print >> file, str(current_node.name) + " --> ",
		for i in current_node.children:
			print >> file, str(i.name) + " ",
		print >> file, "<br>"
		for i in reversed(current_node.children):
			printnodes(i,file)

f = open(sys.argv[1],"r")
code_full = f.read()
f.close()

node = parser.parse(code_full)
f = open(sys.argv[2],"w+")

if node:
	print >> f,'''<!DOCTYPE html>
<html>
<body>'''
	printnodes(node,f)
	print >> f, '''</body>
</html>'''