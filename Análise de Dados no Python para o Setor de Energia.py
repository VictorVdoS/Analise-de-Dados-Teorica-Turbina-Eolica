#!/usr/bin/env python
# coding: utf-8

# # Objetivo
# 
# 
# criar uma análise da turbina eolica com um limite aceitavel de 5% para mais e para menos.

# # 01 - Importando Bibliotecas
# 
# Pandas: Biblioteca para manipulação e analise de dados
# 
# Seaborn: Biblioteca para visualização
# 
# Matplotlib: Biblioteca para visualização

# In[86]:


#Importando as bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # 02 - Lendo o Arquivo
# 
# Wind turbine scada dataset
# Fonte Kaggle: https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset/

# In[87]:


#Carregando os dados.
turbina = pd.read_csv('T1.csv')

#Renomeando as colunas
turbina.columns = ['Date/Time', 'ActivePower(kW)', 'WindSpeed(m/s)', 'TheoreticalPowerCurve(KWh)', 'WindDirection(°)']

#Deletando a coluna direção do vento
del turbina['WindDirection(°)']

#Convertendo a data
turbina['Date/Time'] = pd.to_datetime(turbina['Date/Time'])
display(turbina)


# # 03 - Plotando os Dados

# In[88]:


sns.scatterplot(data=turbina, x= 'WindSpeed(m/s)', y= 'ActivePower(kW)')


# # 04 - Plotando os Dados - Téorica

# In[89]:


sns.scatterplot(data=turbina, x= 'WindSpeed(m/s)', y= 'TheoreticalPowerCurve(KWh)')
print('Grafico de curva teórica')


# ##  Analisando ambos gráficos, é possível identificar um desvio entre o gráfico real para o teórico

# # 05 - Criando Limites aceitaveis

# In[90]:


pot_real= turbina['ActivePower(kW)'].tolist() #converte em lista
pot_teorica= turbina['TheoreticalPowerCurve(KWh)'].tolist() #converte em lista
pot_max = []
pot_min = []
dentro_limite = []

for potencia in pot_teorica:
    pot_max.append(potencia*1.05) #mais 5%
    pot_min.append(potencia*0.95) #menos 5%
    
for p, potencia in enumerate(pot_real):
    if potencia >= pot_min[p] and potencia <= pot_max[p]:
        dentro_limite.append('Dentro')
    elif potencia ==0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')
        
#print(dentro_limite.count('Dentro')/len(dentro_limite))
#print(dentro_limite.count('Zero')/len(dentro_limite))
#print(dentro_limite.count('Fora')/len(dentro_limite))


#checa se as listas tem o mesmo tamanho
#print(len (pot_max), len(pot_min), len(pot_teorica))


# # 06 - Adicionando lista "Dentro_Limite" ao dataframe

# In[91]:


turbina['DentroLimite'] = dentro_limite
display(turbina)


# # 07 - Plotando novamente o gráfico:

# In[92]:


cores = {'Dentro':'blue', 'Fora':'red', 'Zero':'orange'}
sns.scatterplot(data=turbina, x= 'WindSpeed(m/s)', y= 'ActivePower(kW)', hue = 'DentroLimite', s=1, palette=cores)

