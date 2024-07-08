# Funciones y Metodos en Python

[Documentación Python](https://docs.python.org/library/stdtypes.html#string-methods.)

- __Funciones Productivas:__ Son aquellas que producen un resultado(retorna un valor)
- __Funciones Estériles:__ Son aquellas que realizan una acción pero no devuelven un valor.

## Funciones Internas
type(@variable) -> str
Retorna el tipo de dato que corresponde al parametro enviado.

max(@str)
Devuelve el caracter mayor de toda la cadena

min(@str)
Devuelvce el caracter menor de toda la cadena

int(@var) -> int
Combierte la variable en un entero y lo retorna, si la conversión no es posible salta un ValueError

float(@var) - > float
Combiente la variable a un decimal y lo retorn

str(@var) -> str
Combierte a @var en una varible de tipo str y lo retorna

ord(@str) -> int
Combierte un caracter a codigo ASCII

Python tiene una función llamada dir la cual lista los métodos disponibles para un objeto. La función type muestra el tipo de un objeto y la función dir muestra los métodos disponibles.

exit()
Finaliza el programa.

repr(@str)
Recibe cualquier objeto como argumento y devuelve una representación del objeto como una cadena. En el caso de las cadenas, representa los espacios en blanco con secuencias de barras invertidas.
```py
    s = '1 2\t 3\n 4'
    print(s)
    # 1 2   3
    #  4

    print(repr(s))
    # '1 2\t 3\n 4 '
```

list(@objeto)
Convierte en una lista los elementos del objeto enviado
```py
    cadena = 'Hola'
    lista_cadena = list(cadena)
    print(lista_cadena) # -> ['H', 'o', 'l', 'a']
```


## Manejar archivos
- open(@Ruta:str) 
Habre el archivo y crea un flujo de texto o byte(Nos pemite ingresar una ruta relativa o absoluta) pero lo habre en modo de lectura y no s puede modificar pero podemos alladir otra variable que nos permite hacer mas cosas

- 'r' = read: Permite abrir y leer.
- 'w' = write: permite escribir en el archivo, pero elimina todo lo que habia en el documento y si el documento a abrir no existe lo crea.
- 'a' = append: Añade en la ultima linea del documento.

file.close()
Cierra el archivo que hemos abierto.

file.read(@num)
Lee los primeros @num caracteres, si no especificamos @num, leera todo el documento.

readline(@size:num)
Lee toda la linea o hasta que encuentre EOF(final del archivo) Solo lee 1 linea y @size no permite seleccionar n caracteres de cada linea.

readlines()
Lee todas las linea y las retorna en un arreglo con cada linea.

Todos los read funcionan con punteros .

Nota: Si trabajamos en vinario tenemos que añadirle +b al parametro.
## Funciones str
[String(Metodos)](https://docs.python.org/3/library/stdtypes.html#string-methods)

- @str.lower() -> str<br>
retorna una copia con todos los caracteres en minusculas.

- @str.upper() -str<br> 
retorna una copia con todos los caracteres en mayuscula.

- @str.capitalize() -> str<br>
Retorna una copia con la primera letra en mayuscula y las demas en minuscula.

- @str.count(@Sub_str) -> int<br> 
retorna la cantidad de veces que aparece @Sub_str en una cadena o objeto

- @str.replace(@Replece_str, @New_str) -> str<br>Retorna una copia en la cual remplazara todas las ocurrencia @Replece_str por @New_str

Nota: Podemos añadir un parametro numerico(n) para que el lugar de modificar todas las ocurrencias solo modifique las primeras n<br>
@str.replace(@Replece_str, @New_str, @n_int) -> str

- @str.startswith(@Sub_str) -> bool
Retorna de verdadero si la cadena empieza con Sub_@str

- @str.endswith(@Sub_str) -> bool
Retorn verdadero si la cadena termina con @Sub_str

- @str.index(@Sub_str) -> int
Busca en la cadena la primera coincidencia con @Sub_str y retorna el index de donde fue encontra en @str si no encuentra ninguna coincidencia retornara un ValueError

- @str.center(@int) -> str
devuelve una cadena de tamaño @int y colocara @str justo en el centro y rellenara los que falta para llegar a @int con espacios

- @str.encode()
Devuelve la cadena en binario

- @str.isnumeric()
Retorna verdadero si la cadena se puede convertir a un numero

- @str.isalpha()
comprueba si una cadena está formada solo por letras o no. Si encuentra cualquier otro carácter, como un número o un carácter especial, devuelve False. De lo contrario, para una cadena válida, devuelve True.

- @str.find(@sub:str, @int) -> int
Devuelve el índice más bajo de la cadena en la que se encuentra la subcadena sub la rebanada . Los argumentos opcionales start y end son interpretado como en notación de cortes. Devuelve si no se encuentra sub.s[start:end]-1
Nota:
```py
# El metodo solo debe usarse si se necesita saber la posición de la cadena, 
# para comprobar si es o no es una sub cadena utilizamos el operador:

'py' in 'pyton' # -> True

```
-@str.strip() -> str
Elimina los espacios(espacios, tabs, o nuevas líneas) que se encuentren la principio y al final de la cadena y luego lo retorna.

- @str.count(@sub:str) -> int
retorna las veces que aparace @sub en @str

- @str.isupper() -> bool
Retorna verdadero si todos lo caracteres de la cadena son mayusculas de lo contrario son falsos

- @str.title() -> str
Devuelve un aversion de la cadena donde todos lo caracteres iniciales de cada palabra se convertira en mayuscula

- @str.rstrip() -> str
Retorna una copia de @str Eliminando todos los espacios que encuentre en el lado derecho.

- `@str.join(@list) -> str`:<br>
join es el inverso de split. Este toma una lista de cadenas y concatena los elementos. join es un método de cadenas, así que tienes que invocarlo en el delimitador y pasar la lista como un parámetro
```py
lista = ['H', 'o', 'l', 'a']

union = ''.join(lista)
print(union) # -> 'Hola'

union = '-'.join(lista)
print(union) # -> 'H-o-l-a'
``` 
## Diccionarios
@dict.get('@Key') buscar la @key y devuelve su valor, si no lo encuentra devuelve none.

list(d.keys())
Devuelve una lista con las @keys del diccionario.

list(d.value()) 
Devuelve todos los @values del diccionario

list(d.items()) retorna todos los elementos con sus respectivos llave valor en forma de tuplas()

## Tuplas
- @tupla.index(@x) busca el elemeto x en la tupla.
- @tupla.count(@elemento) Busca un elemento en la tupla.

## Listas
- `@list.append(@NewElemento)`:<br>
Agrega un nuevo elemento al final de la lista

- `@list1.extend(@list2)`: <br>
Toma una lista como argunmento agrega todo sus elementos a @list1 y deja a @list2 sin modificar.

- `@list.sort()`:<br>
Ordena los elementos de la lista de menor a mayor

- `@list.sorted()`:<br>
cumple la misma función que sort() solo que esta no modfica la lista original sino que retorna una nueva listas ordenada de mayor a menor.
 
Nota: la mayoría de metodos no retornan nada, sino que modifican la lista original.

# Modulos
En Python, un módulo es un archivo que contiene definiciones y declaraciones de Python, como funciones, clases, variables, etc. El nombre del archivo es el nombre del módulo con el sufijo .py. Los módulos permiten reutilizar y organizar mejor el código en espacios de nombres. Puedes importar un módulo en otro módulo usando la palabra clave `import @clase`

Si en lugar de importar todo el modulo solo queremos exportar un metodos o constante en especifico podemos utilizar: `from @clase import @name` y podemos cambiar como se llamara el elemento importado con `as`
```py
from match import sqrt as raiz

print(raiz(25)) # -> 5
```
---


## 1. math
__import math__

#### Metodos

- `math.log10(@num) -> float`:<br>
retorna el logaritmo base 10 de @num


- `math.sqrt(@num) -> float`:<br>
Permite encontrar la raiz cuadrada de un numero,

#### Constantes
- `math.pi -> float:`<br>
retorna el numero pi

---
## 2. random
import random

- `random.random() -> float`:<br>
imprime numero de [0,1)

- `random.randint(@int1, @int2) -> int`:<br>
retorna un numero ente @int1 y @int2(incluyendolos)

- `random.choice(@Array) -> element`:<br>
Escoge un elemento aleatorio del @Array




