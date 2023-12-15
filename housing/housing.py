#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# convert "Date" column to "date-time" format
# add column "Year"
# add "Month" column between "Date" and "Area"
# remove "Year" and "Month" columns
# show all records where "No of crimes" are zero and how much such records are there
# max and min "Average_price" per year in england
# max amd min no of crimes recorded area
# total count of records of each area, where average price is less than 100000


# In[47]:


import pandas as pd


# In[48]:


housing = pd.read_csv(r'C:\Users\viver\OneDrive\RENDER.UA\12_Lambda\13_IT\UDEMY\Big Data Analysis With Pandas Data Frame\housing\London+Housing+Data.csv')


# In[49]:


housing


# In[50]:


housing.shape


# In[51]:


# show not null values
housing.count()


# In[7]:


# show null (true = null)
housing.isnull()


# In[52]:


# total of null values
housing.isnull().sum()


# In[53]:


# convert "Date" column to "date-time" format
housing.dtypes


# In[54]:


# df.column name = pd.to_datetime(df.column name)
housing.date = pd.to_datetime(housing.date)


# In[55]:


#check
housing.dtypes


# In[56]:


# add column "Year"
housing.head(2)


# In[57]:


# by default new column appears in the end of df
# df["new column name"]= df.date.dt.year) syntax

housing["year"] = housing.date.dt.year


# In[58]:


housing.head(2)


# In[59]:


# add "Month" column between "Date" and "Area"
# insert func, start from 0 index

# df.insert(index, "new column name", df.date.dt.month)

housing.insert(1, "month", housing.date.dt.month)


# In[60]:


housing.head(2)


# In[61]:


# remove "Year" and "Month" columns
# df.drop(['year','month'], axis=1, inplace=True)
# axis=1 for columns, axis=0 for rows

housing.drop(["year","month"], axis=1, inplace=True)


# In[62]:


housing.head(2)


# In[63]:


# show all records where "No of crimes" are zero and how much such records are there

# df[df.column name == 0]
# len(df[df.column name == 0])

housing[housing.no_of_crimes == 0]


# In[64]:


len(housing[housing.no_of_crimes == 0])


# In[65]:


# max and min "Average_price" per year in england
# neeed Year column again
# housing["year"] = housing.date.dt.year
# df=df[df.column name == 'england']

housing.head(2)


# In[66]:


# neeed Year column again
housing['year']=housing.date.dt.year


# In[70]:


# apply filter
housing[housing.area == 'england']


# In[89]:


# new df
new_housing_l = housing[housing.area == 'england']


# In[90]:


new_housing_l


# In[93]:


# max and min "Average_price" per year in englandmax and min "Average_price" per year in england

# df1=groupby('column1 name').column2 name.max()/min()/mean()

new_housing_l.groupby('year').average_price.max()


# In[94]:


new_housing_l.groupby('year').average_price.min()


# In[95]:


# max amd min no of crimes recorded area
# df.groupby('column1 name').column2 name.min()
# df.groupby('column1 name').column2 name.min().sort_values(ascending =True)

housing.groupby('area').no_of_crimes.max()


# In[96]:


housing.groupby('area'). no_of_crimes.min()


# In[97]:


housing.groupby('area'). no_of_crimes.min().sort_values(ascending =True)


# In[ ]:


#  ??? why it shows england


# In[98]:


# total count of records of each area, where average price is less than 100000

#df[df.column1 name < 100000].colun2 name.value_counts()

housing[housing.average_price < 100000].area.value_counts()


# In[ ]:




