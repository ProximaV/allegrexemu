# Register printable name mapping
rg = { 0:"$zero",1:"$at", 2:"$v0", 3:"$v1",
    4:"$a0", 5:"$a1", 6:"$a2", 7:"$a3",
    8:"$a4",9:"$a5",10:"$a6",11:"$a7",12:"$t4",13:"$t5",14:"$t6",15:"$t7",
    16:"$s0",17:"$s1",18:"$s2",19:"$s3",20:"$s4",21:"$s5",22:"$s6",23:"$s7",24:"$t8",25:"$t9",
    26:"$k0",27:"$k1", 28:"$gp", 29:"$sp", 30:"$fp", 31:"$ra"     
            }
# MIPS R type function mapping
r_funcs = {
        32:"add",
        33:"addu",
        34:"sub",
        35:"subu",
        36:"and",
        37:"or",
        38:"xor",    
        39:"nor",
        42:"slt",
        43:"sltu",
        0:"sll",
        2:"srl",
        8:"jr",
        9:"jalr",
        3:"sra",
        4:"sllv",
        6:"srlv",
        7:"srav",
        10:"movz",
        11:"movn",
        12:"syscall",
        13:"break",
        15:"sync",
        16:"mfhi",
        17:"mthi",
        18:"mflo",
        19:"mtlo",
        24:"mult",
        25:"multu",
        26:"div",
        27:"divu",
        23:"clo",
        22:"clz",
        28:"madd",
        29:"maddu",
        46:"msub",
        47:"msubu",
        44:"max",
        45:"min"        
            }
            
i_funcs = { 1:"bltz",
            4:"beq",
            5:"bne",
            6:"blez",
            8:"addi",
            9: "addiu",
            12:"andi",
            13:"ori",
            10:"slti",
            11:"sltiu",
            15:"lui",
            35:"lw",
            43:"sw",
            20:"beql",
            21:"bnezl",
            56:"sc",
            48:"ll",
            32:"lb",
            36:"lbu",
            33:"lh",
            37:"lhu",
            35:"lw",
            49:"lwc1",
            34:"lwl",
            38:"lwr",
            16:"mfc0",
            17:"mfc1",
            40:"sb",
            41:"sh",
            42:"swl",
            46:"swr",
            47:"cache"
                 }

branch_ops = (1,20,21,4,5,6)

j_funcs = { 2:"j", 3:"jal" }
    
a1_funcs = {  0:"ext",
             4:"ins",
               }
               
a2_funcs = { 
             16:"seb",
             24:"seh",
             20:"bitrev",
             70:"rotrv",
             2:"wsbh",
             3:"wsbw"  
}    