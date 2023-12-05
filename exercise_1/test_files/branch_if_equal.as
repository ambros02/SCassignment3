ldc R0 0
ldc R1 0
ldc R2 0
ldc R3 1
loop:
add R2 R1
add R1 R3
beq R2 @loop
ldc R3 50
str R2 R3
hlt