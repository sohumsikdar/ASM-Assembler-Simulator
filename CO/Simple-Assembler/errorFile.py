import sys
from dic import *
from commandFile import *

# Handle Mov seperately
def iscmdvalid(cmd):
    op = cmd[0]
    if(op not in opCode.keys()):
        return False
    t = opCode[op][1]
    

    if(t == 'A'):
        if(len(cmd) != 4):
            return False

        r1 = cmd[1]
        r2 = cmd[2]
        r3 = cmd[3]

        if((r1 not in reg.keys() or r1 == "FLAGS") or (r2 not in reg.keys() or r2 == "FLAGS") or (r3 not in reg.keys() or r3 == "FLAGS")):
            return False
        return True
    

    if(t == 'B'):
        if(len(cmd) != 3):
            return False
        r = cmd[1]
        if(cmd[2][0] != '$'):
            return False

        im = int(cmd[2][1:])
        if((r not in reg.keys() or r == "FLAGS") or im not in range (0, 256)):
            return False
        return True


    if(t == 'C'):
        if(len(cmd) != 3):
            return False
        r1 = cmd[1]
        r2 = cmd[2]
        if((r1 not in reg.keys() or r1 == "FLAGS") or (r2 not in reg.keys() or r2 == "FLAGS")):
            return False
        return True
    

    if(t == 'D'):
        if(len(cmd) != 3):
            return False
        r = cmd[1]
        var = cmd[2]
        if((r not in reg.keys() or r == "FLAGS") or var not in SymbList.keys() or var in label.keys()):
            return False
        return True


    if(t == 'E'):
        if(len(cmd) != 2):
            return False
        var = cmd[1]
        if(var not in label.keys() or var in SymbList.keys()):
            return False
        return True
    
    