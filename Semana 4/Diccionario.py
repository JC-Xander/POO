# Generar un diccioneario vacio
paises = dict()
# o
paises = () # Si contiene un dato se convierte en set
    
# Con elementos
paises = {"HN": "Honduras", "MX": "Mexico"}
# {"Clave": "Valor"}
# El primer elemento es es un key, tiene que ser unico y ser un objeto inmutable.

# Editar un elemento
paises["HN"] # Accediento al valor con la clave "HN"
# Si la clave no exite retorn un error: keyError
