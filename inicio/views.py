from django.shortcuts import render, HttpResponse
import numpy as np
import pandas as pd
from django_tables2.tables import Table
from django.shortcuts import render
import folium

# Create your views here.
def paginiainicial(request):
    labs = pd.read_excel('inicio/labs_atual.xlsx')
    confirmedGlobal=pd.read_excel('inicio/labs_atual.xlsx') 
    confirmedGlobal= confirmedGlobal.replace(np.nan, '', regex=True)
    confirmedGlobal =  confirmedGlobal.replace('?', 'Não disponível')
    confirmedGlobal =  confirmedGlobal.replace('', 'Não disponível')
    df=confirmedGlobal 
    allData=[]
    for i in range(df.shape[0]):
        temp=df.loc[i]
        allData.append(dict(temp))
    context= {'data':allData}
    return render(request, 'inicio/2.html',context)
   # return render(request,"inicio/home.html")
def home(request):
   key1 = request.GET.get('key1') 
   df=pd.read_excel('inicio/labs_atual.xlsx')
   df= df.replace(np.nan, '', regex=True)
   df =  df.replace('?', 'Não disponível')
   df =  df.replace('', 'Não disponível')
   lat= df[df['Site'].str.contains(key1)].values[0][10]
   lng = df[df['Site'].str.contains(key1)].values[0][11]
   m = folium.Map(location=[ lat,lng],zoom_start=20)
   folium.Marker(
   location=[lat,lng],
   popup=df[df['Site'].str.contains(key1)].values[0][3],
   icon=folium.Icon(icon='cloud')).add_to(m)
   m.save('inicio/templates/mapa.html')
   return render(request, 'mapa.html')
