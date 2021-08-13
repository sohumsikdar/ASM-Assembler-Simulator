import sys
from OPCode import *
from typetable import *
from commandFile import *
from symboltable import *

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

for i,cmd in enumerate(commandList):
    printCmd(cmd)
    