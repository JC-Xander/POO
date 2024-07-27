```
░██████╗███████╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░███████╗
██╔════╝██╔════╝████╗░████║██╔══██╗████╗░██║██╔══██╗░╚════██║
╚█████╗░█████╗░░██╔████╔██║███████║██╔██╗██║███████║░░░░░██╔╝
░╚═══██╗██╔══╝░░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║░░░░██╔╝░
██████╔╝███████╗██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║░░░██╔╝░░
╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░
```

@author: J-Xander<br>
@version: 1.0.0<br>
@since:  2024/07/20

## Documentación
### Resumen de Redes
- __Socket__: No permite conectar una pc con otro.
- Nos permite hacer peticiones TCP/IP, UPD
Nota: Esto es un proceso muy basico.
- Puertos usuales:
    - 443 https
    - 20 FTP
    - 3306 MySQL
Al conectarse al servidos se debe conocer la IP y el puerto de conexión. 

- __urllib__: Se conecta mediante HTTP la cual es una capa superior a los socket.

### Implementar nuevos modulos
Podemos instalar modulos en python por ejemplo:
- __beautifulSoap__
Los cuales los encontraremos en la web. Python nos ofrese un sitio en el cual se almacenas miles de modulos los cuales podemos exportar a nuestros proyectos.

Pero puede resultar complicado instalar modulos de forma global ya que aveces solo oacupamos estos importaciones para un proyecto en especifico por los cual haremos un entorno aislado en el cual instalaremos los nuevos modulos y las importaciones solo existiran en ese entorno al que llaman Maquina virtual.

### Ver los datos de nuestro entrono virtual
```sh
    pip > freeze > requirements.txt
```
Permite almacenar en un archivo .txt todos los modulos instalados en nuestra maquina virtual.

### Instalacón
```sh
    pip install -r equirements.txt
```
Nota: Si no especificamos la versión siempre se instalara la mas resiente.
