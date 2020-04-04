import unittest

from assembler import (cleaner,
                       commandType,
                       Acommand,
                       Ccommand)
'''
with open("projects/06/MaxL.asm") as tstfile:
    tstfile = tstfile.read()
'''

cleaner_out = [["@0"],
               ["D=M"],
               ["@1"],
               ["D=D-M"],
               ["@10"],
               ["D;JGT"],
               ["@1"],
               ["D=M"],
               ["@12"],
               ["0;JMP"],
               ["@0"],
               ["D=M"],
               ["@2"],
               ["M=D"],
               ["@14"],
               ["0;JMP"]]
    
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
        self.assertEqual(Acommand("@56"), "0"+"00111000")

    def test_Ccommand(self):
        self.assertEqual(Ccommand("D=D-M"), "111"+"010"+"1010011"+"000")

    def test_Ccommand2(self):
        self.assertEqual(Ccommand("D;JGT"), "111"+"000"+"0001100"+"001")
        
        
if __name__ == '__main__':
    unittest.main()
