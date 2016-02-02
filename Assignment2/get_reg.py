import main
def init_reg():
	for i in range(0,10):
		main.rd.append('$t' + str(i))
def rd_add(reg,var):					#only adds reg into address descr. of var and var into reg descr. of reg
	if var not in main.rd[reg]:
		main.rd[reg].append(var)
		main.ad[var].append(reg)
def rd_del(var):						#Clears register fields of a variable
	for reg in main.ad[var]:
		main.rd[reg].remove(var)
		main.ad[var].remove(reg)
def rd_single_del(reg,var):
	main.rd[reg].remove(var)
	main.ad[var].remove(reg)

def spill(reg):
	for var in main.rd[reg]:
		main.ad[var].remove(reg)
		if len(main.ad[var]) == 0 and var not in main.mem:
			print "\tsw\t" + reg + ", " + var + "\n"
			main.mem.append(var)
	rd[reg] = []
def find_reg(line):
	for reg in main.rd:
		if len(main.rd[reg]) == 0:
			return reg
	
	temp = 100000
	if len(main.live[line]) == 0:
		for reg in main.rd:  
			if len(main.rd[reg]) < temp:
				temp = len(main.rd[reg])
				ind = reg		 
	else:
		var = main.live[line][0]
		for reg in main.ad[var]:  
			if len(main.rd[reg]) < temp:
				temp = len(main.rd[reg])
				ind = reg
	reg = ind 
	spill(reg)
	return reg

def get_regx(x, y, line):

	if len(main.rd[y]) > 1:
		for reg in main.rd[y]:
			flag=1
			for var in main.rd[reg]:
				if len(main.ad[var]) == 1:
					flag = 0
			if flag == 1:
				rd_single_del(reg,y)
				return reg

	if len(main.rd[y]) == 1:
		if y not in main.live[line]:
			reg = main.rd[y][0]
			flag = 1
			for var in main.rd[reg]:
				if len(main.ad[var]) == 1:
					flag = 0
			if flag == 1:
				rd_single_del(reg,y)
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
	if var not in main.live[line]:
		if var not in main.mem:
			print "\tsw\t$" + main.ad[var][0] + ", " + var + "\n"
			main.mem.append(var)

		for reg in main.ad[var]:
			main.rd[reg].remove(var)
			main.ad[var].remove(reg)
