#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input())
x=[] #全部
b=[]
y=[] #3的倍數
z=[] #5的倍數
c=[] #3x5的倍數
b=[]
for j in range(a):
    i=j+1
    x.append(i)
    if(i%3==0):
        if(i%5!=0):
            y.append(i)
        else:
            c.append(i)
            b.append(i)
    elif(i%5==0):
        z.append(i)
    else:
        b.append(i)

print("所有的數字是："+str(x)+"\n其中"+str(y)+"被剔除;"+str(z)+"被剔除;但是"+str(c)+"被保留\n所以剩下來的數字是"+str(b)+",因此\n"
     +"Output:"+str(len(b)))


# In[ ]:




