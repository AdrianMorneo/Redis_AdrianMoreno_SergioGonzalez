import Conexion as conect
import Utiles as ut

cnt = conect.conectar()

def agregarAnimal():
    '''
    Metodo para dar de alta un animal nuevo en la base de datos redis
    :return:
    '''
    finAlta = False
    while not finAlta:
        finAlta = True
        finEntradaAlta = False
        fallos = 0

    while not finEntradaAlta and fallos < 5:
        tipo = input("Introduce el tipo del animal: ")
        if ut.validarNombre(tipo):
           print("\t\tTipo valido\n")
           finEntradaAlta = True
        else:
            fallos = ut.fallo(fallos, "El tipo debe tener minimo un caracter")

    finEntradaAlta = False
    if fallos < 5:
        fallos = 0
        while not finEntradaAlta and fallos < 5:
            nombre = input("Introduce el nombre del animal: ")
            if ut.validarNombre(nombre):
                comp = comprobarAnimal(nombre)
                if not comp[0]:
                    print("\t\tNombre valido\n")
                    finEntradaAlta = True
                else:
                    fallos = ut.fallo(fallos, "El nombre ya existe en otro animal")
            else:
                fallos = ut.fallo(fallos, "El nombre debe tener minimo un caracter")
    finEntradaAlta = False
    if fallos < 5:
        fallos = 0
        while not finEntradaAlta and fallos < 5:
            edad = input("Introduce la edad del animal: ")
            if edad.isdigit():
                print("\t\tEdad valida\n")
                finEntradaAlta = True
            else:
                fallos = ut.fallo(fallos, "La edad debe ser un numero")

    if fallos < 5:
        id = cnt.incr('idAnimal')
        apadrinado = "---"
        dniPadrino = "---"

        informacionA = f"\nTipo: {tipo}\nNombre: {nombre}\nEdad: {edad}\nApadrinado: {apadrinado}\nDniPadrino: {dniPadrino}\n"
        cnt.set("A"+str(id), informacionA)
        print(f"\t\tAnimal {nombre} agregado correctamente con ID: {id}")

def buscarAnimal():
    '''
    Metodo para buscar un animal a traves del nombre del animal
    :param id_animal:
    :return:
    '''
    nombreA = input("Introduce el nombre del animal: ")
    buscarA = comprobarAnimal(nombreA)
    if buscarA[0]:
        keys = cnt.keys('A*')
        if keys:
            for key in keys:
                valor = cnt.get(key)

                if "Nombre: " + nombreA in valor:
                    print(f"Clave: {key}, {valor}")
        else:
            print("No hay animales guardados en la base de datos")
    else:
        print(f"No se ha encontrado el nombre {nombreA} en la base de datos")


def eliminarAnimal():
    '''
    Metodo para eliminar un animal de la base de datos redis
    :param id_animal:
    :return:
    '''
    nombreA = input("Introduce el nombre del animal que deseas eliminar: ")
    buscarA = comprobarAnimal(nombreA)
    if buscarA[0]:
        keys = cnt.keys('A*')
        if keys:
            for key in keys:
                valor = cnt.get(key)

                if "Nombre: " + nombreA in valor:
                    print(valor)
                    conf = ut.confirmacion("Seguro que deseas eliminar este animal?", "Baja")
                    if conf:
                        cnt.delete(key)
                        print("\t\tAnimal borrado")
                    else:
                        print("\t\tOperacion denegada")
        else:
            print("No hay animales guardados en la base de datos")
    else:
        print(f"No se ha encontrado el nombre {nombreA} en la base de datos")


def mostrarTodos():
    keys = cnt.keys('A*')
    if keys:
        print("Animales guardados en la base de datos:\n")
        for key in keys:
            valor = cnt.get(key)
            # Imprimir la clave y su valor asociado
            print(f"Id: {key} {valor}")
    else:
        print("No hay animales guardados en la base de datos")


def comprobarAnimal(nombreA):
    '''
    Metodo para verificar que cada animal tiene un nombre o que el animal que se desea buscar existe
    :param id_animal:
    :return:
    '''
    keys = cnt.keys('A*')
    encontrado = False
    key = ""
    if keys:
        for key in keys:
            valor = cnt.get(key)
            if "Nombre: " + nombreA in valor:
                encontrado = True

    return encontrado , key

def modificarAnimal():
    nombreA = input("Introduce el nombre del animal que deseas modificar: ")
    buscarA = comprobarAnimal(nombreA)
    if buscarA[0]:
        print("Que deseas eliminarle al animal?")
        print("1.Tipo")
        print("2.Nombre")
        print("3.Edad")
        op = input("--> ").strip()
        while True:
            if op == "0":
                break
            elif op == "1":
                modificarA(buscarA[1],"Tipo")
            elif op == "2":
                modificarA(buscarA[1],"Nombre")
            elif op == "3":
                modificarA(buscarA[1],"Edad")
            else:
                print("Opcion no valida")
    else:
        print(f"El nombre {nombreA} no lo tiene ningun animal")

def modificarA(clave , campo ):
    valoresAnimal2 = ""
    nuevoValor = ""
    finEntradaMod = False
    fallos = 0
    hecho = False
    while not finEntradaMod and fallos < 5:

        nuevoValor = input(f"Introduce el nuevo valor para cambiar {campo} del animal: ")
        if campo =="Tipo":
            if ut.validarNombre(nuevoValor):
                print("\t\tTipo valido\n")
                finEntradaMod = True
            else:
                fallos = ut.fallo(fallos, "El tipo debe tener minimo un caracter")
        elif campo =="Nombre":
            if ut.validarNombre(nuevoValor):
                comp = comprobarAnimal(nuevoValor)
                if not comp[0]:
                    print("\t\tNombre valido\n")
                    finEntradaMod = True
                else:
                    fallos = ut.fallo(fallos, "El nombre ya existe en otro animal")
            else:
                fallos = ut.fallo(fallos, "El nombre debe tener minimo un caracter")
        elif campo =="Edad":
            if nuevoValor.isdigit():
                print("\t\tEdad valida\n")
                finEntradaMod = True
            else:
                fallos = ut.fallo(fallos, "La edad debe ser un numero")

    if fallos < 5:
        conf = ut.confirmacion(f"Seguro que deseas modificar {campo} de este animal?", "Modificacion")
        if conf:
            valoresAnimal = cnt.get(clave).split('\n')
            for i in range(len(valoresAnimal)):
                if campo+": " in valoresAnimal[i]:
                    valoresAnimal[i] = campo+ ": "+nuevoValor
                    hecho= True
            if hecho:
                for valor in valoresAnimal:
                    valoresAnimal2 = valoresAnimal2+"\n"+valor
            else:
                print("No se ha realizado la modificacion")
            cnt.set(clave, valoresAnimal2)
        else:
            print("Operacion anulada")
