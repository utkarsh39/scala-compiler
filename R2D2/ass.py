import main
import livegen
import getreg


def MOVE(reg,y):                    # Load the value of variable contained in y to reg
	if len(main.ad[y])==0:
		print "lw " + reg + ", " + y
	else:
		print "move " + reg + ", " + main.ad[y][0] 

def COP(op,z,reg):                  # value(reg) = value(reg) op int(z)
		print "li $a0," + int(z)
		print op + reg + ", $a0"

livegen.gen_live()
getreg.init_reg()
print "\t.data"

lines = open("test1.tac","r").readlines()
identifiers = {}
arrays = {}

for line in lines:
	line = line.split()
	if line[1] in ['+','-','/','*','%','&','|','^']:
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
	print identifier + ":\t.word\t0"
	main.ad[identifier] = []
for array in arrays:
	print array + ":\t.space\t" + str(arrays[array])
	main.ad[array] = []

print "\t.text"
print "main:"
for line in lines:
	line = line.split()
	lno = int(line[0])
	op = line[1]
	if (op == '='):
		if(['&','*','['] not in line):            # x = y
			x = line[2]
			y = line[3]
			if(y.isdigit()):
				reg = getreg.find_reg(lno)
				print "li " + reg + ", " + y
			else:
				reg = getreg.get_regx(x,y,lno)
				MOVE(reg,y)

			getreg.clearmem(x)
			getreg.rd_del(x)
			getreg.rd_add(reg,x)
	
	elif op == 'print':
		x = line[2]
		print "li $v0, 1"
		if (x.isdigit()):
			print "li $a0, " + x
		else:
			(reg,state) = getreg.check_reg(x,lno)
			if(state == -1):
				print "lw " + reg + ", " + x
				getreg.rd_del(x)
				getreg.rd_add(reg,x)
			print "move $a0, " + reg
		print "syscall"
	elif ( op == 'exit'):
			print "li $v0, 10\nsyscall"
print "\n"	

# state -1 => new register is returned && x is in memory and not register
# state 1  => x ka register