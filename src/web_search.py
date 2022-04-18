import time
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bsoup
import requests as req
import pandas as pd
import feedparser
import mysql.connector 
import mysql.connector
from sqlalchemy import create_engine
import multiprocessing as mp

def web_search(url):    
  
    opciones=Options()

    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
    opciones.add_argument('--start-maximized')         # comienza maximizado
    opciones.add_argument("user-data-dir=C:\environments\selenium")    # mantiene las cookies
    opciones.add_argument('--incognito')

    PATH=ChromeDriverManager().install()

    def google(url):
        driver=webdriver.Chrome(PATH, options = opciones)
        driver.get(url)
        time.sleep(2)
        

    return google(url)

def web_find(x,y,z):

    opciones=Options()

    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
    opciones.add_argument('--start-maximized')         # comienza maximizado
    opciones.add_argument("user-data-dir=C:\environments\selenium")    # mantiene las cookies
    opciones.add_argument('--incognito')

    PATH=ChromeDriverManager().install()
    
    def find(x,y,z):
        
        driver=webdriver.Chrome(PATH, options = opciones)
        driver.get(x)
        h1= driver.find_element_by_xpath(y)
        h2= h1.find_elements_by_tag_name(z)
        h2= [i.text for i in h2]
        time.sleep(2)
        return h2

    return find(x,y,z)

def web_find_class(x,y,z):

    opciones=Options()

    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
    opciones.add_argument('--start-maximized')         # comienza maximizado
    opciones.add_argument("user-data-dir=C:\environments\selenium")    # mantiene las cookies
    opciones.add_argument('--incognito')

    PATH=ChromeDriverManager().install()
    
    def find(x,y,z):
        
        driver=webdriver.Chrome(PATH, options = opciones)
        driver.get(x)
        h1= driver.find_element_by_xpath(y)
        h2= h1.find_elements_by_class_name(z)
        h2= [i.text for i in h2]
        time.sleep(2)
        return h2

    return find(x,y,z)
# ojo que es para limpiar solo un dato 'categorias'
def clean_list(x):
    y= x[::3]
    return y
#get links

def web_find_link(x,y,z):

    opciones=Options()

    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
    opciones.add_argument('--start-maximized')         # comienza maximizado
    opciones.add_argument("user-data-dir=C:\environments\selenium")    # mantiene las cookies
    opciones.add_argument('--incognito')

    PATH=ChromeDriverManager().install()
    
    def find(x,y,z):
        
        driver=webdriver.Chrome(PATH, options = opciones)
        driver.get(x)
        h1= driver.find_element_by_xpath(y)
        h2= h1.find_elements_by_tag_name(z)
        h3= [i.get_attribute("href") for i in h2]
        time.sleep(2)
        return h3
    return find(x,y,z)

def rss (url):
    x=feedparser.parse(url)
    return x

def connect_mysql_cursor_execute(x):
    db= mysql.connector.connect(host="localhost", user="root", password="password")
    cursor = db.cursor()
    cursor.execute(x)


def save_csv(x,y,z):
    x.to_csv('data\df.csv', sep=',')
    y.to_csv('data\df2.csv', sep=',', index=False)
    z.to_csv('data\df3.csv', sep=',', index=False)

def connect_mysql_cursor_execute_tables_motor(x,y,z):
    str_conn='mysql+pymysql://root:password@localhost:3306/proyect_semana_4_ETL'
    motor=create_engine(str_conn)
    
    x.to_sql(name='rss', con=motor, if_exists='append', index=False)
    y.to_sql(name='csv', con=motor, if_exists='append', index=False)
    z.to_sql(name='selenium', con=motor, if_exists='append', index=False)

