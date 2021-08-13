import sys
from OPCode import *
from typetable import *

# "cmp" : {("01110", "C"),
#           "jmp" : ("01111", "E"),
#           "jlt" : ("10000", "E"),
#           "jgt" : ("10001", "E"),
#           "je" : ("10010", "E"),
#           "hlt" : ("10011", "F") }

# def printCmd(cmd):
#     op = cmd[0]
#     s = ''
#     if(op == "add"):
#         s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]
#         print (s)

# lst = input().split()
# printCmd(lst)

def printComp(cmd):
    op = cmd[0]
    s = ''
    if(op == "cmp"):
        s = opCode[op][0] + '00000' + reg[cmd[1]] + reg[cmd[2]]
    if(op == "jmp"):
        s = opCode[op][0] + '000' + label[cmd[1]]
    if(op == "jlt"):
        s = opCode[op][0] + '000' + label[cmd[1]]
    if(op == "jgt"):
        s = opCode[op][0] + '000' + label[cmd[1]]
    if(op == "je"):
        s = opCode[op][0] + '000' + label[cmd[1]]
    if(op == "hlt"):
        s = opCode[op][0] + '00000000000'
    

lst = input().split()
printComp(lst)