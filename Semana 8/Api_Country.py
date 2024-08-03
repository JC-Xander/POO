import urllib.request
import json
import ssl

# Ignorar errores de certificado
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_Api_nationalice = 'https://api.nationalize.io/?name='
name = input('Ingrese el nombre: ').strip();
url_Api_nationalice += name

json_Api_nationalice = urllib.request.urlopen(url_Api_nationalice, context=ctx).read()
Data_nationalice = json.loads(json_Api_nationalice)
if (len(Data_nationalice['country'])):
    Country_Probability = Data_nationalice['country'][0]['country_id']


    url_Api_countrie = "https://restcountries.com/v3.1/alpha/" + Country_Probability;
    json_Api_countrie = urllib.request.urlopen(url_Api_countrie, context=ctx).read()
    Data_county = json.loads(json_Api_countrie)

    Country = Data_county[0]['name']['common']

    print("El nombre:",name," Tiene mayor probabilidad de ser de nacionalidad:",Country)
else:
    print("No se encontraron datos");

