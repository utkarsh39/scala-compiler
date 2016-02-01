import re

def next_live_gen(n):
	start = get_start(n)
	end = get_end(n)

	print "Block: " + n + " Start: " + start + " End: " + end

	if start != end:
		word = lines[end].split()

		if word[0] != 'call' and word[0] != 'goto':
			if word[0] == 'ret':
				if word[1].isdigit() == false:
					next_live[end].append(word[1])
			else:
				word.remove(word[0])
				for x in word():
					if x.isdigit() == false and re.search('=',x) == false and re.search('<',x) == false and re.search('>',x) == false:
						next_live[end].append(x)

		for i in range(end-1,start):
			words = lines[i].split
			words.remove(words[0])

			for x in next_live[i+1]:
				if x not in words():
					next_live[i].append(x)

			words.remove(words[0])
			
			for x in words():
				if x.isdigit() == false and x != '[' and x != ']' and x != '&' and x != '*' and x not in next_live[i]:
					next_live[i].append(x)

	for i in range(start,end):
		next_live[i] = next_live[i+1]

	next_live[end].clear()

	for i in range(start,end+1):
		print next_live[i]
