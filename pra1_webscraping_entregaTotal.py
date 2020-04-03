#"""
#Created on Mon Mar 23 19:41:20 2020
#@author: smartinalbar
#@author: bmartineza01
#conda config --set ssl_verify False (se necesita hacer esto)

import requests
import json
import csv
import os
from bs4 import BeautifulSoup
import time
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import base64
import urllib

#Hacemos una función para cargar el json que nos devolverar la peticion.
def carga_json(response):
    #Inicializamos los datos a vacio.
    data = None
    #Si la respuesta es un 200 - OK
    if response.status_code == 200:    
        data = json.loads(response.content)   
    # Si la respuesta da otro valor , levantamos excepcion:
    else:
        raise Exception("Respuesta incorrecta  (%s: %s)." %(response.status_code, response.reason))
    return data


#-----------------------------------------------------------------
# FUNCION : obtener_datos(request,opcion)
# Objetivo: Poder hacer una funcioon en la que según la opción , se recupera la inforación de la petición 
#-----------------------------------------------------------------
def obtener_datos(req,option):
    
    # Se realiza la petición y se recoje la respuesta. Se pone el parámetro verify , ya que daba un tema de certificado
    response = requests.get(req,verify=False)
    #Se cargan los datos del json   
    data =carga_json(response)
    # Se crea la lista donde vamos a almacenar los datos para hacer el CSV File 
    datosCsvList = []

    # En el caso de la opción 1:
    if(option=="1"):
         # Se define la primera fila con la cabecera de los datos
        cabeceraDatos=["Tematicas","Barrio","Nombre","subtemas","FechaInicio","HoraInicio","FechaFin","HoraFin","tipos","perfiles","ficha"]
        datosCsvList.append(cabeceraDatos)
         # si se devuelven datos..
        if(data): 
             # Se obtienen los registros .
             # Se observa la estructura y se recuperan segun las etiquetas..
             datosList = data.get("records")
             #Nos recorremos los datos obtenidos de la respuesta del json.
             for elemento in datosList:
                # Se recuperan cada uno de los elementos existentes de los registros de la agenda
                # En algunos casos, estos elementos son arrays
                tematicas = elemento['tematicas']
                barrio = elemento['barrio']
                nombre = elemento['nombre']
                subtemas = elemento ['subtemas']
                fechaInicio= elemento ['fechaInicio']
                horaInicio= elemento ['horaInicio']
                fechaFin= elemento ['fechaFin']
                horaFin= elemento ['horaFin']
                tipos= elemento ['tipos']
                perfiles= elemento ['perfiles']
                ficha= elemento ['ficha']
                #Se forma la linea de cada registros del fichero CSV
                linea = [tematicas,barrio,nombre,subtemas,fechaInicio,horaInicio,fechaFin,horaFin,tipos,perfiles,ficha]
                #Se añade la información a la lista que se guardara como CSV
                datosCsvList.append(linea)
        else: 
                # Si da error , devolvemos un mensaje            
                print('Error obteniendo los datos de la pagina.')
                
    elif (option =="2"):
         # Se define la primera fila con la cabecera de los datos
        cabeceraDatos=["FamiliaDesc","EspecialidadCertificado","CentroCP","CursoCodigo",
                        "DirigidoA","CentroMunicipio", "CursoDesc","Censo","CentroTfno",
                        "Duracion","SectorDesc","EspecialidadDesc1","CentroEmail","Modalidad",
                        "CentroDireccion","SieCodigo","EspecialidadDesc","AreaDesc",
                        "CentroDesc"]
        datosCsvList.append(cabeceraDatos)
        if(data): 
             # Se obtienen los registros .
             # Se observa la estructura y se recuperan segun las etiquetas..
            datosList = data.get("data")
             #Nos recorremos los datos obtenidos de la respuesta del json.
            i= 0
            for elemento in datosList:
                # Se obtienen los campos del JSON accediendo a cada elemento de cada registro
                familia_desc = elemento['familia_desc']
                especialidad_de_certificado = elemento['especialidad_de_certificado']
                centro_cp =   elemento['centro_cp']
                curso_codigo = elemento['curso_codigo']
                dirigido_a = elemento['dirigido_a']
                centro_municipio = elemento['centro_municipio']
                curso_desc = elemento['curso_desc']
                censo = elemento['censo']
                centro_telefono = elemento['centro_telefono']
                duracion_formacion = elemento['duracion_formacion']
                sector_desc = elemento['sector_desc']
                especialidad_desc_1 = elemento['especialidad_desc_1']
                centro_email = elemento['centro_email']
                modalidad = elemento['modalidad']
                centro_direccion = elemento['centro_direccion']
                sie_codigo = elemento['sie_codigo']
                especialidad_desc = elemento['especialidad_desc']
                area_desc= elemento['area_desc']
                #duracion_practicas = elemento['duracion_practicas']
                centro_desc = elemento['centro_desc']    
                # Se forma la lineas
                linea = [familia_desc,especialidad_de_certificado,centro_cp,curso_codigo,dirigido_a,
                         centro_municipio,curso_desc,censo,centro_telefono,duracion_formacion,sector_desc,
                         especialidad_desc_1,centro_email,modalidad,centro_direccion,sie_codigo,especialidad_desc,
                         area_desc,centro_desc]
                datosCsvList.append(linea)
                i += 1
                #Ponemos límite de elementos puesto que es para un ejemplo..
                if(i>=100):
                    return datosCsvList
        else: 
                # Si da error , devolvemos un mensaje            
                print('Error obteniendo los datos de la pagina.')
    else:
        print("No implementado")
    return datosCsvList


#-----------------------------------------------------------------
# FUNCION : obtener_datos_circ(req,pagina)
# Objetivo: Se ha puesto un metodo aparte porque el uso es con Beautiful Soup
#-----------------------------------------------------------------
def obtener_datos_circ(req,pagina):

    # Se realiza la petición
    response = requests.get(req+pagina) 
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())
    # Se crea la lista 
    datosCsvList = []
    table=soup.find('table')
    if(table is None):
        print("No se encuentran datos con la estructura de resultados ")
    else:
        #Cogemos la cabecera de la tabla
        for fila in table.findAll("tr"): # Solo tiene una 
            cth =fila.findAll('th')
          
  
        #Se busca la tabla de cabecera (tiene 4)
        #Nos recorremos los datos obtenidos de la respuesta del json.
        for elemento in cth:
            #Recuperamos cada uno de las cabeceras
            revistaC=cth[0].find(text=True)
            issnC=cth[1].find(text=True)
            classSSC=cth[2].find(text=True)
            classCHC=cth[3].find(text=True)
            lineaC = [revistaC,issnC,classSSC,classCHC]
            #Si es la pagina inicial, ponemos la cabecera
            if (pagina == "1"):
                #print(pagina)
                datosCsvList.append(lineaC)
   
        #Buscamos la tabla de los datos .Muestra 10 por pagina.
        table2=soup.findAll('table')
    
        for fila2 in table2[1].findAll("tr"):
        
            ctd =fila2.findAll('td')
            #Recuperamos cada uno de los campos.En este caso es un tabla muy sencilla
            revistaE=ctd[0].find(text=True)
            issnE=ctd[1].find(text=True)
            classSSE=ctd[2].find(text=True)
            classCHE=ctd[3].find(text=True)
            lineaE = [revistaE,issnE,classSSE,classCHE]
            #print(lineaE)
            datosCsvList.append(lineaE)
            #print(datosCsvList)
            # Ahora la tabla de busqueda
    return datosCsvList
     

def obtener_datos_scimago(req,pagina,fecha):

    # Se realiza la petición
    req =req+"&page="+pagina+"&year="+fecha
    response = requests.get(req+pagina) 
    soup = BeautifulSoup(response.content, 'html.parser')
    #Se puede imprimir y visualizar como esta construida la pagina HTML
   # print(soup.prettify()) 
      # Se crea la lista 
    datosCsvList = []
    lineaC=[]
    lineaR=[]
    # Se observa en l pagina que la cabecera tiene thead
    tablaC=soup.find('thead')
    # Dentro de esa fila de esa cabecera, obtenemos los datos 
    for filaC in tablaC:
        ths = tablaC.find_all('th')
        #print(filaC)
        for th in ths:
            campoC = th.find(text=True)
            lineaC.append(campoC)
    if (pagina == "1"):
        #print(pagina)
        datosCsvList.append(lineaC)    
    tabla=soup.find('tbody')

    # Me recorro los TR, 
    for fila in tabla.find_all('tr'):
        # print(fila)
        tds= fila.find_all('td')
        lineaR=[]
        for td in tds:
            campo = td.find(text=True)
            lineaR.append(campo)
            # print(lineaR)
        datosCsvList.append(lineaR)
        
    
    # Ahora la tabla de busqueda
    return datosCsvList

#-----------------------------------------------------------------
# FUNCION: Web Scraping milanuncios.com  
# Objetivo: obtener las páginas indicadas del catálogo de milanuncios 
# para una temática y de estas obtener todos los items y algunos de 
# sus campos
#-----------------------------------------------------------------

def procesar_pagina_mil(url):

            # se accede a la url de cada item
            r2 = requests.get(url)
        
            # se comprueba que terminó correctamente y se recoge 
            # en objeto beautifulsoup
            if r2.status_code == requests.codes.ok:
                soup2 = BeautifulSoup(r2.text,features="lxml")
                return obtener_items_mil(soup2, url)
                    
def obtener_items_mil(html, url=""):

    item = {}
    province = ' '
    
    #nombre item
    title = html.find('h1', class_='ad-detail-title')
    if title:
            title = title.text
            item['title'] = title
    
    price = html.find('div', class_='pagAnuPrecioTexto')
    if price:
            price = price.text
            price = price.replace('€', '').replace('.', '')
            price = int(price)
            item['price'] = price
    
    m2 = html.find('div', class_='m2 tag-mobile')
    if m2:
        m2 = m2.text
        m2 = m2.replace('m2', ' ')
        item['m2'] = m2
    
    location = html.find('div', class_='pagAnuCatLoc')
    if location:
        location = location.text
        province=location.split('(')
        province = province [1]
        province = province.replace(')', ' ')
        item['location'] = location
        item['province'] = province
    
    description = html.find('p', class_='pagAnuCuerpoAnu')
    if description:
        description = description.text
        item['description'] = description
    
    
    times = html.find('div', class_='pagAnuStatsData')
    if times:
            times = times.text
            times = int(times)
            item['times'] = times
    
    
    return item


def procesar_catalogo_mil(url, itemList):  
 
   #peticion a la pagina web, filtramos por inmobiliaria, ventas, aticos con 3 dormitorios y 2 baños
   #r = requests.get('https://www.milanuncios.com/venta-de-aticos/?dormd=3&banosd=2&pagina=1')
    r = requests.get(url)
    #comprobamos terminación correcta y pasamos contenido web a objeto 
    #beautifulsoup 
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,features="lxml")
        
    #procesamos pagina
    #obtenemos total paginas y pasamos a numérico
    pages = soup.find('div', class_='adlist-paginator-summary')
    if pages: 
        pages = pages.text.split()[-1]
        pages = int(pages)
        
    #vamos recorriendo por páginas, acotamos para la prueba solo a 2  
    
    pages = 10 
    for i in range(1, pages+1):
         
        r = requests.get(url + str(i))

        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,features="lxml")

       # se buscan todos los item dentro de una pagina        
        ads = soup.find_all('div', class_="aditem")
       #por cada item se obtiene su nombre y su url para hacer petición
       #sobre el detalle de cada item   
        for ad in ads:
        
            # se obtiene la url de cada item
            a_title = ad.find('a', class_='aditem-detail-title')
            complete_url = url + a_title['href']
            itemList.append(procesar_pagina_mil(complete_url))
    
        time.sleep(2)
    return itemList

#-----------------------------------------------------------------
# FUNCION: API idealista 
# Objetivo: obtener datos de idealista accediendo a través de la API key
# y extraer el dataframe 
#-----------------------------------------------------------------

#acceso a la url utilizando la apikey para conseguir el token
def get_oauth_token():

    
    url = "https://api.idealista.com/oauth/token"   
    # Las siguientes variables deberian tener el valor del apikey /secret 
    # que idealista/labs proporcina si las pides en su pagina web.
    apikey = 'apikeyproporcionadaporidealista'
    secret= 'secretididealista'
    s = apikey + ':' + secret
    auth = str(base64.b64encode(s.encode('utf-8')),'utf-8')
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Authorization' : 'Basic ' + auth}
    params = urllib.parse.urlencode({'grant_type':'client_credentials'})
    content = requests.post(url,headers = headers, params=params)
    bearer_token = json.loads(content.text)['access_token']
    return bearer_token

#recuperar el json con los datos
def search_api(token, url):  
    authorization = 'Bearer ' + token
    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' :  authorization }
    content = requests.post(url, headers = headers)
    if content.status_code != 200:    
        print("Error accediendo pagina  (%s: %s)." %(content.status_code, content.reason))
        return 0
    else:
        result = json.loads(content.text)
    return result

#obtener los datos para viviendas en España
def llamada_idealista():
    
    country = 'es' 
    language = 'es' #
    max_items = '50'
    operation = 'sale' 
    property_type = 'homes'
    order = 'priceDown' 
    center = '40.4167,-3.70325' 
    distance = '60000'
    sort = 'desc'
   
    df_tot = pd.DataFrame()
    limit = 3 # Se puede subir ,pero las peticiones tenemos 100 al mes.
    for i in range(1,limit):
        
        url = ('https://api.idealista.com/3.5/'+country+'/search?operation='+operation+#"&locale="+locale+
           '&maxItems='+max_items+
           '&order='+order+
           '&center='+center+
           '&distance='+distance+
           '&propertyType='+property_type+
           '&sort='+sort+ 
           '&numPage=%s'+
           '&language='+language) %(i)
        
        print(url)
        datos = search_api(get_oauth_token(), url)
        if(datos==0):
            return 0
        else:
            df = pd.DataFrame.from_dict(datos['elementList'])
            df_tot = pd.concat([df_tot,df],sort=False)
        time.sleep(2)
    df_tot = df_tot.reset_index()
    return df_tot

#-----------------------------------------------------------------
# FUNCION : grabar_fichero_scv(datosList,opcion)
# Objetivo: Grabar el fichero CSV a una ruta local, con el nombre pra1_datasetX.csv, 
# donde X es el nº de opcion seleccionada
#-----------------------------------------------------------------
def grabar_fichero_csv(datosList,opcion):
    #De momento grabamos el fichero en local.
    localDir = os.path.dirname(os.path.abspath("__file__"))
    # <ori> localDir = os.path.dirname(__file__)
    filename = "pra1_dataset" +opcion+".csv"
    filePath = os.path.join(localDir, filename)
    with open(filePath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for linea in datosList:
            writer.writerow(linea)
    print('Grabando datos en fichero csv...')
    return filePath

#-------------------------------------------------------------------
# FUNCION: grabar fichero de salida csv
# Objetivo: grabarlo desde dataFrame 
#-------------------------------------------------------------------

def grabar_dataframe(df_entrada,opcion):
    
    #De momento grabamos el fichero en local.  
    localDir = os.path.dirname(os.path.abspath("__file__"))
    filename = "pra1_dataset" +opcion+".csv"
    filePath = os.path.join(localDir, filename)
    df = pd.DataFrame(df_entrada)
    df.to_csv(filename)
    print('Grabando datos en fichero csv...')
    return filePath

#-----------------------------------------------------------------
# FUNCION : pintar_grafico(rutaFichero,opcion)
# Objetivo: Hacer un grafico sencillo de cada tipo de juego de datos
#-----------------------------------------------------------------
def pintar_grafico(rutaFichero,opcion):
    #PDTE DE HACER UN GRAFICO CON LOS DATOS OBTENIDOS
    print(rutaFichero) 

    dataset_csv = pd.read_csv(rutaFichero, sep=",", engine='python')
    # Cargamos los datos en un dataframe de pandas.
    df_dataset = pd.DataFrame(dataset_csv)
    grafico =None
    #Mostramos las 3 primeras filas.
    #print(df_dataset.head(n=3))
    sn.set_style("whitegrid")
    if (opcion == "2"):
        plt.figure(figsize=(12, 6))
        plt.title('Nº de Cursos por Area con o sin certificado')
        grafico= sn.countplot(y = "AreaDesc", hue = "EspecialidadCertificado" ,data = df_dataset,  color = "b", orient = "h")
        plt.savefig('pra1_dataset2.jpeg', format='jpeg', orientation= 'landscape')
    elif(opcion == "1"):
       # grafico= sn.catplot(x = "Barrio", hue="perfiles",kind="count", data = df_dataset,  color = "g", orient = "h",height=6, aspect=1)
        # Se utilizan colores más fuertes para distinguir los colores.
        grafico= sn.catplot(x = "Barrio", hue="perfiles", kind="count", data = df_dataset,palette=sn.color_palette(['purple', 'blue', 'green','red','cyan','yellow','black','pink','gray']), orient = "h",height=6, aspect=1)
        plt.title('Nº de eventos agenda por barrio/perfiles')
        plt.savefig('pra1_dataset1.jpeg', format='jpeg')
    elif(opcion == "3"): 
        grafico= sn.catplot(y = "Clasificación Ciencias Sociales", hue= "Clasificación Ciencias Humanas",kind="count", data = df_dataset,  palette=sn.color_palette(['purple', 'blue','green','cyan','red','gray']), orient = "h", height=5, aspect=1)
        plt.title('Tipos de Clasificaciones de Revistas CIRC')
        plt.savefig('pra1_dataset3.jpeg', format='jpeg',dpi=300)
        grafico= sn.catplot(y = "Clasificación Ciencias Sociales", col= "Clasificación Ciencias Humanas",kind="count", data = df_dataset,  palette=sn.color_palette(['purple', 'blue','green','cyan','red','gray']), orient = "h", height=5, aspect=0.6)
        plt.savefig('pra1_dataset3bis.jpeg', format='jpeg',dpi=300)
    elif(opcion == "4"): 
        #obtenemos precio medio por provincia
        price_mean =  pd.DataFrame((df_dataset['price']).groupby(df_dataset['province']).mean())
        df_price_mean = price_mean
        plt.figure(figsize=(8, 6))
        sn.barplot(x=df_price_mean.index, y="price", data=df_price_mean, color="b")
        plt.title('Precio medio por provincia')
        plt.xticks(rotation=70)
        plt.savefig('pra1_dataset4.jpeg', format='jpeg',dpi=300)
    elif(opcion == "5"): 
        pisos = df_dataset['propertyType'] == 'flat'
        df_dataset_pisos=df_dataset[pisos]
        df_dataset_pisos['province'].value_counts().plot(kind='bar',
                                            title='Pisos por provincia')
        plt.savefig('pra1_dataset5.jpeg', format='jpeg', dpi=1000)
    elif(opcion == "6"): 
        grafico=sn.catplot(x = "SJR", y="Type", data = df_dataset,kind = "swarm",  color = "g", orient = "h",height=10, aspect=1)
        plt.title('SJR (Indice de impacto) /Tipologia')
        plt.savefig('pra1_dataset6.jpeg', format='jpeg', dpi=1000)
    else:
        print ("OPCION NO GRAFICABLE")
    return grafico

#-----------------------------------------------------------------
# FUNCION : MENU PARA PODER SELECCIONAR DISTINTAS FORMAS DE ACCEDER A DATOS DE lA WEB.
# Objetivo: Mostrar un menú con las distintas opciones con ver distintos juefos de datos 
# o formas de acceso
#-----------------------------------------------------------------
def menu_scrapy ():
    try:
        print('Introduce la opción que quieras utilizar:------------')
        print('1.- Agenda Datos Alcobendas (Open Data) - JSON')
        print('2.- Cursos Comunidad de Madrid (Open Data) - JSON')
        print('3.- Revistas Cientificas CIRCR:(Beautiful Soup) - Tabla')
        print('4.- Mil anuncios : (Beautiful Soup) - Listado')
        print('5.- Idealista. (API KEY- Autheticación OAuth2)')
        print('6.- SCIMAGO - Ranking de Revisata -BeautifulSoup')
        print('Escriba exit para salir sin ninguna opción')
        print('---------------------------------------------------')
        opcion = input()

        if (opcion == "1"):  #DATOS DE AGENDA
            print("%s\nOpcion Elegida - AGENDA OPEN DATA" %(opcion))
             # Se define la página desde donde vamos a obtener los datos
            req= 'https://datos.alcobendas.org/dataset/2458d605-1fd0-4d16-a1ef-795bc243e152/resource/90836555-54b5-45af-ae67-e7545937f591/download/recurso.json'
            datos_agenda = obtener_datos(req,opcion)
            ruta_fichero = grabar_fichero_csv(datos_agenda,opcion)
            pintar_grafico(ruta_fichero,opcion)
            print('---------------------------------------------------------------------')
            
        elif (opcion == "2"):  #DATOS DE LA COMUINIDAD DE MADRID 
            print("%s\nOpcion Elegida - COMUNIDAD MADRID -CURSOS " %(opcion))
            # Se define la pagina a acceder a  los datos
            req2='https://datos.comunidad.madrid/catalogo/dataset/2347cccf-0cb0-439b-9f99-173cc06be9d3/resource/3e318606-c332-458f-ac3e-cf2721f7f710/download/cursos_formacion_profesional_empleo.json'
            # Se obtienen los datos de los cursos.
            datos_cursos = obtener_datos(req2,opcion)
            ruta_fichero = grabar_fichero_csv(datos_cursos,opcion)
            pintar_grafico(ruta_fichero,opcion)
            print('---------------------------------------------------------------------')
           
        elif (opcion == "3"):  # REVISTAS CIENTIFICAS CIRC
            print("%s\nOpcion Elegida - REVISTAS " %(opcion))
            # Se define la página desde donde vamos a obtener los datos
            req= 'https://clasificacioncirc.es/resultados_busqueda?_pag='
            i = 1
            datosCSV=[]
            while (i < 3): # Nº de request a realizar (bajamos el nº de 10 a 3)
               #se pone un retardo de un segundo
                time.sleep(2)
                datos = obtener_datos_circ(req,str(i))
                datosCSV += datos
                i +=1
            ruta_fichero = grabar_fichero_csv(datosCSV,opcion)
            pintar_grafico(ruta_fichero,opcion)
            print('---------------------------------------------------------------------')
        elif (opcion == "4"):  
            print("%s\nOpcion Elegida -Mil Anuncios " %(opcion))
            # <ori> req= 'http://milanuncios.es/..'
            listaItems = []
           # listaItems = procesar_catalogo_mil('https://www.milanuncios.com/venta-de-aticos/?fromSearch=1&dormd=3&banosd=2', listaItems)
            listaItems = procesar_catalogo_mil('https://www.milanuncios.com/venta-de-aticos/?fromSearch=1&dormd=3', listaItems)
            ruta_fichero = grabar_dataframe(listaItems,opcion)
            pintar_grafico(ruta_fichero,opcion)
            print('---------------------------------------------------------------------')
        elif (opcion == "5"):  
            print("%s\nOpcion Elegida -Idealista " %(opcion))
            df_newdata = pd.DataFrame()
            df_newdata = llamada_idealista()
            ruta_fichero = grabar_dataframe(df_newdata,opcion)
            pintar_grafico(ruta_fichero,opcion)
            print('---------------------------------------------------------------------')
        elif (opcion == "6"):  
            print("%s\nOpcion Elegida -SCIMAGO (country ES)" %(opcion))
            #Los vamos a poner ordenados , pero se podria pasar como parametro ascendente..
            req= 'https://www.scimagojr.com/journalrank.php?country=ES&order=sjr&ord=desc'
            i = 1
            datosCSV=[]
            while (i < 13):
                time.sleep(2)
                datos = obtener_datos_scimago(req,str(i),"2018")
                datosCSV += datos
                i +=1
               
            ruta_fichero = grabar_fichero_csv(datosCSV,opcion)
            pintar_grafico(ruta_fichero,opcion)
            print('---------------------------------------------------------------------')
        elif (opcion == "exit"):
            return
        else:      
            print("%s\nOpcion Elegida - Nº de OPCION NO DISPONIBLE" %(opcion))
           # menu_scrapy()
    except ValueError:
        raise SystemExit('Error al introducir opcion')
    return

print('------------------------------------------------------------')
menu_scrapy ()
print('---------------------------------------------------------------------')