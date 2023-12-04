<h1>Virtual Machine and Debugger Documentation</h1>

<h2>1. Unit Testing</h2>

<h3>Implementation</h3>

<h3>Use</h3>

<h2>2. Disassembler</h2>

<h3>Implementation</h3>

<h3>Use</h3>

<h3>Testing</h3>

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
<p>NEEDS TO BE DONE</p>
<h3>4.2 Breakpoint Addresses</h3>
<h3>4.3 Command Completion</h3>

<h3>4.4 Watchpoints</h3>
