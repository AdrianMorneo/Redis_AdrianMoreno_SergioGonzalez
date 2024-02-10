from datetime import datetime

import Conexion as cx

import Utiles as ut

import json

con = cx.conectar()

def nuevo():
    finAlta = False
    while not finAlta:
        finAlta = True
        finEntradaAlta = False
        fallos = 0

        while not finEntradaAlta and fallos < 5:
            dni = input("\nDNI:").strip().upper()
            # Comprueba si el DNI tiene un formato válido
            if ut.validarDNI(dni):
                print("\t\tDNI Valido\n")
                colaborador = comprobarDNIBBDD(dni)
                if colaborador is None:
                    finEntradaAlta = True
                else:
                    print("El DNI ya está registrado")
                    if ut.confirmacion("¿Quieres introducir otro diferente?", "Petición"):
                        fallos = 0
                    else:
                        fallos = 5

            else:
                ut.fallo(fallos,f"El DNI debe tener 8 números seguidos de una letra. {fallos} fallos, límite 5")


        finEntradaAlta = False

        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                nombre = input("Nombre: ").strip().upper()
                # Comprueba si el nombre tiene al menos 2 caracteres
                if ut.validarNombre(nombre):
                    print("\t\tNombre Valido\n")
                    finEntradaAlta = True
                else:
                    ut.fallo(fallos, f"El nombre debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

        finEntradaAlta = False
        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                apellido = input("Apellido:").strip().upper()
                # Comprueba si el apellido tiene al menos 2 caracteres
                if ut.validarNombre(apellido):
                    print("\t\tApellido Valido\n")
                    finEntradaAlta = True
                else:
                    ut.fallo(fallos, f"El apellido debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

        finEntradaAlta = False
        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                telefono = input("Telefono:")
                if ut.validarTelefono(telefono):
                    print("\t\tTelefono Valido\n")
                    finEntradaAlta = True
                else:
                    ut.fallo(fallos, f"El teléfono debe contener al menos 9 dígitos. {fallos} fallos, límite 5")

        if fallos < 5:
            fechaInscripcion = datetime.now().strftime("%d-%m-%Y")

            # Crea un diccionario con los datos del colaborador
            colaborador = {
                'dni': dni,
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono,
                'fechaInscripcion': fechaInscripcion
            }

            # Convertir el diccionario a formato JSON
            colaborador_json = json.dumps(colaborador)

            # Guardar el colaborador en Redis
            con.set("colaborador:" + dni, colaborador_json)
            print(dni)
            print (colaborador_json)

            return True
        else:
            return False

def borrar():

    colaborador = buscar()

    if colaborador is not None:
        print("DNI:", colaborador["dni"])
        print("Nombre:", colaborador["nombre"])
        print("Apellido:", colaborador["apellido"])
        print("Teléfono:", colaborador["telefono"])
        print("Fecha de inscripción:", colaborador["fechaInscripcion"])
        if ut.confirmacion("Seguro que quieres ELIMINAR el Colaborador?",
                           f"Eliminacion del Colaborador: DNI: {colaborador['dni']}"):
            try:
                con.delete("colaborador:" + colaborador["dni"])
                return True
            except Exception as errorEliminar:
                print("Error al eliminar el colaborador:", errorEliminar)
    return False


def modificar():

    colaboradores = mostrarTodos()

    if colaboradores:
        fallos = 0
        while fallos < 5:
            dni = input("Introduce DNI:").upper()

            if ut.validarDNI(dni):
                # Obtener el objeto colaborador en formato JSON desde Redis
                colaborador_json = con.get(f"colaborador:{dni}")
                if colaborador_json:
                    # Deserializar el JSON a un diccionario de Python
                    colaborador = json.loads(colaborador_json)
                    modifiacion=False
                    fallos = 0

                    print("Qué quieres modificar")
                    print("1. DNI")
                    print("2. Nombre")
                    print("3. Apellido")
                    print("4. Teléfono")
                    print("5. Fecha de inscripción")
                    print("0. Salir de Modificar")
                    opcion = input()

                    if opcion == "0":
                        return False
                    elif opcion == "1":
                        print("Has seleccionado Modificar DNI")
                        while fallos < 5:
                            dniNuevo = input ("Introduzca DNI: ")
                            if ut.validarDNI(dniNuevo):
                                if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                    colaborador['dni'] = dniNuevo
                                    con.delete(f"colaborador:{dni}")
                                    # Convertir el diccionario modificado a formato JSON
                                    colaborador_json_modificado = json.dumps(colaborador)

                                    # Guardar el colaborador modificado en Redis
                                    con.set("colaborador:" + dniNuevo, colaborador_json_modificado)
                                    return True
                            else:
                                ut.fallo(fallos,f"El DNI debe tener 8 números seguidos de una letra. {fallos} fallos, límite 5")

                    elif opcion == "2":
                        while fallos < 5:
                            print("Has seleccionado Modificar NOMBRE")
                            nombre = input ("Introduzca Nombre: ")
                            if ut.validarDNI(nombre):
                                if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                    colaborador['nombre'] = nombre
                                    modifiacion = True
                            else:
                                ut.fallo(fallos, f"El nombre debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

                    elif opcion == "3":
                        while fallos < 5:
                            print("Has seleccionado Modificar APELLIDO")
                            apellido = input ("Introduzca Apellido: ")
                            if ut.validarDNI(apellido):
                                if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                    colaborador['apellido'] = apellido
                                    modifiacion = True

                            else:
                                ut.fallo(fallos, f"El nombre debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

                    elif opcion == "4":
                        while fallos < 5:

                            print("Has seleccionado Modificar TELEFONO")

                            telefono = input("Introduzca Teléfono: ")
                            if ut.validarTelefono(telefono):
                                if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                    colaborador['telefono'] = telefono
                                    modifiacion = True
                            else:
                                ut.fallo(fallos, f"El teléfono debe contener al menos 9 dígitos. {fallos} fallos, límite 5")


                    elif opcion == "5":
                        while fallos < 5:
                            print("Has seleccionado Modificar FECHA DE INSCRIPCION")
                            fecha = input ("Introduzca Fecha de Inscripcion: (dd-mm-aa)")
                            if ut.validarFecha(fecha):
                                if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                    colaborador['fechaInscripcion'] = fecha
                                    modifiacion = True
                            else:
                                ut.fallo(fallos, f"La fehca debe tener el siguiente formato: (dd-mm-aa). {fallos} fallos, límite 5")

                    else:
                        print("Opcion no valida.")

                    if modifiacion:
                        # Convertir el diccionario modificado a formato JSON
                        colaborador_json_modificado = json.dumps(colaborador)

                        # Guardar el colaborador modificado en Redis
                        con.set("colaborador:" + dni, colaborador_json_modificado)
                        return True
                    else:
                        return False
            else:
                fallos += 1
                print(f"El DNI debe tener 8 números seguidos de una letra. {fallos} fallos, límite 5")

def comprobarDNIBBDD(dni):
    # Obtener el objeto colaborador en formato JSON desde Redis
    colaborador_json = con.get(f"colaborador:{dni}")

    # Verificar si el colaborador existe
    if colaborador_json:
        # Deserializar el JSON a un diccionario de Python
        colaborador = json.loads(colaborador_json)
        return colaborador
    else:
        print("El colaborador con DNI", dni, "no se encontró en la base de datos.")
        return None

def buscar():
    colaboradores = mostrarTodos()

    if colaboradores:
        dni = input("Introduce DNI:").upper()
        fallos = 0
        if ut.validarDNI(dni):
            print("\t\tDNI Valido\n")


             # Obtener el objeto colaborador en formato JSON desde Redis
            colaborador_json = con.get(f"colaborador:{dni}")

            # Verificar si el colaborador existe
            if colaborador_json:
                # Deserializar el JSON a un diccionario de Python
                colaborador = json.loads(colaborador_json)
                return colaborador
            else:
                print("El colaborador con DNI", dni, "no se encontró en la base de datos.")
                return None
        else:

            print(f"El DNI debe tener 8 números seguidos de una letra.")



def mostrarTodos():
    keys = con.keys("colaborador:*")
    colaboradores_info = []
    for key in keys:
        colaborador_json = con.get(key)
        if colaborador_json:
            colaborador = json.loads(colaborador_json)
            colaboradores_info.append(colaborador)
    return colaboradores_info

