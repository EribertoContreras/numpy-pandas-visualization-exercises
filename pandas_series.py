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

#Capitalize all the string values in fruits.

#Count the letter "a" in all the string values (use string vectorization).

#Output the number of vowels in each and every string value.

#Write the code to get the longest string value from fruits.

#Write the code to get the string values with 5 or more letters in the name.

#Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.

#Write the code to get only the string values containing the substring "berry".

#Write the code to get only the string values containing the substring "apple".

#
# Which string value contains the most vowels?
# In[ ]: ......

#1 Capitalize all the string values in fruits.
fruits.str.capitalize()

#2 Count the letter "a" in all the string values (use string vectorization).
fruits[fruits.str.count('[a]')]
#fruits.value_counts('a')

### 3 Output the number of vowels in each and every string value.
#[fruits.value_counts(vowels)]
fruits.str.count('[aeiou]')

#4 Write the code to get the longest string value from fruits
#max(fruits.values, key=len)
# or fruits[fruits.str.len()>= 15]
fruits[fruits.str.len().max() == fruits.str.len()]

#5 write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len()>= 5]
#(lambda n: 'even' if n % 2 == 0 else 'odd')

#6 Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
count_o = lambda x: x.count('o')>= 2
fruits[fruits.apply(count_o)]

#7 Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

#8 Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

#9 Which string value contains the most vowels?
fruits[max(fruits.str.lower().str.count(('[aeiou]')))]





#Use pandas to create a Series named letters from the following string. 
# The easiest way to make this string into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))


#1 Which letter occurs the most frequently in the letters Series?
letters.value_counts().nlargest(n=1, keep='all')


#2 Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1, keep='all')


#3 How many vowels are in the Series?
all_vowels = letters.str.lower().str.count(r'[aeiou]')
sum(all_vowels)


#4 How many consonants are in the Series?
sum(letters.str.lower().str.count(r'[a-z]') - all_vowels)


#5 Create a Series that has all of the same letters but uppercased.
letters_up = letters.str.capitalize()


#6 Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters.value_counts().nlargest(n=6, keep='first').plot.bar(rot=0)
plt.plot




n =  ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

n = pd.Series(n)
#7 What is the data type of the numbers Series?

n.dtype
#8 How many elements are in the number Series?
n.count()
#9 Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
nn = n.str.replace('$', '').str.replace(',', '').astype('float')
nn
#10 Run the code to discover the maximum value from the Series.
nn.nlargest(n=1)
#11 Run the code to discover the minimum value from the Series.
min(nn)
#12What is the range of the values in the Series?
nn_range = (min(nn)), max(nn)
nn_range
#13 Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
nn.value_counts(bins=4)
#14 Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
nn.plot.bar(rot=0)
plt.plot

scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#15 How many elements are in the exam_scores Series?
scores.size

#16 Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
scores.min(), scores.max(), scores.mean(), scores.median()

#17 Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

scores.plot()


#18 Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades.
#Add the necessary points to the highest grade to make it 100, 
#and add the same number of points to every other score in the Series as well.

curve = 100 - scores.max()
curved_grades = scores + curve
curved_grades

#19 Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. 
#For example, 86 should be a 'B' and 95 should be an 'A'.
#Save this as a Series named letter_grades.
bins = [0, 60, 70, 80, 90, 100]
labels = ['F','D','C','B','A']
pd.cut(curved_grades, bins = bins, labels = labels)

#20 Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
pd.cut(curved_grades, bins = bins, labels = labels).value_counts().plot.barh()