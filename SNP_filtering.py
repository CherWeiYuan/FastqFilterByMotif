## Quick start

# Requirements: Biopython module

# 1. Create a folder named filtered_fastq in folder with extracted fastq files
# 2. Run function filter_SNP(file_name, marker_seq, ID)
# 3. Check printed output to see if high percentage of reads are successfully filtered

########################################## Source code ##########################################
from Bio import SeqIO
from Bio.Seq import Seq
from regex import findall

def rc(seq):
    return str(Seq(seq).reverse_complement())
    
def filter_SNP(file_name,  # fastq file name in string
               marker_seq, # SNP sequence in string
               presence,   # True if marker_seq is in desired sequences; False if marker_seq is NOT in desired sequences
               ID,         # ID to append to new fastq file name, in string               
               allowed_mismatch): # Number of mismatch between marker_seq and fastq seq is allowed where fastq seq is still considered marker-positive read
               
    count = 0
    total_count = 0
    lst = []
    output_name = "./filtered_fastq/" + ID + "_" + file_name
    
    x = SeqIO.parse(file_name, "fastq")
    
    for record in x:
        total_count += 1
        if presence == True:
            if len(findall("(" + marker_seq.upper() + "){e<=" + str(allowed_mismatch) + "}", str(record.seq.upper()))) > 0:
                count += 1
                lst += [record]       
        elif presence == False:
            if len(findall("(" + marker_seq.upper() + "){e<=" + str(allowed_mismatch) + "}", str(record.seq.upper()))) == 0:
                    count += 1
                    lst += [record]               

    print(f"Proportion of total reads remaining is {count}/{total_count}")
    SeqIO.write(lst, output_name, "fastq")
    print(f"{count} reads are extracted to folder {output_name}")
