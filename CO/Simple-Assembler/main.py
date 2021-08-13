import sys
from dic import *
from commandFile import *

PC = 1
commandList = []

def giveOut(OP, lst):
    pass

# Assigns the Symbol/var none and returns bool to append the command
def valid(lst):
    if(lst[0] != 'var'):
        return True
    global SymbList
    SymbList[lst[1]] = None
    return False

# Storing the input lines in different lists
while True:
    try:
        lst = input().split()
        if(valid(lst) == True):
            commandList.append(lst)

    except EOFError:
        break



# Giving the values to the Symbols/var
ctr = len(commandList)
for k in SymbList.keys():
    SymbList[k] = ctr
    ctr += 1

# Giving the values to the labels

for i,cmd in enumerate(commandList):
    if((cmd[0][0:-1] and cmd[0]) not in opCode.keys()):
        label[cmd[0][0:-1]] = get8bit(i)


for i,cmd in enumerate(commandList):
    if(cmd[0][-1] == ':'):
        cmd = cmd[1:]
    printCmd(cmd)
