#nand2tetris project 2 and 6
Individual assignment 4 for advanced programming: Project 2 and 6 from the [nand2tetris] (https://www.nand2tetris.org) online course.

###[Project 2] (https://www.nand2tetris.org/project02):
Build the following chips: **Half-** and **FullAdder**, **16-bit Adder** and **Incrementer**, **Arithhmetic Logic Unit** (with and without output status handler)
In order to build the Half-, FullAdder and ALU chips we needed some basic logic chips (Not, And, Or, Xor, Mux) from project 1. We also needed the 16-bit Multiplexor chip for the ALU.

> In order to make sure the chips are working correctly individually, the .hdl chips are tested with .tst files which compare the outputs (.out) to the .cmp files.

###[Project 6] (https://www.nand2tetris.org/project06):
The goal of this project is to write an **assembler** (in assembler.py). [An assembler is] "a program designed to translate code written in a symbolic machine language into code written in binary machine language."
It should read the .asm file, translate it into correct Hack binary code and write that code to the .hack file.
    $ ./assembler.py < Prog.asm > Prog.hack

The assembler will be built in two stages:
1. write a basic assembler designed to translate assembly programs that contain no symbols
1. extend your basic assembler with symbol handling capabilities, yielding the final assembler

> Similarly to project 2, in order to make sure the assembler is working correctly, it will be tested. Most 3 out of 4 .asm files have an *L.asm file which is without symbols to check wether the first step is working correctly.