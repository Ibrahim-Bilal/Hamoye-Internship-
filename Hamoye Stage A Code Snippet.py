#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Question 11 

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Downloads\FoodData.csv', encoding='ISO-8859-1')
df.head()


# In[28]:


df.groupby('Item')['Y2014'].sum()


# In[29]:


df.groupby('Item')['Y2017'].sum()


# In[35]:


df_gptest = df[['Item','Y2014']]
df_gptest.groupby(['Item','Y2014'],as_index=False).mean()
df_gptest.loc[1060, ]


# In[41]:


#Question 12 
df["Y2015"].mean()


# In[40]:


df["Y2015"].std()


# In[50]:


#Question 13 
df.isnull().sum()


# In[51]:


df.isnull().sum()/60943


# In[52]:


Question 14
df[["Element Code", "Y2014", "Y2015","Y2016", "Y2017", "Y2018"]].corr()           


# In[102]:


#Question 15
df.groupby('Element')['Y2017'].sum()


# In[53]:


#Question 16
df.groupby('Element')['Y2014'].sum()


# In[74]:


df_group_one = df[['Element','Y2018']]
df_group_one = df_group_one.groupby(['Element'], as_index=False).sum()     
df_group_one.sort_values(by="Element", ascending=True)


# In[76]:


#Question 18
df_group_one = df[['Element','Y2018']]
df_group_one = df_group_one.groupby(['Element'], as_index=False).sum()     
df_group_one.sort_values(by="Element", ascending=True,)


# In[96]:


#Question 19
df_group_two = df[['Element','Y2018', 'Area']]
df_group_two = df_group_two.groupby(['Element','Area'],as_index=False).sum()
print(df_group_two[df_group_two['Element'].str.contains('Import Quantity')])


# In[92]:


#Question 20
len(pd.unique(df['Area']))


# In[ ]:




