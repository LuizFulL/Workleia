#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[62]:


life = pd.read_csv('life_expectancy.csv')
population = pd.read_csv('population.csv')
population = population.rename(columns={'District.Name': 'District_Name', 'Neighborhood.Name': 'Neighborhood_Name'})
life


# In[63]:


life = life.sort_values(by=['2006-2010'], ascending=True)
life.head(60)


# In[64]:


life_s = pd.concat([life.loc[[130, 119]], life.loc[[91, 89]]])
life_s


# In[113]:


select = life.sort_values(by=['2006-2010'], ascending=True)
select = life.query('Neighborhood == "Baró de Viver" | Neighborhood == "Can Peguera" | Neighborhood == "les Corts" | Neighborhood == "Sants - Badal"')
select = select.sort_values(by=['Neighborhood'])
select = select[['Neighborhood', '2006-2010','Gender']]


# In[115]:


g = sns.catplot(
    data=select, kind="bar",
    x="Neighborhood", y="2006-2010", hue="Gender")

