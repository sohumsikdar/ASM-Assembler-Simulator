import sys
from OPCode import *
from typetable import *

# "add" : ("00000", "A"),
# "sub" : ("00001", "A"),
# "movI" : ("00010", "B", ),
# "movR" : ("00011", "C"),
# "ld" : ("0010", "D"),
# "st" : ("00101", "D"),
# "mul" : ("00110", "A"),



def get8bit (k):
    s = '{0:08b}'.format(k)
    return s
  
def printCmd(cmd):
    op = cmd[0]
    s = ''
    if(op == "add"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
    if(op == "sub"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
    if(op == "mov"):
        if(cmd[-1][0] == '$'):
            k = int(cmd[-1][1:])
            s = "00010" + reg[cmd[1]] + get8bit(k)
        else :
            s = "00011" + "00000" + reg[cmd[1]] + reg[cmd[2]]
    if(op == "mul"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
    if(op == 'ld'):
        s = opCode[op] + reg[cmd[1]] + get8bit(SymbList[cmd[2]])
    if(op == 'st'):
        s = opCode[op] + reg[cmd[1]] + get8bit(SymbList[cmd[2]])
    print(s)

lst = input().split()
printCmd(lst)
