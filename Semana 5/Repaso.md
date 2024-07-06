```
╔═══╗
║╔═╗║
║╚═╝╠══╦══╦══╦══╦══╗
║╔╗╔╣║═╣╔╗║╔╗║══╣╔╗║
║║║╚╣║═╣╚╝║╔╗╠══║╚╝║
╚╝╚═╩══╣╔═╩╝╚╩══╩══╝
───────║║
───────╚╝
```

@author: jeancarlosmaradiaga@unah.hn<br>
@version: 1.0.0<br>
@since:  2024/07/06

### Listas:
- Pos valor
- No tienen tamaño fijo
- Son heterogeneos
- si el index enviado no existe devuelve IndexError

### Diccionarios
Clave - valor
- Unicos 
    - Clave Unica : La clave no se puede repetir y si se ingresa un elemento con una calve ya existente reescribe el elemento.
    - De tipo inmutable
    - Tiene cierto parecido a los JSON pero  no son lo mismo
    - El value puede ser cualquier objeto, numeros enteros, listas e incluso nuevos diccionarios

```py
 # Los set solo permiten la creación de un elemento individial y se crean de la misma forma.
    Paises = {}
    Paises['Key'] # buscando la clave y si existe devuelve el valor, si no existe devuelve un KeyError 

    Paises['NewKey'] = 'Value' # si lo hacemos de esta forma si la llave existe reescribe el valor de los contrario creara una nueva (NewKey : Value) en el diccionario.

    paises.get('Key') # Si lon encuentra devuelve el value de lo contrario devuelve None por defecto o podemos indicar que queremos que retorne
    Paises.get('Key', []) # devuelve una lista vacia si no encuentra la key
```


   

