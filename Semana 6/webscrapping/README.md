```
╔═╗╔═╗────╔╗──╔╗───────────╔╗──────╔╗
║║╚╝║║────║║──║║──────────╔╝╚╗─────║║
║╔╗╔╗╠══╦═╝╠╗╔╣║╔══╗╔╗╔╦╦═╬╗╔╬╗╔╦══╣║
║║║║║║╔╗║╔╗║║║║║║╔╗║║╚╝╠╣╔╝║║║║║║╔╗║║
║║║║║║╚╝║╚╝║╚╝║╚╣╚╝║╚╗╔╣║║─║╚╣╚╝║╔╗║╚╗
╚╝╚╝╚╩══╩══╩══╩═╩══╝─╚╝╚╩╝─╚═╩══╩╝╚╩═╝
```

@author: J-Xander<br>
@version: 1.0.0<br>
@since:  2024/07/13

# Documentación
### Creación de un modulo virtual
Exlicare 2 formas de crear un entorno virtual:

#### venv
si contamos con una version de pyton superior a 3.3 (Nota: podremos saber la version de nuestro python con el comando `python`) podremos usar este metodo de los contrario tendra que utilizar el otro metodo: virtualenvc.

Si nuestro la version de nuestro python es superior a la 3.3 ejecutaremos lo siguiente:
```sh
python  -m venv [@nombre_del_folder]
```
-  __Activación__
```sh
# --- Linux ---
source [@Nombre_del_folder]/bin/activate
#Si el archivo no tiene permisos ejecutamos
chmod +x [@Nombre_del_folde]/bin/activate

# --- Windows ----
.\[@nombre_del_folder]\Scripts\activate
```

- __Desactivar el entorno__
```sh
deactivate
```

#### virtualenv
Para crear un entorno virtual en Python usando virtualenv y especificar el nombre de la carpeta, puedes seguir estos pasos:

- __Instalar virtualenv (si no lo tienes instalado):__
```sh
# - linux -
pip install virtualenv

# si no tienes el comando pip deberar instalarlo
sudo apt install pip # Linux

# en windows deberas buscar el instalar en linea
```

- __Crear el entorno virtual:__
```sh
virtualenv [@nombre_del_folder]
# Por ejemplo, si quieres crear un entorno virtual 
# en una carpeta llamada EntornoVirtual, usarías:
virtualenv EntornoVirtual
```
- __Activar el entorno virtual__
    - Linux:
    ```sh
    # Hay que darle permiso de ejecucion al script
    chmod +x [@nombre_del_folder]/bin/activate

    # Activamos el entorno
    source [@nombre_del_folder]/bin/activate
    ```

    - windows:
    ```sh
    .\[@nombre_del_folder]\Scripts\activate
    ```

- __Desactivar el entorno__
```sh
deactivate
```






