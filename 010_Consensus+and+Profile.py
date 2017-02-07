
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/010_rosalind_cons.txt", 'r') as f:
    file = f.read()

presplit = file.split(">") # splits into each subject
presplit.remove(presplit[0]) # removes the extra element caused by the split placement
split = []

for i in presplit: # required to remove '\n' from each new line
    name = i.split("\n")
    name.remove(name[0])
    content = ''.join(name)
    split.append(content)
   
A = [] # list for each nucleotide
C = []
G = []
T = []
m = 0

for i in range(0, len(split)):
    substring = split[i]
    nuc = list(substring)
    if m == 0: # can only run this one once to create the necessary elements in each nucleotide list
        for i in range(0, len(nuc)):
            Ac = 0
            Cc = 0
            Gc = 0
            Tc = 0
            if nuc[i] == "A":
                Ac = Ac + 1
            elif nuc[i] == "C":
                Cc = Cc + 1
            elif nuc[i] == "G":
                Gc = Gc + 1
            elif nuc[i] == "T":
                Tc = Tc + 1
            A.append(Ac)
            C.append(Cc)
            G.append(Gc)
            T.append(Tc)
        m = 1
    else:
        for i in range(0, len(nuc)):
            Ac = 0
            Cc = 0
            Gc = 0
            Tc = 0
            if nuc[i] == "A":
                Ac = Ac + 1
            elif nuc[i] == "C":
                Cc = Cc + 1
            elif nuc[i] == "G":
                Gc = Gc + 1
            elif nuc[i] == "T":
                Tc = Tc + 1
            A[i] = A[i] + Ac
            C[i] = C[i] + Cc
            G[i] = G[i] + Gc
            T[i] = T[i] + Tc
finseqls = []
for i in range(0, len(A)):
    letter = (max(A[i], C[i], G[i], T[i]))
    if A[i] == letter:
        finseqls.append("A")
    elif C[i] == letter:
        finseqls.append("C")
    elif G[i] == letter:
        finseqls.append("G")
    elif T[i] == letter:
        finseqls.append("T")
    
for i in range(0, len(A)):
    A[i] = str(A[i]) # if it isn't a string it can't be joined
    C[i] = str(C[i])
    G[i] = str(G[i])
    T[i] = str(T[i])
    finseqls[i] = str(finseqls[i])
Afin = " ".join(A)
Cfin = " ".join(C)
Gfin = " ".join(G)
Tfin = " ".join(T)
finseq = "".join(finseqls)
print(finseq)


# In[ ]:




# In[ ]:



