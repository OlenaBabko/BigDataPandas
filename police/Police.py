#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# remove colomn with missing values
# speeding - men or women stopped more?
# gender affects who gets searched?
# mean of stop_duration
# violation age distribution


# In[1]:


import pandas as pd


# In[2]:


police_data = pd.read_csv(r"C:\Users\viver\OneDrive\RENDER.UA\12_Lambda\13_IT\UDEMY\Big Data Analysis With Pandas Data Frame\police\Police+Data.csv")


# In[3]:


police_data


# In[4]:


# number of rowss and colomns
police_data.shape


# In[5]:


# remove colomn with missing values
police_data.isnull()


# In[6]:


# check the missing value colomn
police_data.isnull().sum()


# In[7]:


# try delete this colomn and move others
police_data.drop('country_name', axis=1)


# In[8]:


# check - and see its not gone
police_data


# In[11]:


# now really delete
police_data.drop('country_name', axis=1, inplace=True)


# In[12]:


police_data


# In[ ]:


# speeding - men or women stopped more?
# filtering and value counts


# In[13]:


police_data.head()


# In[14]:


police_data[police_data.violation == 'Speeding']


# In[15]:


#value counts
police_data[police_data.violation == 'Speeding'].driver_gender.value_counts()


# In[16]:


# gender affects who gets searched?
# groupby: make a group of unique values in colomn
# driver_gender and Search_conducted


# In[17]:


police_data.groupby('driver_gender').search_conducted.sum()


# In[18]:


# verification
police_data.search_conducted.value_counts()


# In[ ]:


# mean of stop_duration
# mapping data type casting


# In[20]:


police_data.stop_duration.value_counts()


# In[26]:


police_data['stop_duration']=police_data['stop_duration'].map({'0-15 Min' : 7.5, '16-30 Min' : 23, '30+ Min' : 45})


# In[27]:


police_data
# why it doesnt work ???


# In[28]:


police_data['stop_duration'].mean()


# In[ ]:


# violation age distribution
# groupby and describe = Statistics function


# In[29]:


police_data.groupby('violation').driver_age.describe()


# In[ ]:




