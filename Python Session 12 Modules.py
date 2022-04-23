#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keyword


# In[2]:


print(keyword.kwlist)


# In[3]:


import sys


# In[4]:


sys.path


# In[5]:


import os


# In[6]:


#getcwd means get the current working directory
os.getcwd()


# In[7]:


#changing directory
#os.chdir(C:\\Users')
#os.getcwd()


# In[9]:


#Show the list of files and folders
os.listdir()


# In[10]:


import math


# In[11]:


math.pi


# In[12]:


math.sqrt(16)


# In[13]:


math.pow(2,3)


# Import with Renaming

# In[14]:


import math as m


# In[15]:


m.pi


# In[16]:


m.sqrt(16)


# Python from import statement

# In[18]:


from math import pi
pi


# In[20]:


math.__dict__.keys()


# In[21]:


m.sin (60)


# Get Date and Time

# In[22]:


import datetime 


# In[24]:


dt=datetime.datetime.now()


# In[25]:


dt


# Get Current Date

# In[26]:


dt1=datetime.date.today()
dt1


# In[32]:


import datetime
d=datetime.date(2022, 4, 23)
d


# In[43]:


td=datetime.date(2022, 4, 23)
td


# In[37]:


from datetime import time


# In[38]:


a=time()
print(a)

b=time(11,35,36)
print(b)


# # IO Operations

# In[50]:


savefile=open('D:\\Santhosh\\April18.txt','w')
savefile.write("This is thge first line")


# In[51]:


savefile.close()


# In[53]:


appendfile=open('D:\\Santhosh\\April18.txt','a')
appendfile.write('\n Lets add this in the next line')


# In[54]:


appendfile.close()


# # Pickle in Python: Object Serialization

# In[56]:


import pickle


# In[57]:


flower__Dict={1:'Rose', 2:'Lilly', 3:'Lotus'}


# In[59]:


filename='flower'
outfile=open(filename,'wb')


# In[60]:


outfile=open('flower.obj','wb')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




