import main
import livegen
import getreg


def NAME(op):
	if( op == '+'):
		return "add"
	elif(op == '-'):
		return "sub"
	elif(op == '*'):
		return "mult"
	elif (op == '/'):
		return "div"
	elif (op == '&'):
		return "and"
	elif (op == '|'):
		return "or"
	elif (op == '^'):
		return "xor"
	elif (op == "<="):
		return "ble"
	elif (op == ">="):
		return "bge"
	elif (op == ">"):
		return "bgt"
	elif (op == "<"):
		return "blt"
	elif (op == "=="):
		return "beq"
	elif (op == "!="):
		return "bne"

def MOVE(reg,y):                    # Load the value of variable contained in y to reg
	if len(main.ad[y])==0:
		print "lw " + reg + ", " + y
	elif (reg!= main.ad[y][0]):
			print "move " + reg + ", " + main.ad[y][0] 

def COP(op,z,reg):                  # value(reg) = value(reg) op int(z)
	print "li $a0," + z
	if(op in ['/', '*']):
		print op + " " + reg + ', $a0'
	else:
		print op + " " + reg + ', ' + reg + ', $a0'

def VOP(op,regz,regx):
	if(op in ['/', '*']):
		print op + " " + regx + ', ' + regz
	else:
		print op + " " + regx + ', ' + regx + ', ' + regz


def UPDATE(x,reg):
	getreg.clearmem(x)
	getreg.rd_del(x)
	getreg.rd_add(reg,x)

def LOADADDR(y, reg):
	print "la " + reg +", " + y


def XequalY(x,y):
	if(y.isdigit()):
				reg = getreg.find_reg(lno)
				print "li " + reg + ", " + y
				UPDATE(x,reg)
	else:       
				if y in main.ptrmap:
					main.ptrmap[x] = main.ptrmap[y]
					getreg.rd_del(x)
					getreg.clearmem(x)
				else:
					if x in main.ptrmap:
						del main.ptrmap[x]
					reg = getreg.get_regx(x,y,lno)
					MOVE(reg,y)
					UPDATE(x,reg)

livegen.gen_live()
getreg.init_reg()
print ".data"

lines = open("test1.tac","r").readlines()
identifiers = {}
arrays = {}

for line in lines:
	line = line.split()
	if line[1] in ['+','-','/','*','%','&','|','^', ">>" , "<<"]:
		if line[2] not in identifiers:
			identifiers[line[2]]=1
	elif line[1]=='=':
		if(['&','*','['] not in line):
			if line[2] not in identifiers:
				identifiers[line[2]]=1
		elif line[-1]==']':
			if line[2] not in identifiers:
				identifiers[line[2]]=1
		elif line[3] in ['&','*'] :
			if line[2] not in identifiers:
				identifiers[line[2]]=1
		elif line[2] == '*':
			if line[3] not in identifiers:
				identifiers[line[3]]=1
	elif line[1]== 'Array':
		if line[2] not in arrays:
			arrays[line[2]] = line[3]
for identifier in identifiers:
	if identifier not in arrays:
		print identifier + ":\t.word\t0"
		main.ad[identifier] = []
for array in arrays:
	print array + ":.space\t" + arrays[array]

print ".text"
print "main:"
for line in lines:
	line = line.split()
	lno = int(line[0])
	op = line[1]
	if main.get_block[lno] != main.get_block[lno-1]:
		print "BLOCK" + str(main.get_block[lno]) + ":"
	if (op == '='):
		if('[' not in line and '&' not in line and '*' not in line):            # x = y
			x = line[2]
			y = line[3]
			XequalY(x,y)
		elif '[' in line:                 # x[i] = y or x = y[i]
			if( line[-1] == ']'):            # x = y[i]
				x = line[-5]
				y = line[-4] 
				i = line[-2]
				reg = getreg.get_regx(x,y, lno)
				LOADADDR(y, reg)                              ##
				if(i.isdigit()): 
					print "addi " + reg + ', ' + str(4*int(i))
				else:
					MOVE('$a0',i)
					print "loadi $a1, 4\n"
					print " mult $a0, $a1\n"
					print "mflo $a0\n"
					print "add " + reg + ' , ' + reg + ", $a0" 
				print "lw " + reg + ", 0(" + reg + ')'
				UPDATE(x,reg)
			else:
				x = line[2]                            # x[i] = y
				y = line[6]
				i = line[4]
				reg = getreg.get_regx(x,y,lno)
				LOADADDR(x,reg)
				if(i.isdigit()): 
					print "addi " + reg + ',' + str(4*int(i))
				else:
					MOVE('$a0',i)
					print "loadi $a1, 4\n"
					print " mult $a0, $a1\n"
					print "mflo $a0\n"
					print "add " + reg + ' , ' + reg + ", $a0" 
				if(y.isdigit()):
					print "li $a0, " + y
				else:
					MOVE('$a0',y)
				print "sw $a0, 0(" + reg + ')'
		elif('&' in line):        # = x & y
			x = line[2]
			y = line[4]
			main.ptrmap[x] = y
			getreg.rd_del(x)
			getreg.clearmem(x)
		elif("*" in line):        # = * x y      or = x * y
			if(line[2] == '*'):
				x = line[3]
				y = line[4]
				z = main.ptrmap[x]
				XequalY(z,y)
			else:
				x = line[2]
				y = line[4]
				z = main.ptrmap[y]
				XequalY(x,z)



	elif (op in ['+','-','/','*','%','&','|','^','>>','<<']):           # x = y op z  where x & y are variables and z can or cannot be
			x = line[2]
			y = line[3]
			z = line[4]
			if(z.isdigit()):
				reg = getreg.get_regx(x,y,lno)
				MOVE(reg,y)
				if (op in ['+','-','/','*','%','&','|','^']):
					COP(NAME(op), z, reg)
				elif( op == '>>'):
					COP('srl', z, reg)
				elif (op == '<<'):
					COP('sll', z, reg)
				UPDATE(x,reg)
			else:
				(reg,regz) = getreg.get_reg(x,y,z,lno)
				MOVE(reg,y)
				MOVE(regz,z)
				if (op in ['+','-','/','*','%','&','|','^']):
					VOP(NAME(op), regz, reg)
				elif( op == '>>'):
					COP('srlv', z, reg)
				elif (op == '<<'):
					COP('sllv', z, reg)
				UPDATE(x,reg)
				UPDATE(z,regz)
			if(op == '*' or op =='/'):
				print "mflo " + reg 
			elif(op =='%'):
				print "mfhi " + reg 
			

	elif op == '~':
		x = line[2]
		y = line[3]
		reg = getreg(x,y)
		MOVE(y,reg);
		print "li $a0, -1"
		print "xori " + reg + ' , ' + reg + ", $a0"
		

	elif op == "goto":
		branch = int(line[2])
		print "b " + "BLOCK" + str(main.get_block[branch])

	elif op == "ifgoto":
		x = line[-2]
		y = line[-1]
		relop = line[-3]
		branch = int(line[2])

		if(y.isdigit()):
			(reg,state) = getreg.check_reg(x,lno)
			if(state == -1):
				print "lw " + reg + ", " + x
				getreg.rd_del(x)
				getreg.rd_add(reg,x)
			print NAME(relop) + " " + reg + ", " + y + ", " + "BLOCK" + str(main.get_block[branch])
		else:
			(regx,state) = getreg.check_reg(x,lno)
			if(state == -1):
				print "lw " + reg + ", " + x
				getreg.rd_del(x)
				getreg.rd_add(regx,x)
			(regy,state) = getreg.check_reg(y,lno)
			if(state == -1):
				print "lw " + reg + ", " + x
				getreg.rd_del(x)
				getreg.rd_add(reg,x)
			print NAME(relop) + " " + regx + ", " + regy + ", " + "BLOCK" + str(main.get_block[branch])
				
	elif op == 'print':
		x = line[2]
		if (x == 'newline'):
			print "addi $a0, $0, 0xA" 
			print "addi $v0, $0, 0xB" 
			print "syscall"
		else:
			print "li $v0, 1"
			if (x.isdigit()):
				print "li $a0, " + x
			elif x in main.ptrmap:
				#print "ffoo"
				print "la $a0, " + main.ptrmap[x]
			else:
				#print "foo"
 				(reg,state) = getreg.check_reg(x,lno)
				if(state == -1):
					print "lw " + reg + ", " + x
					getreg.rd_del(x)
					getreg.rd_add(reg,x)
				print "move $a0, " + reg
			print "syscall"

	elif ( op == 'scan'):
		x = line[2]
		reg = getreg.find_reg(lno)
		print "li $v0, 5\nsyscall"
		print "move " + reg + ", $v0"
		UPDATE(x,reg)
	elif ( op == 'exit'):
		print "li $v0, 10\nsyscall"
	
	for x in line:
		getreg.update_dead(x,lno)
print "\n"	

# state -1 => new register is returned && x is in memory and not register
# state 1  => x ka register