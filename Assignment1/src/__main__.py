
def main():
    
    import ply.lex as lex
    import sys
    from collections import defaultdict
    # List of token names.   This is always required
    myfile = open(sys.argv[1])
    reserved = {
	'if' 		: 'KEYWORD_IF',
	'else' 		: 'KEYWORD_ELSE',
	'for' 		: 'KEYWORD_FOR',
	'while' 	: 'KEYWORD_WHILE',
	'do' 		: 'KEYWORD_DO',
	'break' 	: 'KEYWORD_BREAK',
	'var' 		: 'KEYWORD_VAR',
	'val' 		: 'KEYWORD_VAL',
	'return' 	: 'KEYWORD_RETURN',
	'type' 		: 'KEYWORD_TYPE',
	'import' 	: 'KEYWORD_IMPORT',
	'class' 	: 'KEYWORD_CLASS',
	'private' 	: 'KEYWORD_PRIVATE',
	'protected' : 'KEYWORD_PROTECTED',
	'define'	: 'KEYWORD_DEFINE',
	'null' 		: 'KEYWORD_NULL',
	'object' 	: 'KEYWORD_OBJECT',
	'package' 	: 'KEYWORD_PACKAGE',
	'case' 		: 'KEYWORD_CASE',
	'def' 		: 'KEYWORD_DEF',
	'new' 		: 'KEYWORD_NEW',
	'this' 		: 'KEYWORD_THIS',
	'with'		: 'KEYWORD_WITH',
	
	'Int'		: 'TYPE_INT',
	'Long'		: 'TYPE_LONG',
	'String'	: 'TYPE_STRING',
	'Float'		: 'TYPE_FLOAT',
	'Double'	: 'TYPE_DOUBLE',
	'Char'		: 'TYPE_CHAR'
    }
    

    def t_DOUBLE_NUMBER(t):
        r'[-+]?[0-9]+\.[0-9]*([eE][-+]?[0-9]+)?| [-+]?[0-9]+([eE][-+]?[0-9]+)'
        t.value = float(t.value)    
        return t

    def t_INT_NUMBER(t):
        r'[-+]?\d+'
        t.value = int(t.value)    
        return t

    tokens = [
        'LPAREN', 'RPAREN','BLOCKBEGIN','BLOCKEND',
        'LBRAC','RBRAC',
        'INT_NUMBER','DOUBLE_NUMBER',
        'COLON','COMMA','TERMINATOR','INST','STRINGID',
        'BINARY',
        'AROP', 'RELOP','BINOP','LOGOP','ASOP',
        'IDENTIFIER',
        'COMMENT','COMMENT_BEGIN','COMMENT_END',
        'STRING','CHAR'
    ] + list(reserved.values())


    # Regular expression rules for simple tokens
    t_BINARY 	 = r'true|false'
    t_AROP   	 = r'[-%+*/]'
    t_ASOP 	 	 = r'='
    t_LPAREN     = r'\('
    t_RPAREN     = r'\)'
    t_BLOCKBEGIN = r'\{'
    t_BLOCKEND   = r'\}'
    t_LBRAC   	 = r'\['
    t_RBRAC      = r'\]'
    t_COLON      = r'\:'
    t_COMMA      = r'\,'
    t_TERMINATOR = r'\;'
    t_INST     	 = r'\.'
    
    t_RELOP = r'==|<=|>=|<|>|!='
    t_BINOP = r'&|\||~|<<|>>|>>>'
    t_LOGOP = r'&&|!|\|\|'
    def t_STRING(t):
        r'"[^"\n]*"'
        t.value=t.value[1:-1]
        return t
    def t_CHAR(t):
        r'\'.\''
        t.value=t.value[1:-1]
        return t
    
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

    def t_COMMENT(t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        pass

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    # Build the lexer
    lexer = lex.lex()
        
    # Test it out
    data = myfile.read()

    # Give the lexer some input
    lexer.input(data)

    d = {}
    e = defaultdict(list)

    # Tokenize
    #print("hi")
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        if(tok.type in d):
            d[tok.type] = d[tok.type]+1
        else:
            d[tok.type] = 1
        if (tok.value not in e[tok.type]):
            e[tok.type].append(tok.value)
        
    print("{0:15s} {1:10s}\tLexemes".format("Token","Occurences"))
    print('-' * 70)
    for k in sorted(d.keys()):
        print("{0:<18s} {1:<4d} \t".format(k,d[k]),end=" ")
        print(e[k])

            
if __name__ == '__main__':
    main()
    
