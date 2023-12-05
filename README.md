<h1>Virtual Machine and Debugger Documentation</h1>

<h2>1. Unit Testing</h2>

<h3>Implementation</h3>

<h4>Overview</h4>
<p>The virtual Machine and the assembler are tested individually, however since we are allowed to assume the assembler to be correct we can use the output files of the assembler to test the virtual machine. Usually in unit testing we would like the tests to be completly independent from factors which are not being tested. In this case this would mean writing the mx files for the virtual machine tests by hand.</p>

<h4>Structure</h4>
<p>Root directory is exercise_1, in the vm_tests directory are all files with the tests. In the test_files directory are all files used and generated by the tests.</p>

<h4>Assembler</h4>
<p>To test the assember several .as files are created and put into the test_files directory.These files consist of simple operations using the operations for the virtual machine. The desired output of the assembler is calculated by hand and saved in a dictionary. Then the assembler is used to assemble the operations from the file into binary format. The tests assert if the actual output the assembler gave matches the desired output calculated by hand. For simplicity and scalability fixtures are used to access the informations for a given file, aswell as a helper function assemble_basis which assembles the code.</p>

<h4>Virtual Machine</h4>
<p>To test the virtual machine the .as file from the assembler test is passed through the assembler and stored as an mx file. The virtual machine can then use this file for testing and later call the remove_file function to cleanup. Further there is the helper function fetch_instructions and execute_vm which simulate the main function of the vm.py file. All what is left to do is use the existing files and test if the vm handles the instructions correctly.</p>

<h4>Integration Testing</h4>
<p>The Integration tests are used to verify the correctness of the helper functions such as the show or main function. To achieve this for vm and assembler an inegration .as respectively .mx file is created and the program is run as if it was called. This might not seem to do much now, however if we extend the program and say there could be extra data in an .as file which is being handled by the assembler this can come in handy.</p>


<h4>Coverage</h4>
<p>The tests have a total branch coverage of 98% missing </p>

<h3>Use</h3>

<h4>Run Tests<h4>
<p>To run all tests navigate to the exercise_1 directory and use the command: <br>
>>>pytest<br></p>

<h4>Test covergage</h4>
<p>To gain a test coverage report navigate to the exercise_1 directory and use the command:<br>
>>>pytest --cov --cov-branch --cov-report=html.'name'<br>
to get a folder containing an index.html which will display the report info</p>

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
<h4>Implementation</h4>
<p>To increment the value of a register by one, we added the "inc" command to the OPS dictionary in the architecture.py file. Since the instruction only operates on one register, we use the "r-" in the format field. We also have to modify the vm.py file a little. We added a new elif to the run method. The elif checks if the instruction command is "inc" and adds 1 to the value of the register. <br>
To decrement the value of a register by one we do the same thing like the increment instruction. We added "dec" in the OPS dictionary and added a new elif in the run method, which decrements the value of the given register. </p>
<h4>Use</h4>
<p>We wrote a new file: example_3_1.as which loads the value 5 to a register and increments the register afterwards. We also use the "prr" command to make the new value of the register visible. We then use "dec" to decrement the value and print it aout again with "prr". We halt the programm with the "hlt" command.
</p>

<h3>3.2 Swap Values</h3>
<h4>Implementation</h4>
<p>We added a new instruction to the OPS dictionary in the architecture.py file. Since we need two registers to swap the values the format would be "rr". Like with the increment and decrement we also added a new elif to the run method in the vm.py file. The elif simply just swaps the two values of the two register.
</p>
<h4>Use</h4>
<p>We wrote a example_3_2.as file with the istruction to swap the values of two given registers. We used the "prr" instruction to print the values out to make it visible if the swap worked.
</p>
<h3>3.3 Reverse array in place</h3>
<p>NEEDS TO BE DONE
</p>

<h2>4. New features - Debugger</h2>

<h3>4.1 Show Memory Range</h3>
<p> We changed the _do_memory method in the vm_extend.py file and added two new methods: show_memory_at_address and show_memory_range. The _do_memory method uses self.read to prompt the user to enter one or two addresses. If the user only entered a single address, the we convert it to an interger and call the show_memory_at_address method with the given address. If the users entered two addresses (start and end address), we convert both to interger and call show_method_range. For any other input we give an error message back. show_memory_at_address displays the content of the memory within the specified address. show_memory_range displays the content of the memory within the specified address range. 
</p>
<h3>4.2 Breakpoint Addresses</h3>
<p>This Implementation was not only made for breakpoint addresses but more general for all commands. Just specify the addresses after the command, sepperated by single whitespaces e.g. break 2 3 will create a breakpoint at address 2 and 3. It uses a loop to run the command once for each specified address. Also note it is in the programmers responsibility to use correct addresses e.g. in the range of the program.if no address is specified, the current address will be used.</p>

<h3>4.3 Command Completion</h3>
<p>From the input of the user all handlers that start with the specified string are fetched. If there is only one handle it will execute. If there are multiple options a list of the possible matches is returned and the user may try again. This however implies that if a file is run all the commands must be uniquely identifying a handler or the program will crash.</p>

<h3>4.4 Watchpoints</h3>
<p>In the vm_break file a dictionary for the the watchpoints is used to keep track of them. It uses the memory addresses of the watchpoints as keys and their value as value. Also in the 
handlers dictionary the handlers for adding and clearing watchpoints were implemented. In the run method, after an operation is executed the progranm checks all watched values, against the actual values and tells the user which one and lets the iser interact in the same position. 
.</p>