import warnings
import readTitle 
from TituloClass import *
import requests
import urllib3
import re
import socket

def SendToApi(titulo_a_enviar:Titulo):
    """
        Sends the title information to the mangakat api
        Args: 
            titulo_a_enviar(Titulo):objeto con la informacion del titulo a enviar
    """
    titulo=titulo_a_enviar
    
    url = "http://www.mangakat.api/api/Titulos"
    data={"nombre":titulo.nombre,"autor":titulo.autores , "idEditorial":6,"idFormato":1,"isbn":titulo.isbn, "fechaPublicacion":titulo.fecha_publicacion, "paginas": 0 if re.search('[a-zA-Z]',titulo.paginas) else titulo.paginas, "precio":titulo.precio,"pasta":titulo.pasta,"tamaño":titulo.tamaño,"imagenes":"null"}
    
    #print(data)
    #print('\n')
    urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
    
    warnings.filterwarnings("ignore")
    response=requests.post(url,json=data,verify=False)

    if response.status_code==200:

        if "endApp" in response.text:
            print('.')
        else:
            print("agregados datos de "+titulo.nombre)
    elif response.status_code==500:        
            print('.')                    
    else:
        print(f"Error al enviar "+titulo.isbn+" "+response.text) 