import Conexion as conect
import Utiles as ut
import ColaboradorConsola as cc

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
        tipo = input("Introduce el tipo del animal (mamifero, ave, pez, reptil, anfibio): ")
        if ut.validarTipoA(tipo.upper()):
           print("\t\tTipo valido\n")
           finEntradaAlta = True
        else:
            fallos = ut.fallo(fallos, "Tipo no valido, escriba uno de los tipos mostrados")

    finEntradaAlta = False
    if fallos < 5:
        fallos = 0
        while not finEntradaAlta and fallos < 5:
            nombre = input("Introduce el nombre del animal: ").upper()
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
                if int(edad) < 100:
                    print("\t\tEdad valida\n")
                    finEntradaAlta = True
                else:
                    fallos = ut.fallo(fallos, "La edad no puede ser mayor a 100")
            else:
                fallos = ut.fallo(fallos, "La edad debe ser un numero")

    if fallos < 5:
        id = cnt.incr('idAnimal')
        dniPadrino = "Sin Padrino"

        informacionA = f"\nTipo: {tipo}\nNombre: {nombre}\nEdad: {edad}\nDniPadrino: {dniPadrino}\n"
        cnt.set("A"+str(id), informacionA)
        print(f"\t\tAnimal {nombre} agregado correctamente con ID: {id}")

def buscarAnimal():
    '''
    Metodo para buscar un animal a traves del nombre del animal
    :param id_animal:
    :return:
    '''
    if comprobarVacioA():
        nombreA = input("Introduce el nombre del animal: ").upper()
        buscarA = comprobarAnimal(nombreA).upper()
        if buscarA[0]:
            keys = cnt.keys('A*')
            if keys:
                for key in keys:
                    valor = cnt.get(key)

                    if "Nombre: " + nombreA in valor:
                        print(f"Clave: {key} {valor}")
        else:
            print(f"No se ha encontrado el nombre {nombreA} en la base de datos")
    else:
        print("Todavia no hay animales registrados en la base de datos")

def eliminarAnimal():
    '''
    Metodo para eliminar un animal de la base de datos redis
    :param id_animal:
    :return:
    '''
    if comprobarVacioA():
        nombreA = input("Introduce el nombre del animal que deseas eliminar: ").upper()
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
            print(f"No se ha encontrado el nombre {nombreA} en la base de datos")
    else:
        print("Todavia no hay animales registrados en la base de datos")

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
    keyE = ""
    if keys:
        for key in keys:
            valor = cnt.get(key)
            if "Nombre: " + nombreA in valor:
                keyE = key
                encontrado = True

    return encontrado , keyE

def modificarAnimal():
    if comprobarVacioA():
        nombreA = input("Introduce el nombre del animal que deseas modificar: ").upper()
        buscarA = comprobarAnimal(nombreA)
        if buscarA[0]:
            print("Que deseas eliminarle al animal?")
            print("1.Tipo")
            print("2.Nombre")
            print("3.Edad")
            op = input("--> ").strip()
            if op == "1":
                modificarA(buscarA[1],"Tipo")
            elif op == "2":
                modificarA(buscarA[1],"Nombre")
            elif op == "3":
                modificarA(buscarA[1],"Edad")
            else:
                print("Opcion no valida")
        else:
            print(f"El nombre {nombreA} no lo tiene ningun animal")
    else:
        print("Todavia no hay animales registrados ")

def modificarA(clave , campo ):
    valoresAnimal2 = ""
    nuevoValor = ""
    finEntradaMod = False
    fallos = 0
    hecho = False
    while not finEntradaMod and fallos < 5:

        nuevoValor = input(f"Introduce el nuevo valor para cambiar {campo} del animal: ").upper()
        if campo =="Tipo":
            if ut.validarTipoA(nuevoValor):
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
                    valoresAnimal2 = "\n".join(valoresAnimal)
            else:
                print("No se ha realizado la modificacion")

            cnt.set(clave, valoresAnimal2)
        else:
            print("Operacion anulada")

def asignarPadrino():
    valoresAnimal2 = ""
    animalN = input("Introduce el nombre del animal al que deseas asignar un padrino: ")
    anim = comprobarAnimal(animalN)
    #comprueba si el animal seleccionado ya tiene un padrino asignado y avisa
    if anim[0]:
        valoresAnimal = cnt.get(anim[1]).split('\n')
        dniP = input(f"Introduce el Dni del padrino que deseas asignarle a {animalN}: ")
        existeP = comprobarPadrino("colaborador:"+dniP)

        if not "DniPadrino: Sin Padrino" in valoresAnimal[4]:#si el animal ya contiene un padrino

            if f"DniPadrino: {dniP}" in valoresAnimal[4].strip():  # si el padrino que se le desea asignar ya lo conteine
                print(f"{animalN} ya tiene asignado este Padrino")
            else:
                if existeP[0]:
                    print(f"Este animal ya contiene un padrino, se sustituira")
                    conf = ut.confirmacion(f"Seguro que deseas sustituir?", "Asignacion de Padrino")
                    if conf:
                        valoresAnimal[4] = f"DniPadrino: {dniP}"
                        hecho = True
                        if hecho:
                            for valor in valoresAnimal:
                                valoresAnimal2 = "\n".join(valoresAnimal)
                        else:
                            print("Error al asignar padrino")
                        cnt.set(anim[1], valoresAnimal2)
                    else:
                        print("Operacion Denegada")
                else:
                    print(existeP[1])#Mensaje indicando el error que se provoco al comprobar padrino

        else:#si el animal no contiene ningun padrino
            if existeP[0]:
                conf = ut.confirmacion(f"Seguro que deseas asignar el Padrino?", "Asignacion de Padrino")
                if conf:
                    valoresAnimal[4] = f"DniPadrino: {dniP}"
                    hecho = True
                    if hecho:
                        for valor in valoresAnimal:
                            valoresAnimal2 = "\n".join(valoresAnimal)
                    else:
                        print("Error al asignar padrino")
                    cnt.set(anim[1], valoresAnimal2)
                else:
                    print("Operacion Denegada")
            else:
                print(existeP[1])#Mensaje indicando el error que se provoco al comprobar padrino
    else:
        print(f"El animal con el nombre {animalN} no existe en la BBDD")

def desapadrinarAnimal():
    valoresAnimal2 = ""
    hecho = False
    nombreA = input("Introduce el nombre del animal que deseas quitar el padrino: ")
    buscarA = comprobarAnimal(nombreA)
    if buscarA[0]:
        valoresAnimal = cnt.get(buscarA[1]).split('\n')
        if not "DniPadrino: Sin Padrino" in valoresAnimal[4]:  # si el animal ya contiene un padrino
            conf = ut.confirmacion(f"Seguro que deseas desapadrinar a {nombreA}?", "Desapadrinacion")

            if conf:
                valoresAnimal[4] = f"DniPadrino: Sin Padrino"
                hecho = True
                if hecho:
                    for valor in valoresAnimal:
                        valoresAnimal2 = "\n".join(valoresAnimal)
                else:
                    print("Error al desapadrinar padrino")
                cnt.set(buscarA[1], valoresAnimal2)
            else:
                print("Operacion Denegada")
        else:#si el animal no contiene un padrino
            print("Este animal no tiene padrino")


def comprobarPadrino(dniPadrino):
    mensaje=''
    claveC = dniPadrino.split(':')
    #Primero comprueba si es un dni para despues comprobar si esta registrado en la BBDD
    if ut.validarDNI(claveC[1]):
        keys = cnt.keys()
        if dniPadrino in keys:
                return True, mensaje
        else:
            #dni no encontrado
            mensaje = "Dni no encontrado en la bbdd"
            return False, mensaje
    else:
        #dni no valido
        mensaje = "Formato del dni no valido"
        return False, mensaje

def mostrarAnimalesP():
    '''
    Metodo para mostrar todos los animales que tiene un colaborador apadrinados
    Muestra el nombre y el id del animal
    :return:
    '''
    nombres = ""
    dniP = input("Introduce el dni del Padrino del que quieres conocer los animales: ")
    existeP = comprobarPadrino("colaborador:" +dniP)
    if existeP[0]:
        keys = cnt.keys('A*')
        encontrado = False
        keyE = ""
        if keys:
            for key in keys:
                valor = cnt.get(key)
                #print(valor)
                valorA = valor.split("\n")
                if "DniPadrino: "+dniP in valor:
                    ani = valorA[2]+ f", ID: {key}"
                    nombres= nombres+ani+"\n"

            if nombres:
                print("--Animales apadrinados--")
                print(nombres)
            else:
                print("Este Colaborador todavia no ha apadrinado ningun  animal")
        else:
            print("Todavia no hay animales registrados")
    else:
        print(existeP[1])

def comprobarVacioA():
    keys = cnt.keys('A*')
    if keys:
       return True
    else:
        return False



