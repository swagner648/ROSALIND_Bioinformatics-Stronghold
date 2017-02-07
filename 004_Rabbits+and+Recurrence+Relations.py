
# coding: utf-8

# In[85]:

with open("/Users/simonwager/ROSALIND/004_rosalind_fib.txt", 'r') as f:
    content = f.read()
file = content.split(" ")
list(file)
n = int(file[0])
k = int(file[1])
a = 0
b = 1
c = 0

fibolst = [1]
for i in range(0,(n-1)):
    a = 3 * a
    c = b + a
    fibolst.append(c)
    a = b
    b = c
print(fibolst)
print(c)


# In[ ]:



