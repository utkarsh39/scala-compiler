	.data
t8:	.word	0
t6:	.word	0
t7:	.word	0
t4:	.word	0
t5:	.word	0


	.text

BLOCK1:
	fun1: 
	addi $sp, $sp, -12
	li $a0,8
	sw $a0, 8($sp)
	sw $fp, 4($sp)
	sw $ra, 0($sp)
	addi $fp, $sp, 0 
	addi $sp,8
	li $t9, 0
	sw $t9, -4($fp)
	lw $t9, 16($fp)
	lw $t8, 20($fp)
	blt $t9, $t8, BLOCK3
	sw $t9, 16($fp)
	sw $t8, 20($fp)

BLOCK2:
	b BLOCK4

BLOCK3:
	lw $t9, 16($fp)
	lw $t8, 20($fp)
	add $t9, $t9, $t8
	move $t3, $t9
	sw $t9, t4
	move $t9, $t3
	sub $t9, $t9, $t8
	sw $t8, 20($fp)
	move $t8, $t9
	sw $t9, t5
	move $t9, $t3
	sub $t9, $t9, $t8
	sw $t8, 20($fp)
	move $t8, $t9
	sw $t8, 16($fp)
	sw $t9, t6

BLOCK4:
	lw $t9, 20($fp)
	beq $t9, 0, BLOCK6

BLOCK5:
	b BLOCK7

BLOCK6:
	lw $t9, 16($fp)
	sw $t9, -4($fp)
	b BLOCK14

BLOCK7:
	lw $t9, 16($fp)
	lw $t8, 20($fp)
	div $t9, $t8
	mfhi $t9
	sw $t8, 20($fp)
	move $t8, $t9
	sw $t9, t7
	bne $t8, 0, BLOCK9
	sw $t8, -4($fp)

BLOCK8:
	b BLOCK14

BLOCK9:
	lw $t9, 16($fp)
	lw $t8, 20($fp)
	div $t9, $t8
	mfhi $t9
	sw $t9, t8
	sw $t8, 20($fp)

BLOCK10:
	addi $sp, $sp, -4
	lw $a0,20($fp)
	sw $a0, 0($sp)

BLOCK11:
	addi $sp, $sp, -4
	lw $a0,t8
	sw $a0, 0($sp)

BLOCK12:
	jal fun1

BLOCK13:
	move $t9, $v0
	sw $t9, -4($fp)

BLOCK14:
	lw $v0, -4($fp)
	lw $ra, 0($fp)
	lw $a0, 8($fp)
	add $sp, $fp, $a0
	lw $fp, 4($fp)
	jr $ra

BLOCK15:
	main: 
	addi $sp, $sp, -12
	li $a0,0
	sw $a0, 8($sp)
	sw $fp, 4($sp)
	sw $ra, 0($sp)
	addi $fp, $sp, 0 
	addi $sp,4

BLOCK16:
	addi $sp, $sp, -4
	li $a0,  4
	sw $a0, 0($sp)

BLOCK17:
	addi $sp, $sp, -4
	li $a0,  10
	sw $a0, 0($sp)

BLOCK18:
	jal fun1

BLOCK19:
	move $t9, $v0
	sw $t9, -4($fp)
	li $v0, 1
	lw $t9, -4($fp)
	move $a0, $t9
	syscall
	addi $a0, $0, 0xA
	addi $v0, $0, 0xB
	syscall
	li $v0, 10
	syscall


