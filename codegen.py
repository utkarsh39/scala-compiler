def f(op):
    if op == '+':
        return add
    elif op == '-':
        return sub
    elif op == '*':
        return mul
    elif op == '/':
        return div

def loadaddr( y,reg):               # Loads the address of variable in y to reg
    add_des = ad[y]
    if ( add_des[1] != '-1'):
        print " li $" + reg +"," + add_des[1]                  
    else:
        print " li $" + reg +"," + add_des[2]
    return

def loadval( y, reg):                     # Loads the value of variable contanied in y to reg
        add_des = ad[y]
        if ( add_des[0] != '-1'):                  # Register value = value of y
            print " move $" + reg +", $" + add_des[0]
        elif ( add_des[1] != '-1'):
            print " lw $" + reg +"," + add_des[1]                  
        else:
            print " lw $" + reg +"," + add_des[2]
        return
def var_operation(op,z,reg):                  # value(reg) = value(reg) op (value of variable contained in z)  
        add_des = ad[z]
        if ( add_des[0] != '-1' ):
                    print op + '$' + reg + ", $" + add_des[0]
        elif ( add_des[1] != '-1'):                        # if z is in memory/stack, it's value is loaded in $a0 but the address descriptor or register descriptor is not changed
                    print"loadw $a0," + add_des[1]
                    print op + '$' + reg + ", $a0" 
        else:
                    print"loadw $a0," + add_des[2]
                    print op + '$' + reg + ", $a0"

def cons_operation(op,z,reg):                  # value(reg) = value(reg) op int(z)
        print "li $a0," int(z)
        print op + '$' + reg + ", $a0"

lines = open("test.tac","r").readlines()
for line in lines:
	line = line.split()
	op = line[1]
	if (op == '='):
		if(['&','*','['] not in line):            # x = y
			x = line[2]
			y = line[3]
			#offset = add_des(line[3])
            reg = getreg(x,y)
            if(y.isdigit()):
                print "li $" + reg +", " + int(y)
            else:
                loadval(y, reg)
        elif ( '[' in line):                 # x[i] = y or x = y[i]
        	if( line[-1] == ']'):            # x = y[i]
                x = line[-5]
                y = line[-4] 
                i = line[-2]
                reg = getreg(x,y)
                loadaddr(y, reg)
                if(i.isdigit()): 
                    print "addi $" + reg + ',' + 4* int(i)
                else:
                    loadval(i,a0)
                    print "loadi $a1, 4\n"
                    print " mult a0 a1\n"
                    print "mflo $a0\n"
                    print "add $" + reg + ", a0" 
                print "lw $" + reg + ", 0($" + reg + ')'
            else:
            	x = line[2]                            # x[i] = y
            	y = line[6]
                i = line[4]
                reg = getreg(x,y)
                loadaddr(x,reg)
                if(i.isdigit()): 
                    print "addi $" + reg + ',' + 4* int(i)
                else:
                    loadval(i,a0)
                    print "loadi $a1, 4\n"
                    print " mult a0 a1\n"
                    print "mflo $a0\n"
                    print "add $" + reg + ", a0" 
                if(y.isdigit()):
                    print "li $a0, " + int(y)
                else:
                    loadval(y,a0)
                print "sw $a0, 0(" + reg + ')'
                
        if( line[3] != '['):
                    	update register descriptor of reg that it contains x now. remove x from all other register descriptions
                    	update address descriptor of x that it is contained in register reg
        	    
                
	elif (op in ['+','-','/'.'*','%','&','|','^']):           # x = y op z  where x & y are variables and z can or cannot be
	    x = line[2]
	    y = line[3]
	    z = line[4]
		reg = getreg(x,y)
        loadval(y,reg);
        if( op == '+' && z.isdigit()):
                print "addi" + '$' + reg + "," + int(z)
        elif ( op == '+'):
                var_operation("add", z, reg)
        elif( op == '-' && z.isdigit()):
                print "addi" + '$' + reg + "," + -1*int(z)
        elif( op == '-'):
                var_operation("sub", z, reg)
        elif( op == '*'):
                if (z.isdigit()):
                    cons_operation("mult", z, reg) 
                else:
                    var_operation("mult", z, reg)
                print "mflo $" + reg                               # Lower 32 bit of the product.
        elif( op == '/' || op =='%'):
                if (z.isdigit()):
                    cons_operation("div", z, reg)
                else:
                    var_operation("div", z, reg)
                if(op == '/'):
                        print "mflo $" + reg
                else:
                        print "mfhi $" + reg 
        elif( op == '&'):
                if(z.isdigit()):
                    cons_operation("and",z,reg)
                else:
                    var_operation("and",z,reg)
        elif( op == '|'):
                if(z.isdigit()):
                    cons_operation("or",z,reg)
                else:
                    var_operation("or",z,reg)
        elif( op == '^'):
                if(z.isdigit()):
                    cons_operation("xor",z,reg)
                else:
                    var_operation("xor",z,reg)
        elif( op == '<<'):
                if(z.isdigit()):
                    cons_operation("sll",z,reg)
                else:
                    var_operation("sllv",z,reg)
        elif( op == '>>'):
                if(z.isdigit()):
                    cons_operation("srl",z,reg)
                else:
                    var_operation("srlv",z,reg)        

        update address descriptor of reg that it contains x now. Remove x from all other register descriptions
        update address descriptor of x that it is contained in register reg

    elif( op == '~'):
        x = line[2]
        y = line[3]
        reg = getreg(x,y)
        loadval(y,reg);
        print "li $a0, -1"
        print "xori $" + reg + ", $a0"

	#elif ( op == '~'):
     #   x=line[2]
      #  y=line[3]

        
    elif ( op in ["call","return","goto"]):
           # To do



    elif ( op == "ifgoto"):
    	if( line[2] in ["<=",'>=','<','>','==','!=']):
    		# Mohak did it.


    elif ( op == 'scan'):
        x = line[2]
        reg = getreg(x,-1)
        print "li $v0, 5\nsyscall"
        print "mov $" + reg + ", $v0"

    elif ( op == 'print'):             #change the code for constants too
        x = line[2]
        print "li $v0, 1\n "
        if (x.isdigit()):
            print "loadi $a0, " + int(x)
        else: 
            lod(x,a0)
        print"syscall"

    elif ( op == 'label'):

    elif ( op == 'exit'):
        print "li $v0, 10\nsyscall\n"