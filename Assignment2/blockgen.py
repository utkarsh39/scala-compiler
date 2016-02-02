from collections import defaultdict
blockn=[]
block=[]
lines=[]
nextlive=[]
func=defaultdict(list)
f=open("in.txt",'r')
bcount=1
blockn.append(0)
block.append((0,0))
tempfunc="-1"
end=-1
for line in f:
    lines.append(line)
    nextlive.append([])
    blockn.append(0)
    word=line.split()
    if(word[1] == "ret" and end == -1):
        end = int(word[0])
    if(word[1] == "label"):
        func[word[2]].append(int(word[0]))
        tempfunc=word[2]
    if(word[1] == "ret" and tempfunc != "-1"):
        func[tempfunc].append(int(word[0]))
        tempfunc = "-1"
for line in lines:
    word=line.split()
    if(int(word[0])==1):
        temp = int(word[0])
        block.append((temp,0))
        blockn[temp] = bcount
        print "hi1 ",temp,bcount
        bcount += 1

    if(word[1] == "call"):
       ''' temp = func[word[2]][0]
        block.append((temp,0))
        blockn[temp] = bcount
        print "hi2 ",temp,bcount
        bcount += 1'''
       temp = int(word[0]) +  1
       block.append((temp,0))
       blockn[temp] = bcount
       print "hi2 ",temp,bcount
       bcount += 1

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
    if(temp > end):
        block[i] = (leader,end)
    elif(blockn[temp] != 0 ):
        block[i] = (leader,temp-1)
    while( temp <= end and blockn[temp]==0):
        blockn[temp] = tempblock
        print temp,tempblock
        temp += 1
        if(temp>end):
            block[i] = (leader,temp-1)
        elif (blockn[temp] != 0):
            block[i] = (leader,temp-1)
        if(temp>end):
            break
for f in func:
    block.append((func[f][0],func[f][1]))
    for i in range(func[f][0],func[f][1]+1):
        blockn[i] = bcount
    print "hi2 ",temp,bcount
    bcount += 1
for b in block:
    print b
