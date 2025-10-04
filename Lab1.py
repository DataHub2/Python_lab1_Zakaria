import matplotlib 

# Lab-1 
# I have named the file, and then assigend (dna_raw.txt) as the value. 
file_name = "dna_raw.txt"
dic_seq = {}
id = ""
# This code will open the file that i will be working with (dna_raw.txt) 
#W3schools hjälpte mig gå genom detta! Sedan fick jag lite vägledning från Anton 
with open(file_name) as f:
 for line in f:
    line = line.strip().upper()
    if line.startswith(">"):
        id = line[1:]
        dic_seq[id] = []
    else:
        dic_seq[id].append(line)

print(dic_seq)

#Cleaning data, im only looking for the letters (A, T, C, G)
clean_seq = {}
only_letters = {"A", "T", "C", "G"}

for id, seq_lines in dic_seq.items():
   dna_strang = seq_lines[0]


