
# coding: utf-8

# In[2]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/009_rosalind_subs.txt", 'r') as f:
    file = f.read()

split = file.split('\n')
string = split[0]
substring = split[1]

n = len(substring)
subls = [] # list of all possible combinations matching substring
samels = [] # list containing all times the substring is in the string, number is python placement (1st = 0)

for i in range(0, len(string)-(n-1)): # splits string into all possible combinations matching substring
    subls.append(string[i:i+n])
for i in range(0, len(subls)): # by number so i can be added to find placement of substring in string
    if subls[i] == substring: # looks for a substring possibiliy that matches the substring
        samels.append(str(i+1)) # must add one because number in python 0 is actually 1st number
fin = ' '.join(samels)
print(fin)


# In[ ]:



