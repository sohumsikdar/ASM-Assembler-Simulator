from OPClass import *
PC = 0
commandList = []

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
            sub(reg1, reg2, reg2)
        if(OPC == "00110"):
            mul(reg1, reg2, reg2)
        if(OPC == "01010"):
            OR(reg1, reg2, reg2)
        if(OPC == "01011"):
            XOR(reg1, reg2, reg2)
        if(OPC == "01100"):
            AND(reg1, reg2, reg2)
            
    
    elif OPC in OPDic["B"]:
        reg = cmd[5:8]
        IM = int(cmd[8:], 2)
        print(reg, IM)
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
        Reg[r1] = Reg[r1] % 65535
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
    Reg[r] >> im
    flagReset()
    dump()

def LS(r, im):
    Reg[r] = Reg[r] << im
    if Reg[r] > 65535:
        Reg[r] = Reg[r] % 65535
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

def store(reg, mem):
    memAddr[mem] = Reg[reg]


while True:
    try:
        s = input()
        commandList.append(s)

    except EOFError:
        break

    
while(commandList[PC] != "1001100000000000"):
    print(get8bit(PC), end = " ")
    getOut(commandList[PC])
    print()
    PC += 1

flagReset()
print(get8bit(PC), end = " ")
dump()
PC += 1

