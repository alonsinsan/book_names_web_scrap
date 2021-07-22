import requests
import bs4
import re
import pandas as pd
def getAndParseURL(url):
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    return(soup)
# en este path pon en donde está el excel con la info para buscar y descomenta esta línea
#datos = pd.read_excel("\path_a_los_datos")
#supondré que hay una columa con e nombre ISBN para hacer la lista
# ISBN = datos.ISBN
ISBN = ['19786076195376', '9786075471570']
n = len(ISBN)
titulos = []
autores = []
#editoriales = []
no_queridos_titulos = ['confianza-ciega', '21-lecciones-para-el-siglo-xxi']
no_queridos_autores = ['KATZENBACH JOHN', 'YUVAL NOAH HARARI']
m = len(no_queridos_titulos)
for i in range(n):
    URL = 'https://www.elsotano.com/busqueda/listaLibros.php?tipoBus=full&tipoArticulo=&palabrasBusqueda=' + ISBN[i]
    soup = getAndParseURL(URL)
    no_encontrar = [x.text for x in soup.findAll("span")]
    no_encontrar = [x for x in no_encontrar if "Lo sentimos, no hay resultados para:" in x]
    if no_encontrar:
        titulo_aux = ["No encontrado"]
        autor_aux = ["No encontrado"]
    else:        
        titulo_aux = [x.h3.a.get('href') for x in soup.findAll("div", class_ = "so-booktitle")]
        autor_aux = [x.text for x in soup.findAll("span", class_ = "so-bookwriter")]
    titulos = titulos + titulo_aux
    autores = autores + autor_aux
for j in range(m):
    autores = [x for x in autores if no_queridos_autores[j] not in x]
    titulos = [x for x in titulos if no_queridos_titulos[j] not in x]
titulos = [re.sub("\n", "", x) for x in titulos]
autores = [re.sub("\n", "", x) for x in autores]
titulos = [re.sub("\.", "", x) for x in titulos]
autores = [re.sub("\.", "", x) for x in autores]
titulos = [re.sub("\/", "-", x) for x in titulos]
titulos = [re.sub("\-"," ",x) for x in titulos]
titulos = [x.strip() for x in titulos]
autores = [x.strip() for x in autores]

todo = pd.DataFrame({"ISBN": ISBN, "autor": autores, "titulo": titulos})
print(todo)

#para guardar el archivo como un csv en el path que quieras
todo.to_csv("path_deseado_del_archivo_de_salida")
    