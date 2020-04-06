import unittest

from assembler import (jump,
                       comp,
                       dest,
                       cleaner,
                       commandType,
                       Acommand,
                       Ccommand,
                       parser,
                       symboltable,
                       symbol_table1,
                       symbol_table2)

clean_code = cleaner("Max.asm")
pseudofreecode =  ['@R0',
  'D=M',
  '@R1',
  'D=D-M',
  '@OUTPUT_FIRST',
  'D;JGT',
  '@R1',
  'D=M',
  '@OUTPUT_D',
  '0;JMP',
  '@R0',
  'D=M',
  '@R2',
  'M=D',
  '@INFINITE_LOOP',
  '0;JMP']
symbolfreecode = ['@0',
 'D=M',
 '@1',
 'D=D-M',
 '@10',
 'D;JGT',
 '@1',
 'D=M',
 '@13',
 '0;JMP',
 '@0',
 'D=M',
 '@2',
 'M=D',
 '@16',
 '0;JMP']
symboltable2 = {'ARG': '2',
  'INFINITE_LOOP': '16',
  'KBD': '24576',
  'LCL': '1',
  'OUTPUT_D': '13',
  'OUTPUT_FIRST': '10',
  'R0': '0',
  'R1': '1',
  'R10': '10',
  'R11': '11',
  'R12': '12',
  'R13': '13',
  'R14': '14',
  'R15': '15',
  'R2': '2',
  'R3': '3',
  'R4': '4',
  'R5': '5',
  'R6': '6',
  'R7': '7',
  'R8': '8',
  'R9': '9',
  'SCREEN': '16384',
  'SP': '0',
  'THAT': '4',
  'THIS': '3'}

cleaner_out = ['@0',
 'D=M',
 '@1',
 'D=D-M',
 '@10',
 'D;JGT',
 '@1',
 'D=M',
 '@12',
 '0;JMP',
 '@0',
 'D=M',
 '@2',
 'M=D',
 '@14',
 '0;JMP']

assemblylist = ["@0",
                "D=M",
                "@1",
                "D=D-M",
                "@10",
                "D;JGT",
                "@1",
                "D=M",
                "@12",
                "0;JMP",
                "@0",
                "D=M",
                "@2",
                "M=D",
                "@14",
                "0;JMP"]

with open("Max.hack") as correct:
    binlist = []
    for line in correct.readlines():
        binlist.append(line)

class TestPM(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_cleaner(self): 
        self.assertEqual(cleaner("MaxL.asm"), cleaner_out)
    
    def test_commandTypeA(self):
        self.assertEqual(commandType("@56"), "A")

    def test_commandTypeL(self):
        self.assertEqual(commandType("(LOOP)"), "L")

    def test_commandTypeC(self): 
        self.assertEqual(commandType("D=D-M"), "C")

    def test_Acommand(self):
        self.assertEqual(Acommand("@56"), "0"+'{0:{fill}15b}'.format(56, fill="0"))

    def test_Ccommand(self):
        self.assertEqual(Ccommand("D=D-M"), "111"+dest["D"]+comp["D-M"]+jump["null"])

    def test_Ccommand2(self):
        self.assertEqual(Ccommand("D;JGT"), "111"+dest["null"]+comp["D"]+jump["JGT"])

    def test_parser(self):
        self.assertEqual(parser(assemblylist),binlist)

    def test_symbol_table1(self):
        self.assertEqual(symbol_table1(clean_code, symboltable),(pseudofreecode, symboltable2))

    def test_symbol_table2(self):
        self.assertEqual(symbol_table2(pseudofreecode,symboltable2),symbolfreecode)
        
if __name__ == '__main__':
    unittest.main()
