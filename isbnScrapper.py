import sys
from editoriales import Editoriales
import readTitle
from TituloClass import *
from SendTitleToApi import *
from sendEmail import *
from readPages import leer_paginas

#go to the isbn website and look for information of the titles of certain editorial given a editorial id
print("inicia aplicación")

try:
    if len(sys.argv)>1:
        first_argument=sys.argv[1]
        
    else:
        print("args vacio")
except Exception  as e:
    print("Error:{e}")


if first_argument=="1":
    for i in range(1,10,1):
        print(i)
        numero_pag=str(i)
        leer_paginas(Editoriales.Panini,numero_pag)
        
if first_argument=="2":
    idTituloBuscar=input("id del titulo a agregar:")
    print("id a buscar: ",idTituloBuscar)
    try:
        nuevo_titulo=readTitle.leer_titulo_por_id(idTituloBuscar) 
        SendToApi(nuevo_titulo)

    except Exception as e:
        print("error en id "+str(idTituloBuscar)+" "+e.__str__)                
        
    
print("finaliza aplicación")

