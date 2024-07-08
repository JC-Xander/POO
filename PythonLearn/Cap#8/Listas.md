```
██╗░░░░░██╗░██████╗████████╗░█████╗░░██████╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║╚█████╗░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║░╚═══██╗
███████╗██║██████╔╝░░░██║░░░██║░░██║██████╔╝
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░
```

@author: J-Xader<br>
@version: 1.0.0<br>
@since:  2024/07/05

## Resumen
Hay varias formas de crear una nueva lista; la más simple es encerrar los elementos en corchetes (“[" y "]”):

[10, 20, 30, 40]
['rana crujiente', 'vejiga de carnero', 'vómito de alondra']

``` PY
    quesos = ['chedar', 'Edam', 'Gouda']
    numeros = [1, 2, 3, 4]
    vacio = []
    print(quesos, numeros, vacio)
    # Salida :
    # ['chedar', 'Edam', 'Gouda'] [1, 2, 3, 4] []
```
__Las listas son mutables__
___

Para acceder a un elemeto de una lista utilizamos la misma sintaxis para acceder a los elementos de una cadena de caracteres.
```py
    quesos[0] # -> return 'chedar'
```

Al ser mutables podemos cambiar el orden de los elementos y modificarlos.
```py
    numero = [10, 15]
    print(numero[0]) # -> 10
    
    numero[0] = 5
    print(numero[0]) # -> 5
    # A cambiado el valor que almacena
``` 
- Cualquier forma de entero puede ser utilizada como indice
- Si tratas de leer o escribir un elemento que no existe optenemos un `IndexError`
- Si un indice tiene un valor negativo, éste cuenta hacia atrás desde el final de la lista.
- El operador in tambien funciona en las listas

#### Operaciones
Podemos usar los operadores '+'(concatenar), *(Multiplicar) listas
```py
    lista_1 = [1, 2, 3]
    lista_2 = [4, 5, 6]
    lista_3 = lista_1 + lista_3
    print(lista_3) # -> [1, 2, 3, 4, 5, 6]

    print(lista_1 * 2) # -> [1, 2, 3, 1, 2, 3]
```

#### Rebanado de listas
```py
    lista = [1, 2, 3, 4, 5]

    print(lista[:2]) # -> [1, 2]
    print(lista[2:4]) # -> [3, 4]
``` 
#### Listas como Argumentos
Cuando pasas una lista a una función, la función obtiene un apuntador a la lista. Si la función modifica un parámetro de la lista, el código que ha llamado la función también verá el cambio.
```py
    def remover_primero(lista:list):
        del t[0]

    letras = ['a', 'b', 'c']
    remover_primero(letras)
    print(letras) # -> ['b', 'c']
```

Nota: el metodo append() modifica las lista y los operadores crean una nueva lista.

