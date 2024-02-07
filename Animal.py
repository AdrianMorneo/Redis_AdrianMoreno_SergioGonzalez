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
        dniPadrino = "Vacio"

        informacionA = f"\nTipo: {tipo}\nNombre: {nombre}\nEdad: {edad}\nDniPadrino: {dniPadrino}\n"
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
                    print(f"Clave: {key} {valor}")
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



def asignarPadrino():
    animalN = input("Introduce el nombre del animal al que deseas asignar un padrino")
    anim = comprobarAnimal(animalN)
    #comprueba si el animal seleccionado ya tiene un padrino asignado y avisa
    if anim[0]:
        valoresAnimal = cnt.get(clave).split('\n')
        if not "Vacio" in valoresAnimal[3]:
            dniP = input(f"Introduce el Dni del padrino que deseas asignarle al animal {valoresAnimal[1]}")
            existeP = comprobarPadrino(dniP)
            if existeP[0]:
                print(f"Este animal ya contiene un padrino: {valoresAnimal[3]} , se sustituira")
                conf = ut.confirmacion(f"Seguro que deseas sustituit?", "Asignacion de Padrino")
                    if conf:
                        #coger el elemento de dniPadrino de valorAnimal e asignarle el valor dniP
                        #guardar toda la cadena con eso nuevo y hacer set con anim[0] que es la clave y valoresAnimal/2
                        print("")
                    else:
                        print("Operacion Denegada")
            else:
                print(existeP[1])
        else:
            print("")
    else:
        print(f"El animal con el nombre {animalN} no existe")

def comprobarPadrino(dniPadrino):
    mensaje=''
    #Primero comprueba si es un dni para despues comprobar si esta registrado en la BBDD
    if ut.validarDNI(dniPadrino):
        keys = cnt.keys()
        for key in keys:
            if key == dniPadrino:
                return True
            else:
                #dni no encontrado
                mensaje = "Dni no encontrado en la bbdd"
                return False, mensaje
    else:
        #dni no valido
        mensaje = "Formato del dni no valido"
        return False, mensaje







