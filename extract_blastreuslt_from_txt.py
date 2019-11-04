#!/usr/bin/env python
# File created on 2019/10/21

__author__ = "Wang,Yansu"
__license__ = "GPL"
__version__ = "1.0"

from optparse import OptionParser
import sys

def MakeOption():
    # make option
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=]  -a[--accession=]  -o[--output=]",
                          version="%prog 1.2")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="blast result with outfmt 6",
                      default=False)
    parser.add_option("-a", "--txt", action="store", dest="accession",
                      help="the accession_ID of fasta sequence",
                      default=False)
    parser.add_option("-o", "--output", action="store", dest="output",
                      help="blast result after pick out",
                      default=False)
    (options, args) = parser.parse_args()

    # extract option from command line
    input = options.input
    accession = options.accession
    output = options.output
    return (input, accession, output)

def main():
    input, accession, output = MakeOption()
    output = open(output, "w")
    for line in open(accession, "r"):
        line1 = line.strip()
        for eachline in open (input,"r"):
            eachline1 = eachline.split("\t")[0].strip()
            if line1 in eachline1:
                output.write(eachline)
    output.close()

if __name__ == "__main__":
    main()
