#R2 as condition for loop
#R1 as the variable
ldc R2 2
ldc R0 1
ldc R3 50
ldr R1 R3
loop:
add R1 R0
sub R2 R0
bne R2 @loop
str R1 R3
hlt