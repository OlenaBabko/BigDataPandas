#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


covid_19 = pd.read_csv(r"C:\Users\viver\OneDrive\RENDER.UA\12_Lambda\13_IT\UDEMY\Big Data Analysis With Pandas Data Frame\covid_19_data.csv")


# In[3]:


covid_19


# In[4]:


covid_19.shape


# In[5]:


#not null values
covid_19.count()


# In[7]:


#boolean
covid_19.isnull()


# In[6]:


#not null in colomn
covid_19.isnull().sum()


# In[7]:


import seaborn as sns


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


sns.heatmap(covid_19.isnull())
plt.show()


# In[ ]:


# all number of confirmed, deaths and recovered cases in each region


# In[10]:


covid_19.head(3)


# In[13]:


covid_19.groupby('Region').sum()


# In[11]:


covid_19.groupby('Region').sum().head(25)


# In[12]:


covid_19.groupby('Region')['Confirmed'].sum()


# In[13]:


#ascending=False \\ ascending=True 
#max and min recorded?
#Pakistan?
covid_19.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)


# In[14]:


covid_19.groupby('Region')['Recovered'].sum()


# In[15]:


covid_19.groupby('Region').Deaths.sum().sort_values(ascending=True).head(50)


# In[16]:


covid_19[covid_19.Region == 'Pakistan']


# In[17]:


covid_19.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10)


# In[18]:


covid_19.groupby('Region')['Confirmed', 'Deaths'].sum()


# In[19]:


#Remove records with less than10 cases


# In[20]:


covid_19.Confirmed < 10


# In[21]:


covid_19[covid_19.Confirmed < 10]


# In[22]:


covid_19[~covid_19.Confirmed < 10]


# In[23]:


covid_19 = covid_19[~covid_19.Confirmed < 10]


# In[24]:


#check
covid_19


# In[ ]:




