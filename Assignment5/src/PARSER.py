import LEXER
import re
import os
import sys
from backpatch import *
import ply.yacc as yacc
import cPickle as pickle

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

function_list = {} 				# gives info about parameters and local variables of function with name as per 3AC
variable_list = {}

for i in range(1,len(dict_symboltable) + 1):
	d = dict_symboltable[i].table

	for key in d:
		if d[key]['type'] == 'function':
			param = {}
			local = {}
			a = dict_symboltable[d[key]['tid']].table
			# print a
			paramsize = 0
			localsize = 0
			# print a
			for key1 in a:
				if key1 == 'return':
					continue

				if a[key1]['scopetype'] == 'param':
					param[a[key1]['paramno']] = a[key1]['place']
					variable_list[a[key1]['place']] = d[key]['place']
					paramsize += 4

				if a[key1]['scopetype'] == 'local':
					b = {}
					b['type'] = a[key1]['type']
					if b['type'] == 'array':
						b['size'] = a[key1]['size']
						localsize += 4*int(b['size'])
					else:
						localsize += 4
					local[a[key1]['place']] = b
					variable_list[a[key1]['place']] = d[key]['place']

			tempdict = {}
			tempdict['param'] = param
			tempdict['local'] = local
			tempdict['paramsize'] = paramsize
			tempdict['localsize'] = localsize

			function_list[d[key]['place']] = tempdict

filename = sys.argv[1]

filename = filename[:-6]

pickle.dump(function_list, open(filename + '_func_list.p', 'wb'))
pickle.dump(variable_list, open(filename + '_var_list.p', 'wb'))