<h1>Virtual Machine and Debugger Documentation</h1>

<h2>1. Unit Testing</h2>

<h3>Implementation</h3>

<h3>Use</h3>

<h2>2. Disassembler</h2>

<h3>Implementation</h3>
<p>The Disassembler class is initialized with a dictionary "labels" and a counter "count". This is necessary to keep 
track of the different labels of the program. The disassemble method takes the machine code instructions and compiles 
every instruction. After compiling every instruction it returns the result.</p>
<p>First in the compile method the two last digits from the instruction are taken to find the correct operation. This is
done by the get_op method, where it searches the corresponding operation name and format from the OPS dictionary. To do 
so the hexadecimal number has to be converted to an integer to find the correct code. The two arguments are taken from 
the other part of the instruction and now we have gathered all the information to generate the assembly code.</p>
<p>There are if, elif conditions to handle all the different formats. For "--" it simply returns the code "hlt" found in
the get_op method. In the "r-" and "rr" format, it converts one respectively two argument(s) to registers. The "rv" 
block is the most special because it handles the "bne" and "bqe" operations different. For the branches, labels are 
generated and put into the labels dictionary with the second argument as the position value, which indicated the target
address. The count variable is then incremented for the next branch instruction to have another label name.</p>

<h3>Use</h3>
<p>It's similar used like the assembler. In the main() the content of an input file is read and the instructions are put
into a list. Then it creates an instance of the Disassembler class and passes an empty dictionary for the labels. The 
instructions are disassembled and after that, the labels are inserted in the correct position of the program. Finally,
the output is printed to an output file. For the example input file we used the same instructions as in the assembler 
example to showcase that the disassembler is just the reverse action.</p>

<h3>Testing</h3>
<p>Test cases are implemented in one test_disassembler file to test the correctness of the disassembler. First we tested
if the correct output is generated when the program contains one or various instructions. Another important 
functionality to test was the implementation of labels. We tested if there is no, one or various branch instructions to
create labels. Also, it was crucial to test if the labels where inserted in the correct position in the result. Finally,
we tested if the conversion of the hexadecimal to integer was done correctly.</p>

<h2>3. New features and Problems - Assembler</h2>

<h3>3.1 Increment and Decrement</h3>

<h3>3.2 Swap Values</h3>

<h3>3.3 Reverse array in place</h3>

<h2>4. New features - Debugger</h2>

<h3>4.1 Show Memory Range</h3>

<h3>4.2 Breakpoint Addresses</h3>

<h3>4.3 Command Completion</h3>

<h3>4.4 Watchpoints</h3>
<p>In the architecture.py a new instruction 'wpt' for watchpoints was added. In the vm_break file a dictionary for the
the watchpoints was needed. It stores the memory addresses of the watchpoints and their original value. Also in the 
handlers dictionary the handlers for adding and clearing watchpoints were implemented. In the run method, if a 
watchpoint instruction is encountered, it checks if the value at the specified address has changed or not. If there was 
a change, it sets the VMState to FINISHED which halts the VM and lets the user interact. There is a method to create 
watchpoints which adds them to the dictionary with the original value and the clear method deletes it from the 
dictionary.</p>