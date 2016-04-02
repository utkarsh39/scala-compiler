import LEXER
import re
import os
import sys
from GRAMMAR import *
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

# Unomment to enable generation of Parse Tree
'''def printnodes1(current_node, file):
    #sys.stderr.write(str(current_node.name) + "\n")
    if (len(current_node.children)==0):
        return;
    for i in current_node.children:
        flag=0
        if (isinstance(i.name, basestring)):
            matchObj = re.match( r'".*"', i.name , re.M|re.I)
            if matchObj:
                if (len(matchObj.group())==len(i.name)):
                    flag=1
                    print >> file, str(current_node.id)+" [label=\""+str(current_node.name)+"\"];"+str(i.id)+" [label=\""+str((matchObj.group()).replace('"', '\\\"'))+"\"];"+str(current_node.id)+"->"+str(i.id)
        if flag==0 :
            print >> file, str(current_node.id)+" [label=\""+str(current_node.name)+"\"];"+str(i.id)+" [label=\""+str(i.name)+"\"];"+str(current_node.id)+"->"+str(i.id)
        flag=0
        
    for i in current_node.children:
        printnodes1(i, file)'''


def printnodes(current_node,file):
		global START
		if (len(current_node.children)==0):
			return;

		SSPL = START
		for i,item in reversed(list(enumerate(START))):
			if item == current_node.name:
				Index = i
				break
			
		S = []
		for i in current_node.children:
			S.append(str(i.name))

		START = START[:Index] + S + START[Index+1:]
		SPL = str(current_node.children[-1].name)

		if current_node.name not in LEAVES:
			index1=0
			Pre = START
			for i,item in reversed(list(enumerate(Pre))):
				if item == SPL:
					index1 = i
					break


			Pre = " ".join(Pre[0:index1])
			print >> file, " ".join(START[:Index]) + " <font color=\"green\"> " + " ".join(S[:-1]) + " <b> " + SPL + " </font> </b> <font color = \"red\"> " + " ".join(START[index1+1:]) + " </font> <br><br>"
		
		else:
			Suf = " ".join(SSPL[Index+1:])
			if Index!=0:
				Pre = " ".join(SSPL[:Index-1])
				print >> file, str(Pre) + " <b> " + str(SSPL[Index-1]) + " </b> " + " <font color = \"red\"> " + str(current_node.children[-1].name) + " " + str(Suf) + "</font> <br><br>"
			else:
				print >> file, str(current_node.children[-1].name) + " <font color = \"red\">" + str(Suf) + "</font><br><br>"

			
		if current_node.name not in LEAVES:
			for i in reversed(current_node.children):
				printnodes(i,file)


f = open(sys.argv[1],"r")
code_full = f.read()
f.close()

node = parser.parse(code_full)
f = open(sys.argv[1][5:-6] + ".html","w+")

#Uncomment to enable genearion of Parse Tree
#if node:
#  print >> f, "digraph G {"
#  printnodes1(node, f)
#  print >> f, "}"

if node:
	print >> f,'''<!DOCTYPE html>
<html>
<body>'''
	print >>f,"<b>" , START[0],"</b> <br><br>"
	printnodes(node,f)
	print >> f, '''</body>
</html>'''

f.close()
