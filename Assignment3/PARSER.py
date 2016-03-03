import LEXER
import re
import os
import sys
from GRAMMAR import *
import ply.yacc as yacc

tokens = LEXER.tokens
START = "ProgramStructure"

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
		global START
		if (len(current_node.children)==0):
			return;
		SSPL = START.split()
		print SSPL
		Index = SSPL.index(current_node.name)

		S = ""
		for i in current_node.children:
			S += str(i.name)
			S += " "
		S1 = re.sub(current_node.name[::-1],S[::-1],START[::-1],1)
		START = S1[::-1]

		SPL = str(current_node.children[-1].name)

		if current_node.name not in LEAVES:
			index1 = START.find(SPL)
			index2 = START[::-1].find(SPL[::-1])
			index2 = index2 * (-1)
			print >> file, START[0:index1] + " <b> " + SPL + "</b>" + START[index2:] + "<br>"
		else:
			Suf = " ".join(SSPL[Index+1:])
			if Index!=0:
				Pre = " ".join(SSPL[:Index-1])
				print >> file, str(Pre) + " <b> " + str(SSPL[Index-1]) + " </b> " + str(current_node.children[-1].name) + " " + str(Suf) + "<br>"
			else:
				print >> file, str(current_node.children[-1].name) + " " + str(Suf) + "<br>"

			
		if current_node.name not in LEAVES:
			for i in reversed(current_node.children):
				printnodes(i,file)

f = open(sys.argv[1],"r")
code_full = f.read()
f.close()

node = parser.parse(code_full)
print node
f = open(sys.argv[2],"w+")

if node:
	print >> f,'''<!DOCTYPE html>
<html>
<body>'''
	print >>f,"<b>" , START,"</b> <br>"
	printnodes(node,f)
	print >> f, '''</body>
</html>'''