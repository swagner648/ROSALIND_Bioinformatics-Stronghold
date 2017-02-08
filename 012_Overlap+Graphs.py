
# coding: utf-8

# In[26]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/012_rosalind_grph.txt", 'r') as f:
    content = f.read()
    
file3 = []
popls = []
seqls = [] # list of sequences with names eliminated
seqdict = {} # dictionary with keys of sequences and values of the names corresponding to it
corseqi1 = [] # list of sequence 1 of pair 
corseqi2 = [] # list of sequence 2 of pair
finalcorseqi1 = [] # list of sequence 1 of pair with repeats removed
finalcorseqi2 = [] # list of sequence 2  of pair with repeats removed
name1 = [] # name of final pair 1
name2 = [] # name of final pair 2
k = 3 # positive integer given
num = 1

file = list(content)
for i in range(0, len(file)):
    if file[i] == "\n":
        popls.append(i)

for i in list(reversed(popls)):
    file.pop(i)
file2 = ''.join(file)   
file2 = file2.split('>')
file2.pop(0)
for i in file2:
    file3.append(i[13:])
    
for i in file2:
    seqdict[i[13:]] = i[:13]

for i1 in file3:
    for i2 in file3:
        if i1[-k:] == i2[:k]: # selects the last k letters and first k letters
            corseqi1.append(i1)
            corseqi2.append(i2)
            
for i in range(0, len(corseqi1)):
    if corseqi1[i] != corseqi2[i]: # checks for repeats
        finalcorseqi1.append(corseqi1[i])
        finalcorseqi2.append(corseqi2[i])

for i in finalcorseqi1:
    name1.append(seqdict[i])
for i in finalcorseqi2:
    name2.append(seqdict[i])
            
for i in range(0, len(name1)):
    print(name1[i], name2[i])
    


# In[ ]:



