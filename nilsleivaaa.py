tareas = []

def mostrarmenu():
    print("\n===MENU PRINCIPAL===")
    print("1- Agregar Tarea")
    print("2- Buscar Tarea")
    print("3- Eliminar Tarea")
    print("4- Actualizar Estado")
    print("5- Mostrar Tareas")
    print("6- Salir")
    print("======================")


def leeropcion():
    try:
        opcion = int(input("Seleccione una opcion: "))
        if opcion < 1 or opcion > 6:
            print("Opcion invalida. Ingrese un numero entre 1 y 6")
            return None
        return opcion
    except ValueError:
        print("Opcion invalida. Ingrese un numero entre 1 y 6")
        return None

def validartiempo(tiemposs):
    try:
        tiempo = float(tiemposs)
        return tiempo > 0
    except ValueError:
        return False


def validardescripcion(descripcion):
    return descripcion.strip() != ""


def validaprioridad(prioridadd):
    try:
        prioridad = int(prioridadd)
        return 1 <= prioridad <= 10
    except ValueError:
        return False


def agregartarea(lista):
    descripcion = input("Describe la tarea: ")
    prioridadd = input("Prioridad (del 1 al 10): ")
    tiemposs = input("Tiempo estimado (horas): ")
    
    if not validardescripcion(descripcion):
        print("Error! La descripcion no puede estar vacia ")
        return
    if not validaprioridad(prioridadd):
        print("La prioridad debe estar entre 1 y 10")
        return
    if not validartiempo(tiemposs):
        print("Error! El tiempo estimado debe ser un numero decimal mayor que cero")
        return

    tarea = {
        "descripcion": descripcion.strip(),
        "tiempo_estimado": float(tiemposs),
        "prioridad": int(prioridadd),
        "completada": False 
    }
    lista.append(tarea)
    print("Tarea agregada con exito ")

def buscartarea(lista, descripcion):
    for i, tarea in enumerate(lista):
        if tarea["descripcion"] == descripcion:
            return i
    return -1
    
def eliminartarea(lista):
    descripcion = input("descripcion de tarea que desea eliminar: ")
    posicion = buscartarea(lista, descripcion)
    if posicion != -1: 
        lista.pop(posicion)
        print("Tarea eliminada con exito")
    else:
        print(f"La tarea '{descripcion}' no se encuentra registrada")

def actualizarestado(lista):
    for tarea in lista:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False

def mostrartareas(lista):
    actualizarestado(lista)
    print("\n==LISTA DE TAREAS==")
    for tarea in lista:
        estado = "COMPLETADA" if tarea["completada"] else "PENDIENTE"
        print(f"descripcion: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
        print(f"Estado: {estado}")
        print("*" * 44)


def opcionbuscar(lista):
    descripcion = input("Descripcion de la tarea a buscar: ")
    posicion = buscartarea(lista, descripcion)
    if posicion != -1:
        tarea = lista[posicion]
        estado = "COMPLETADA" if tarea["completada"] else "PENDIENTE"
        print(f"Tarea encontrada en la posicion {posicion}: ")
        print(f"descripcion: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
        print(f"Estado: {estado}")
    else:
        print("No se encontro ninguna tarea con la descripcion")

while True: 
    mostrarmenu()
    opcion = leeropcion()
    if opcion is None:
        continue
    if opcion == 1:
        agregartarea(tareas)
    elif opcion == 2:
        opcionbuscar(tareas)
    elif opcion == 3:
        eliminartarea(tareas)
    elif opcion == 4:
        actualizarestado(tareas)
        print("Estado de todas la tareas actualizado")
    elif opcion == 5:
        mostrartareas(tareas)
    elif opcion == 6:
        print("Gracias por usar el sistema vuelva pronto")
        break