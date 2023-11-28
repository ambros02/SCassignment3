ldc R0 0
ldc R1 1
ldc R2 0
loop:
add R2 R1
beq R2 @loop
ldc R3 50
str R2 R3
hlt