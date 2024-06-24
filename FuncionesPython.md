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

### Manejar archivos
- open(@Ruta:str) 
Habre el archivo y crea un flujo de texto o byte(Nos pemite ingresar una ruta relativa o absoluta) pero lo habre en modo de lectura y no s puede modificar pero podemos alladir otra variable que nos permite hacer mas cosas

- 'r' = read: Permite abrir y leer
- 'w' = write: elimina todo lo que habia en el documento y escribe lo nuevo
- 'a' = append: Añade en la ultima linea del documento

file.close()
Cierra el archivo que hemos abierto

file.read(@num)
Lee los primeros @num caracteres, si no especificamos @num, leera todo el documento.

readline(@size:num)
Lee toda la linea o hasta que encuentre EOF(final del archivo) Solo lee 1 linea y @size no permite seleccionar n caracteres de cada linea

readlines()
Lee todas las linea y las retorna en un arreglo con cada linea

Todos los read funcionan con punteros 

Nota: Si trabajamos en vinario tenemos que añadirle +b al parametro
## Funciones str

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

## Modulos
### math
import math
Para utilizarlas hay que importar un modulo con
En este modulo encontraremos todo tipo de funciones matematicas.

math.log10(@num) -> float
retorna el log base 10 de un numero

math.pi -> float
retorna el numero pi

math.sqrt(@num) -> float
Permite encontrar la raiz cuadrada de un numero,

---
### random
import random

random.random() -> float
imprime numero de [0,1)

random.randint(@int1, @int2) -> int
retorna un numero ente @int1 y @int2(incluyendolos)

random.choice(@Array)
Escoge un elemento aleatorio del @Array













