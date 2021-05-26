#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


accidents = pd.read_csv('accidents_2017.csv')
accidents


# Renomear District Name -> District_Name & Part of the day -> Part_of_the_day

# In[5]:


accidents = accidents.rename(columns={'District Name': 'District_Name', 'Part of the day': 'Part_of_the_day'})
accidents


# Descobrir qual mês tem mais acidentes, agrupando dados por mês, depois contanto e colocando em ordem decrescente

# In[7]:


month = accidents.groupby(by=['Month']).count().sort_values(by=['Id'],ascending=False)
month


# Descobrimos que novembro é o mês com mais acidentes, com isso filtramos o banco de dados, somente as linhas que apresentam "November" na coluna "Month", resetamos o index, para a contagem certa e excluimos a coluna gerada "index".

# In[8]:


accidentsNovember = accidents.query('Month=="November"').reset_index(inplace=False).drop(columns=['index'])
accidentsNovember


# Vamos agora descobrir, qual o periodo do dia em novembro que ocorreu mais acidentes

# In[9]:


accidentsNovemberP = accidentsNovember.groupby(by=['Part_of_the_day']).count()
accidentsNovemberP


# Agora o dia da semana que mais ocorreu mais acidentes

# In[10]:


accidentsNovemberD = accidentsNovember.groupby(by=['Weekday']).count().sort_values(by=['Id'],ascending=False)
accidentsNovemberD


# Agora vamos visualizar o distrito que em Novembro, que sofreu mais acidentes

# In[11]:


accidentsNovemberDis = accidentsNovember.groupby(by=['District_Name']).count().sort_values(by=['Id'],ascending=False)
accidentsNovemberDis


# Por últimos, vamos filtrar mais nossa tabela de novembro para as colunas -> distritos, dia e periodo

# In[33]:


accidentsNovemberPDJ = accidentsNovember[['District_Name','Weekday','Part_of_the_day']].sort_values(by=['District_Name'], ascending=True)
accidentsNovemberPDJ


# In[30]:


palette = sns.color_palette("rocket_r", as_cmap=True)
sns.displot(data=accidentsNovemberPDJ, x='Weekday', y='Part_of_the_day', palette=palette, cbar=True)
plt.title('Acidentes, por periodo e dia de novembro')
plt.xticks(rotation=90)


# Vamos agora ver os acidentes por dia e periodo distribuido por distrito

# In[34]:


g = sns.displot(accidentsNovemberPDJ, col='District_Name', x='Weekday', y='Part_of_the_day', cbar=True)
g.set_xticklabels(rotation=90)


# Vamos retomar nosso banco de dados original ('accidents') para fazer uma análise global, primeiro vamos ver o dia com mais ocorrência 

# In[36]:


weekday = accidents.groupby(by=['Weekday']).count().sort_values(by=['Id'],ascending=False)
weekday


# Vamos ver agora o periodo

# In[37]:


PartDay = accidents.groupby(by=['Part_of_the_day']).count().sort_values(by=['Id'],ascending=False)
PartDay


# o Distrito com mais ocorrência, também

# In[40]:


DistrictAccidents = accidents.groupby(by=['District_Name']).count().sort_values(by=['Id'],ascending=False)
DistrictAccidents


# 
# Por fim vamos ver novamente o mês com mais ocorrência também

# In[42]:


month = accidents.groupby(by=['Month']).count().sort_values(by=['Id'],ascending=False)
month


#  

# Um breve resumo do que já conseguimos
# Concluimos de acordo com as tabelas que:
# -Distrito com mais acidentes = Eixample(3029)
# -Mês com mais acidentes = Novembro(991)
# -Dia com mais acidentes = Sexta-Feira(1761)
# -Periodo com mais acidentes = Tarde(5082)

#  

# Vamos mostrar isso de forma gráfica, primeiro vamos resumir nosso banco de dados em Distrito, Mês, Dia e Periodo

# In[62]:


AccidentsR = accidents[['District_Name','Month','Weekday','Part_of_the_day']].sort_values(by=['District_Name'], ascending=True)
AccidentsR


# Vamos fazer um análise geral, gerando gráficos de acordo com mês e distrito, analisando o dia da semana e periodo

# In[60]:


sns.displot(AccidentsR, col='Month', row='District_Name', x='Weekday', y='Part_of_the_day')


# por fim, Vamos descompactar esses dados agora, em três análises, Distrito por Mês, Distrito, por dia e Distrito por Periodo

# In[58]:


sns.displot(AccidentsR, x='District_Name', y='Month')
plt.xticks(rotation=90)
plt.title('Distrito por mês')

sns.displot(AccidentsR, x='District_Name', y='Weekday')
plt.xticks(rotation=90)
plt.title('Distrito por dia')

sns.displot(AccidentsR, x='District_Name', y='Part_of_the_day')
plt.xticks(rotation=90)
plt.title('Distrito por periodo')


# CONCLUSÃO:

# Em novembro(mês que ocorreu mais acidentes, 991)
# o Distrito:    Eixample(310, ou ~31,3%)
# o Dia:         Quinta-feira(199, ou ~20,1%)
# o Periodo:     Tarde(501, ou ~50,6)

# No Geral(10.339)
# o Mês:         Novembro(991, ou ~9,6%)
# o Distrito:    Eixample(3029, ou ~29,3%)
# o Dia:         Sexta-Feira(1761, ou ~17%)
# o Periodo:     Tarde(5082, ou ~49,2%)

# In[ ]:




