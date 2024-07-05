# Cadenas
Una Cadena es una sentencia de caracteres. Puedes acceder a los caracteres con el operador corchete.<br>
Alternativamente, puedes usar índices negativos, los cuales cuentan hacia atrás desde el final de la cadena.

El operador [n:m] retorna la parte de la cadena desde el “n-ésimo” carácter hasta el “m-ésimo” carácter, incluyendo el primero pero excluyendo el último.

Si omites el primer índice (antes de los dos puntos), el rebanado comienza desde el inicio de la cadena. Si omites el segundo índice, el rebanado va hasta el final de la cadena.

Si el primer índice es mayor que o igual que el segundo, el resultado es una cadena vacía, representado por dos comillas

las cadenas son inmutables, lo cual significa que no puedes modificar una cadena existent.

## IN
La palabra in es un operador booleano que toma dos cadenas y regresa True si la primera cadena aparece como una subcadena de la segunda

Podemos usar los comparadores `< >` para ver que paralabras esta antes que otra en orden alfabetico
Nota: Las mayusculas va antes de cualquier minuscula por ejemplo Z < a -> True

## Operador Formato
`%` En numero este es el operador modulo pero en cadenas se utiliza para crear cadenas con formto<br>
```py
    num1 = 42
    num2 = 50

    print('%d' % num1)
    print('%d %d' % (num1, num2))
```

%d : Enteros
%s : Cadenara
%g : Escribe el numero en notación cientifica si es muy grande de lo contrario lo escribe normal
%f : Flotante, Podemos añadir un .@int antes del f para indicar la cantidad de decimales que queremos que se impriman
```py
    num = 11.025555
    print(%.2f % num) # -> 11.02
```

