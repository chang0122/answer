#!/usr/bin/env python
# coding: utf-8

# In[3]:


s="flipped class room is important"
y=s.split(" ")
x=" "
sum=0
for i in y:
    x+=i[::-1]
    sum+=1
    if sum!=len(y):
        x+=" "
print(x)


# In[ ]:




