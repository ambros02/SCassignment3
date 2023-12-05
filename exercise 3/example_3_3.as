#R0 Starting point of array
#R1 Size of the array
#R2 End point of array
#R3 Temporary pointer for swapping

ldc R0 @data        # Fetch the starting address of @data
ldc R1 6            # length is given
cpy R2 R1           #copy length of array from R1 to R2
add R2 R0           # end pointer
dec R2              #last element of array is one less than end pointer

loop:
    ldr R3 R0       # load value from start of array into R3
    ldr R1 R2       # load value from end of array into R1
    str R1 R0       # store value from R1 at start of array
    str R3 R2       # store value from R3 at end of array

    inc R0          # new start of array since we swapped the previous first
    dec R2          # new end of array since we swapped the previous end

    cpy R1 R2       # copy end pointer to R1
    sub R1 R0       # sub the R0 from R1 to get the remaining lenght

    beq R1 @end     # if R1 is 0 finished swapping

    inc R1          # inc R1 in case of even number of elements in array
    beq R1 @end     # if R1 is 0 finished swapping

    bne R1 @loop    # if R1 is not 0 continue loop

# Label to jump out of the loop
end:
hlt

.data
data: 6
