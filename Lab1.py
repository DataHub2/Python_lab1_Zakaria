import matplotlib 

# Lab-1 
# I have named the file, and then assigend (dna_raw.txt) as the value. 
file_name = "dna_raw.txt"
dic_seq = {}
key = []
# This code will open the file that i will be working with (dna_raw.txt)
with open(file_name) as f:
 for line in f:
    line = line.strip()
    if line.startswith(">"):
        key = line[1:]
        dic_seq[key] = []
    else:
        dic_seq[key].append(line)


        
print(dic_seq)