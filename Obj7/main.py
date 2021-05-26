#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[40]:


transports = pd.read_csv('transports.csv')
bus_stops = pd.read_csv('bus_stops.csv')
transports = transports.rename(columns={'District.Name': 'District_Name'})
bus_stops = bus_stops.rename(columns={'District.Name': 'District_Name'})


# In[41]:


transportsD = transports.groupby(by=['District_Name']).count().sort_values(by=['Code'],ascending=False)
transportsD


# In[42]:


bus_stopsD = bus_stops.groupby(by=['District_Name']).count().sort_values(by=['Code'],ascending=False)
bus_stopsD


# In[43]:


transportE = transports.query('District_Name == "Eixample"')
bus_stopsE = bus_stops.query('District_Name == "Eixample"')


# In[134]:


Code_bus = bus_stops[['Transport','Code']].groupby('Code')["Transport"].value_counts().to_frame()
Code_bus["Bus_Number"] = Code_bus["Transport"]
Code_bus = Code_bus.drop('Transport', axis='columns')
Code_bus


# In[156]:


Code_transport = transportE[['Transport','Code']].groupby('Code')['Transport'].value_counts().to_frame()
Code_transport["Transp_Number"] = Code_transport["Transport"] 
Code_transport = Code_transport.drop('Transport', axis='columns')
Code_transport


# In[158]:


Transport_Eixamples = pd.concat([Code_bus, Code_transport], axis=1)
Transport_Eixamples = Transport_Eixamples['Bus_Number'].fillna(Transport_Eixamples['Transp_Number']).to_frame()
Transport_Eixamples = Transport_Eixamples.rename(columns={'Bus_Number':'Number of stops'})
Transport_Eixamples


# In[159]:


bus_Stop = pd.concat([Transport_Eixamples.loc["K014"], Transport_Eixamples.loc["K015"]], axis=0)
bus_Stop

