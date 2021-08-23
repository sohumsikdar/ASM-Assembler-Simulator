import sys
from matplotlib import pyplot as plt
from OPClass import *
PC = 0
commandList = []
y_coord = []
temp = []

def get16bit (k):
    s = '{0:016b}'.format(k)
    return s

def get8bit (k):
    s = '{0:08b}'.format(k)
    return s

# Dump all values of the registers
def dump():
    for r in Reg.keys():
        print(get16bit(Reg[r]), end = " ")

def flagReset():
    Reg["111"] = 0

def getOut(cmd):
    OPC = cmd[:5]
    if OPC in OPDic["A"]:
        reg1 = cmd[7:10]
        reg2 = cmd[10:13]
        reg3 = cmd[13:]
        if(OPC == "00000"):
            add(reg1, reg2, reg3)
        if(OPC == "00001"):
            sub(reg1, reg2, reg3)
        if(OPC == "00110"):
            mul(reg1, reg2, reg3)
        if(OPC == "01010"):
            XOR(reg1, reg2, reg3)
        if(OPC == "01011"):
            OR(reg1, reg2, reg3)
        if(OPC == "01100"):
            AND(reg1, reg2, reg3)
            
    
    elif OPC in OPDic["B"]:
        reg = cmd[5:8]
        IM = int(cmd[8:], 2)
        if(OPC == "00010"):
            movI(reg, IM)
        if(OPC == "01000"):
            RS(reg, IM)
        if(OPC == "01001"):
            LS(reg, IM)


    elif OPC in OPDic["C"]:
        reg1 = cmd[10:13]
        reg2 = cmd[13:]

        if(OPC == "00011"):
            movR(reg1, reg2)
        if(OPC == "00111"): 
            div(reg1, reg2)
        if(OPC == "01101"):
            NOT(reg1, reg2)
        if(OPC == "01110"):
            CMP(reg1, reg2)

    elif OPC in OPDic["D"]:
        reg = cmd[5:8]
        mem = cmd[8:]

        if(OPC == "00100"):
            load(reg, mem)
        if(OPC == "00101"):
            store(reg, mem)


def add(r1, r2, r3):
    Reg[r1] = Reg[r2] + Reg[r3]
    if Reg[r1] > 65535:
        Reg[r1] = Reg[r1] % 65536
        Reg["111"] = 8
    else:
        flagReset()
    dump()


def sub(r1, r2, r3):
    Reg[r1] = Reg[r2] - Reg[r3]
    if Reg[r1] < 0:
        Reg[r1] = 0
        Reg["111"] = 8
    else:
        flagReset()
    dump()

def mul(r1, r2, r3):
    Reg[r1] = Reg[r2] * Reg[r3]
    if Reg[r1] > 65535:
        Reg[r1] = Reg[r1] % 65536
        Reg["111"] = 8
    else:
        flagReset()
    dump()

def OR(r1, r2, r3):
    Reg[r1] = Reg[r2] | Reg[r3]
    flagReset()
    dump()

def XOR(r1, r2, r3):
    Reg[r1] = Reg[r2] ^ Reg[r3]
    flagReset()
    dump()

def AND(r1, r2, r3):
    Reg[r1] = Reg[r2] & Reg[r3]
    flagReset()
    dump()

def movI(r, im):
    Reg[r] = im
    flagReset()
    dump()

def RS(r, im):
    Reg[r] = Reg[r] >> im
    flagReset()
    dump()

def LS(r, im):
    Reg[r] = Reg[r] << im
    if Reg[r] > 65535:
        Reg[r] = Reg[r] % 65536
        Reg["111"] = 8
    else:
        flagReset()
    dump()

def movR(reg1, reg2):
    Reg[reg1] = Reg[reg2]
    flagReset()
    dump()

def div(reg1, reg2):
    Reg["000"] = Reg[reg1] // Reg[reg2]
    Reg["001"] = Reg[reg1] % Reg[reg2]
    flagReset()
    dump()
    
def NOT(reg1, reg2):
    Reg[reg1] = 65535 ^ Reg[reg2]
    flagReset()
    dump()

def CMP(reg1, reg2):
    flagReset()
    if(Reg[reg1] > Reg[reg2]):
        Reg["111"] = 2

    if(Reg[reg1] < Reg[reg2]):
        Reg["111"] = 4

    if(Reg[reg1] == Reg[reg2]):
        Reg["111"] = 1
    dump()

def load(reg, mem):
    if(mem not in memAddr.keys()):
        memAddr[mem] = 0
    Reg[reg] = memAddr[mem]
    flagReset()
    dump()


def store(reg, mem):
    memAddr[mem] = Reg[reg]
    flagReset()
    dump()


while True:
    try:
        s = input()
        commandList.append(s)

    except EOFError:
        break


while(commandList[PC] != "1001100000000000"):
    OPC = commandList[PC][:5]
    print(get8bit(PC), end = " ")
    y_coord.append(PC)
    # For non jump OPs
    if(OPC in OPDic["A"] or OPC in OPDic["B"] or OPC in OPDic["C"]):
        getOut(commandList[PC])
        print()
        PC += 1

    elif (OPC in OPDic["D"]):
        getOut(commandList[PC])
        print()
        mem = int(commandList[PC][8:], 2)
        y_coord.append(mem)
        temp.append(PC)
        PC += 1
    
    # For jump OPs
    else:
        mem = int(commandList[PC][8:], 2)
        # jmp
        if OPC == "01111":
            PC = mem
    
        # jlt
        if OPC == "10000":
            if(Reg["111"] == 4):
                PC = mem
            else:
                PC += 1
       
        # jgt
        if OPC == "10001":
            if(Reg["111"] == 2):
                PC = mem
            else:
                PC += 1
                
        # jge
        if OPC == "10010":
            if(Reg["111"] == 1):
                PC = mem
            else:
                PC += 1   
                

        flagReset()
        dump()
        print()



flagReset()
print(get8bit(PC), end = " ")
dump()
y_coord.append(PC)
PC += 1
print()

for i in range (0,256):
    if(i < len(commandList)):
        print(commandList[i])
    else:
        if(get8bit(i) in memAddr.keys()):
            print(get16bit(memAddr[get8bit(i)]))
        else:
            print("0000000000000000")

#Plotting the graph
def plot(): 
    x_coord = [i for i in range(len(y_coord))]
    x_coord += temp
    x_coord.sort()
    x_coord = x_coord[:len(y_coord)]
    plt.style.use('seaborn')
    plt.scatter(x_coord,y_coord, cmap='summer', edgecolor='black', linewidth=1, alpha=0.75)
    plt.title('Memory accessed Vs Cycles')
    plt.xlabel('Cycle number')
    plt.ylabel('Memory address')
    plt.tight_layout()
    plt.show()

plot()