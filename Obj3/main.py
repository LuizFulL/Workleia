#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


air_quality = pd.read_csv('air_quality_Nov2017.csv')
air_quality


# In[50]:


air_quality = air_quality.rename(columns={'Air Quality': 'Air_Quality'})
air_quality


# In[51]:


air_quality_bad = air_quality.query('Air_Quality == "Moderate"')
air_quality_bad


# In[52]:


air_quality = air_quality.query('Air_Quality == "Good" & Generated=="02/11/2018 21:00"')
air_quality

