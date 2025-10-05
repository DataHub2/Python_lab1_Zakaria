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
        dic_seq[id] = ""
    else:
        dic_seq[id] += line

print(dic_seq)

#This code will be counting the letters
letter_count = {}

for seq_name, dna_string in dic_seq.items():
   count_dic = {"A": 0, "T": 0, "C": 0, "G": 0}
   for letter in dna_string:
      if letter in count_dic:
         count_dic[letter] += 1
         letter_count[seq_name] = count_dic

 



print("letter count")
print(letter_count) 
         
