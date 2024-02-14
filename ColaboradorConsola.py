# Importación de módulos necesarios
from datetime import datetime  # Para trabajar con fechas y horas
import Conexion as cx  # Importar módulo de conexión a la base de datos
import Utiles as ut  # Importar módulo de utilidades
import json  # Importar módulo para manejar JSON

# Conexión a la base de datos
con = cx.conectar()

# Función para agregar un nuevo colaborador
def nuevo():
    '''
    Metodo que realiza la creacción de un nuevoco laborador, controla los parametros y crea diccionario de colaboradores
    :return:
    '''
    finAlta = False  # Variable para controlar el bucle de alta de colaborador
    while not finAlta:
        finAlta = True
        finEntradaAlta = False  # Variable para controlar la entrada de datos del colaborador
        fallos = 0  # Contador de fallos en la entrada de datos

        # Bucle para introducir el DNI del colaborador
        while not finEntradaAlta and fallos < 5:
            dni = input("\nDNI:").strip().upper()
            if ut.validarDNI(dni):  # Validar el formato del DNI
                print("\t\tDNI Valido\n")
                colaborador = comprobarDNIBBDD(dni)  # Comprobar si el DNI ya existe en la base de datos
                if colaborador is None:
                    finEntradaAlta = True  # Si el DNI no existe, se termina la entrada de datos
                else:
                    print("El DNI ya está registrado")
                    if ut.confirmacion("¿Quieres introducir otro diferente?", "Petición"):
                        fallos = 0
                    else:
                        fallos = 5
            else:
                fallos=ut.fallo(fallos,f"El DNI debe tener 8 números seguidos de una letra. {fallos} fallos, límite 5")

        finEntradaAlta = False  # Restablecer la variable para la entrada de datos

        if fallos < 5:
            fallos = 0
            # Bucle para introducir el nombre del colaborador
            while not finEntradaAlta and fallos < 5:
                nombre = input("Nombre: ").strip().upper()
                if ut.validarNombre(nombre):  # Validar el formato del nombre
                    print("\t\tNombre Valido\n")
                    finEntradaAlta = True  # Si el nombre es válido, se termina la entrada de datos
                else:
                    fallos=ut.fallo(fallos, f"El nombre debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

        finEntradaAlta = False  # Restablecer la variable para la entrada de datos
        if fallos < 5:
            fallos = 0
            # Bucle para introducir el apellido del colaborador
            while not finEntradaAlta and fallos < 5:
                apellido = input("Apellido:").strip().upper()
                if ut.validarNombre(apellido):  # Validar el formato del apellido
                    print("\t\tApellido Valido\n")
                    finEntradaAlta = True  # Si el apellido es válido, se termina la entrada de datos
                else:
                    fallos = ut.fallo(fallos, f"El apellido debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

        finEntradaAlta = False  # Restablecer la variable para la entrada de datos
        if fallos < 5:
            fallos = 0
            # Bucle para introducir el teléfono del colaborador
            while not finEntradaAlta and fallos < 5:
                telefono = input("Telefono:")
                if ut.validarTelefono(telefono):  # Validar el formato del teléfono
                    print("\t\tTelefono Valido\n")
                    finEntradaAlta = True  # Si el teléfono es válido, se termina la entrada de datos
                else:
                    fallos = ut.fallo(fallos, f"El teléfono debe contener al menos 9 dígitos. {fallos} fallos, límite 5")

        if fallos < 5:
            fechaInscripcion = datetime.now().strftime("%d-%m-%Y")  # Obtener la fecha de inscripción actual

            # Crear un diccionario con los datos del colaborador
            colaborador = {
                'dni': dni,
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono,
                'fechaInscripcion': fechaInscripcion
            }

            # Convertir el diccionario a formato JSON
            colaborador_json = json.dumps(colaborador)

            # Guardar el colaborador en la base de datos
            con.set("colaborador:" + dni, colaborador_json)


            return True  # Retornar verdadero si se añadió correctamente el colaborador
        else:
            return False  # Retornar falso si hubo problemas al añadir el colaborador

# Función para borrar un colaborador
def borrar():
    '''
    Elimina un colaborador, pidiendo la clave DNI
    :return:
    '''
    colaborador = buscar()  # Buscar el colaborador a borrar en la base de datos

    if colaborador is not None:
        print("DNI:", colaborador["dni"])
        print("Nombre:", colaborador["nombre"])
        print("Apellido:", colaborador["apellido"])
        print("Teléfono:", colaborador["telefono"])
        print("Fecha de inscripción:", colaborador["fechaInscripcion"])
        if ut.confirmacion("Seguro que quieres ELIMINAR el Colaborador?",
                           f"Eliminacion del Colaborador: DNI: {colaborador['dni']}"):
            try:
                con.delete("colaborador:" + colaborador["dni"])  # Eliminar el colaborador de la base de datos
                return True  # Retornar verdadero si se eliminó correctamente el colaborador
            except Exception as errorEliminar:
                print("Error al eliminar el colaborador:", errorEliminar)
    return False  # Retornar falso si hubo problemas al eliminar el colaborador

def borrarMod(dni):
    '''
    Elimina un colaborador, pidiendo la clave DNI
    :return:
    '''
    colaborador = buscarMod(dni)  # Buscar el colaborador a borrar en la base de datos
    try:
        con.delete("colaborador:" + colaborador["dni"])  # Eliminar el colaborador de la base de datos
        return True  # Retornar verdadero si se eliminó correctamente el colaborador
    except Exception as errorEliminar:
        print("Error al eliminar el colaborador:", errorEliminar)
        return False

# Función para modificar un colaborador

def buscarMod(dni):

    '''
    Busca colaborador con dni
    :return: colaborador
    '''

     # Obtener el objeto colaborador en formato JSON desde Redis
    colaborador_json = con.get(f"colaborador:{dni}")

    # Verificar si el colaborador existe

    # Deserializar el JSON a un diccionario de Python
    colaborador = json.loads(colaborador_json)
    return colaborador


def modificar():
    '''
    metodo que modifica un colaborador, de manera que elimina el colaborador que entra y lo introduce de nuevo con los
    mismos parametros, salvo el que se ha modificado.
    :return:
    '''
    colaboradores = mostrarTodos()

    if colaboradores:
        fallos = 0

        dni = input("Introduce DNI:").upper()

        if ut.validarDNI(dni):
            # Obtener el objeto colaborador en formato JSON desde Redis
            colaborador_json = con.get(f"colaborador:{dni}")
            if colaborador_json:
                # Deserializar el JSON a un diccionario de Python
                colaborador = json.loads(colaborador_json)
                modifiacion=False
                fallos = 0
                print("Colaborador encontrado\n")

                print("DNI:", colaborador["dni"])
                print("Nombre:", colaborador["nombre"])
                print("Apellido:", colaborador["apellido"])
                print("Teléfono:", colaborador["telefono"])
                print("Fecha de inscripción:", colaborador["fechaInscripcion"])

                print("\nQué quieres modificar?")
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
                    while fallos < 5 and not modifiacion:
                        dniNuevo = input ("Introduzca nuevo DNI: ").upper()
                        if ut.validarDNI(dniNuevo):
                            if not comprobarDNIBBDD(dniNuevo):
                                if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                    colaborador['dni'] = dniNuevo
                                    con.delete(f"colaborador:{dni}")
                                    # Convertir el diccionario modificado a formato JSON
                                    colaborador_json_modificado = json.dumps(colaborador)

                                    # Guardar el colaborador modificado en Redis
                                    con.set("colaborador:" + dniNuevo, colaborador_json_modificado)
                                    return True
                        else:

                            fallos=ut.fallo(fallos,f"El DNI debe tener 8 números seguidos de una letra. {fallos} fallos, límite 5")

                elif opcion == "2":
                    while fallos < 5 and not modifiacion:
                        print("Has seleccionado Modificar NOMBRE")
                        nombre = input ("Introduzca nuevo Nombre: ").upper()
                        if ut.validarDNI(nombre):
                            if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                colaborador['nombre'] = nombre
                                modifiacion = True
                        else:
                            fallos=ut.fallo(fallos, f"El nombre debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

                elif opcion == "3":
                    while fallos < 5 and not modifiacion:
                        print("Has seleccionado Modificar APELLIDO")
                        apellido = input ("Introduzca nuevo Apellido: ").upper()
                        if ut.validarDNI(apellido):
                            if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                colaborador['apellido'] = apellido
                                modifiacion = True

                        else:
                            fallos=ut.fallo(fallos, f"El nombre debe contener al menos 2 caracteres. {fallos} fallos, límite 5")

                elif opcion == "4":
                    while fallos < 5 and not modifiacion:

                        print("Has seleccionado Modificar TELEFONO")

                        telefono = input("Introduzca nuevo Teléfono: ")
                        if ut.validarTelefono(telefono):
                            if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                colaborador['telefono'] = telefono
                                modifiacion = True
                        else:
                            fallos = ut.fallo(fallos, f"El teléfono debe contener al menos 9 dígitos. {fallos} fallos, límite 5")


                elif opcion == "5":
                    while fallos < 5 and not modifiacion:
                        print("Has seleccionado Modificar FECHA DE INSCRIPCION")
                        fecha = input ("Introduzca nueva Fecha de Inscripcion: (dd-mm-aa)")
                        if ut.validarFecha(fecha):
                            if ut.confirmacion("¿Seguro que quieres Modificarlo?","Modificación"):
                                colaborador['fechaInscripcion'] = fecha
                                modifiacion = True
                        else:
                            fallos = ut.fallo(fallos, f"La fehca debe tener el siguiente formato: (dd-mm-aa). {fallos} fallos, límite 5")

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
            print(f"El DNI debe tener 8 números seguidos de una letra.")
            return False

def comprobarDNIBBDD(dni):
    '''
    Comprueba si el dni introducido está en la BBDD
    :param dni: recibe DNI
    :return: Colaborador o None
    '''
    # Obtener el objeto colaborador en formato JSON desde Redis
    colaborador_json = con.get(f"colaborador:{dni}")

    # Verificar si el colaborador existe
    if colaborador_json:
        # Deserializar el JSON a un diccionario de Python
        print("Dni metido en la BBDD")
        colaborador = json.loads(colaborador_json)
        return colaborador
    else:
        print("El colaborador con DNI", dni, "es válido, todavía no está registrado en la base de datos.")
        return None

def buscar():

    '''
    Busca colaborador con dni
    :return: colaborador o None
    '''
    colaboradores = mostrarTodos()
#Comprueba si hay colaboradores
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
    '''
    Busca todos los colaboradores
    :return: listaColaboradores
    '''
    # Obtener todas las claves que coinciden con el patrón "colaborador:*" en la base de datos
    keys = con.keys("colaborador:*")

    # Inicia lista vacía para almacenar la información de los colaboradores
    colaboradores_info = []

    # Recorre las claves obtenidas y obtiene la información de los colaboradores
    for key in keys:
        # Obtener el valor asociado a la clave, que contiene la información del colaborador en formato JSON
        colaborador_json = con.get(key)

        # Verificar si el valor existe y no es None
        if colaborador_json:
            # Deserializar el JSON a un diccionario de Python para obtener la información del colaborador
            colaborador = json.loads(colaborador_json)

            # Agregar el diccionario del colaborador a la lista de información de colaboradores
            colaboradores_info.append(colaborador)

    # Devolver la lista de información de colaboradores
    return colaboradores_info

