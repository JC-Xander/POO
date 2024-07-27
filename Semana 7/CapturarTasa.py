from bs4 import BeautifulSoup
from urllib import request
import ssl
import datetime

#ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Una variable que no se deberia modificar se escribe mayuscula
SERVICIO = 'https://www.bancatlan.hn/'

html = request.urlopen(SERVICIO, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
p_dolar = sopa.find('p', {'id' : 'moneda_dolar'})

dia = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

txt = p_dolar.text
lista = txt.split(' | ')

with open('Tasa de Cambio.txt', mode='a') as file:
    file.write(dia + '\n')
    file.write(lista[0] + '\n')
    file.write(lista[1] + '\n')
    file.write('========================\n')

