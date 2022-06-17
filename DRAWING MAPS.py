#!/usr/bin/env python
# coding: utf-8

# DRAWING MAPS

# In[7]:


import numpy as np # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# In[9]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium
print('Folium installed and imported!')


# In[10]:


# define the world map
world_map = folium.Map()
# display world map
world_map


# In[11]:


# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
# display world map
world_map


# In[12]:


# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)
# display world map
world_map


# In[ ]:





# map of uganda

# In[15]:


uganda_latitude = 1.3733
uganda_longitude = 32.2903
# define the world map centered around mexico with a higher zoom level
uganda_map = folium.Map(location=[uganda_latitude, uganda_longitude],zoom_start=4)
# display world map
uganda_map


# In[17]:


uganda_latitude = 1.3733
uganda_longitude = 32.2903
# define the world map centered around mexico with a higher zoom level
uganda_map = folium.Map(location=[uganda_latitude, uganda_longitude],zoom_start=7)
# display world map
uganda_map


# In[21]:


kampala_latitude = 0.3476
kampala_longitude = 32.5825
# define the world map centered around mexico with a higher zoom level
kampala_map = folium.Map(location=[kampala_latitude, kampala_longitude],zoom_start=12)
# display world map
kampala_map


# In[ ]:





# map of east africa

# In[23]:


east_africa_latitude = 1.9577
east_africa_longitude = 37.2972
# define the world map centered around mexico with a higher zoom level
east_africa_map = folium.Map(location=[east_africa_latitude, east_africa_longitude],zoom_start=6)
# display east africa map
east_africa_map


# map of africa

# In[25]:


africa_latitude = 8.7832
africa_longitude = 34.5085
# define the world map centered around mexico with a higher zoom level
africa_map = folium.Map(location=[africa_latitude, africa_longitude],zoom_start=3)
# display world map
africa_map


# Question: Create a map of Mexico with a zoom level of 4.

# In[13]:


### type your answer here
mexico_latitude = 23.6345
mexico_longitude = -102.5528
# define the world map centered around mexico with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude],zoom_start=4)
# display world map
mexico_map


# In[ ]:





# Stamen Toner Maps

# In[ ]:


Let’s create a Stamen Toner map of canada with a zoom level of 4.


# In[14]:


# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='StamenToner')
# display map
world_map


# In[ ]:





# stamen toner map of uganda

# In[29]:


# create a Stamen Toner map of the world centered around uganda
world_map = folium.Map(location=[1.3733, 32.2903], zoom_start=4, tiles='StamenToner')
# display map
world_map


# stamen toner map of east africa

# In[32]:


# create a Stamen Toner map of the world centered around east africa
world_map = folium.Map(location=[1.9577, 37.2972], zoom_start=6, tiles='StamenToner')
# display map
world_map


# stamen toner map of africa

# In[33]:


# create a Stamen Toner map of the world centered around africa
world_map = folium.Map(location=[8.7832, 34.5085], zoom_start=4, tiles='StamenToner')
# display map
world_map


# In[ ]:





# In[ ]:


stamen toner map of kampala


# In[37]:


# create a Stamen Toner map of the world centered around kampala
world_map = folium.Map(location=[0.3476, 32.5825], zoom_start=10, tiles='StamenToner')
# display map
world_map


# In[ ]:





# Stamen Terrain Maps

# In[38]:


# create a Stamen Toner map of the world centered around Canada
import folium
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Terrain')
# display map
world_map


# In[ ]:


Stamen Terrain Map of kampala


# In[40]:


# create a Stamen Toner map of the world centered around kampala
import folium
world_map = folium.Map(location=[0.3476, 32.5825], zoom_start=10, tiles='Stamen Terrain')
# display map
world_map


# In[ ]:


Stamen Terrain Map of east africa


# In[42]:


# create a Stamen Toner map of the world centered around east africa
import folium
world_map = folium.Map(location=[1.9577, 37.2972], zoom_start=6, tiles='Stamen Terrain')
# display map
world_map


# In[ ]:


Stamen Terrain Map of africa


# In[45]:


# create a Stamen Toner map of the world centered around africa
import folium
world_map = folium.Map(location=[8.7832, 34.5085], zoom_start=3, tiles='Stamen Terrain')
# display map
world_map


# In[ ]:


Stamen Terrain Map of uganda


# In[49]:


# create a Stamen Toner map of the world centered around uganda
import folium
world_map = folium.Map(location=[1.9577, 37.2972], zoom_start=6, tiles='Stamen Terrain')
# display map
world_map


# In[ ]:




