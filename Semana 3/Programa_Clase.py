# Ciudad [TGU, SPS, CBA]
# Dia: 
# Mes: 
# Venta: 
# -> Todo se guardara en un archivo (archivo.txt)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def pedirDia() -> int:
    dia = input("Ingrese el día: ")
    try:
        if 0 < int(dia) <= 30:
            return dia
        else:
            print("Ingrese un dia entre 1 y 30")
            return pedirDia()
    except ValueError:
        print("Dato no valido")
        return pedirDia()


def pedirMes() -> str:
    mes = input("Ingrese el mes: ")
    if (mes.capitalize()) in meses:
        return mes
    else:
        print(meses)
        print("Ingrese un mes valido")
        return pedirMes()
    


newFile = open("archivo.txt", "a")

with open("archivo.txt", "r") as file:
    contenido = file.read()

if not contenido:
    newFile.write(f'|{"Ciudad".center(15)}|{"Fecha".center(15)}|{"Ventas".center(10)}|\n')

while(True):
    ciudad = input("Ingrese la ciudad: ")
    dia = pedirDia()
    mes = pedirMes()
    ventas = input("Ingrese el total ventas: ")


    fecha = f'{dia}/{mes}'
    newFile.write(f"|{ciudad.center(15)}|{fecha.center(15)}|${ventas.center(9)}|\n")

    if input("Desea ingresar otro dato?\n[S=si][N=no\n>>").lower() != "s":
        break;

newFile.close()