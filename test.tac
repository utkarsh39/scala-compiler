Done 1 op a b c       // +,-,/,*,^, %                                 
2 = d a          // d=a
3 ! a d          // logical not
4 ~ a d          // bitwise not
4 call fun        
5 ret value
6 goto line_number                               //unconditional Jump
7 ifgoto line_number relop lhs rhs            // conditional jump    <=, <, >, >=, ==,!=
8 ifgoto line_number x 
9 = x [ i ] y                                   // x[i]=y
10 = x y [ i ]                                  // x=y[i]
11 = x & y
12 = x * y
13 = * x y
Done 14 print x
Done 15 scan x
16 label foo                                      // function foo declaration
17 exit 



# While generation op a b c, if either one of b or c is a variable, then b has to be a variable



