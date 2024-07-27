# from bs4 import BeautifulSoup # Importando el nuevo modulo instalado

# Programa del libro
import urllib.error
import ssl

def buscar_links(bsoup: BeautifulSoup):
    pass

def buscar_img(bsoup: BeautifulSoup):
    pass

def buscar_encabezado(bsoup: BeautifulSoup):
    div = bsoup.find('div', {'class': 'sb-msg'})
    h4 = div.find("h4")
    p = div.find('p')
    print(h4)
    print('-' * 10)
    print(p)


#ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Ingrese la URL: ')
#html = 


