#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


accidents = pd.read_csv('accidents_2017.csv')
accidents = accidents.rename(columns={'District Name': 'District_Name', 'Part of the day': 'Part_of_the_day'})
accidents


# In[6]:


month = accidents.groupby(by=['Month']).count().sort_values(by=['Id'],ascending=False)
month


# In[14]:


AccidentsNovember = accidents.query('Month == "November"')
AccidentsNovember = AccidentsNovember[['District_Name', 'Weekday','Part_of_the_day']]
AccidentsNovember


# In[22]:


AccidentsD = AccidentsNovember.groupby(by=['District_Name']).count().sort_values(by=['Weekday'], ascending=False)
AccidentsD


# In[13]:


sns.displot(AccidentsNovember,col='District_Name', x='Part_of_the_day',y='Weekday')

