import sys
import requests
from bs4 import BeautifulSoup, Tag
import readTitle
from TituloClass import *
from SendTitleToApi import *
from sendEmail import *
#go to the isbn website and look for information of the titles of certain editorial given a editorial id
print("inicia aplicación")

#read the number of items in page then look for the specific info of the item
def leer_paginas(id_editorial,numero_pagina):        
        url="https://isbnmexico.indautor.cerlalc.org/catalogo.php?mode=busqueda_menu&id_editor="+id_editorial+"&pagina="+numero_pagina
        all_items_ids=[]
        try:
            pagina= requests.get(url)
        except Exception as e:
            print("Error:"+str(e))

        full_page = BeautifulSoup(pagina.content,"html.parser")    
        items_collection=full_page.find_all("div", class_="row lista_libros")        
        
        for item in items_collection:                 
            ids= item.find_all("a", class_="titulo")
            for idz in ids:        
                link=idz['href']        
                all_items_ids.append(link.split("=")[2])
                    
        all_items_ids=set(all_items_ids)    
        all_items_ids= list(all_items_ids)
        all_items_ids.sort(reverse=True)

        print(all_items_ids)
        #sendEmail(str(all_items_ids))
        #looking for specific title info based on id and sends to the apis
        for item_id in all_items_ids:
            try:
                nuevo_titulo=readTitle.leer_titulo_por_id(item_id) 
                SendToApi(nuevo_titulo)

            except Exception as e:
                print("error en id "+str(item_id)+" "+e.__str__)                
                continue
#3506=panini 
#numero de paginas a buscar 6          

#modo = int(input("En que modo debe correr la aplicacion \n 1.agregar ultimos isbn. \n 2. agregar registro especifico \n") ) 
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
        leer_paginas("3506",numero_pag)
        
if first_argument=="2":
    idTituloBuscar=input("id del titulo a agregar:")
    print("id a buscar: ",idTituloBuscar)
    try:
        nuevo_titulo=readTitle.leer_titulo_por_id(idTituloBuscar) 
        SendToApi(nuevo_titulo)

    except Exception as e:
        print("error en id "+str(idTituloBuscar)+" "+e.__str__)                
        
    
print("finaliza aplicación")