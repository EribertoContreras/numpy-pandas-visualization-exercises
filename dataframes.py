#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydataset import data
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# In[2]:


from pydataset import data


# In[3]:


# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable


# In[4]:


import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)


# In[5]:


df


# # #1
# Copy the code from the lesson to create a dataframe full of student grades.
# 
# - a.Create a column named passing_english that indicates whether each student has a passing grade in english.
# - b.Sort the english grades by the passing_english column. How are duplicates handled?
# - c.Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
# - d.Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
# - e.Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

# In[6]:


# a.Create a column named passing_english that indicates whether each student has a passing grade in english.
df["passing_english"] = df.english >70
df


# In[7]:


# b.Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by = 'passing_english', ascending = False)


# In[8]:


# c.Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by =["passing_english", "name"], ascending=True)


# In[9]:


# d.Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by = 'passing_english', ascending = False)


# In[10]:


# e.Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df["overall_grade"] = (df.math + df.english + df.reading) / 3
df


# # #2
# 
# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
# 
# - How many rows and columns are there?
# - What are the data types of each column?
# - Summarize the dataframe with .info and .describe
# - Rename the cty column to city.
# - Rename the hwy column to highway.
# - Do any cars have better city mileage than highway mileage?
# - Create a column named mileage_difference this column should contain the - difference between highway and city mileage for each car.
# - Which car (or cars) has the highest mileage difference?
# - Which compact class car has the lowest highway mileage? The best?
# - Create a column named average_mileage that is the mean of the city and - highway mileage.
# - Which dodge car has the best average mileage? The worst?
# 

# In[11]:


mpg


# #How many rows and columns are there? 
# 238 rows x 11 coumns

# In[12]:


#What are the data types of each column?
mpg.dtypes


# In[13]:


#Summarize the dataframe with .info and .describe
mpg.info()


# In[14]:


mpg.describe().round(2)


# In[15]:


#Rename the cty column to city.
mpg = mpg.rename(columns={"cty": "city"})
mpg


# In[16]:


#Rename the hwy column to highway.
mpg = mpg.rename(columns={"hwy": "highway"})
mpg


# In[17]:


# Do any cars have better city mileage than highway mileage? NO
mpg[mpg.city > mpg.highway]


# In[18]:


# Create a column named mileage_difference this column should contain the - difference between highway and city mileage for each car.
mpg["mileage_difference"] = mpg.highway - mpg.city
mpg


# In[19]:


#Which car (or cars) has the highest mileage difference? Honda Civic, VW new Beetle
mpg.sort_values(by =["mileage_difference"], ascending=False)


# In[ ]:





# In[20]:


# Which compact class car has the lowest highway mileage? The best?
#volkswagenjetta 2.8,1999,6 lowest.. highest volkswagen,jetta,1.9,1999
compact = mpg[mpg["class"].str.startswith("c")]
compact.sort_values(by='highway', ascending=True)


# In[21]:


#Create a column named average_mileage that is the mean of the city and - highway mileage.
mpg['average_mileage']=(mpg.city + mpg.highway)/2
mpg


# In[22]:


#Which dodge car has the best average mileage? The worst?
dodge = mpg[mpg["manufacturer"].str.startswith("dodge")]
dodge.sort_values(by='average_mileage', ascending=False).head(1)


# In[23]:


#The worst?
dodge = mpg[mpg["manufacturer"].str.startswith("dodge")]
dodge.sort_values(by='average_mileage', ascending=True).head(1)


# In[24]:


dodge = mpg[mpg["manufacturer"] == "dodge"].sort_values(by='average_mileage', ascending=True)
dodge


# In[27]:


Mammals = data('Mammals')


# In[29]:


Mammals


# #1 How many rows and columns are there?
# 107 x 4

# In[31]:


#2 What are the data types?
Mammals.dtypes


# In[32]:


#3 Summarize the dataframe with .info and .describe..
Mammals.info()


# In[33]:


Mammals.describe()


# In[37]:


#What is the the weight of the fastest animal?
Mammals[(Mammals.speed > 106)]


# In[96]:


#What is the overal percentage of specials?
#(Mammals.specials.count)
Specials_percent=(sum(Mammals.specials) / len(Mammals)) * 100
print("overall percentage of specials:%", Specials_percent)


# In[105]:


#How many animals are hoppers that are above the median speed? What percentage is this?
median_speed = Mammals.speed.median()


# In[108]:


median_speed


# In[182]:


Mammals[Mammals.hoppers & (Mammals.speed > median_speed)]


# In[181]:


HP=len(Mammals[Mammals.hoppers & (Mammals.speed > median_speed)])
print("Hoppers that are above median speed: ",HP)


# In[184]:


PHAS=len(Mammals[Mammals.hoppers & (Mammals.speed > median_speed)])/len(Mammals) * 100
print("Hopper percent above median speed: %", PHAS)


# In[ ]:




