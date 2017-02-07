
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/007_rosalind_iprb.txt", 'r') as f:
    content = f.read()

organisms = content.split(' ')
k = int(organisms[0])
m = int(organisms[1])
n = int(organisms[2])
tot = k + m + n
kk = (k/tot)*((k-1)/(tot-1))
km = (k/tot)*(m/(tot-1))
kn = (k/tot)*(n/(tot-1))
mm = (m/tot)*((m-1)/(tot-1))*0.75
mn = (m/tot)*((n)/(tot-1))*0.5
mk = (m/tot)*(k/(tot-1))
nk = (n/tot)*(k/(tot-1))
nm = (n/tot)*(m/(tot-1))*0.5
totprop = kk + km + kn + mm + mn + mk + nk + nm
print(totprop)


# In[ ]:



