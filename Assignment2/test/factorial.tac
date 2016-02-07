1 = a 0
2 = c 0
3 scan a
4 call fact c
5 print c
6 print newline
7 exit 0
8 label fact
9 ifgoto 17 == a 1 
10 - a a 1
11 call fact c
12 print c
13 print newline
14 + a a 1
15 * c c a
16 ret c
17 ret 1