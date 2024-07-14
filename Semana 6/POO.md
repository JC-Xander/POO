```
╔═══╗──────────╔╗──────────╔╗─╔╦════╦═╗╔═╦╗
║╔═╗║──────────║║──────────║║─║║╔╗╔╗║║╚╝║║║
║╚══╦══╦═╦╗╔╦╦═╝╠══╦═╦══╦══╣╚═╝╠╝║║╚╣╔╗╔╗║║
╚══╗║║═╣╔╣╚╝╠╣╔╗║╔╗║╔╣║═╣══╣╔═╗║─║║─║║║║║║║─╔╗
║╚═╝║║═╣║╚╗╔╣║╚╝║╚╝║║║║═ ══║║─║║─║║─║║║║║║╚═╝║
╚═══╩══╩╝─╚╝╚╩══╩══╩╝╚══╩══╩╝─╚╝─╚╝─╚╝╚╝╚╩═══╝
```

@author: J-Xander<br>
@version: 1.0.0<br>
@since:  2024/07/13

## Documentación
Nos conectamos en la ip de nuestro servidor en caso de nuestra maquina sera LocalHost(127.0.0.1)

- Podemos utilizar el comando `ping @dominio` para conocer la ip asociada al dominio o URL.

si queremos conectarnos a un servidor utilizaremos un puerto usualmente utilizamos el puerto 80

[Información de los puertos](https://www.stationx.net/common-ports-cheat-sheet/)

- Usualmente los datos se envian de forma cifrada. ya que puede haber un intermediario que intercepte la información.

- Enviar: f"GET {URL} HTTP/1.0\r\n\r\n".encode()
GET -> Pide datos, a la URL y mediante el socked podemos hacer una conexión con el puerto y especificar el protocolo con HTTP/@1.0 

Ejemplo de como se veria el GET
```
GET http://unah.edu.hn http/1.0


```
Cuano utilizamos el get tambien enviamos datos extras como por ejemplo el usario y luego el servidor envia datos

A la hora de recibir los datos podemos utilizar un bucle que y con el socked podemos leer n cantidad de bytes en cada siclo, y cuando sece el envio de información cierra el bucle

y luego el socked se cierra.
```py
misock.close()
```

### Clases
- self indica la misma clase, es como el this en Java

- Comando para encontrar la IP

### BeautifulSoup
Tolera código HTML bastante defectuoso y aún así te deja extraer los datos que necesitas
- No esta en la libreria estandar de python pero podemos descargar el modulo desde:
[Modulos de terceros](https://packaging.python.org/tutorials/installing-packages/)

Como instalar un paquete
- los buscamos y tenemos que ejecutar el comando de instalación.

Podemos crear un contenedor para instalar versiones y modulos de python, tambien podemos instalarlo de forma global pero puede generar fallos en otros dispositivos

