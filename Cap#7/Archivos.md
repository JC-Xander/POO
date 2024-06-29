# Archivos
## Persistencis
Alamcenar archivos en la memoria secundaria, para que estos datos no se pierdan a la hora de finalizar el programa

## Abrir Archivos
```py
File = open('@ruta') # Nos permite abrir un archivo.
```
Si el open es exitoso, el sistema operativo nos devuelve un manejador de archivo. El manejador de archivo no son los datos contenidos en el archivo, sino un “manejador” (handler) que podemos usar para leer los datos. Obtendrás un manejador de archivo si el archivo solicitado existe y si tienes los permisos apropiados para leerlo.

## Lectura de Archivos
Podemos leer linea por linea de un archivo con un siclo for, Cuando el archivo es leído usando un bucle for de esta manera, Python se encarga de dividir los datos del archivo en líneas separadas utilizando el separador de línea. Python lee cada línea hasta el separador e incluye el separador como el último carácter en la variable line para cada iteración del bucle for.

Con el metodo read() podemos almacenar todo el contenido del archivo en una variable como una enorme cadena de texto, esto solo es recomendable hacerlo si la cantidad de datos son apropiados para la memoria principal.

 y con len(@file) podemos saber el numero de caracteres del archivo.