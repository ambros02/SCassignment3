ldc R0 0
ldc R1 3
L1:
prr R0
ldc R2 1
add R0 R2
cpy R2 R1
sub R2 R0
bne R2 @L1
hlt