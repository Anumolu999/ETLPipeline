#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np
#from scipy.stats import norm
#from sklearn.preprocessing import StandardScaler
#from scipy import stats
#import warnings
#warnings.filterwarnings('ignore')
#%matplotlib inline


# In[8]:


data = pd.read_csv("house_data.csv")


# In[9]:


data


# In[11]:


df_train = pd.read_csv('house_data.csv')


# In[12]:


df_train


# In[13]:


df_train.shape


# In[14]:


df_train.dtypes


# In[18]:


#descriptive statistics summary
df_train['price'].describe()


# In[21]:


#missing data
total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)


# In[22]:


sum(df_train.isnull().sum())


# In[28]:


plt.figure(figsize=(8, 6))


# In[46]:


#scatter plot grlivarea/saleprice
var = 'sqft_living'
data = pd.concat([df_train['price'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='price', ylim=(0,5000000));


# In[ ]:




