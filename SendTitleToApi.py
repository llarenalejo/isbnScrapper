import warnings
import readTitle 
from TituloClass import *
import requests
import urllib3
import re
import socket

def SendToApi(titulo_a_enviar):
    #titulo=Titulo()
    titulo=titulo_a_enviar
    #url = "https://localhost:44347/api/Titulos"
    url = "http://www.mangakat.api/api/Titulos"
    data={"nombre":titulo.nombre,"autor":titulo.autores , "idEditorial":6,"idFormato":1,"isbn":titulo.isbn, "fechaPublicacion":titulo.fecha_publicacion, "paginas": 0 if re.search('[a-zA-Z]',titulo.paginas) else titulo.paginas, "precio":titulo.precio,"pasta":titulo.pasta,"tamaño":titulo.tamaño,"imagenes":"null"}
    
    #print(data)
    #print('\n')
    urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
    
    warnings.filterwarnings("ignore")
    response=requests.post(url,json=data,verify=False)

    if response.status_code==200:
        #print("datos de "+titulo.nombre)
        
        if "endApp" in response.text:
            print('.')
            #print("ya existe en la base de datos, se detiene la aplicación")
            #exit()
        else:
            print("agregados datos de "+titulo.nombre)
    elif response.status_code==500:
        
            print('.')        
            #print(titulo.nombre+" "+response.text)
    else:
        print(f"Error al enviar "+titulo.isbn+" "+response.text) 