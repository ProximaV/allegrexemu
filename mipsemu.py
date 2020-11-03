import struct
from binascii import unhexlify as uhx
from binascii import hexlify as hx


import os
import sys
from mapping import *
            
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
    x=(instr) & 0xFFFF
    return x

def geta(instr):
    return instr&0x7FF
    
def getaddr(instr):
    return (instr) & 0x3FFFFFF


            
def process_r(rs,rt,rd,shamt,funct):
    if funct not in r_funcs:
        print("Can't decode %d func\n" % funct)
    if(shamt != 0):
        print("%s %s, %s, 0x%x" % (r_funcs[funct], rg[rd],rg[rt],shamt))
    else:
        print("%s %s, %s, %s" % (r_funcs[funct], rg[rd],rg[rs],rg[rt]))


    
def process_j(op,addr):
    print("%s 0x%x" % (j_funcs[op], addr<<2))


def process_i(op,rs,rt,imm):
    if op in branch_ops:
        if(imm > 0x8000):
            imm = -0x10000 + imm
            imm <<= 2 
            print("%s %s, %s, %s" % (i_funcs[op], rg[rs],rg[rt],hex(imm)))
        else:
            imm <<= 2 
            print("%s %s, %s, 0x%x" % (i_funcs[op], rg[rs],rg[rt],imm))
    elif op >= 32:
        print("%s %s, 0x%x(%s)" % (i_funcs[op], rg[rt],imm,rg[rs]))
    else:
        if(imm > 0x8000):
            imm = -0x10000 + imm 
            print("%s %s, %s, %s" % (i_funcs[op], rg[rt],rg[rs],hex(imm)))
        else:
            print("%s %s, %s, 0x%x" % (i_funcs[op], rg[rt],rg[rs],imm))

               
def process_a(rs,rt,rd,funct2,funct1):
    if(funct1 & 0x20):
        print("%s %s, %s" % (a2_funcs[funct2], rg[rd], rg[rt]))
    else:
        if funct1 == 4:
            print("%s %s, %s, %d, %d" % (a1_funcs[funct1], rg[rt], rg[rs],funct2,rd+1-funct2))
        else:
            print("%s %s, %s, %d, %d" % (a1_funcs[funct1], rg[rt], rg[rs],funct2,rd+1))
    
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


  
def main(argc, argv):
    mipscode = []

    with open(sys.argv[1], 'rb') as f:
        data = f.read()
        for i in range (0, len(data)>>2):
            #print(struct.unpack('<i',data[(i*4):(i*4)+4]))
            mipscode.append(int.from_bytes(data[(i*4):(i*4)+4], byteorder='little'))
        for i in mipscode:
            #print(hex(mipscode[i]))
            decodemips(i)
                    


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)