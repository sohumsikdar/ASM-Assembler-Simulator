import sys
from OPCode import *
from typetable import *

# "div" : ("00111", "C"),
# "rs" : ("01000", "B"),
# "ls" : ("01001", "B"),
# "xor" : ("01010", "A"),
# "or" : ("01011", "A"),
# "and" : ("01100", "A"),
# "not" : ("01101", "C"),

def printCmd(cmd):
    op = cmd[0]
    s = ''
    if(op == "div"):
        s = opCode[op][0] + '00000' + reg[cmd[1]] + reg[cmd[2]]
    if(op ==  "rs"):
        # if(cmd[-1][0] != '$'):
        #     print("Error")                        #give error statement
        # p = int(cmd[-1][1:])
        # p = p>>1
        # bit8 = get8bit(p)
        s = opCode[op][0] + '000' + get8bit(cmd[-1][1:])
    if(op == "ls"):
        # if(cmd[-1][0] != '$'):
        #     print("Error")                        #give error statement
        # p = int(cmd[-1][1:])
        # p = p<<1
        bit8 = get8bit(p)
        s = opCode[op][0] + '000' + bit8
    if(op == "xor"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
    if(op == "or"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
    if(op == "and"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
    if(op == "not"):
        bit8 = get8bit(p)
        s = opCode[op][0] + '000' + get8bit(cmd[-1][1:])
    
    print(s)

        
    

