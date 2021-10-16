# SNP_Filtering

## Function to filter fastq reads to obtain reads with a unique motif.
Input: fastq file, motif sequence in string (e.g. "ATGCGGTGT"), presence/ absence, number of mismatches between motif and fastq read allowed
Output: fastq file with reads containing the motif sequence (if presence == True), otherwise reads without the motif if presence == False

## Quick start

Requirements: Python3, Biopython module, any python IDE (e.g. IDLE/ Spyder)

1. Create a folder with the following inside [1] SNP_filtering.py, [2] a new directory named "filtered_fastq" and [3] fastq files (.fastq format, not .gz)

3. Run function filter_SNP(file_name, marker_seq, presence, ID, allowed_mismatch)
    
    file_name | extracted fastq file name (for instance, S30_S30_L001_R1_001.fastq)
    
    marker_seq | signature sequence present in the desired amplicon in strings, not CAPS-sensitive (e.g. "attagg")
    
    presence | If the marker_seq is present in desired amplicon, then type True (no need for ""). If not present, type False (no need for ""). For the latter, the function will give you reads without the marker_seq.
    
    ID | ID to append to new fastq file name, in string  (e.g. "accession1_gene1")
    
    allowed_mismatch | Integer. Number of mismatches allowed between marker_seq and its alignment with the read. 
    
3. Check printed output to see if high percentage of reads are successfully filtered. If not, check if the marker_seq is correct or if presence is set to True or False. Another possibility is that your desired reads are rare in the fastq file.
