#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data cleaning
# values counts (Make)
# filter Origin - Asia or Europe
# removing records Weight > 4000
# applying function on column 'MPG' (increase on 3)

import pandas as pd


# In[2]:


cars = pd.read_csv((r"C:\Users\viver\OneDrive\RENDER.UA\12_Lambda\13_IT\UDEMY\Big Data Analysis With Pandas Data Frame\cars\Cars+Data.csv"))


# In[3]:


cars.head()


# In[4]:


# rows and columns
cars.shape


# In[5]:


#all Null values
cars.isnull()


# In[6]:


cars.isnull().sum()


# In[8]:


cars['Cylinders'].fillna(cars['Cylinders'].mean())


# In[9]:


# replace ('Cylinders'= 0)
cars['Cylinders'].fillna(cars['Cylinders'].mean(),inplace=True)


# In[10]:


cars.isnull().sum()


# In[11]:


cars


# In[12]:


# values counts (Make)

cars.head(3)


# In[13]:


cars['Make'].value_counts()


# In[14]:


# filter Origin - Asia or Europe


cars.head(4)


# In[15]:


cars[cars['Origin'].isin(['Asia', 'Europe'])]


# In[16]:


# removing records Weight > 4000


cars.head()


# In[17]:


cars['Weight'] > 4000


# In[19]:


#show W > 4000

cars[cars['Weight'] > 4000]


# In[20]:


# deleting (W > 4000)
cars[~(cars['Weight'] > 4000)]


# In[21]:


#applying function on column 'MPG' (increase on 3)


cars['MPG_city']=cars['MPG_City'].apply(lambda x:x+3)


# In[22]:


cars


# In[ ]:




