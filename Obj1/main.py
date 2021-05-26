#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# Objetivo: Distribuição etária da população para um determinado ano e distrito;

# In[38]:


population = pd.read_csv('population.csv')
population


# DataFrame Completo com todas as informações!! e "District_Code Corrigido

# In[39]:


population = population.rename(columns={'District.Name': 'District_Name', 'District.Code': 'District_Code'})
population


# Distrito: Ciutat Vella
# Ano: 2017

# In[40]:


population = population.query('Year=="2017" & District_Name=="Ciutat Vella"')
population.reset_index(inplace=True)
population


# In[41]:


population.Age[population.Age == '0-4'] = '00-4'
population.Age[population.Age == '5-9'] = '05-9'
population


# In[48]:


age_pop = population[['Age', 'Number']]
age = age_pop.groupby(by=['Age']).sum().index.tolist()
age_pop


# In[51]:


age_pop1 = age_pop.groupby(by=['Age']).sum().sort_values(by=['Age'],ascending=True)
age_pop1


# In[1]:


line,ax = plt.subplots(figsize=(12,6)) 
ax = sns.lineplot(data=age_pop1).set_title('Distribuição Etária em 2017 no distrito de Ciutat Vella')


# In[ ]:




