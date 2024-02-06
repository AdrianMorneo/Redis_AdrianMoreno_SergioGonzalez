import Conexion as conect

cnt = conect.conectar()


def agregarAnimal():
    id = cnt.incr('idAnimal')
    tipo = input("Introduce el tipo del animal: ")
    nombre = input("Introduce el nombre del animal: ")
    edad = int(input("Introduce la edad del animal: "))
    apadrinado = False
    dniPadrino = ''

    informacionA = f"Tipo: {tipo},Nombre: {nombre},Edad: {edad},Apadrinado: {apadrinado},DniPadrino: {dniPadrino}"
    cnt.set(id, informacionA)

    print(f"Animal agregado correctamente con ID: {id}")

def buscarAnimal():
    '''
    Metodo para buscar un animal a traves del id
    :param id_animal:
    :return:
    '''
    nombreA = input("Introduce el nombre del animal: ")
    keys = cnt.keys()

    if keys:
        for key in keys:
            valor = cnt.get(key)

            if "Nombre: "+nombreA in valor:
                print(f"Clave: {key}, {valor}")
    else:
        print("No hay animales guardados en la base de datos")

def eliminarAnimal():
    '''
    Metodo para eliminar un animal a traves del id
    :param id_animal:
    :return:
    '''
    nombreA = input("Introduce el nombre del animal que deseas eliminar: ")
    keys = cnt.keys()
    if keys:
        for key in keys:
            valor = cnt.get(key)

            if "Nombre: "+nombreA in valor:
                cnt.delete(key)
                print("animal borrado")
    else:
        print("No hay animales guardados en la base de datos")

def mostrarTodos():
    # Obtener todas las claves de Redis que corresponden a animales
    keys = cnt.keys()

    if keys:
        print("Animales guardados en la base de datos:\n")
        for key in keys:
            valor = cnt.get(key)
            # Imprimir la clave y su valor asociado
            print(f"Clave: {key}, {valor}")
    else:
        print("No hay animales guardados en la base de datos")
