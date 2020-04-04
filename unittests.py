import unittest

from assembler import (jump,
                       comp,
                       dest,
                       cleaner,
                       commandType,
                       Acommand,
                       Ccommand,
                       parser)
'''
with open("projects/06/MaxL.asm") as tstfile:
    tstfile = tstfile.read()
'''

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

binlist =  ['0000000000000000',
  '1110101110000000',
  '0000000000000001',
  '1110101010011000',
  '0000000000001010',
  '1110000001100001',
  '0000000000000001',
  '1110101110000000',
  '0000000000001100',
  '1110000101010111',
  '0000000000000000',
  '1110101110000000',
  '0000000000000010',
  '1110010001100000',
  '0000000000001110',
  '1110000101010111']

class TestPM(unittest.TestCase):

    def setUp(self):
        pass
    
    #def test_cleaner(self): 
    #    self.assertEqual(cleaner(tstfile), cleaner_out)
    
    def test_commandTypeA(self):
        self.assertEqual(commandType("@56"), "A")

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
        
if __name__ == '__main__':
    unittest.main()
