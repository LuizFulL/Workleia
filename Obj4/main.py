#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[31]:


air_quality = pd.read_csv('air_quality_Nov2017.csv')
air_quality = air_quality.rename(columns={'Air Quality': 'Air_Quality'})


# In[39]:


air_quality = air_quality.query('Station=="Barcelona - Eixample"')
air_quality = air_quality[['Station','Air_Quality', 'Generated' ]]
air_quality = air_quality.iloc[0:167].reset_index().drop(['index'], axis='columns')
air_quality


# In[40]:


air_moderate = air_quality.query('Air_Quality == "Moderate"')
air_moderate


# In[37]:


Chart = sns.lineplot(data=air_quality, x='Generated', y='Air_Quality')

