import matplotlib.pyplot as plt 

# Lab-1 
# jag la in filen i variabel  
file_name = "dna_raw.txt"
dic_seq = {}
id = "" #Jag testa först med [] men det blev fel så jag la in tom citat tecken vilket funkade
# koden ska vara för att öppna filen  
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

# koden kommer räkna antal bostäver # fick lite vägledning från LLM då jag fastnade helt
letter_count = {}

for seq_name, dna_string in dic_seq.items():
   count_dic = {"A": 0, "T": 0, "C": 0, "G": 0}
   for letter in dna_string:
      if letter in count_dic:   
         count_dic[letter] += 1
         letter_count[seq_name] = count_dic


print("letter count")
print(letter_count) 


   

         
