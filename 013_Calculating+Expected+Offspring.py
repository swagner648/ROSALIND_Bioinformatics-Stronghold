
# coding: utf-8

# In[9]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/013_rosalind_iev.txt", 'r') as f:
    content = f.read()

num = content.split(' ') # creates a list with each element indexed by group number

P1 = float(num[0]) # estimated dominant in population of couple 1, 2, etc.
P2 = float(num[1])
P3 = float(num[2])
P4 = 0.75 * float(num[3])
P5 = 0.5 * float(num[4])
# couple group 6 has no dominant offspring

Pt = 2 * (P1 + P2 + P3 + P4 + P5) # sum all populations and multiply by 2 because each couple has 2 offspring

print(Pt)


# In[ ]:



