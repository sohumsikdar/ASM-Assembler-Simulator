from errorFile import *
from dic import *
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
        k = SymbList[cmd[-1]]
        tempS = get8bit(k)
        s = opCode[op][0] + reg[cmd[1]] + tempS

    if(op == 'st'):
        k = SymbList[cmd[-1]]
        tempS = get8bit(k)
        s = opCode[op][0] + reg[cmd[1]] + tempS
    
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

    if(op == "div"):
        s = opCode[op][0] + '00000' + reg[cmd[1]] + reg[cmd[2]]

    if(op ==  "rs"):
        k = int(cmd[-1][1:])
        s = opCode[op][0] + '000' + get8bit(k)

    if(op == "ls"):
        k = int(cmd[-1][1:])
        s = opCode[op][0] + '000' + get8bit(k)

    if(op == "xor"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]

    if(op == "or"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]

    if(op == "and"):
        s = opCode[op][0] + '00' + reg[cmd[1]] + reg[cmd[2]] + reg[cmd[3]]

    if(op == "not"):
        k = int(cmd[-1][1:])
        s = opCode[op][0] + '000' + get8bit(k)

    print(s)
