
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/003_rosalind_revc.txt", 'r') as f:
    content = f.read()
DNA = list(content)[::-1]
comDNA = []

for i in DNA:
    if i == 'A':
        comDNA.append("T")
    if i == 'C':
        comDNA.append("G")
    if i == 'T':
        comDNA.append("A")
    if i == 'G':
        comDNA.append("C")
        
DNAn = ''.join(comDNA)    
print(DNAn)


# In[ ]:



