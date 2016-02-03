from main import *
def init_reg():
	for i in range(0,10):
		rd.append('$t' + str(i))
def rd_add(reg,var):					#only adds reg into address descr. of var and var into reg descr. of reg
	if var not in rd[reg]:
		rd[reg].append(var)
		ad[var].append(reg)

def rd_del(var):						#Clears register fields of a variable
	for reg in ad[var]:
		rd[reg].remove(var)
		ad[var].remove(reg)

def rd_remove(reg,var):
	if reg in ad[var]:
		rd[reg].remove(var)
		ad[var].remove(reg)


def spill(reg):
	for var in rd[reg]:
		ad[var].remove(reg)
		if len(ad[var]) == 0 and var not in mem:
			print "\tsw\t" + reg + ", " + var + "\n"
			mem.append(var)
	rd[reg] = []

def check_reg(var,line):
	if len(ad[var]) == 0:
		return find_reg(line), -1
	else:
		return ad[var][0], 1 


def find_reg(line):
	for reg in rd:
		if len(rd[reg]) == 0:
			return reg
	
	temp = 100000
	if len(live[line]) == 0:
		for reg in rd:  
			if len(rd[reg]) < temp:
				temp = len(rd[reg])
				ind = reg		 
	else:
		var = live[line][0]
		for reg in ad[var]:  
			if len(rd[reg]) < temp:
				temp = len(rd[reg])
				ind = reg
	reg = ind 
	spill(reg)
	return reg

def get_regx(x, y, line):

	if len(rd[y]) > 1:
		for reg in rd[y]:
			flag=1
			for var in rd[reg]:
				if len(ad[var]) == 1:
					flag = 0
			if flag == 1:
				rd_remove(reg,y)
				return reg

	if len(rd[y]) == 1:
		if y not in live[line]:
			reg = rd[y][0]
			flag = 1
			for var in rd[reg]:
				if len(ad[var]) == 1:
					flag = 0
			if flag == 1:
				rd_remove(reg,y)
				return reg

	return find_reg(line)

def get_reg(x,y,z,line):
	regx = get_regx(x, y, line)
	if len(ad[z]) == 0:
		regz = find_reg(line)
	else:
		regz = ad[z][0]

	return regx,regz

def update_dead(var,line):
	if var not in live[line]:
		if var not in mem:
			print "\tsw\t$" + ad[var][0] + ", " + var + "\n"
			mem.append(var)

		for reg in ad[var]:
			rd[reg].remove(var)
			ad[var].remove(reg)
