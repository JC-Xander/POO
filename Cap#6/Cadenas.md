# Cadenas
Una Cadena es una sentencia de caracteres. Puedes acceder a los caracteres con el operador corchete.<br>
Alternativamente, puedes usar índices negativos, los cuales cuentan hacia atrás desde el final de la cadena.

El operador [n:m] retorna la parte de la cadena desde el “n-ésimo” carácter hasta el “m-ésimo” carácter, incluyendo el primero pero excluyendo el último.

Si omites el primer índice (antes de los dos puntos), el rebanado comienza desde el inicio de la cadena. Si omites el segundo índice, el rebanado va hasta el final de la cadena.

Si el primer índice es mayor que o igual que el segundo, el resultado es una cadena vacía, representado por dos comillas

las cadenas son inmutables, lo cual significa que no puedes modificar una cadena existent.

## IN
La palabra in es un operador booleano que toma dos cadenas y regresa True si la primera cadena aparece como una subcadena de la segunda

Podemos usar los comparadores `< >` para ordenar paralabras en orden alfabetico