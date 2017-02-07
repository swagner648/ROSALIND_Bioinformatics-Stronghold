
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/005_rosalind_gc.txt", 'r') as f:
   content = f.read()

best = 0
bestname = 'Title'

def cgperc(seq, title):
    ls = list(seq) # turns sequence into individual characters in a list
    a = 0
    global best # allows me to reference variables within the function
    global bestname
    for i in ls:
        if i == 'C':
            a = a + 1
        elif i == 'G':
            a = a + 1
    for i in ls: # can't be included in prior for loop because them the i removed will be skipped
        if i == '\n': # so that if a C or G were the first in a new line they wouldn't be counted
            ls.remove(i)
    fin = (a/len(ls))*100 # finds percentage of Cs and Gs
    if fin > best: # assigns the best value to the variable
        best = fin
        bestname = title

file = content.split('>') # creates a list seperated by title
for i in range(1,len(file)):
    name = file[i].split("\n", 1) # creates a list for eat title seperated by title and sequence
    seq = name[1] # sequence of genes
    title = name[0] # FASTA format title
    cgperc(seq, title) # runs each list of title and sequence through function
print(bestname,best)


# In[ ]:



