
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/002_rosalind_rna.txt", 'r') as f:
    content = f.read()
DNA = list(content)
RNAls = []

for i in DNA:
    if i == 'T':
        RNAls.append("U")
    else:
        RNAls.append(i)
RNA = ''.join(RNAls)    
print(RNA)


# In[ ]:



