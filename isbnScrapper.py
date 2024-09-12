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
        """
        Reads the isbn website of a given a editor 
        Args:
            id_editorial: numeric id that identifies the editorial in the isbn website
            numero_pagina: numbers of pages with titles of the editorial that will be read
        """    
        url="https://isbnmexico.indautor.cerlalc.org/catalogo.php?mode=busqueda_menu&id_editor="+id_editorial+"&pagina="+numero_pagina
        all_items_ids=[]
        try:
            pagina= requests.get(url)
        except Exception as e:
            print("Error:"+str(e))
        #Once we get the web page we start to parse the content in order to get the specific id of each title in the page
        full_page = BeautifulSoup(pagina.content,"html.parser")    
        items_collection=full_page.find_all("div", class_="row lista_libros")        
        
        for item in items_collection:                 
            ids= item.find_all("a", class_="titulo")
            for idz in ids:        
                link=idz['href']        
                all_items_ids.append(link.split("=")[2])
                    
        #sorting items in the order that apear in the web page
        all_items_ids=set(all_items_ids)    
        all_items_ids= list(all_items_ids)
        all_items_ids.sort(reverse=True)

        print(all_items_ids)
        
        #looking for specific title info based on id and sends to the apis
        for item_id in all_items_ids:
            try:
                nuevo_titulo=readTitle.leer_titulo_por_id(item_id) 
                SendToApi(nuevo_titulo)

            except Exception as e:
                print("error en id "+str(item_id)+" "+e.__str__)                
                continue
#3506=panini 



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