
# coding: utf-8

# In[2]:

with open("/Users/simonwager/ROSALIND/001_rosalind_dna.txt", 'r') as f:
    content = f.read()
DNA = list(content)

A = 0
C = 0
G = 0
T = 0

for i in DNA:
    if i == "A":
        A = A+1
    elif i == "C":
        C = C+1
    elif i == "G":
        G = G+1
    elif i == "T":
        T = T+1
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)


# In[ ]:



