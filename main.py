
from src.src import *

#web_search ('x,y,z') con esta funcion que he hecho en otro file logre hacer un buscador
# x= 'url', y='xpath', z='tag'
#web_find_link(x,y,z) con esta funcion como la otra me devuelve el texto esta hice que me buscara el href de un id(links)
#clean_list limpia una lista pero es muy especifico puede ser que borre esta funcion 

#OJO ya que la pagina se actualiza dependiendo de la hora y de que esta abierto se tendra que actualizar el xpath y tag que buscas 

#fui tonto y hice que la funcion de agarrar la data de uina pagina lo corriera por dato que quiero en vez de pedir que baje la pagina como html y hacer un soup de la info que queria o lammar una vez el drive y guardar toda las lista que queria y luego hacer un quit
# lo bueno de hacerlo asi es que poco a poco puedo ir construyendo con la info que quiero viendo que esta pasando y entiendo donde esta el fallo


col1= web_find('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div', 'h3.card-title')
col1= col1[0:10]
df= pd.DataFrame (col1, columns = ['Name Of Restaurantes'])


#esta columna esta propensa a dar datos mal limpiados porque cambia mucho
x= web_find_class('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div/main/div[2]', 'flex')
col2 =clean_list(x)
col2=col2[0:10] # para asegurar que los valores esten bien y pueda agregar column a columna
df['Category'] = col2

col3= web_find('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div/main/div[2]/div/div','span.store-card-rating-info__rating')
df['Rating'] = col3[0:10]

col4= web_find_link('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div/main/div[2]/div','a')
df['Links'] = col4[0:10]

col5=[]
for el in col4[0:10]:
    fr= web_find(el,'//*[@id="default-wrapper"]/div/section/div[3]/div','div.service-fee__label.dark-text')
    col5.append(fr)


#lst_df=Parallel(n_jobs=8, verbose=True)(delayed(extraer)(url) for url in equipos_stats_urls[:2])

df['Price of delivery'] = col5[0:10]

#falta limpiar 

df2= pd.read_csv("data\FOOD_DELV.csv")
#cambiar la columna Average order value a un numero usable sino drop it 
#quizas cambiar el nombre de las columnas
#reordenar



rss_bon= rss('https://www.bonappetit.com/feed/rss')
x= rss_bon['entries']
df3= pd.DataFrame(x)
df3= df3.drop(labels=['title_detail','links','id','guidislink','published_parsed','published_parsed','media_content','summary_detail','tags', 'authors', 'author_detail','publisher_detail','media_thumbnail'], axis=1)

# Ya tengo 3 dataframes creado (df2) que es un csv, (df) que es un web scraping con selenium, (df3) que es un rss
#cree una funcion para salvar los tres si quiero actiualizar la base de dato

#save_csv(df,df2,df3) #quitar comentariuo para ejecutar

#creo una funcion para comunicarme con mysql : connect_mysql_cursor_execute("x")
#donde x es el comando que quiero ejecutar

#connect_mysql_cursor_execute("CREATE DATABASE proyect_semana_4_ETL") #quitar comentariuo para ejecutar

#creo una funcion para pasar el df al sql
#cada vez que ejecuto este codigo actualiza la tabla
connect_mysql_cursor_execute_tables_motor( df, df2, df3)

