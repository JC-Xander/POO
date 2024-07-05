# Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido 
# hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.

s = 'Esto es una cadena'

cont = 1;
while cont <= len(s):
    print(s[-cont])
    cont += 1

