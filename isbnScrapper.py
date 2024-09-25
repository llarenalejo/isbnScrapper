import sys
from editoriales import Editoriales
import readTitle
from TituloClass import *
from SendTitleToApi import *
from sendEmail import *
from readPages import leer_paginas
import cutie

#go to the isbn website and look for information of the titles of certain editorial given a editorial id
print("inicia aplicación")

        

options=['Look for latests ISBNs','Add title by ID']
print(f"select a function to execute:")
selected_option=cutie.select(options)

if selected_option==0:
    print("Looking for latests ISBNs")
    for i in range(1,10,1):
        print(i)
        numero_pag=str(i)
        leer_paginas(Editoriales.Panini,numero_pag)    

elif selected_option==1:
    print("Adding title by ID")
    idTituloBuscar=input("id del titulo a agregar:")
    print("id a buscar: ",idTituloBuscar)
    try:
        nuevo_titulo=readTitle.leer_titulo_por_id(idTituloBuscar) 
        SendToApi(nuevo_titulo)

    except Exception as e:
        print("error en id "+str(idTituloBuscar)+" "+e.__str__)

print("finaliza aplicación")

