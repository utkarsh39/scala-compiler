import re
import blockgen

def live_gen(n):
	start = blockgen.block[n][0]
	end = blockgen.block[n][1]

	for i in range(start,end+1):
		live.append([])

	print "Block: " , n , " Start: " , start , " End: " , end

	if start != end:
		word = blockgen.lines[end].split()

		word.remove(word[0])

		if word[0] != 'call' and word[0] != 'goto':
			if word[0] == 'ret':
				if len(word) > 0: word.remove(word[0])
				for x in word:
					if x.isdigit() == False:
						live[end].append(x)
			else:
				word.remove(word[0])
				for x in word:
					if x.isdigit() == False and x != '=' and x != '==' and x != '!=' and x != '==' and x != '>=' and x != '<=':
						live[end].append(x)

		for i in range(end-1,start,-1):
			word = blockgen.lines[i].split()
			if len(word) > 0: word.remove(word[0])
			if len(word) > 0: word.remove(word[0])

			for x in live[i+1]:
				if x not in word:
					live[i].append(x)

			if len(word) > 0: word.remove(word[0])
			
			for x in word:
				if x.isdigit() == False and x != '[' and x != ']' and x != '&' and x != '*' and x not in live[i]:
					live[i].append(x)

	for i in range(start,end):
		live[i] = live[i+1]

	live[end] = []

	for i in range(start,end+1):
		print live[i]

live = []
live.append([])
N_BLOCKS = blockgen.generate_block()

for i in range(1,N_BLOCKS):
	live_gen(i)