
display=0

def getop(instr):
    return instr>>26

def getrs(instr):
    return (instr>>21) & 0x1F

def getrt(instr):
    return (instr>>16) & 0x1F

def getrd(instr):
    return (instr>>11) & 0x1F

def getsh(instr):
    return (instr>>6) & 0x1F

def getfun(instr):
    return (instr) & 0x3F

def getimm(instr):
    imm=(instr) & 0xFFFF
    return imm

def makesigned8(imm):
    imm &= 0xFF
    if(imm & 0x80):
        imm = -0x100 + imm
    return imm


def makesigned16(imm):
    imm &= 0xFFFF
    if(imm & 0x8000):
        imm = -0x10000 + imm
    return imm

def makesigned32(imm):
    imm &= 0xFFFFFFFF
    if(imm & 0x80000000):
        imm = -0x100000000 + imm
    return imm

def geta(instr):
    return instr&0x7FF

def getaddr(instr):
    return (instr) & 0x3FFFFFF

KL4E_Decompress = [
    0x27BDF4F0, 0xAFB20B00, 0x00856021, 0x248B0000,
    0xAFB10AFC, 0x240A0005, 0x27A5F508, 0xAFB00AF8,
    0x0000C821, 0x24080001, 0xAFB30B04, 0x2413FFFF,
    0x27A10038, 0xAFB40B08, 0x2594FFC0, 0x7C142804,
    0x80D00000, 0x88C90004, 0x98C90001, 0xAFB50B0C,
    0x06000222, 0x7C0948E0, 0x7E1508C0, 0x0015A900,
    0x24110080, 0x0235A823, 0x7EB57A04, 0x32100007,
    0x7EB5FC04, 0xACB50AF8, 0x24A50008, 0x14BDFFFD,
    0xACB50AF4, 0x080009C6, 0x241500FF, 0x90D20005,
    0x00094A00, 0x24C60001, 0x01324821, 0x026E0018,
    0x000E90C2, 0x01D27023, 0x00006812, 0x012DC02B,
    0x17000013, 0x00199202, 0x00139A00, 0x012D4823,
    0xA1EEFFFF, 0x16400013, 0x026D9823, 0x00797821,
    0x00136E02, 0x91EEFFFF, 0x11A0FFEC, 0x0019C840,
    0x00139202, 0x024E0018, 0x000E90C2, 0x01D27023,
    0x00006812, 0x012DC02B, 0x1300FFF0, 0x00199202,
    0x00009812, 0x25CE001F, 0xA1EEFFFF, 0x1240FFEF,
    0x27390001, 0x00138E02, 0x90AD09B8, 0x1220001C,
    0xA1790000, 0x00131A02, 0x006D0018, 0x256B0001,
    0x000D1902, 0x00008812, 0x0131702B, 0x15C00020,
    0x01A31823, 0xA0A309B8, 0x24A5FFFF, 0x00BD282C,
    0x01314823, 0x116C01DE, 0x02719823, 0x7D795204,
    0x02191807, 0x30630007, 0x0003CA00, 0x0323C023,
    0x03B81821, 0x080009A2, 0x24190001, 0x00405821,
    0x91790000, 0x00138E02, 0x1620FFE6, 0x90AD09B8,
    0x90D80005, 0x256B0001, 0x00094A00, 0x24C60001,
    0x01384821, 0x026D0018, 0x00139A00, 0x000D1902,
    0x00008812, 0x0131702B, 0x11C0FFE2, 0x01A31823,
    0x2418FFFF, 0x2463000F, 0x90AD09C0, 0x0011CE02,
    0x13200149, 0x00009812, 0xA0A309B8, 0x00139202,
    0x024D0018, 0x24A50008, 0x000D9102, 0x00008812,
    0x0131C82B, 0x1720014D, 0x01B21823, 0x02719823,
    0x07000068, 0x01314823, 0xA0A309B8, 0x030BC804,
    0x00188940, 0x7F3120C4, 0x7CB11004, 0x03B18821,
    0x2719FFFD, 0x922509F8, 0x00131E02, 0x07220027,
    0x240E0001, 0x92320A10, 0x10600179, 0x00131202,
    0x00520018, 0x001210C2, 0x02429023, 0x00001812,
    0x0123102B, 0x14400186, 0x244E0002, 0x01234823,
    0x02639823, 0x1B200018, 0x00131E02, 0x10600186,
    0x00131202, 0x00520018, 0x001210C2, 0x02429023,
    0x00007812, 0x012F102B, 0x1440016C, 0x000E7040,
    0x026F9823, 0x00131E02, 0x1328000B, 0x012F4823,
    0x1060016D, 0x000E7040, 0x00139842, 0x0133102B,
    0x01331823, 0x0062480A, 0x2739FFFF, 0x1728FFF9,
    0x01C27021, 0x00131E02, 0xA2320A10, 0x10600141,
    0x00131202, 0x00450018, 0x000510C2, 0x00A22823,
    0x00001812, 0x0123102B, 0x14400146, 0x000E7040,
    0xA22509F8, 0x01234823, 0x1B00002B, 0x02639823,
    0x92250A00, 0x00131E02, 0x1060012B, 0x00131202,
    0x00450018, 0x000510C2, 0x00A22823, 0x00001812,
    0x0123102B, 0x1440011D, 0x000E7040, 0xA2250A00,
    0x01234823, 0x1308000F, 0x02639823, 0x92250A08,
    0x00131E02, 0x106000FE, 0x00131202, 0x00450018,
    0x000510C2, 0x00A22823, 0x00001812, 0x0123102B,
    0x144000FE, 0x000E7040, 0x01234823, 0x02639823,
    0xA2250A08, 0x00386821, 0x24120100, 0x24110008,
    0x00131E02, 0x1460000E, 0x01B1C821, 0x90C30005,
    0x00094A00, 0x24C60001, 0x01234821, 0x08000A5F,
    0x00139A00, 0xA0A309B8, 0x24120040, 0x24110008,
    0x03B86821, 0x00131E02, 0x1060FFF4, 0x01B1C821,
    0x933807F1, 0x00131202, 0x00118840, 0x00580018,
    0x001810C2, 0x03027823, 0x00001812, 0x0123C02B,
    0x13000130, 0x0232C023, 0x00009812, 0x25EF001F,
    0xA32F07F1, 0x0700FFEF, 0x26310008, 0x03B88821,
    0x0018C0C3, 0x2719FFFD, 0x8E2D0928, 0x07220027,
    0x240F0001, 0x00131602, 0x10400096, 0x7DB23E00,
    0x00131202, 0x00520018, 0x001210C2, 0x02429023,
    0x00001812, 0x0123102B, 0x144000A2, 0x244F0002,
    0x01234823, 0x1B200018, 0x02639823, 0x00131602,
    0x104000A2, 0x00131202, 0x00520018, 0x001210C2,
    0x02429023, 0x00001812, 0x0123102B, 0x14400088,
    0x000F7840, 0x01234823, 0x1328000B, 0x02639823,
    0x00131602, 0x10400089, 0x000F7840, 0x00139842,
    0x0133102B, 0x01331823, 0x2739FFFF, 0x0062480A,
    0x1728FFF9, 0x01E27821, 0x7E4DFE04, 0x00131602,
    0x10400069, 0x7DB23800, 0x00131202, 0x00520018,
    0x001210C2, 0x02429023, 0x00001812, 0x0123102B,
    0x14400054, 0x000F7840, 0x7E4D3804, 0x01234823,
    0x1B00001E, 0x02639823, 0x00131602, 0x10400053,
    0x7DB23A00, 0x00131202, 0x00520018, 0x001210C2,
    0x02429023, 0x00001812, 0x0123102B, 0x1440003F,
    0x000F7840, 0x7E4D7A04, 0x01234823, 0x1308000F,
    0x02639823, 0x00131602, 0x1040002D, 0x7DB23C00,
    0x00131202, 0x00520018, 0x001210C2, 0x02429023,
    0x00001812, 0x0123102B, 0x1440002C, 0x000F7840,
    0x7E4DBC04, 0x01234823, 0x02639823, 0x25EFFFFF,
    0x0164C823, 0x01F9C82B, 0x132000D6, 0xAE2D0928,
    0x37A50006, 0x016E1021, 0x0282882B, 0x1620000F,
    0x016F1823, 0xBD78003F, 0x29F10003, 0x1620000E,
    0x7C450004, 0x7C0E0804, 0x016E7021, 0x88790002,
    0x9879FFFF, 0xA9790003, 0x24630004, 0x116EFEF3,
    0xB9790000, 0x08000AD6, 0x256B0004, 0x004C882B,
    0x122000C3, 0x7C450004, 0x1162FED2, 0x9079FFFF,
    0xA1790000, 0x256B0001, 0x08000AE1, 0x24630001,
    0x90C30005, 0x00094A00, 0x24C60001, 0x01234821,
    0x02720018, 0x08000ABD, 0x00139A00, 0x2652001F,
    0x7E4DBC04, 0x08000AC7, 0x00009812, 0x2652001F,
    0x7E4D7A04, 0x1308FFD2, 0x00009812, 0x08000AB8,
    0x25EF0001, 0x2652001F, 0x7E4D3804, 0x1B00FFCC,
    0x00009812, 0x08000AA9, 0x25EF0001, 0x90C30005,
    0x00094A00, 0x24C60001, 0x01234821, 0x02720018,
    0x08000AAE, 0x00139A00, 0x90C30005, 0x00094A00,
    0x24C60001, 0x01234821, 0x02720018, 0x08000A9F,
    0x00139A00, 0x90C30005, 0x00094A00, 0x24C60001,
    0x01234821, 0x02720018, 0x08000A79, 0x00139A00,
    0x00009812, 0x25EF0001, 0x1328FF83, 0x2652001F,
    0x00131602, 0x1440FF79, 0x000F7840, 0x90C30005,
    0x00094A00, 0x24C60001, 0x01234821, 0x08000A93,
    0x001399C0, 0x00009812, 0x1B20FF77, 0x2652001F,
    0x00131602, 0x1440FF60, 0x00131202, 0x90C30005,
    0x00094A00, 0x24C60001, 0x01234821, 0x00139A00,
    0x08000A85, 0x00131202, 0x90D20005, 0xA0A309B8,
    0x00094A00, 0x24C60001, 0x01324821, 0x24A50008,
    0x026D0018, 0x00119A00, 0x000D9102, 0x00008812,
    0x0131C82B, 0x1320FEB5, 0x01B21823, 0x170AFEA5,
    0x27180001, 0x2463000F, 0x080009F1, 0x00009812,
    0x90C30005, 0x00094A00, 0x24C60001, 0x01234821,
    0x02650018, 0x08000A43, 0x00139A00, 0x24A5001F,
    0x25CE0001, 0x15D5FF02, 0x00009812, 0x01641023,
    0x10E00002, 0x24C60005, 0xACE60000, 0x8FB50B0C,
    0x8FB40B08, 0x8FB30B04, 0x8FB20B00, 0x8FB10AFC,
    0x8FB00AF8, 0x03E00008, 0x27BD0B10, 0x24A5001F,
    0xA2250A00, 0x25CE0001, 0x1308FEF2, 0x00009812,
    0x08000A3F, 0x92250A08, 0x90C30005, 0x00094A00,
    0x24C60001, 0x01234821, 0x02650018, 0x08000A34,
    0x00139A00, 0x90C30005, 0x00094A00, 0x24C60001,
    0x01234821, 0x02650018, 0x00139A00, 0x000510C2,
    0x00A22823, 0x00001812, 0x0123102B, 0x1040FEBC,
    0x000E7040, 0x24A5001F, 0xA22509F8, 0x00009812,
    0x1B00FED8, 0x25CE0001, 0x08000A30, 0x92250A00,
    0x90C30005, 0x00094A00, 0x24C60001, 0x01234821,
    0x02720018, 0x08000A00, 0x00139A00, 0x00009812,
    0x25CE0001, 0x2652001F, 0x1328FE9F, 0x00131E02,
    0x1460FE95, 0x000E7040, 0x90C30005, 0x00094A00,
    0x24C60001, 0x01234821, 0x08000A1A, 0x001399C0,
    0x00009812, 0x2652001F, 0x1B20FE93, 0x00131E02,
    0x1460FE7C, 0x00131202, 0x90C30005, 0x00094A00,
    0x24C60001, 0x01234821, 0x00139A00, 0x08000A0C,
    0x00131202, 0x02639823, 0x01234823, 0x0700FEC1,
    0xA32F07F1, 0x5700FED1, 0x2718FFF8, 0x15ABFF2C,
    0x00007821, 0x3C028000, 0x08000B4E, 0x34420108,
    0x3C028000, 0x08000B4E, 0x34420104, 0x01244821,
    0x012C182B, 0x1060FFFA, 0x00000000, 0x90C30005,
    0x256B0001, 0x1169FF9D, 0xA1630000, 0x08000BAA,
    0x24C60001,
]


# Register printable name mapping
rg = { 0:"$zero",1:"$at", 2:"$v0", 3:"$v1",
    4:"$a0", 5:"$a1", 6:"$a2", 7:"$a3",
    8:"$a4",9:"$a5",10:"$a6",11:"$a7",12:"$t4",13:"$t5",14:"$t6",15:"$t7",
    16:"$s0",17:"$s1",18:"$s2",19:"$s3",20:"$s4",21:"$s5",22:"$s6",23:"$s7",24:"$t8",25:"$t9",
    26:"$k0",27:"$k1", 28:"$gp", 29:"$sp", 30:"$fp", 31:"$ra"
            }
rgid= {'$zero': 0, '$at': 1, '$v0': 2, '$v1': 3, '$a0': 4, '$a1': 5, '$a2': 6, '$a3': 7, '$a4': 8, '$a5': 9, '$a6': 10, '$a7': 11, '$t4': 12, '$t5': 13, '$t6': 14, '$t7': 15, '$s0': 16, '$s1': 17, '$s2': 18, '$s3': 19, '$s4': 20, '$s5': 21, '$s6': 22, '$s7': 23, '$t8': 24, '$t9': 25, '$k0': 26, '$k1': 27, '$gp': 28, '$sp': 29, '$fp': 30, '$ra': 31}
# Actually MIPS 32 Registers
regs = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
CP0 = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
CP1 = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]

# Special registers
LL = 0
LO = 0
HI = 0
PC = 0
IntegerOverflow=0

Memory = bytearray(0x1000000)
MemoryBase = 0

def readMemory32(addr):
    global MemoryBase
    global Memory
    address=addr - MemoryBase
    if address>0x1000000:
        print("Error! %x is too big for memory, something is wrong" % address)
        return 0
    else:
        x = Memory[address]
        x |= (Memory[address+1]<<8)
        x |= (Memory[address+2]<<16)
        x |= (Memory[address+3]<<24)
        return x

def readMemory16(addr):
    global MemoryBase
    global Memory
    address=addr - MemoryBase
    if address>0x1000000:
        print("Error! %x is too big for memory, something is wrong" % address)
        return 0
    else:
        x = Memory[address]
        x |= (Memory[address+1]<<8)
        return x

def readMemory8(addr):
    global MemoryBase
    global Memory
    address=addr - MemoryBase
    if address>0x1000000:
        print("Error! %x is too big for memory, something is wrong" % address)
        return 0
    else:
        x = Memory[address]
        return x

def writeMemory32(addr, value):
    global MemoryBase
    global Memory
    address=addr - MemoryBase

    Memory[address] = value & 0xFF
    Memory[address+1] = (value>>8) & 0xFF
    Memory[address+2] = (value>>16) & 0xFF
    Memory[address+3] = (value>>24) & 0xFF

def writeMemory16(addr, value):
    global MemoryBase
    global Memory
    address=addr - MemoryBase
    Memory[address] = value & 0xFF
    Memory[address+1] = (value>>8) & 0xFF

def writeMemory8(addr, value):
    global MemoryBase
    global Memory
    address=addr - MemoryBase
    Memory[address] = value & 0xFF

def executeDelaySlot():
    global PC
    global display
    x=readMemory32(PC)
    if(display):
        print("0x%08x-DELAY: " % PC, end='')
    PC = PC + 4
    decodemips(x)
    
def op_r_add(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("add",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x=regs[rs] + regs[rt]
    if x >=0x100000000:
        IntegerOverflow=1
    else:
        regs[rd] = x & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))

def op_r_addu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("addu",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x=regs[rs] + regs[rt]
    regs[rd] = x & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))

def op_r_sub(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("sub",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x=regs[rs] - regs[rt]
    if x <0:
        IntegerOverflow=1
    else:
        regs[rd] = x & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))

def op_r_subu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("subu",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x=regs[rs] - regs[rt]
    regs[rd] = x & 0xFFFFFFFF

    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_and(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("and",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = regs[rs] & regs[rt]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_or(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("or",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = regs[rs] | regs[rt]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_xor(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("xor",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = regs[rs] ^ regs[rt]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_nor(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("nor",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = (regs[rs]^0xFFFFFFFF) & (regs[rt] ^ 0xFFFFFFFF)
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_slt(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("slt",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = makesigned32(regs[rs]) < makesigned32(regs[rt])
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_sltu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("sltu",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = regs[rs] < regs[rt]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))

def op_r_sll(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("sll",rg[rd], rg[rt],hex(shamt)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = (regs[rt] << shamt)  & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_srl(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("srl",rg[rd], rg[rt],hex(shamt)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = (regs[rt] >> shamt)  & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_jr(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global PC
    crs=regs[rs]
    if(display):
        print("%s %s" % ("jr",rg[rs]))
    executeDelaySlot()        
    PC = crs

def op_r_jalr(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global PC
    crs=regs[rs]
    if(display):
        print("%s %s" % ("jalr",rg[rs]))
    executeDelaySlot()
    regs[rgid['$ra']] = PC
    PC = crs

def op_r_sra(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("sra",rg[rd], rg[rt],hex(shamt)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x = regs[rt]
    #Handle Sign Extention
    if (x & 0x80000000):
        x = 0xFFFFFFFF00000000 | x
    
    regs[rd] = (x >> shamt)  & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_sllv(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("sllv",rg[rd], rg[rt],rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = (regs[rt] << (regs[rs] & 0x1f)) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_srlv(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("srlv",rg[rd], rg[rt],rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rd] = (regs[rt] >> (regs[rs] & 0x1f)) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_srav(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("srav",rg[rd], rg[rt],rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    #regs[rd] = (makesigned32(regs[rt]) >> (regs[rs] & 0x1f)) & 0xFFFFFFFF
    x = regs[rt]
    #Handle Sign Extention
    if (x & 0x80000000):
        x = 0xFFFFFFFF00000000 | x
    
    regs[rd] = (x >> (regs[rs] & 0x1f))  & 0xFFFFFFFF

    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_movz(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("movz",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    if regs[rt] == 0:
        regs[rd] = regs[rs]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))



def op_r_movn(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("movn",rg[rd], rg[rs],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    if regs[rt] != 0:
        regs[rd] = regs[rs]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


def op_r_syscall(rs,rt,rd,shamt):
    x= (rs<<15 | rt<<10 | rd<<5 | shamt)
    if(display):
        print("%s %s" % ("syscall",hex(x)))

def op_r_break(rs,rt,rd,shamt):
    x= (rs<<15 | rt<<10 | rd<<5 | shamt)
    if(display):
        print("%s %s" % ("break",hex(x)))

def op_r_sync(rs,rt,rd,shamt):
    if(display):
        print("%s" % ("sync"))

def op_r_mthi(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global HI
    if(display):
        print("%s %s" % ("mthi",rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd],"HI", HI), end='')
    HI = regs[rs]
    if(display):
        print("===> %s= 0x%08x" % ("HI", HI))
        
def op_r_mfhi(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global HI
    if(display):
        print("%s %s" % ("mfhi",rg[rd]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd],"HI", HI), end='')
    regs[rd] = HI
    if(display):
        print("===> %s= 0x%08x" % (rg[rd],regs[rd]))
        
def op_r_mtlo(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    if(display):
        print("%s %s" % ("mtlo",rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd],"LO", LO), end='')
    LO = regs[rs]
    if(display):
        print("===> %s= 0x%08x" % ("LO", LO))
        
def op_r_mflo(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    if(display):
        print("%s %s" % ("mflo",rg[rd]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd],"LO", LO), end='')
    regs[rd] = LO
    if(display):
        print("===> %s= 0x%08x" % (rg[rd],regs[rd]))

def op_r_mult(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("mult",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    #x = (makesigned32(regs[rs]) * makesigned32(regs[rt])) & 0xFFFFFFFFFFFFFFFF
    if (regs[rs] & 0x80000000):
        xs = 0xFFFFFFFF00000000 | regs[rs]
        print("negative mult1")
    else:
        xs = regs[rs]
    if (regs[rt] & 0x80000000):
        xt = 0xFFFFFFFF00000000 | regs[rt]
        print("negative mult2")
    else:
        xt = regs[rt]    
    x = (xs * xt) & 0xFFFFFFFFFFFFFFFF
    LO = x & 0xFFFFFFFF
    HI = (x>>32) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))


def op_r_multu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("multu",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x = (regs[rs] * regs[rt]) & 0xFFFFFFFFFFFFFFFF
    LO = x & 0xFFFFFFFF
    HI = (x>>32) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))

def op_r_div(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("div",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x = makesigned32(regs[rs]) // makesigned32(regs[rt])
    LO = x & 0xFFFFFFFF
    x = makesigned32(regs[rs]) % makesigned32(regs[rt])
    HI = x & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))

def op_r_divu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("divu",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    x = regs[rs] // regs[rt]
    LO = x & 0xFFFFFFFF
    x = regs[rs] % regs[rt]
    HI = x & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))

def op_r_madd(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("madd",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x LO=0x%08x, HI=0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt], LO, HI), end='')
    x = makesigned32(regs[rs]) * makesigned32(regs[rt])
    y = (HI<<32) | LO
    z = (y + x) & 0xFFFFFFFFFFFFFFFF
    LO = z & 0xFFFFFFFF
    HI = (z>>32) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))

def op_r_maddu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("maddu",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x LO=0x%08x, HI=0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt], LO, HI), end='')
    x = regs[rs] * regs[rt]
    y = (HI<<32) | LO
    z = (y + x) & 0xFFFFFFFFFFFFFFFF
    LO = z & 0xFFFFFFFF
    HI = (z>>32) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))


def op_r_msub(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("msub",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x LO=0x%08x, HI=0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt], LO, HI), end='')
    x = makesigned32(regs[rs]) * makesigned32(regs[rt])
    y = (HI<<32) | LO
    z = (y - x)  & 0xFFFFFFFFFFFFFFFF
    LO = z & 0xFFFFFFFF
    HI = (z>>32) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))


def op_r_msubu(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    global LO
    global HI
    if(display):
        print("%s %s %s" % ("msubu",rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x LO=0x%08x, HI=0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt], LO, HI), end='')
    x = regs[rs] * regs[rt]
    y = (HI<<32) | LO
    z = (y - x)  & 0xFFFFFFFFFFFFFFFF
    LO = z & 0xFFFFFFFF
    HI = (z>>32) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % ("LO", LO, "HI", HI))



def op_r_min(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("min",rg[rd],rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    if (makesigned32(regs[rs]) < (makesigned32(regs[rt]))):
        regs[rd] = regs[rs]
    else:
        regs[rd] = regs[rt]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))

def op_r_max(rs,rt,rd,shamt):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("max",rg[rd],rg[rs], rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    if (makesigned32(regs[rs]) < (makesigned32(regs[rt]))):
        regs[rd] = regs[rt]
    else:
        regs[rd] = regs[rs]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x, %s= 0x%08x" % (rg[rd],regs[rd], rg[rs], regs[rs], rg[rt], regs[rt]))


# MIPS R type function mapping
r_funcs = {
        32:op_r_add,
        33:op_r_addu,
        34:op_r_sub,
        35:op_r_subu,
        36:op_r_and,
        37:op_r_or,
        38:op_r_xor,
        39:op_r_nor,
        42:op_r_slt,
        43:op_r_sltu,
        0:op_r_sll,
        2:op_r_srl,
        8:op_r_jr,
        9:op_r_jalr,
        3:op_r_sra,
        4:op_r_sllv,
        6:op_r_srlv,
        7:op_r_srav,
        10:op_r_movz,
        11:op_r_movn,
        12:op_r_syscall,
        13:op_r_break,
        15:op_r_sync,
        16:op_r_mfhi,
        17:op_r_mthi,
        18:op_r_mflo,
        19:op_r_mtlo,
        24:op_r_mult,
        25:op_r_multu,
        26:op_r_div,
        27:op_r_divu,
        28:op_r_madd,
        29:op_r_maddu,
        46:op_r_msub,
        47:op_r_msubu,
        44:op_r_max,
        45:op_r_min
            }

# MIPS R type instruction support
def process_r(rs,rt,rd,shamt,funct):
    if funct in r_funcs:
        op_fun = r_funcs[funct]
        op_fun(rs,rt,rd,shamt)
    else:
        print("r_type %d is not supported yet\n" % funct)

#--------------------------------------------------------------------------
# J-type function supported
#

def op_j_j(addr):
    global regs
    global rg
    global display
    global PC
    addr <<= 2
    if (display):
        print("%s %s" % ("j", hex(addr)))
    executeDelaySlot()
    PC = addr

def op_j_jal(addr):
    global regs
    global rg
    global display
    global PC
    addr <<= 2
    if (display):    
        print("%s %s" % ("jal", hex(addr)))
    executeDelaySlot()
    regs[rgid['$ra']] = PC
    PC = addr


j_funcs = { 2:op_j_j,
            3:op_j_jal
          }

def process_j(op,addr):
    if op in j_funcs:
        op_fun = j_funcs[op]
        op_fun(addr)
    else:
        print("j_type %d is not supported yet\n" % op)


#--------------------------------------------------------------------------
# I-type function supported
#

def op_i_bltz(rs,rt,immin):
    global regs
    global rg
    global display
    global PC
    imm = makesigned16(immin)
    imm <<= 2
    cPC=PC
    crs=regs[rs]
    if rt == 0:
        if(display):
            print("%s %s, %s" % ("bltz", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        executeDelaySlot()
        #x = makesigned32(regs[rs])
        if (crs&0x80000000):
            PC = cPC + imm
    elif rt == 1:
        if(display):
            print("%s %s, %s" % ("bgez", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        executeDelaySlot()
        #x = makesigned32(regs[rs])
        if ((crs&0x80000000) == 0):
            PC = cPC + imm
    elif rt == 2:
        if(display):
            print("%s %s, %s" % ("bltzl", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        #executeDelaySlot()
        #x = makesigned32(regs[rs])
        if (crs&0x80000000):
            executeDelaySlot()
            PC = cPC + imm
        else:
            PC = cPC + 4
    elif rt == 3:
        if(display):
            print("%s %s, %s" % ("bgezl", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        #executeDelaySlot()
        #x = makesigned32(regs[rs])
        if ((crs&0x80000000) == 0):
            executeDelaySlot()
            PC = cPC + imm
        else:
            PC = cPC + 4
    elif rt == 16:
        if(display):
            print("%s %s, %s" % ("bltzal", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        executeDelaySlot()
        #x = makesigned32(regs[rs])
        if (crs&0x80000000):
            PC = cPC + imm
            regs[rgid['$ra']] = cPC +4
    elif rt == 17:
        if(display):
            print("%s %s, %s" % ("bgezal", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        executeDelaySlot()
        #x = makesigned32(regs[rs])
        if ((crs&0x80000000) == 0):
            PC = cPC + imm
            regs[rgid['$ra']] = cPC +4
    elif rt == 18:
        if(display):
            print("%s %s, %s" % ("bltzall", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        #executeDelaySlot()
        #x = makesigned32(regs[rs])
        if (crs&0x80000000):
            executeDelaySlot()
            PC = cPC + imm
            regs[rgid['$ra']] = cPC +4
        else:
            PC = cPC + 4
    elif rt == 19:
        if(display):
            print("%s %s, %s" % ("bgezall", rg[rs],hex(cPC+imm)), end='')
            print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
        #executeDelaySlot()
        #x = makesigned32(regs[rs])
        if ((crs&0x80000000) == 0):
            executeDelaySlot()
            PC = cPC + imm
            regs[rgid['$ra']] = cPC +4
        else:
            PC = cPC + 4

    else:
        print("Error! Don't understand type: 0x%x" % rt)

        
def op_i_beq(rs,rt,immin):
    global regs
    global rg
    global display
    global PC
    imm = makesigned16(immin)
    imm <<= 2
    cPC=PC
    crs=regs[rs]
    crt=regs[rt]
    if(display):
        print("%s %s, %s, %s" % ("beq", rg[rs],rg[rt],hex(cPC+imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
    executeDelaySlot()
    if crs == crt:
        PC = cPC + imm

def op_i_bne(rs,rt,immin):
    global regs
    global rg
    global display
    global PC
    imm = makesigned16(immin)
    imm <<= 2
    cPC=PC
    crs=regs[rs]
    crt=regs[rt]    
    if(display):
        print("%s %s, %s, %s" % ("bne", rg[rs],rg[rt],hex(cPC+imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
    executeDelaySlot()
    if crs != crt:
        PC = cPC + imm

def op_i_blez(rs,rt,immin):
    global regs
    global rg
    global display
    global PC
    imm = makesigned16(immin)
    imm <<= 2
    cPC=PC
    crs=regs[rs]
    if(display):
        print("%s %s, %s" % ("blez", rg[rs],hex(cPC+imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
    executeDelaySlot()
    if (makesigned32(crs) <=0  ):
        PC = cPC + imm


def op_i_addi(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s, %s, %s" % ("addi",rg[rt], rg[rs],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    x = regs[rs] + imm
    IntegerOverflow = 0
    if(x >= 0x100000000):
        IntegerOverflow = 1
    regs[rt] =  x & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))
        
def op_i_addiu(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s, %s, %s" % ("addiu",rg[rt], rg[rs],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    x = regs[rs] + imm
    IntegerOverflow = 0
    x &= 0xFFFFFFFF
    regs[rt] =  x
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_andi(rs,rt,imm):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("andi",rg[rt], rg[rs],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt] =  regs[rs] & imm
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_ori(rs,rt,imm):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %s" % ("ori",rg[rt], rg[rs],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt] =  regs[rs] | imm
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_slti(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s, %s, %s" % ("slti",rg[rt], rg[rs],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt] =  makesigned32(regs[rs]) < imm
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_sltiu(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s, %s, %s" % ("sltiu",rg[rt], rg[rs],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt] =  regs[rs] < imm
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_lui(rs,rt,imm):
    global regs
    global rg
    global display
    if imm < 0:
        imm = 0x10000 + imm
    if(display):
        print("%s %s,  %s" % ("lui",rg[rt],hex(imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt] =   (imm << 16) & 0xFFFF0000
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_lw(rs,rt,imm):
    global regs
    global rg
    global display
    x=makesigned16(imm)
    if(display):
        print("%s %s,  %s(%s)" % ("lw",rg[rt],hex(x),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt] = readMemory32(regs[rs]+x)
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))

def op_i_sw(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("sw",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    writeMemory32(regs[rs]+imm, regs[rt])
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_beql(rs,rt,immin):
    global regs
    global rg
    global display
    global PC
    imm = makesigned16(immin)
    imm <<= 2
    cPC= PC
    crs=regs[rs]
    crt=regs[rt]
    if(display):
        print("%s %s, %s, %s" % ("beq", rg[rs],rg[rt],hex(cPC+imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
    if (crs == crt):
        # Add branch delay slot support
        executeDelaySlot()
        PC = cPC + imm
    else:
        PC = cPC +4

def op_i_bnel(rs,rt,immin):
    global regs
    global rg
    global display
    global PC
    imm = makesigned16(immin)
    imm <<= 2
    cPC=PC
    crs=regs[rs]
    crt=regs[rt]    
    if(display):
        print("%s %s, %s, %s" % ("bnel", rg[rs],rg[rt],hex(cPC+imm)), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]))
    if (crs != crt):
        # Add branch delay slot support
        executeDelaySlot()
        PC = cPC + imm
    else:
        PC = cPC + 4

def op_i_sc(rs,rt,immin):
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("sc",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    if(LL):
        writeMemory32(regs[rs]+imm, regs[rt])
        regs[rt]=1
        LL=0
    else:
        regs[rt]=0
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_ll(rs,rt,immin):
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("ll",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rs], regs[rs], rg[rt], regs[rt]), end='')
    regs[rt]=readMemory32(regs[rs]+imm)
    LL=1
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))

def op_i_lb(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("lb",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    x=readMemory8(regs[rs]+imm)
    if(x&0x80):
        x = 0xFFFFFF00 | (x&0xFF)
    regs[rt]=x
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))

def op_i_lbu(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("lbu",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt]=readMemory8(regs[rs]+imm) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))

def op_i_lh(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("lh",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    x=readMemory16(regs[rs]+imm)
    if(x&0x8000):
        x = 0xFFFF0000 | (x&0xFFFF)
    regs[rt]=x  & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))

def op_i_lhu(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("lhu",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt]=readMemory16(regs[rs]+imm) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))


def op_i_lwl(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("lwl",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    addr = regs[rs]+imm
    shift = (addr & 3) * 8
    x = readMemory32(addr & 0xFFFFFFFC)
    regs[rt]= ((regs[rt] & (0x00FFFFFF >> shift)) | (x << (24-shift))) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_lwr(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("lwr",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    addr = regs[rs]+imm
    shift = (addr & 3) * 8
    x = readMemory32(addr & 0xFFFFFFFC)
    regval = regs[rt]
    regs[rt]= (( regval & (0xFFFFFF00 << (24 - shift)) ) | ( x	>> shift ))  & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_mfc0(rs,rt,immin):
    global regs
    global rg
    global display
    rd = immin>>11
    if(display):
        print("%s %s, %s" % ("mfc0",rg[rt],rg[rd]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt]=CP0[rd]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_mfc1(rs,rt,immin):
    global regs
    global rg
    global display
    rd = immin>>11
    if(display):
        print("%s %s, %s" % ("mfc1",rg[rt],rg[rd]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    regs[rt]=CP1[rd]
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_sb(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("sb",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    writeMemory8(regs[rs]+imm, (regs[rt]&0xFF))
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_sh(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("sh",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    writeMemory16(regs[rs]+imm, (regs[rt]&0xFFFF))
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_swl(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("swl",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    addr = regs[rs]+imm
    shift = (addr & 3) * 8
    x = readMemory32(addr & 0xFFFFFFFC)
        
    result = (( regs[rt] >>	(24 - shift) ) | (	x & (0xffffff00 << shift) )) & 0xFFFFFFFF
    writeMemory32((addr & 0xFFFFFFFC), result)
    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))

def op_i_swr(rs,rt,immin):
    global regs
    global rg
    global display
    imm = makesigned16(immin)
    if(display):
        print("%s %s,  %s(%s)" % ("swr",rg[rt],hex(imm),rg[rs]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    addr = regs[rs]+imm
    shift = (addr & 3) << 3
    x = readMemory32(addr & 0xFFFFFFFC)
    result = (( regs[rt] << shift)  | (	x & (0x00FFFFFF >> (24 - shift) ))) & 0xFFFFFFFF
    writeMemory32((addr & 0xFFFFFFFC), result)

    if(display):
        print("===> %s= 0x%08x, %s= 0x%08x" % (rg[rt], regs[rt], rg[rs], regs[rs]))



def op_i_cache(rs,rt,imm):
    if(display):
        print("%s %s,  %s(%s)" % ("cache",hex(rt),hex(imm),rg[rs]))

# MIPS I type function mapping
i_funcs = { 1:op_i_bltz,
            4:op_i_beq,
            5:op_i_bne,
            6:op_i_blez,
            8:op_i_addi,
            9: op_i_addiu,
            12:op_i_andi,
            13:op_i_ori,
            10:op_i_slti,
            11:op_i_sltiu,
            15:op_i_lui,
            35:op_i_lw,
            43:op_i_sw,
            20:op_i_beql,
            21:op_i_bnel,
            56:op_i_sc,
            48:op_i_ll,
            32:op_i_lb,
            36:op_i_lbu,
            33:op_i_lh,
            37:op_i_lhu,
            35:op_i_lw,
            34:op_i_lwl,
            38:op_i_lwr,
            16:op_i_mfc0,
            17:op_i_mfc1,
            40:op_i_sb,
            41:op_i_sh,
            42:op_i_swl,
            46:op_i_swr,
            47:op_i_cache
                 }

ibranch_ops = (1,20,21,4,5,6)

# MIPS I type instruction support
def process_i(op,rs,rt,imm):
    if op in i_funcs:
        op_fun = i_funcs[op]
        op_fun(rs,rt,imm)
    else:
        print("i_type %d is not supported yet\n" % op)


#--------------------------------------------------------------------------
# Allergrex custom type function supported
#
# Allegrex custom type function mapping

def op_a_wsbw(rs,rt,rd,funct2,funct1):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s" % ("wsbw",rg[rd],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rd], regs[rd], rg[rt], regs[rt]), end='')
    x = regs[rt]
    regs[rd] = ((x&0xFF)<<24) | (((x>>8)&0xFF)<<16) | (((x>>16)&0xFF)<<8) | ((x>>24)&0xFF)
    if(display):
        print("===> %s= 0x%08x" % (rg[rd], regs[rd]))

def op_a_wsbh(rs,rt,rd,funct2,funct1):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s" % ("wsbh",rg[rd],rg[rt]), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rd], regs[rd], rg[rt], regs[rt]), end='')
    x = regs[rt]
    regs[rd] = ((x&0xFF)<<8) | ((x>>8)&0xFF) | (((x>>16)&0xFF)<<24) | (((x>>24)&0xFF) << 16)
    if(display):
        print("===> %s= 0x%08x" % (rg[rd], regs[rd]))


def op_a_ins(rs,rt,msb,pos,funct1):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %d, %d" % ("ins", rg[rt], rg[rs],pos,msb+1-pos), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    sz = (msb + 1) - pos
    sourcemask = 0xFFFFFFFF >> (32 - sz)
    destmask = sourcemask << pos
    regs[rt] = ((regs[rt] & ~destmask) | ((regs[rs] & sourcemask) << pos)) & 0xFFFFFFFF
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))
        
def op_a_ext(rs,rt,msbd,pos,funct1):
    global regs
    global rg
    global display
    if(display):
        print("%s %s, %s, %d, %d" % ("ext", rg[rt], rg[rs],pos,msbd+1), end='')
        print("\t\t||\t%s= 0x%08x, %s= 0x%08x" % ( rg[rt], regs[rt], rg[rs], regs[rs]), end='')
    sz = msbd+1
    sourcemask = 0xFFFFFFFF >> (32-sz)
    regs[rt] = (regs[rs] >> pos) & sourcemask
    if(display):
        print("===> %s= 0x%08x" % (rg[rt], regs[rt]))
    
    
    
    
#-----------------------------------------------------------

a1_funcs = {  0:op_a_ext,
             4:op_a_ins,
               }

a2_funcs = {
             2:op_a_wsbh,
             3:op_a_wsbw
}


# Allegrex Custom Instructions
def process_a(rs,rt,rd,funct2,funct1):
    if(funct1 & 0x20):
        if funct2 in a2_funcs:
            op_fun = a2_funcs[funct2]
            op_fun(rs,rt,rd,funct2,funct1)
        else:
            print("allegrex function type 2- %d is not supported\n" % funct2)
    else:
        if funct1 in a1_funcs:
            op_fun = a1_funcs[funct1]
            op_fun(rs,rt,rd,funct2,funct1)
        else:
            print("allegrex function type 1- %d is not supported\n" % funct1)



def decodemips(instr):
    op=getop(instr)
    if op == 0:
        #Process R format
        rs=getrs(instr)
        rt=getrt(instr)
        rd=getrd(instr)
        shamt=getsh(instr)
        funct=getfun(instr)
        process_r(rs,rt,rd,shamt,funct)
    elif op in j_funcs:
        #Process J format
        addr=getaddr(instr)
        process_j(op,addr)
    elif op in i_funcs:
        #Process I format
        rs=getrs(instr)
        rt=getrt(instr)
        imm=getimm(instr)
        process_i(op,rs,rt,imm)
    elif op == 31:
        #custom allegrex instruction
        rs=getrs(instr)
        rt=getrt(instr)
        rd=getrd(instr)
        funct2=getsh(instr)
        funct1=getfun(instr)
        process_a(rs,rt,rd,funct2,funct1)
    else:
        print("\nInvalid opcode: %d\n0x%x" % (op, instr))


def decompress_kl4e(kl4e_data):
    global PC
    global display
    global regs
    global regid
    global rg

    magic = [0x4B, 0x4C, 0x34, 0x45 ]
    if(kl4e_data[0:4] != bytes(magic)):
        print("Error! Not a KL4E file")
        return None
    inc=0
    codestart = 0x25BC # original version
 
    for i in KL4E_Decompress:
        writeMemory32(codestart+inc, i)
        inc = inc + 4    

    #set initial stack pointer
    regs[rgid['$sp']] = 0xC00000    
    datain = 0x50000
    dataout = 0x300000
    datalen= len(kl4e_data)
    #copy input buffer into processor memory
    for i in range(0,datalen-4):
        writeMemory8(datain+i, kl4e_data[i+4])
    PC=codestart
    regs[rgid['$a0']] = dataout
    regs[rgid['$a1']] = 0x200000
    regs[rgid['$a2']] = datain
    regs[rgid['$a3']] = 0
    regs[rgid['$ra']] = 0xBABEF00D
    #execute the MIPS function
    while(PC != 0xBABEF00D):
        x=readMemory32(PC)
        if(display):
            print("0x%08x: " % PC, end='')
        PC = PC + 4
        decodemips(x)

    #Get the result
    result=regs[rgid['$v0']]
    if (result & 0x80000000):
        print("Error decompessing(0x%08x)",result)
        return None
    else:
        out=bytearray(result)
        for i in range (0,result):
            out[i] = readMemory8(dataout+i)
        return out


