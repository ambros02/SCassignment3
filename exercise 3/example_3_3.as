hlt        # Halt program

# Load base address of the array into R0
ldc R0 99  

# Load length of the array into R1
ldr R0 R1  

# Calculate the last index of the array
dec R1     

# Loop to reverse the array
loop_start:
    # Check if the current index is greater than or equal to the last index
    beq R0 99

    # Load the values at the current and last indices
    ldr R0 R2  # Load value at current index to R2
    ldr R1 R3  # Load value at last index to R3

    # Swap values in R2 and R3
    swp R2 R3  

    # Store the swapped values back to the array
    str R2 R0  

    # Increment current index
    add R0 R1 

    # Decrement last index
    sub R0 R1 

    # Repeat the loop
    bne R0 99 

# Print the reversed array
prr R0      

# Print memory
prm R0 99    

