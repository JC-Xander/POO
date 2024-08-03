```
░██████╗███████╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░░█████╗░
██╔════╝██╔════╝████╗░████║██╔══██╗████╗░██║██╔══██╗░██╔══██╗
╚█████╗░█████╗░░██╔████╔██║███████║██╔██╗██║███████║░╚█████╔╝
░╚═══██╗██╔══╝░░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║░██╔══██╗
██████╔╝███████╗██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║░╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░╚════╝░
```

@author: J-Xander<br>
@version: 1.0.0<br>
@since:  2024/07/27

## Documentación
Existen archivos con extencion xml y json los cuales sirven para almacenar informacion de jorma jerarquica 
```xml
<Persona>
    <nombre>

    </nombre>
</Persona>
```
Lo que se requiere es captura estos archivos y poder iterarlos

y para pode hacerlo python ya nos efrece ciertas librerias
```py
import json  # Convierte archivo json
import xml.etree.cElementTree # Combierte los archivos json en arboles de busqueda
```
