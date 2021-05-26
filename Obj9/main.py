#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[38]:


imm_nat = pd.read_csv('immigrants_by_nationality.csv')
imm_nat = imm_nat.rename(columns={'District Name': 'District_Name', 'Neighborhood Name': 'Neighborhood_Name'})
imm_nat


# In[32]:


imm_age = pd.read_csv('immigrants_emigrants_by_age.csv')
imm_age = imm_age.rename(columns={'District Name': 'District_Name', 'Neighborhood Name': 'Neighborhood_Name'})
imm_age


# In[1]:


imm_sex = pd.read_csv('immigrants_emigrants_by_sex.csv')
imm_sex = imm_sex.rename(columns={'District Name': 'District_Name', 'Neighborhood Name': 'Neighborhood_Name'})
imm_sex


# In[96]:


imm_natCiu = imm_nat.query('Year == 2017 & District_Name == "Ciutat Vella"')
imm_natCiu


# In[45]:


imm_ageCiu = imm_age.query('Year == 2017 & District_Name == "Ciutat Vella"')
imm_ageCiu


# In[49]:


imm_sexCiu = imm_sex.query('Year == 2017 & District_Name == "Ciutat Vella"')
imm_sexCiu


# In[52]:


Nat = imm_natCiu[['Neighborhood_Name', 'Nationality', 'Number']]
Age = imm_ageCiu[['Neighborhood_Name', 'Age', 'Immigrants']]
Sex = imm_sexCiu[['Neighborhood_Name', 'Gender', 'Immigrants']]


# In[284]:


NatN = Nat.groupby(['Nationality','Neighborhood_Name']).sum().sort_values(by=['Number'], ascending=False)
NatN = NatN.loc[~(NatN==0).all(axis=1)]
NatN.head(70)


# In[252]:


NatE = NatN.head(70)
Nations = NatE.groupby(by=['Nationality']).sum().sort_values(by=['Nationality'], ascending=True).reset_index()
Nations


# In[249]:


sns.barplot(data=Nations, x='Nationality', y='Number')
plt.xticks(rotation=90)


# In[289]:


total = Nations['Number'].sum()
Nations['%'] = (Nations['Number']*100)/total
Nations['%'] = Nations['%'].round(2)
Nations.sort_values(by=['%'], ascending=False).head(9)


# In[285]:


Neigh = NatE.groupby(by=['Neighborhood_Name']).sum().sort_values(by=['Number'], ascending=True).reset_index()
Neigh


# In[198]:


sns.barplot(data=Neigh, x='Neighborhood_Name', y='Number')
plt.xticks(rotation=45)


# In[236]:


total = Neigh['Number'].sum()
Neigh['%'] = (Neigh['Number']*100)/total
Neigh['%'] = Neigh['%'].round(2)
Neigh


#  

# In[292]:


Age


# In[290]:


Ages = Age.groupby(['Age']).sum().reset_index()
Ages


# In[291]:


sns.barplot(data=Ages, x='Age', y='Immigrants')
plt.xticks(rotation=90)


# In[275]:


NeighS = Sex.groupby(['Neighborhood_Name','Gender']).sum().reset_index()
NeighS


# In[276]:


sns.catplot(data=NeighS, kind='bar', hue='Gender', x='Neighborhood_Name', y='Immigrants')
plt.xticks(rotation=90)

