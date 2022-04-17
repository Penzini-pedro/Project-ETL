
import pandas as pd  
from src.web_search import *

df= pd.read_csv("data\FOOD_DELV.csv")
#cambiar la columna Average order value a un numero usable sino drop it 
#quizas cambiar el nombre de las columnas
#reordenar
#creaer table en my servidor 

#print(df.columns)
#web_search ('x,y,z') con esta funcion que he hecho en otro file logre hacer un buscador
# x= 'url', y='xpath', z='tag'
#web_find_link(x,y,z) con esta funcion como la otra me devuelve el texto esta hice que me buscara el href de un id(links)
#clean_list limpia una lista pero es muy especifico puede ser que borre esta funcion 

#OJO ya que la pagina se actualiza dependiendo de la hora y de que esta abierto se tendra que actualizar el xpath y tag que buscas 

#fui tonto y hize que la funcion de cojer la data de uina pagina lo corriera por dato que quiero en vez de pedir que baje la pagina como html y hacer un soup de la info que queria o lammar una vez el drive y guardar toda las lista que queria y luego hacer un quit
# lo bueno de hacerlop asi es que poco a poco puedo ir construyendo con la info que quiero viendo que esta pasando y entiendo donde esta el fallo
'''col1= web_find('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div', 'h3.card-title')
df = pd.DataFrame (col1, columns = ['Name Of Restaurantes'])


#esta columna esta propensa a dar datos mal limpiados porque cambia mucho
x= web_find_class('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div/main/div[2]', 'flex')
col2 =clean_list(x)
col2=col2[0:48] # para asegurar que los valores esten bien y pueda agregar column a columna
df['Category'] = col2

col3= web_find('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div/main/div[2]/div/div','span.store-card-rating-info__rating')
df['Rating'] = col3[0:48]
'''
col4= web_find_link('https://glovoapp.com/es/es/madrid/restaurantes_1/','//*[@id="default-wrapper"]/div/div/div/main/div[2]/div','a')
#df['Links'] = col4[0:48]
#print(df)




col5=[]
for el in col4:
    fr= web_find(el,'//*[@id="default-wrapper"]/div/section/div[3]/div','p.store-info__note')
    col5.append(fr)

print(col5)  