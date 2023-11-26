ldc R0 0        # Load value 0 into register R0 (index)
ldr R1 0        # Load the base address of the array into register R1
ldr R2 1        # Load the length of the array into register R2
add R2 R1 R2    # Calculate the end address of the array (base + length)

# Loop to reverse the array
reverse_loop:
    cmp R0 R2     # Compare the current index with the end address
    bge reverse_done # If index >= end address, exit the loop

    ldr R3 R1     # Load the value at the current index
    sub R2 R2 1   # Move the end address back by one
    ldr R4 R2     # Load the value at the end address

    # Swap values at current index and end address
    str R3 R2
    str R4 R1

    add R0 R0 1   # Increment the index
    add R1 R1 1   # Move to the next element in the array
    jmp reverse_loop # Jump back to the beginning of the loop

reverse_done:
hlt             # Halt the program
