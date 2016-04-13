	.data
t8:	.word	0
t9:	.word	0
t6:	.word	0
t7:	.word	0
t4:	.word	0
t5:	.word	0
t3:	.word	0


	.text

BLOCK1:
	fun1: 
	addi $sp, $sp, -12
	li $a0,8
	sw $a0, 8($sp)
	sw $fp, 4($sp)
	sw $ra, 0($sp)
	addi $fp, $sp, 0 
	addi $sp, $sp, 0

BLOCK2:
	lw $t9, 12($fp)
	lw $t8, 16($fp)
	bgt $t9, $t8, BLOCK6

BLOCK3:
	b BLOCK4

BLOCK4:
	lw $t9, 12($fp)
	blt $t9, 0, BLOCK6

BLOCK5:
	b BLOCK7

BLOCK6:
	li $v0, 0
	lw $ra, 0($fp)
	lw $a0, 8($fp)
	addi $a0, 12
	add $sp, $fp, $a0
	lw $fp, 4($fp)
	jr $ra

BLOCK7:
	lw $t9, 12($fp)
	beq $t9, 0, BLOCK9

BLOCK8:
	b BLOCK10

BLOCK9:
	li $v0, 1
	lw $ra, 0($fp)
	lw $a0, 8($fp)
	addi $a0, 12
	add $sp, $fp, $a0
	lw $fp, 4($fp)
	jr $ra

BLOCK10:
	lw $t9, 16($fp)
	li $a0,1
	sub $t9, $t9, $a0
	sw $t9, t3

BLOCK11:
	addi $sp, $sp, -4
	lw $a0,t3
	sw $a0, 0($sp)

BLOCK12:
	addi $sp, $sp, -4
	lw $a0,12($fp)
	sw $a0, 0($sp)

BLOCK13:
	jal fun1

BLOCK14:
	move $t9, $v0
	sw $t9, t4
	lw $t9, 16($fp)
	li $a0,1
	sub $t9, $t9, $a0
	sw $t9, t5
	lw $t9, 12($fp)
	li $a0,1
	sub $t9, $t9, $a0
	sw $t9, t6

BLOCK15:
	addi $sp, $sp, -4
	lw $a0,t5
	sw $a0, 0($sp)

BLOCK16:
	addi $sp, $sp, -4
	lw $a0,t6
	sw $a0, 0($sp)

BLOCK17:
	jal fun1

BLOCK18:
	move $t9, $v0
	lw $t8, t4
	add $t8, $t8, $t9
	sw $t8, t8
	sw $t9, t7

BLOCK19:
	lw $v0, t8
	lw $ra, 0($fp)
	lw $a0, 8($fp)
	addi $a0, 12
	add $sp, $fp, $a0
	lw $fp, 4($fp)
	jr $ra

BLOCK20:
	main: 
	addi $sp, $sp, -12
	li $a0,0
	sw $a0, 8($sp)
	sw $fp, 4($sp)
	sw $ra, 0($sp)
	addi $fp, $sp, 0 
	addi $sp, $sp, -4

BLOCK21:
	addi $sp, $sp, -4
	li $a0,  4
	sw $a0, 0($sp)

BLOCK22:
	addi $sp, $sp, -4
	li $a0,  2
	sw $a0, 0($sp)

BLOCK23:
	jal fun1

BLOCK24:
	move $t9, $v0
	move $t8, $t9
	sw $t8, -4($fp)
	sw $t9, t9
	li $v0, 1
	lw $t9, -4($fp)
	move $a0, $t9
	syscall
	addi $a0, $0, 0xA
	addi $v0, $0, 0xB
	syscall
	li $v0, 10
	syscall


