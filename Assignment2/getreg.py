from collections import defaultdict

ad=defaultdict(tuple) 									#Stores only memory and register locations
rd=defaultdict(list)
emptyr={}
def getreg(varl, varr, line):
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
		return ad[varl][1],'m'


def updaterd(reg,var):
	if reg in rd:
		if(var not in rd[reg]):
			rd[reg].append(var)
	else:
		rd[reg].append(var)

def updatead(var,loc,type):
	if(type == 'r'):
                ad[var][0] = loc
        else if type == 'm':
		ad[var][1] = loc

