#!/usr/bin/env python
# coding: utf-8

# In[2]:


# what courses udemy offers?
# max № of courses in categoties
# show all free
# all paid
# top selling
# least selling
# all from "graphic design" in price <100
# all related to Python
# published in 2017
# max № of subscribers for each level of courses


# In[3]:


import pandas as pd


# In[4]:


udemy_courses = pd.read_csv(r"C:\Users\viver\OneDrive\RENDER.UA\12_Lambda\13_IT\UDEMY\Big Data Analysis With Pandas Data Frame\courses\Udemy+Courses.csv")


# In[5]:


udemy_courses


# In[6]:


udemy_courses.shape


# In[7]:


# what courses udemy offers?
# (subject column and unique function)

udemy_courses.head(2)


# In[8]:


udemy_courses.subject.unique()


# In[9]:


# max № of courses in categoties
# (subject column and value_counts())

udemy_courses.head(2)


# In[10]:


udemy_courses.subject.value_counts()


# In[11]:


# show all free
#(is_paid column true = paid, false=free)

udemy_courses.is_paid == False


# In[12]:


# to see data frame:
udemy_courses[udemy_courses.is_paid == False]


# In[13]:


udemy_courses[udemy_courses.is_paid == False].shape


# In[14]:


# all paid
udemy_courses[udemy_courses.is_paid == True].shape


# In[15]:


udemy_courses[udemy_courses.is_paid == True]


# In[16]:


# top selling
# (column num_subscribers and sort_values function)
# default ascending=True so we need False

udemy_courses.sort_values('num_subscribers', ascending = False)


# In[17]:


# least selling

udemy_courses.sort_values('num_subscribers')


# In[18]:


# all from "graphic design" in price <100
# (column price and subject, filter & operator)

udemy_courses.subject=='Graphic Design'


# In[19]:


# data frame result
udemy_courses[udemy_courses.subject=='Graphic Design']


# In[20]:


udemy_courses[(udemy_courses.subject=='Graphic Design') & (udemy_courses.price < '100')]


# In[21]:


# =100
udemy_courses[(udemy_courses.subject=='Graphic Design') & (udemy_courses.price == '100')]


# In[22]:


# all related to Python
# (str contains function and  course_title column)

udemy_courses.head(2)


# In[23]:


udemy_courses[udemy_courses.course_title.str.contains('Python')]


# In[24]:


udemy_courses[udemy_courses.course_title.str.contains('Python')].shape


# In[25]:


# only column:
len(udemy_courses[udemy_courses.course_title.str.contains('Python')])


# In[26]:


# published in 2017
# data type of all columns

udemy_courses.dtypes


# In[27]:


#change (published_timestamp) type into datetime
udemy_courses['published_timestamp']=pd.to_datetime(udemy_courses.published_timestamp)


# In[28]:


udemy_courses.dtypes


# In[29]:


udemy_courses.head(2)


# In[30]:


# add new column with year only
udemy_courses['Year']=udemy_courses['published_timestamp'].dt.year


# In[31]:


udemy_courses.head(3)


# In[32]:


udemy_courses['Year']==2017


# In[34]:


udemy_courses[udemy_courses.Year==2017]


# In[35]:


len(udemy_courses[udemy_courses.Year==2017])


# In[36]:


# max № of subscribers for each level of courses
# (groupby function, columns level and num_subscribers)

udemy_courses.level.unique()


# In[37]:


udemy_courses.groupby('level')['num_subscribers'].max()


# In[38]:


udemy_courses.groupby('level')['num_subscribers'].min()


# In[39]:


udemy_courses.groupby('level').max()


# In[ ]:




