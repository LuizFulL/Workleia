#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[87]:


population = pd.read_csv('population.csv')
population.rename(columns={'District.Name': 'District_Name', 'District.Code': 'District_Code'}, inplace = True)
population


# In[88]:


population = population.query('Year=="2017"')
population 


# In[92]:


population =  population[['District_Name', 'Gender', 'Number']]
population


# In[115]:


Gender_District =  population.pivot_table(values='Number', index='District_Name',
                    columns=['Gender'], aggfunc=np.sum)

Gender_District = Gender_District.reset_index()
Gender_District


# In[118]:


chart = sns.barplot(
        data=population, hue='Gender', x='District_Name', y='Number')
plt.xticks(rotation=90)

