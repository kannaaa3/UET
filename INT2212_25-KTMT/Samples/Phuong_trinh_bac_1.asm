.data	
	msg_a: .asciiz "Nhap a="
	msg_b: .asciiz "Nhap b="
	msg_vn: .asciiz "Vo nghiem"
	msg_vsn: .asciiz "Vo so nghiem"
	msg_mn: .asciiz "Mot nghiem x="
	minus_1: .float -1.0
.text	
main:

# Hien thong bao "Nhap a="
	la $a0,msg_a
	li $v0,4
	syscall 
# Nhap s? th?c a (k?t qu? trong $f0)
	li $v0,6
	syscall 
# L?u giá tr? c?a a vào $f1	
	mov.s  $f1, $f0
	
# Hien thong bao "Nhap b="
	
	la $a0,msg_b
	li $v0,4
	syscall 
	
# Nhap s? th?c b (k?t qu? trong $f0)
	
	li $v0, 6
	syscall 
# L?u giá tr? c?a b vào $f2	
	
	mov.s $f2, $f0
# ??t $f3 = 0	
	li $t0, 0
	mtc1 $t0,$f3
	cvt.s.w $f3,$f3
# So sánh a = 0?
	c.eq.s $f1,$f3
	bc1t  A_0
# Hi?n k?t qu? khi a <> 0	
	la $a0,msg_mn
	li $v0,4
	syscall
# Tính b/a	
	div.s  $f12, $f2, $f1

# ??t $f4 = -1 	
	#li $t0, -1
	#mtc1 $t0,$f4
	#cvt.s.w $f4,$f4
	l.s $f4, minus_1
# Tính -b/a 	

	mul.s $f12,$f12,$f4
# In ra k?t qu?	
	li $v0,2
	syscall 
	
	j EXIT
# Tr??ng h?p a= 0
	# So sánh b=0?	
	A_0: c.eq.s $f2,$f3
	bc1t B_0
	
	la $a0,msg_vn
	li $v0,4
	syscall 
	j EXIT
	
# Tr??ng h?p b= 0

	B_0:
	la $a0,msg_vsn
	li $v0,4
	syscall 
	j EXIT
	
# K?t thúc	
	EXIT: 	li $v0,10
	syscall 

	
	