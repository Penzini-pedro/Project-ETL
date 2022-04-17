import time
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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


