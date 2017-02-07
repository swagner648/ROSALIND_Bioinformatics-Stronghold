
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/008_rosalind_prot.txt", 'r') as f:
    file = f.read()

aminoacids = {
"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
"UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
"UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
"UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
"UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
"UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
"UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
"UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
"UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
"UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
"UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
"UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
"UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
"UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
"UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
"UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G",
}

n = 3
codons = []
aminos = []

name = file.split("\n")
content = ''.join(name)
for i in range(0, len(content), n): # range 0 to length of content by n characters
    codons.append(content[i:i+n])
for i in codons:
    amino = aminoacids[i]
    #amino = aminoacids[codons[i]] used to be but doesn't work because i is already the element not the placement
    aminos.append(amino)
for i in aminos:
    if i == 'Stop':
        aminos.remove(i)
finaminos = ''.join(aminos)
print(finaminos)


# In[ ]:



