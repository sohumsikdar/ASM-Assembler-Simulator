import sys
from dic import *
from commandFile import *
from errorFile import *

PC = 0
commandList = []
lineArr = []
linNum = 0

def giveOut(OP, lst):
    pass

# Assigns the Symbol/var none and returns bool to append the command
def valid(lst, i):
    if(lst[0] != 'var'):
        return True

    if(len(lst) == 1):
        print("Error: no variable name was mentioned during declaration at line " + str(i))
        sys.exit()

    elif(lst[1] in SymbList.keys()):
        print("Error: Redeclaration of a variable at line " + str(i))
        sys.exit()

    if(len(commandList) != 0):
        print("Error: Variable not declared at the beginning at line " + str(i))
        sys.exit()

    for char in lst[1]:
        if(not(char.isalnum() == True or char == "_")):
            print("Error: invalid varible name at line " + str(i))
            sys.exit()

    if(lst[1].isdigit()):
        print("Error: purely numberic variable name at line " + str(i))
        sys.exit()

    SymbList[lst[1]] = None
    return False

# Storing the input lines in different lists
while True:
    linNum += 1
    try:
        lst = input().split()
        if(len(lst) == 0):
            continue
        if(valid(lst, linNum) == True):
            commandList.append(lst)
            lineArr.append(linNum)

    except EOFError:
        break


# Giving the values to the Symbols/var
ctr = len(commandList)
for k in SymbList.keys():
    SymbList[k] = ctr
    ctr += 1
    


# Giving the values to the labels
for i,cmd in enumerate(commandList):
    if((cmd[0][0:-1] and cmd[0]) not in (opCode.keys() or reg.keys())):
        l = cmd[0]
        if(l[-1] != ':'):
            print("Error: invalid label in instruction " + str(lineArr[i]))
            sys.exit()
        l = l[0:-1]

        for char in l:
            if(not(char.isalnum() == True or char == '_')):
                print("Error: invalid label in instruction " + str(lineArr[i]))
                sys.exit()
        
        if(l.isdigit()):
            print("Error: invalid label in instruction " + str(lineArr[i]))
            sys.exit()
        
        if(cmd[0][0:-1] in label.keys()):
            print("Error: Redeclaration of a label in instruction " + str(lineArr[i]))
            sys.exit()   

        label[cmd[0][0:-1]] = get8bit(i)

# check for lesser than 257 instructions
if(len(commandList) > 256):
    print("Error: More than 256 instuctions")
    sys.exit()


for i,cmd in enumerate(commandList):
    # Strip for flags
    if(cmd[0][-1] == ':'):
        if(len(cmd) == 1):
            print("Error in instruction " + str(lineArr[i]))
            sys.exit()
        cmd = cmd[1:]

    # Check for hlts
    hltCheck = True
    if(cmd[0] == "hlt"):
        if(not(len(cmd) == 1 and i + 1 == len(commandList))):
            print("Error in instruction " + str(lineArr[i]))
            break
        else:
            print("1001100000000000")
            break
           
    #Checks for Syntax error
    flag = iscmdvalid(cmd)

    if(flag == False):
        print("Error in instruction at line " + str(lineArr[i]))
        break
    else:
        printCmd(cmd)

    if(i == len(commandList) - 1 and cmd != "hlt"):
        print("Error: missing hlt instruction at line " + str(lineArr[i]))
        sys.exit()