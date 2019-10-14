#!/usr/bin/env python
# File created on 2019/10/14

__author__ = "Wang,Yansu"
__license__ = "GPL"
__version__ = "1.0"

from optparse import OptionParser

def MakeOption():
    # make option
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=] -o[--output=]", version="%prog 1.0")
    parser.add_option("-i", "--input_outfmt6", action="store", dest="input_outfmt6",
                      help="The input txt file is the blast result with outfmt 6",
                      default=False)
    parser.add_option("-o", "--output_txt", action="store", dest="output_txt",
                      help="The output txt file contain the first blast result",
                      default=False)
    (options, args) = parser.parse_args()
    input_txt = options.input_outfmt6
    output_txt = options.output_txt
    return (input_txt, output_txt)

def pick_blast_result(input_txt,output_txt):
    dict = {}
    output = open(output_txt,"w")
    for eachline in open (input_txt,"r"):
        line1 = eachline.split("\t")[0].strip()
        line2 = eachline.split("\t")[1].strip()
        if not dict.get(line1):
           dict[line1]= line2
        else:
           continue
    for key,value in dict.items():
        output.write("%s\t%s\n" % (key, value))
    output.close()

def main():
    input_txt, output_txt = MakeOption()
    pick_blast_result(input_txt, output_txt)
if __name__ == '__main__':
    main()
