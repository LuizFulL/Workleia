#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium import plugins


# # CONTROLAR A QUALIDADE DO AR

# In[2]:


Air_quality = pd.read_csv('air_quality_Nov2017.csv')
Air_quality = Air_quality.rename(columns={'Air Quality': 'Air_Quality'})
Air_quality


# In[3]:


Air_Moderate = Air_quality.query('Air_Quality == "Moderate"')
Air_Moderate = Air_Moderate[['Station', 'Air_Quality', 'Longitude', 'Latitude', 'Generated']]
Air_Moderate.groupby(['Station']).count()


# In[4]:


Air_Moderate.groupby(['Generated']).count()
hour = Air_Moderate['Generated'].str.split(' ')
hours = []
days = []
for i in hour:
    days.append(i[0])
    hours.append(i[1])    
Air_Moderate['Generated'] = days
Air_Moderate['Hour'] = hours


# In[5]:


Air_Moderate.groupby(['Hour']).count().sort_values(['Station'], ascending=False)


# Conclusão, conseguimos filtrar os bairros com mais ocorrência de air equal moderate, e seus respectivos horários.

# _________________________________________________________________________________________________
# 

#  

# # REORGANIZAR AS PARADAS DE AUTOCARRO

# In[6]:


bus_stops = pd.read_csv('bus_stops.csv')
bus_stops = bus_stops.rename(columns={'District.Name': 'District_Name'})
bus_stops


# In[7]:


bus_stopsD = bus_stops.groupby(by=['District_Name']).count().sort_values(by=['Code'],ascending=False)
bus_stopsD


# In[8]:


Code_bus = bus_stops[['Transport','Code']].groupby('Code')["Transport"].value_counts().to_frame()
Code_bus["Bus_Number"] = Code_bus["Transport"]
Code_bus = Code_bus.drop('Transport', axis='columns')
Code_bus.loc[['K014','K015']]


# In[9]:


bus_stopsDN = bus_stops.query('Code == "K014" | Code == "K015"')
stops = bus_stopsDN.groupby(['District_Name', 'Transport']).count().sort_values(by=['District_Name'],ascending=False)
stops = stops.reset_index()
stops = stops.rename(columns={'Code' : 'N°_Stop', 'Transport': 'P_Stop'})
stops = stops[['District_Name','P_Stop', 'N°_Stop']]
stops


# In[10]:


fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=stops, x='District_Name', y='N°_Stop', hue='P_Stop',ax=ax).set_title('Bus Stop')
x = plt.xticks(rotation=90)


# In[11]:


day_stop = stops.query('P_Stop == "Day bus stop"')
day_stop = day_stop[['District_Name','N°_Stop']]
night_stop = stops.query('P_Stop == "Night bus stop"')
night_stop = night_stop[['District_Name', 'N°_Stop']]


Stops = stops.groupby(['District_Name']).count().reset_index().sort_values(['District_Name'], ascending=False)
Stops = Stops[['District_Name', 'P_Stop']]
Stops = Stops.merge(day_stop, how ='inner', on ='District_Name')
Stops = Stops.rename(columns={'N°_Stop': 'N°_DayStop'}).drop('P_Stop', axis='columns')
Stops = Stops.merge(night_stop, how = 'inner', on = 'District_Name')
Stops = Stops.rename(columns={'N°_Stop': 'N°_NightStop'})
Stops


# In[12]:


Stops.sort_values(['N°_DayStop'])


# In[13]:


Stops.sort_values(['N°_NightStop'])


# In[14]:


fig, ax =plt.subplots(1,2,figsize=(15,7))
g = sns.barplot(data=Stops, x='District_Name', y='N°_DayStop', color="salmon", ax=ax[0]).set_title('Bus_Stop on Day')
g1 = sns.barplot(data=Stops, x='District_Name', y='N°_NightStop', palette="Blues_d", ax=ax[1]).set_title('Bus_Stop on Night')
x = plt.xticks(rotation=90)
y = plt.sca(ax[0])
z = plt.xticks(rotation=90)


# Concluimos quais distritos tem mais e menos paradas durante o dia e durante a noite

#  

# _______________________________________________________

#  
#  

# # MELHORAR A RELAÇÃO COM OS HABITANTES

# In[15]:


population = pd.read_csv('population.csv')
population = population.rename(columns={'District.Name': 'District_Name', 'Neighborhood.Name':'Neighborhood_Name'})
population = population.query('Year=="2017" & District_Name == "Eixample"')
pop_Ciut = population.groupby(['Neighborhood_Name'])['Number'].sum().to_frame().reset_index()
pop_Ciut


# In[16]:


gender_Ciut = population[['Neighborhood_Name', 'Gender', 'Number']]
male_Ciut = gender_Ciut.query('Gender=="Male"').groupby(['Neighborhood_Name']).sum().reset_index()
female_Ciut = gender_Ciut.query('Gender=="Female"').groupby(['Neighborhood_Name']).sum().reset_index()

gender_Ciut = gender_Ciut.groupby(['Neighborhood_Name']).sum().reset_index()
gender_Ciut = gender_Ciut.rename(columns={'Number': 'Total'})

male_Ciut = male_Ciut.rename(columns={'Number': 'Male'})
female_Ciut = female_Ciut.rename(columns={'Number': 'Female'})

gender_Ciut = gender_Ciut.merge(male_Ciut, how='inner', on='Neighborhood_Name')
gender_Ciut = gender_Ciut.merge(female_Ciut, how='inner', on='Neighborhood_Name')
gender_Ciut


# In[17]:


immigrants = pd.read_csv('immigrants_by_nationality.csv')
immigrants = immigrants.rename(columns={'District Name': 'District_Name', 'Neighborhood Name':'Neighborhood_Name'})
immigrants = immigrants.query('Year=="2017" & District_Name == "Eixample"')
immi_Ciut = immigrants.groupby(['Neighborhood_Name'])['Number'].sum().to_frame().reset_index()
immi_Ciut


# In[18]:


imm_sex = pd.read_csv('immigrants_emigrants_by_sex.csv')
imm_sex = imm_sex.rename(columns={'District Name': 'District_Name', 'Neighborhood Name':'Neighborhood_Name'})
imm_sex = imm_sex.query('Year=="2017" & District_Name == "Eixample"')
imm_sex = imm_sex[['Neighborhood_Name', 'Gender', 'Immigrants']]


# In[19]:


imm_male = imm_sex.query('Gender=="Male"').groupby(['Neighborhood_Name']).sum().reset_index()
imm_female = imm_sex.query('Gender=="Female"').groupby(['Neighborhood_Name']).sum().reset_index()

immi_Ciut = immi_Ciut.rename(columns={'Number': 'Total'})

imm_male = imm_male.rename(columns={'Immigrants': 'Male'})
imm_female = imm_female.rename(columns={'Immigrants': 'Female'})

genderimmi_Ciut = immi_Ciut.merge(imm_male, how='inner', on='Neighborhood_Name')
genderimmi_Ciut = genderimmi_Ciut.merge(imm_female, how='inner', on='Neighborhood_Name')
genderimmi_Ciut = genderimmi_Ciut.rename(columns={'Total': 'Total_Immigrants', 'Male': 'Male_Immi', 'Female': 'Female_immi'})
genderimmi_Ciut


# In[20]:


poptotal_Ciu = gender_Ciut.merge(genderimmi_Ciut, how='inner', on='Neighborhood_Name')
poptotal_Ciu


# In[21]:


total = poptotal_Ciu['Total'].sum()
totals = poptotal_Ciu[['Neighborhood_Name', 'Total']]
totals['% pop_Eix'] = (poptotal_Ciu['Total']*100)/total
totals['% pop_Eix'] = totals['% pop_Eix'].round(1)

totals['% neigh_imm'] = (poptotal_Ciu['Total_Immigrants']*100)/poptotal_Ciu['Total']
totals['% neigh_imm'] = totals['% neigh_imm'].round(1)
totals


#  

# _____________________________________________________________________

#  

# # PREVENIR ACIDENTES

# In[35]:


accidents = pd.read_csv('accidents_2017.csv')
accidents


# In[41]:


coordenadas = []
for lat, lng in zip(accidents.Latitude.values[:10339], accidents.Longitude.values[:10339]):
    coordenadas.append([lat, lng])


# In[63]:


mapa = folium.Map(width=1000,height=1000)
mapa.add_child(plugins.HeatMap(coordenadas, radius=5, blur=3.5))
mapa


# In[ ]:




