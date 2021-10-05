# SNP_Filtering

## Function to filter fastq reads to obtain reads with a signature sequence

### Quick start

Requirements: Python3 and Biopython module

1. Create a folder named filtered_fastq in folder with extracted fastq files
2. Run function filter_SNP(file_name, marker_seq, presence, ID, allowed_mismatch)
    file_name | extracted fastq file name (for instance, S30_S30_L001_R1_001.fastq)
    marker_seq | signature sequence present in the desired amplicon in strings, not CAPS-sensitive (e.g. "attagg")
    presence | If the marker_seq is present in desired amplicon, then type True. If not present, type False. For the latter, the function will give you reads without the marker_seq.
    ID | ID to append to new fastq file name, in string  (e.g. "File1")
    allowed_mismatch | Number of mismatches allowed between marker_seq and its alignment with the read. Integer.
4. Check printed output to see if high percentage of reads are successfully filtered. If not, check if the marker_seq is correct or if presence is set to True or False.
