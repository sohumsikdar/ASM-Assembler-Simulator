import sys
from OPCode import *
from typetable import *

PC = 1
SymbList = []
commandList = []

def valid(lst):
    if(lst[0] != 'var'):
        return True
    global SymbList
    SymbList.append(lst[1])
    return False

while True:
    try:
        lst = input().split()
        if(valid(lst) == True):
            commandList.append(lst)
    except EOFError:
        break

print(commandList)
print(len(commandList))
print(SymbList)