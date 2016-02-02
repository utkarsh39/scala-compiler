def generate_block():
	f=open("in.txt",'r')
	blockn.append(0)
	block.append((0,0))
	bcount = 1
	for line in f:
	    lines.append(line)
	    blockn.append(0)

	for line in lines:
	    word=line.split()
	    if(int(word[0])==1):
	        temp = int(word[0])
	        block.append((temp,0))
	        blockn[temp] = bcount
	        print "hi1 ",temp,bcount
	        bcount += 1

	    if(word[1] == "call"):
	        '''    temp = get_line(word[2])                                           //Get line number where function begins
	        blockn[temp] = bcount
	        bcount += 1
	        '''
	    elif (word[1] == "ifgoto" or word[1] == "goto"):
	        temp = int(word[2])
	        block.append((temp,0))
	        blockn[temp] = bcount
	        print "hi2 ",temp,bcount
	        bcount += 1
	        temp = int(word[0]) + 1
	        block.append((temp,0))
	        blockn[temp] = bcount
	        print "hi2 ",temp,bcount
	        bcount += 1
	i=0
	for b in block:
	    if(b[0]==0):
	        continue
	    #print b
	    i += 1
	    leader=b[0]
	    tempblock = i
	    #print "yo ",leader,tempblock
	    temp=leader+1
	    if(blockn[temp] != 0 ):
	        block[i] = (leader,temp-1)
	    while( temp <= len(lines) and blockn[temp]==0):
	        blockn[temp] = tempblock
	        print temp,tempblock
	        temp += 1
	        if(temp>len(lines)):
	            block[i] = (leader,temp-1)
	        elif (blockn[temp] != 0):
	            block[i] = (leader,temp-1)
	        if(temp>len):
	            break
	for b in block:
	    print b

	lines.insert(0,"")

	return bcount

blockn=[]
block=[]
lines=[]