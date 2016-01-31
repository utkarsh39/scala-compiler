from collections import defaultdict

ad=defaultdict(list) 				#Stores  register at 0 index, memory at 1 and stack locations after this. Access by ad[var][index]
rd=defaultdict(list)                            # Access by rd[var]. This will be a list

emptyr={}

'''def getreg(varl, varr, line):
	if(varr in ad and ad[varr][0] != "" and next_use(line,varr)==0):
		return ad[varr][0],'r'
	else if (len(emptyr) != 0):                 		# check size of list of empty registers
		tempr = emptyr[0]
		emptyr.remove(tempr)
		return tempr,'r'
	else if (next_use(line,varl) != 0):
		tempr= spill()
		return tempr,'r'
	else
		return ad[varl][1],'m' '''

def updaterd_add(reg,var):
	if reg in rd:
		if(var not in rd[reg]):
			rd[reg].append(var)
	else:
		rd[reg].append(var)
def updaterd_del(reg,var):
	for reg in rd:
		if(var in rd[reg]):
			rd[reg].remove(var)

def updatead_add(var,loc,type):
	if var not in ad:
                if(type == 'r'):
		        ad[var].insert(0,loc)
                elif(type == 'm'):
                        ad[var].insert(1,loc)
                elif(type == 's'):
                        ad[var].append(loc)
	elif(type == 'r'):
		ad[var][0] = loc
        elif type == 'm':
                ad[var][1] = loc
        elif(type == 's'):
                ad[var].append(loc)

def updatead_del(var,type):
        if(type == 'r'):
		ad[var].pop(0)
        elif type == 'm':
                ad[var].pop(1)
        elif(type == 's'):
                ad[var] = ad[var][0:2]                #Removes all the stack addresses
def del_reg(reg):                                        #Remove a register from all address descriptors
        for var in ad:
                if ad[var][0] == reg:
                        ad[var].pop(0)


