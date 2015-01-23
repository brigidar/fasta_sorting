import argparse, os, sys
import pdb
from Bio import SeqIO


#argument to give to the script
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', help="contigs filtered by length fasta")
parser.add_argument('-i', '--input', help="unfilterd contigs fasta")
parser.add_argument('-c', '--cutoff', help="length cutoff")


args = parser.parse_args()
output_file = args.output
input_file = args.input
cutoff_num = args.cutoff

#open fasta file and select everything above cutoff:

seq_iterator = []
for record in SeqIO.parse(open(input_file, 'rU'), "fasta"):
    if len(record.seq) >= int(cutoff_num):
        seq_iterator.append(record)
# save in output
with open(output_file, 'w') as output_handle:
    SeqIO.write(seq_iterator, output_handle, "fasta")




