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


print '\n'
print '\n'

variable_list = {} 				# gives info about parameters and local variables of function with name as per 3AC

for i in range(1,len(dict_symboltable) + 1):
	d = dict_symboltable[i].table

	for key in d:
		if d[key]['type'] == 'function':
			param = {}
			local = {}
			a = dict_symboltable[d[key]['tid']].table
			# print a
			for key1 in a:
				if a[key1]['scopetype'] == 'param':
					param[a[key1]['paramno']] = a[key1]['place']

				if a[key1]['scopetype'] == 'local':
					b = {}
					b['type'] = a[key1]['type']
					if b['type'] == 'array':
						b['size'] = a[key1]['size']
					local[a[key1]['place']] = b

			tempdict = {}
			tempdict['param'] = param
			tempdict['local'] = local

			variable_list[d[key]['place']] = tempdict

for key in variable_list:
	print key, variable_list[key]