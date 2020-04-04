# PROJECTS
Proyectos y prácticas uoc
# PRACTICA Nº º 1 - WEB SCRAPING 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3739478.svg)](https://doi.org/10.5281/zenodo.3739478)


Integrantes Practicas : 
- Mº Begona Martinez Arribas
- Silvia Martín Albarrán


Con el fin de probar distintas opciones de juegos de datos y distintos modos de acceso (JSON,API,Beautiful), se ha realizado la practica con un menú en el que se pueden seleccionar varias opciones : 
 
Como primera opcioón: Se ha elegido el conjunto de datos de Agenda Cultural , accesible a través del siguiente enlace:
https://datos.alcobendas.org/dataset/2458d605-1fd0-4d16-a1ef-795bc243e152/resource/90836555-54b5-45af-ae67-e7545937f591/download/recurso.json

Se ha elegido la web de datos abiertos de Alcobendas: https://datos.alcobendas.org/  ya que proporciona  los conjuntos de datos expuestos se ofrecen bajo licencias de propiedad abiertas, que permiten su redistribución, reutilización y aprovechamiento con fines comerciales.

Se van a obtener distintos tipos de campos para poder luego crear un fichero .csv con distintos campos como :
- Temáticas
- Barrio
- Nombre del evento
- Subtemas:
- FechaInicio
- HoraInicio
- FechaFin
- HoraFin
- Tipos
- Perfiles 
- URL_Ficha 

Este dataset ha sido el seleccionado para publicar Zenodo. En este reporitorio se ha subido como pra1_dataset_agenda.csv, dataset que se encuentra en el repositorio de Github. 

 Como segunda opcion: Se ha elegido el conjunto de datos de Cursos de la Comunidad de Madrid también acceso open data 
 https://datos.comunidad.madrid/catalogo/dataset/2347cccf-0cb0-439b-9f99-173cc06be9d3/resource/3e318606-c332-458f-ac3e-cf2721f7f710/download/cursos_formacion_profesional_empleo.json
En dicho enlace se proporcionan los distintos cursos existentes. COmo el juego de datos es elevando. En el programa hemos puesto un corte y solo extraemos unos cuantos cursos para luego que el gráfico utilizado sea sencillo.
Se van a obtener distintos tipos de campos para poder luego crear un fichero .csv con distintos campos como :
 - Descripcion de la Familia 
 - Especialidad_de_certificado 
 - Codigo Postal del centro 
 - Código del curso 
 - A quien va dirigido
 - Municipio del centro
 - Curso Descripcion
 - censo 
 - Telefono del centro
 - Duración Formacion 
 - Sector_desc 
 - Descripcion de la especialidad 
 - Email del centro 
 - Modalidad 
 - Dirección del Centro  
 - Codigo SIE
 - Otra descripcion Especialidad
 - Area
 - Descripcion del centro.
 
 Como tercera opcion: Se ha elegido la pagina de Revistas Cientificas CIRC , para hacer un ejemplo con Beautiful Soup, muy sencillo de una tabla de cuatro campos: 
 https://clasificacioncirc.es/resultados_busqueda?_pag=
 Metemos por parametro el nº de pagina y para no hacerlo que tarde mucho, solo capturaremos en un bucle de 10 paginas.
 - Revista
 - ISSN
 - Clasificacion de Ciencias Sociales 
 - Clasificación de Ciencias Humanas
 
Como cuarta opción: se ha optado por la página web de milanuncios, con objetivo limitado al aprendizaje académico, utilizando la librería de Beutiful Soup en los niveles de anidamiento de la página.
https://www.milanuncios.com/
Se realiza un filtro para el yipo de casuística a seleccionar, en este caso ha sido por tipo de area (Inmobiliaria), tipo de operación dentro de la temática, en el ejemplo ha sido la operación de ventas y tipo de producto, para el caso tratado han sido áticos, además se ha incluido una característica de estos (3 dormitorios). La búsqueda se acota a un número de páginas.
Los datos recuperados para llevar a fichero son: titulo del inmueble, precio, ubicación, descripción y estadísticas de veces anunciado.
 
Como quinta opción: se eligió el portal inmobiliario de idealista.
Pagina web https://www.idealista.com/. El acceso a los datos que proporcionan se realiza a través de OAuth 2.0 previa autorización y tras la recepción de la API key.
Se recoge el elemento completo contenedor de todos los campos que trata la API para llevar a un fichero .csv sobre el que se realiza una visualización de una agrupación básica. El juego de datos es suficientemente extenso para y de diferentes tipologías para realizar análiticas que entendemos quedan fuera de esta práctica. 

Como sexta opcion: Se ha elegido la pagina de Revistas SCIMAGO, que hay un ranking de las revistas por impacto y si se citan en otros documentos etc.. . En este caso , se han capturado todos los campos que se muestran en el listado y todas las paginas de las revistas del pais ESPAÑA

https://www.scimagojr.com/journalrank.php?country=ES&order=sjr&ord=desc
Pero en este caso, se pasará la pagina y el año en la peticion para filtrar. 
- Number - Nº del registro en la tabla
- Title - Título de la revista/conferencia etc
- Type - Tipología de si es artículo/conferencia etc
- SJR - SCImago Journal Rank. Según se indica en la página web, este índice expresa la media de las  referencias (con un peso) recibidas en el año seleccionado por los documentos publicados en dicho periodico en los tres años anteriores 
Es un índice de cuánto puede impactar
- H index - The h index indica el nº de artículos   del periodico que ha recibido al menos h referencias/citaciones .Esto cuantifica la productividad y el impacto científico 
- Total Docs. (2018) - Nº de documentos de periodo seleccionado, incluidos los que se referencian/citan y los que no.
- Total Docs (3 years) - Nº de documentos publicados en los tres años anteriores ( los documentos del año seleccionado se excluyen). Se indican los nº de documentos totales, los que se referencias y los que no.
- Total Refs. (2018) Indica todas las referencias bibliográficas del periodico en el periodico seleccionado (en este caso 2018)
- Total Cites (3years) - Nº de citaciones recibidas en el año seleccionado por un periodico/revista de los documentos publicados en los 3 años anteriores. 
- Citable Docs. (3years) - Nº de documentos citados publicados por una revista en los tres últimos años anteriores(Los del este año seleccionado son excluidos).  Se tiene en cuenta : artículos, reviews, y papeles de la conferencias.
- Cites / Doc. (2years) - Promedio de citas por documento en un período de 2 años. Se calcula considerando el número de citas recibidas por una revista en el año en curso a los documentos publicados en los dos años anteriores, es decir. citas recibidas en el año X a documentos publicados en los años X-1 y X-2.
- Ref. / Doc. (2018) - Nº medio de referencias por documento en el año seleccionado


