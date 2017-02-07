
# coding: utf-8

# In[1]:

with open("/Users/simonwager/ROSALIND/Bioinformatics_Stronghold/011_rosalind_fibd.txt", 'r') as f:
    content = f.read()

file = content.split(" ")
n = int(file[0]) # number of months
m = int(file[1]) # length of rabbit life (months)
mc = 1 # needs to start at 1 otherwise the youth of the month will be determined by already dead rabbits
mcc = 0
a = [0] # mature rabbits
b = [1] # premature rabbits
c = [0, 1] # total rabbits
died = 0
#print("A:", a[0], "B:", b[0], "C:", c[1])
#print("Died", died)
for i in range(1,n):
    if mc == m: # when the first rabbit dies this will replace the previous new mature rabbits and account for deaths
        died = b[mcc]
        a.append(b[i-1] + a[i-1] - (died))
        mcc = mcc + 1
    else:
        a.append(b[i-1] + a[i-1])
        mc = mc + 1
    b.append(a[i-1])
    c.append(a[i]+b[i])
    #print("A:", a[i], "B:", b[i], "C:", c[i+1])
    #print("Died", died)
print(c[i+1])


# In[ ]:



