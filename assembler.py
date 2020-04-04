# Each line of the assembly such be transleted into binary code



# "//", white spaced and lines should be ignored
def cleaner(code):
    """All comments, "//", white spaces and white lined will be removed to clean up the code.
Also, every line of code will be out in a list."""
    clean_code = []
    for line in code:
        print(line)
    #return clean_code


#Symbols: variables and labels
def symbol_table(clean_code):
    """All symbols in the code gathered in the symbol table which will be a dict"""
    symbol_table = {}

    "Label stored in computer's memory starting at address 0"
    label_mem = 0

    "Variable stored in computer's memory starting at address 1024"   
    var_mem = 1024
    
    if label:
        label_mem += 1
    else:
        var_mem += 1
    
    return symbol_table, parse_code


def commandType(line):
    """Returns type of current command"""
    if line[0] == "@":
        return "A"
        "We need to add L command at second step"
    else:
        return "C"


def parser(parse_code):
    """The final parser that turns the assembly into binary code"""
    binlist = []
    for line in parse_code:
        if commandType(line) == "A":
            binline = Acommand(line)
        elif commandType(line) == "C":
            binline = Ccommand(line)
        binlist.append(binline)
    return binlist
    '''
    The list of binary lines will be wtitten out per line in the output .hack file    
    with open(".hack", "w") as hack:
        for line in binlist:
            f.write("%s\n" % line)
    '''
    
def Acommand(Acommand):
    """A-command converted to binary code. A-command consists out of 0[ValueInBinary]."""
    bin_value = '{0:{fill}15b}'.format(int(Acommand[1:]),fill="0")
    bin_Acommand = '0' + bin_value
    return bin_Acommand

def Ccommand(Ccommand):
    """This function uses dest, comp, jump to turn the C-command into binary code.
    C-command consists out of 111[dest][comp][jump]
    dest = comp;jump"""

    if "=" in Ccommand:
        splitted_C = Ccommand.split("=")
        ass_dest = splitted_C[0]
        ass_comp_jump = splitted_C[1]
    #If there is not a '=', dest is null    
    else:
        ass_dest = "null"
        ass_comp_jump = Ccommand
        
    if ";" in ass_comp_jump:
        splitted_C2 = Ccommand.split(";")
        ass_comp = splitted_C2[0]
        ass_jump = splitted_C2[1]
    # if jump 'null', ";" omitted     
    else:
        ass_comp = ass_comp_jump
        ass_jump = "null"
   
    bin_Ccommand = "111" + dest[ass_dest] + comp[ass_comp] + jump[ass_jump] 
    return bin_Ccommand

# For eacht part of the C-command we use a dictionary to translate that part quickly.
dest = {}
dest['null']='000'
dest['M']='001'
dest['D']='010'
dest['MD']='011'
dest['A']='100'
dest['AM']='101'
dest['AD']='110'
dest['AMD']='111'

comp = {}
comp['0']='0101010'
comp['1']='0111111'
comp['-1']='0111010'
comp['D']='0001100'
comp['A']='0110000'
comp['!D']='0001101'
comp['!A']='0110001'
comp['-D']='0001111'
comp['-A']='0110011'
comp['D+1']='0011111'
comp['A+1']='0110111'
comp['D-1']='0001110'
comp['A-1']='0110010'
comp['D+A']='0000010'
comp['D-A']='0010011'
comp['A-D']='0000111'
comp['D&A']='0000000'
comp['D|A']='0010101'
comp['M']='1110000'
comp['!M']='1110001'
comp['-M']='1110011'
comp['M+1']='1110111'
comp['M-1']='1110010'
comp['D+M']='1000010'
comp['D-M']='1010011'
comp['M-D']='1000111'
comp['D&M']='1000000'
comp['D|M']='1010101'

jump = {}
jump['null']='000'
jump['JGT']='001'
jump['JEQ']='010'
jump['JGE']='011'
jump['JLT']='100'
jump['JNE']='101'
jump['JLE']='110'
jump['JMP']='111'

