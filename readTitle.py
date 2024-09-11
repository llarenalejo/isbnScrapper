import requests
from bs4 import BeautifulSoup, Tag
import TituloClass 

# scrap ttrought the page with info of an specific tittle using the id
def leer_titulo_por_id(id):
    url="https://isbnmexico.indautor.cerlalc.org/catalogo.php?mode=detalle&nt="+id
    page= requests.get(url)
    paragraphArray=[]
    libro_datos={}

    soup = BeautifulSoup(page.content,"html.parser")
    results=soup.find("div", class_="row lista_libros")
    try:
        caja_sinopsis=results.find("p", class_="texto_gris").text
    except:
        caja_sinopsis=""
    
    results=results.find("div", class_="col-md-7 no-padding")

    isbn=results.find("span", class_="isbn").text.split(" ")[1]
    titulo = results.find("span", class_="TituloNolink").text.strip()
    libro_datos["isbn"]=isbn
    libro_datos["titulo"]=titulo
    
    for label in results.find_all("span", attrs={"class": ["labels","labels C_Colaboradores"]}): #results.find_all("span", class_="labels"):
        key=label.text.strip().split(":")[0]  #texto del label como keu
        if key in ("Autor","Autores","Colaborador","Colaboradores"):
            value_span=label.find_next_siblings("a") #label.find_next_sibling("a")
            #print(str(label.find_next_siblings(attrs={"class":"texto"})[0].text)+"\n")
            
            value=label.find_next_siblings(attrs={"class":"texto"})[0].text
            #print(allValueSiblings+"\n")
            
        else:
            value_span=label.find_next_sibling("span") # busca el span que sigue para sacarle el valor
            value=value_span.text.strip() if value_span else "" # saca el valor si o asigna uno por defecto
        libro_datos[key]=value   
   
    
    
    isbn=libro_datos["isbn"]
    titulo=libro_datos["titulo"]
    try:autores=libro_datos["Autor"]         
    except:autores=libro_datos["Autores"]
    fecha_publicacion=libro_datos["Publicado"]
    try:numero_paginas=libro_datos["Número de páginas"] 
    except: numero_paginas=0
    tamaño=libro_datos["Tamaño"]
    precio=libro_datos["Precio"]
    encuadernacion=libro_datos["Encuadernación"]
    manga=TituloClass.Titulo(id,isbn,titulo,autores,fecha_publicacion,numero_paginas,tamaño,precio,encuadernacion,caja_sinopsis)    
    
        
    return manga
