import sys
from dic import *
from commandFile import *

# Handle Mov seperately
def iscmdvalid(cmd):
    op = cmd[0]
    if(op not in opCode.keys()):
        print("Invalid OP Code ")
        return False
    t = opCode[op][1]
    
    if(op == "mov"):
        if(len(cmd) != 3):
            print("Invalid syntax ")
            return False

        if(cmd[2][0] == '$'):
            if(((cmd[1] not in reg.keys() or cmd[1] == "FLAGS"))):
                print(cmd[1] + " not a register ")
                return False
            im = cmd[2][1:]
            if(im.isdigit() == False):
                print("Invalid immediate value ")
                return False
            im = int(im)
            if(im not in range(0, 256)):
                print("Imm value not in range ")
                return False
            return True

        elif(cmd[2] in reg.keys()):
            if(cmd[1] in reg.keys() and cmd[1] != "FLAGS"):
                return True
            print("Invalid register ")
            return False

        else:
            print("Invalid syntax ")
            return False

    elif(t == 'A'):
        if(len(cmd) != 4):
            print("Invalid syntax ")
            return False

        r1 = cmd[1]
        r2 = cmd[2]
        r3 = cmd[3]

        if((r1 not in reg.keys() or r1 == "FLAGS") or (r2 not in reg.keys() or r2 == "FLAGS") or (r3 not in reg.keys() or r3 == "FLAGS")):
            print("Invalid register names ")
            return False
        return True
    

    elif(t == 'B'):
        if(len(cmd) != 3):
            print("Invalid syntax ")
            return False
        r = cmd[1]
        if(cmd[2][0] != '$'):
            print("Invalid syntax ")
            return False

        im = cmd[2][1:]
        if(im.isdigit() == False):
            print("Invalid immediate value ")
            return False
        im = int(im)
        if((r not in reg.keys() or r == "FLAGS")):
            print("Invalid register names ")
            return False
        if im not in range (0, 256):
            print("Imm value not in range ")
            return False
        return True


    elif(t == 'C'):
        if(len(cmd) != 3):
            print("Invalid syntax ")
            return False
        r1 = cmd[1]
        r2 = cmd[2]
        if((r1 not in reg.keys() or r1 == "FLAGS") or (r2 not in reg.keys() or r2 == "FLAGS")):
            print("Invalid register names ")
            return False
        return True
    

    elif(t == 'D'):
        if(len(cmd) != 3):
            print("Invalid syntax ")
            return False
        r = cmd[1]
        var = cmd[2]
        if((r not in reg.keys() or r == "FLAGS")):
            print("Invalid register names ")
            return False
        if var not in SymbList.keys() or var in label.keys():
            print("Invalid use of variables ")
            return False
        return True


    elif(t == 'E'):
        if(len(cmd) != 2):
            print("Invalid syntax ")
            return False
        var = cmd[1]
        if(var not in label.keys() or var in SymbList.keys()):
            print("Invalid use of label ")
            return False
        return True

    else:
        print("Invalid syntax ")
        return False
    
    