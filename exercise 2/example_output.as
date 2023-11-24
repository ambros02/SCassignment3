ldc R0 0
ldc R1 3
prr R0
ldc R2 1
add R0 R0
cpy R2 R2
sub R2 R2
bne R2 2
hlt

# solution
ldc R0 0          000002
ldc R1 3          030102
prr R0            00000A
ldc R2 1          010202
add R0 R2         020006
cpy R2 R1         010204
sub R2 R0         000207
bne R2            020209
hlt               000001