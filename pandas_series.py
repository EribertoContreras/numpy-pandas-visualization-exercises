#!/usr/bin/env python
# coding: utf-8

# ## Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.
# 
# Use pandas to create a Series named fruits from the following list:
# 
#     ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# Use Series attributes and methods to explore your fruits Series.
# 
# - Determine the number of elements in fruits.
# 
# - Output only the index from fruits.
# 
# - Output only the values from fruits.
# 
# - Confirm the data type of the values in fruits.
# 
# - Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
# 
# - Run the .describe() on fruits to see what information it returns when called on a Series with string values.
# 
# - Run the code necessary to produce only the unique string values from fruits.
# 
# - Determine how many times each unique string value occurs in fruits.
# 
# - Determine the string value that occurs most frequently in fruits.
# 
# - Determine the string value that occurs least frequently in fruits.

# In[3]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# In[4]:


fruits= pd.Series (["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# In[5]:


#1 Determine the number of elements in fruits.
fruits.size


# In[6]:


#2 Output only the index from fruits.
fruits.sort_index()


# In[7]:


#3 Output only the values from fruits.
fruits.values


# In[8]:


#4 Confirm the data type of the values in fruits.
fruits.dtype


# In[9]:


#5 Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5)


# In[10]:


fruits.tail(3)


# In[12]:


fruits.sample(2)


# In[11]:


#6 Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()


# In[13]:


#7 Run the code necessary to produce only the unique string values from fruits.
fruits.unique()


# In[14]:


#8 Determine how many times each unique string value occurs in fruits.
fruits.value_counts()


# In[15]:


#9 Determine the string value that occurs most frequently in fruits.
fruits.value_counts().head()
#fruits.value_counts().idxmax()


# In[16]:


#10 Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(n=1, keep='all' )


# In[ ]: ......




