#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import math


# ## 1. Use matplotlib to plot the following equation:
# - y = x^2 − x + 2

# In[21]:


x = range(-100,100)
y = [(x**2 - x + 2) for x in x]
plt.plot(x,y)
plt.axhline(y=0)
plt.axvline(x=0)
plt.text(0,0,'the origin', color = 'k', fontsize = 14)
plt.show()


# ## 2. Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
# 
# - y=√x
# - y=x^3
# - y=2^x
# - y=1/(x+1)
# - You can use functions from the math module to help implement some of the equations above.

# In[54]:


x = range(0,100)
y = [(math.sqrt(x)) for x in x]
plt.plot(x,y)
plt.title('y=√x')
plt.show()


# In[53]:


x = range(0,100)
y = [((x**3)) for x in x]
plt.plot(x,y)
plt.title('y=x^3')
plt.show()


# In[51]:


x = range(0,100)
y = [((2**x)) for x in x]
plt.plot(x,y)
plt.title('y=2^x')
plt.show()


# In[50]:


x = range(0,100)
y = [(1/(x+1)) for x in x]
plt.plot(x,y)
plt.title('y=1/(x+1)')
plt.show()


# ## 3. Combine the figures you created in the last step into one large figure with 4 subplots.

# In[55]:


x = range(0,100)

y1 = [(math.sqrt(x)) for x in x]
y2 = [((x**3)) for x in x]
y3 = [((2**x)) for x in x]
y4 = [(1/(x+1)) for x in x]

plt.figure(figsize = (8,8))

plt.subplot(221)
plt.plot(x,y1)
plt.title('y=√x')

plt.subplot(222)
plt.plot(x,y2)
plt.title('y=x^3')

plt.subplot(223)
plt.plot(x,y3)
plt.title('y=2^x')


plt.subplot(224)
plt.plot(x,y4)
plt.title('y=1/(x+1)')


# ## 4. Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend and an appropriate title for the figure.

# In[91]:


x = range(0,100)

y1 = [(math.sqrt(x)) for x in x]
y2 = [((x**3)) for x in x]
y3 = [((2**x)) for x in x]
y4 = [(1/(x+1)) for x in x]

plt.figure(figsize = (8,8))

#plt.subplot(221)
plt.plot(x,y1,label = 'y=√x')
#plt.title('y=√x')

#plt.subplot(222)
plt.plot(x,y2,label = 'y=x^3')
#plt.title('y=x^3')

#plt.subplot(223)
plt.plot(x,y3, label = 'y=2^x')
#plt.title('y=2^x')


#plt.subplot(224)
plt.plot(x,y4,label = 'y=1/(x+1)')
#plt.title('y=1/(x+1)')

plt.xlim(0,50)
plt.ylim(0,10)
plt.title('numero cuatro')

plt.legend(loc = 'upper right')


# ## Make a new Jupyter notebook named big_o_notation.ipynb
# - Title your chart "Big O Notation"
# - Label your x axis "Elements"
# - Label your y axis "Operations"
# - Label your curves or make a legend for the curves
# - Use LaTex notation where possible
# - Curves to graph
# 
# - y = 0n+1
#  and label the curve "O(1)"
# - y = log(n)
#  and label the curve "O(log n)"
# - y = n
#  and label the curve "O(n)"
# - y = n∗log(n)
#  and label it "O(n log n)"
# - y = n^2
#  and label it "O(n^2)"
# - y = 2^n
#  and label it "O(2^n)"
# - y = n!
#  and label it "O(n!)"
# - y = n^n
#  and label it "O(n^n)"
# 

# In[ ]:




