#nand2tetris project 2 and 6
Individual assignment 4 for advanced programming: Project 2 and 6 from the [nand2tetris] (https://www.nand2tetris.org) online course.

##[Project 2] (https://www.nand2tetris.org/project02):
Build the following chips: **Half-** and **FullAdder**, **16-bit Adder** and **Incrementer**, **Arithhmetic Logic Unit** (with and without output status handler)
In order to build the Half-, FullAdder and ALU chips we needed some basic logic chips (Not, And, Or, Xor, Mux) from project 1. We also needed the 16-bit Multiplexor chip for the ALU.

> In order to make sure the chips are working correctly individually, the .hdl chips are tested with .tst files which compare the outputs (.out) to the .cmp files.

##[Project 6] (https://www.nand2tetris.org/project06):
The goal of this project is to write an **assembler** (in assembler.py). [An assembler is] "a program designed to translate code written in a symbolic machine language into code written in binary machine language."
It should read the .asm file, translate it into correct Hack binary code and write that code to the .hack file.
    $ ./assembler.py < Prog.asm > Prog.hack

####The assembler will be built in two stages:
#####1. write a basic assembler designed to translate assembly programs that contain no symbols.
- helper functions
  - cleaner: All comments, "//", white spaces and white lined will be removed to clean up the code.
Also, every line of code will be out in a list.
  - Acommand: A-command converted to binary code. A-command consists out of 0[ValueInBinary].
  - Ccommand: This function uses dest, comp, jump to turn the C-command into binary code.
    C-command consists out of 111[dest][comp][jump]
    dest = comp;jump
  - commandType: Returns type of current command
  - parser: The final parser that turns the assembly into binary code
- dictionaries to look up binary translation for C-command
  - dest
  - comp
  - jump

#####2. extend your basic assembler with symbol handling capabilities, yielding the final assembler
- (additional) helper functions
  - symbol_table
    - symbol_table1: All pseudo commands (LCommands) will be put in the symboltable for later reference and the line will be deleted
    - symbol_table2: The second pass replaces symbolic Acommands @Xxx with its associated binary memory location. All variables will be put in the symboltable and all the symbols (labels and variables) will be replaced with their keys.

> The unittest.py file applies unittest on the seperate functions in the assembler to make sure all of them work correctly seperately.

> Similarly to project 2, in order to make sure the assembler is working correctly, it will be tested. 3 out of 4 .asm files have an *L.asm file which is without symbols to check whether the first step is working correctly.