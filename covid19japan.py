#!/usr/bin/env python
# coding: utf-8

# In[42]:


import folium
import pandas as pd
from pandas import Series,DataFrame
cov = pd.read_csv("filepath/covid19japan.csv",encoding = "cp932")
data_size = len(cov["name"])
test_map = folium.Map(
    location=[35.5366158 , 139.74857073333332], #新しい地図を作るときの中央にくる緯度と経度を入れます
    zoom_start=9) 
for i in range(data_size):
    pin = [cov['lat'][i], cov['lon'][i]] #pinに緯度と経度を入れます
    if cov["npatients"][i] >= 2000:
        folium.CircleMarker(pin,popup=["patients: "+ str(cov['npatients'][i])],
                  radius=40,color="red",fill_color="red").add_to(test_map)        
    elif 2000 > cov["npatients"][i] >= 1500:
        folium.CircleMarker(pin,popup=["patients: "+ str(cov['npatients'][i])],
                  radius=30,color="red",fill_color="red").add_to(test_map)
    elif 1500 > cov["npatients"][i] >= 1000:
        folium.CircleMarker(pin,popup=["patients: "+ str(cov['npatients'][i])],
                  radius=20,color="red",fill_color="red").add_to(test_map)      
    elif 1000 > cov["npatients"][i] >= 500:
        folium.CircleMarker(pin,popup=["patients: "+ str(cov['npatients'][i])],
                  radius=15,color="red",fill_color="red").add_to(test_map)
    elif 500 > cov["npatients"][i] >= 100:
        folium.CircleMarker(pin,popup=["patients: "+ str(cov['npatients'][i])],
                  radius=10,color="red",fill_color="red").add_to(test_map)
    elif 100 > cov["npatients"][i] > 0:
        folium.CircleMarker(pin,popup=["patients: "+ str(cov['npatients'][i])],
                  radius=5,color="red",fill_color="red").add_to(test_map)
    else:
        pass
test_map


# In[ ]:




