
from bs4 import BeautifulSoup
import requests
from SendTitleToApi import SendToApi
from readTitle import leer_titulo_por_id


def leer_paginas(id_editorial:str,numero_pagina:str):   
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
                nuevo_titulo=leer_titulo_por_id(item_id) 
                SendToApi(nuevo_titulo)

            except Exception as e:
                print("error en id "+str(item_id)+" "+e.__str__)                
                continue
