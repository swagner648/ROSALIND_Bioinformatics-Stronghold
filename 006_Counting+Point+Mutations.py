
# coding: utf-8

# In[26]:

with open("/Users/simonwager/ROSALIND/006_rosalind_hamm.txt", 'r') as f:
   content = f.read()

seqs = content.split('\n') # creates a list with two items: seq 1 and complimentary 2
seq1 = seqs[0] # splits two sequence into individual lists for each
seq2 = seqs[1]
pmc = 0 # sets point mutation count to 0
for i in range(0,len(seq1)):
    pair = str(seq1[i] + seq2[i])
    if pair != 'CC' and pair != 'GG' and pair != 'AA' and pair != 'TT': # if combination is abnormal increase pmc
        pmc = pmc + 1
print(pmc)


# In[ ]:



