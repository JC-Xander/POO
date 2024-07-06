```
╔════╗─────╔╗
║╔╗╔╗║─────║║
╚╝║║╚╬╗╔╦══╣║╔══╗
──║║─║║║║╔╗║║║╔╗║
──║║─║╚╝║╚╝║╚╣╔╗║
──╚╝─╚══╣╔═╩═╩╝╚╝
────────║║
────────╚╝
```

@author: jeancarlosmaradiaga@unah.hn<br>
@version: 1.0.0<br>
@since:  2024/07/06

Funciona igual que las listas pero tiene una diferencia es inmutable, una vez definidos sus elementos no podemos modificarlos
- Listas: [] ->  list() ------------ [1,2,3]
- Diccionario: {} -> dict() -- {'a' : 1, 'b' : 2}
- set: -> set() ------------------ {1, 2, 3}
- tupla: -> tuple() ------------ (1,)   -   (1,2)
    - No existen las tuplas vacias
    - y si solo tiene un elemento se pone ',' despues de elemento
    - No se pueden modificar los datos.
    - listar elemento es mas rapido en una tupla que una lista
    - podemos omitir los parentesis
        - (1,) o 1,
    - Accedemos a ellas con []
        - t[0] - t[1]
    - (a,b) = (10,20): a -> 10 | b -> 20
    - No es permitido x[0] = 10, ya que es imnutable
    - pero si el elemento que almacena es mutable podemos modificar los valores del elemento.
    - Contiene los metodos
        - count(aparicion de un elemento en una tupla)
        - index(Buscar el elemento x en la tupla)
        
