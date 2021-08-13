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



def printCmd(cmd):
    op = cmd[0]
    s = ''
    if(op == "add"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
        print (s)

lst = input().split()
printCmd(lst)

# 00000 00 000 001 010
