# Escribe un programa que lea un archivo e imprima su contenido (línea por línea), todo en mayúsculas. Al ejecutar el programa, debería parecerse a esto:

# python shout.py
# Ingresa un nombre de archivo: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500


file_name = input('Ingrese el nombre del archivo: ')


try:
    with open(file_name) as file:
        for _ in range(5):
            print(file.readline(), end='')
except FileNotFoundError:
    print('El archivo ingresado no existe')


