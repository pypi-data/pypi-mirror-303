import os
import sys
from tlfs import TLF

def usage():
    print("""Usage:   
       tlfs structure_file.xlsx   
""")

def main():
    if len(sys.argv) != 2:
        usage()
    else:
        f = sys.argv[1]
        outdir = "."
        outfile = os.path.basename(os.path.splitext(f)[0] + "_TLF.docx")
        outpath = os.path.join(outdir, outfile)
        tlf = TLF()
        tlf.from_xlsx(f)
        tlf.to_docx(outpath, view = True)
        return(0)


def debug():
    ## same as main but with debug
    if len(sys.argv) != 2:
        usage()
    else:
        f = sys.argv[1]
        outdir = "."
        outfile = os.path.basename(os.path.splitext(f)[0] + "_TLF.docx")
        outpath = os.path.join(outdir, outfile)
        tlf = TLF(debug = True)
        tlf.from_xlsx(f)
        tlf.to_docx(outpath, view = True)
        return(0)
    
