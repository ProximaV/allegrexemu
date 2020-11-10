import sys
import os
from decompress_kl4e import decompress_kl4e as decompress

def main(argc, argv):

    with open(sys.argv[1], 'rb') as f:
        data = f.read()
        

        decomp=decompress(data)
        if(decomp is not None):
            with open(sys.argv[1] + ".elf", 'wb') as o:
                o.write(decomp)            

 

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)