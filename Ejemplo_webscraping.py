


#importamos las librerías que necesitamos para hacer web scrapping
import requests
from bs4 import BeautifulSoup
import time
import seaborn as sns

def procesarPagina(url):

            # se accede a la url de cada item
            r2 = requests.get(url)
        
            # se comprueba que terminó correctamente y se recoge 
            # en objeto beautifulsoup
            if r2.status_code == requests.codes.ok:
                soup2 = BeautifulSoup(r2.text)
            
                return obtienedatos(soup2, url)
        
               

def obtienedatos(html, url=""):

    item = {}
    province = ' '
    
    #nombre item
    title = html.find('h1', class_='ad-detail-title')
    if title:
           title = title.text
           item['title'] = title
    #else:
    #       item['title'] = ' '
    
    # precio item
    price = html.find('div', class_='pagAnuPrecioTexto')
    if price:
            price = price.text
            price = price.replace('€', '').replace('.', '')
            price = int(price)
            item['price'] = price
    #else:
    #        item['price'] = ' '
            
    # tamaño item
    m2 = html.find('div', class_='m2 tag-mobile')
    if m2:
        m2 = m2.text
        item['m2'] = m2
    #else:
    #    item['m2'] = ' '  
        
    # ubicación item
    location = html.find('div', class_='pagAnuCatLoc')
    if location:
        location = location.text
        location = location.replace('M&AACUTE;LAGA', 'MALAGA')        
        province=location.split('(')
        province = province [1]
        province = province.replace(')', ' ')
        item['location'] = location
        item['province'] = province
    #else:
    #    item['location'] = ' '
    
    # descripción item
    description = html.find('p', class_='pagAnuCuerpoAnu')
    if description:
        description = description.text
        item['description'] = description
    #else:
    #    item['description'] = ' '
    
    times = html.find('div', class_='pagAnuStatsData')
    if times:
            times = times.text
            times = int(times)
            item['times'] = times
    
       
    return item

        #with open('salida.txt', 'at') as f_salida:
        #    f_salida.write(title + '\n')
        
        
            
def procesarcatalogo(url, itemList):  
 
   #peticion a la pagina web, filtramos por inmobiliaria, ventas, aticos con 3 dormitorios y 2 baños
   #r = requests.get('https://www.milanuncios.com/venta-de-aticos/?dormd=3&banosd=2&pagina=1')
     r = requests.get(url)
    #comprobamos terminación correcta y pasamos contenido web a objeto 
    #beautifulsoup 
     if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text)
        
    #procesamos pagina
    #obtenemos total paginas y pasamos a numérico
     pages = int(soup.find('div', class_='adlist-paginator-summary').text.split()[-1])

    #vamos recorriendo por páginas   
    #for i in range(1, pages+1):
     for i in range(1, 3):

        r = requests.get(url + str(i))

        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text)

       # se buscan todos los item dentro de una pagina        
        ads = soup.find_all('div', class_="aditem")
       #por cada item se obtiene su nombre y su url para hacer petición
       #sobre el detalle de cada item   
        for ad in ads:
        
            # se obtiene la url de cada item
            a_title = ad.find('a', class_='aditem-detail-title')
            complete_url = url + a_title['href']
            itemList.append(procesarPagina(complete_url))
            
#time.sleep(5)



listaItems = []

procesarcatalogo('https://www.milanuncios.com/venta-de-aticos/?dormd=3&banosd=2&pagina=1', listaItems)




listaItems



import pandas as pd
df = pd.DataFrame(listaItems)
df.to_csv("listaItems.csv", sep=";", index=False)
df





df_listaItems = pd.read_csv('/Users/begomartinez/listaItems.csv',sep=';' )




df_listaItems




df_listaItems.dropna()




#obtenemos la provincia con más venta de áticos
plot = df_listaItems['province'].value_counts().plot(kind='bar',
                                            title='Agrupados por provincia')




price_mean =  pd.DataFrame((df_listaItems['price']).groupby(df['province']).mean())





df_price_mean = price_mean



df_price_mean



province = df_price_mean.index
price = df_price_mean['price']




sns.barplot(x=df_price_mean.index, y="price", data=df_price_mean)







