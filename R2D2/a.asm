	.data
a:	.word	0
	.text
main:
li $t9, 2
li $v0, 1
move $a0, $t9
syscall
li $v0, 10
syscall


