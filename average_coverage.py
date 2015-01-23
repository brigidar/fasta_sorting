import argparse, os, sys
import pdb
import glob
from Bio import SeqIO


#argument to give to the script
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', help="contigs filtered by length fasta")
parser.add_argument('-d', '--directory', help="unfilterd contigs fasta")



args = parser.parse_args()
output_file = args.output
directory = args.directory

# retrieves a list of files with _500.fasta
def retrieve(directory):
    files = []
    files = glob.glob("%s/*_500.fasta" % directory)
    return files
#-------------------------------------------

# function that makes the average
def coverage(seq_iterator):
    sum = 0.0
    for item in seq_iterator:
        temp = float(item.split('_')[5])
        sum += temp
    return (sum / float(len(seq_iterator)))

#--------------------------------------------------

#open fasta file and calculate average coverage:
def fasta_input(input_file):
    seq_iterator=[]
    for record in SeqIO.parse(open(input_file, 'rU'), "fasta"):
            seq_iterator.append(record.id)
    mode = 'w'
# check if file already exists:
    if os.path.isfile(output_file):
        mode = 'a'

# save in output
    with open(output_file, mode) as output_handle:
        output_handle.write(str(input_file ) + ' '+ str(coverage(seq_iterator)) + "\n")

#----------------------------------------------------

# main execution loop to go through all the fasta files
files = retrieve(directory)
for f in files:
    fasta_input(f)







