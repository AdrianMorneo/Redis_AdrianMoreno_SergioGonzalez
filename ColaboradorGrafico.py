# Importación de módulos necesarios
from datetime import datetime  # Para obtener la fecha actual
import json  # Para serializar y deserializar datos en formato JSON
import Conexion as cx  # Importar el módulo de conexión a la base de datos
import Utiles as ut  # Importar módulo de utilidades
import ColaboradorConsola as cc  # Importar el módulo de consola para los colaboradores
from ColaboradorConsola import comprobarDNIBBDD  # Importar función para comprobar el DNI en la consola de colaboradores

# Establecer conexión con la base de datos
con = cx.conectar()

# Función para agregar un nuevo colaborador a la base de datos
def nuevo(dni, nombre, apellido, telefono):
    # Obtener la fecha actual en formato "dd-mm-aaaa"
    fechaInscripcion = datetime.now().strftime("%d-%m-%Y")

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

    # Guardar el colaborador en Redis con la clave "colaborador:DNI"
    con.set("colaborador:" + dni, colaborador_json)

    # Imprimir el DNI y el JSON del colaborador para verificar su almacenamiento
    print(dni)
    print(colaborador_json)

    # Devolver True para indicar que se ha agregado el colaborador exitosamente
    return True

# Función para buscar un colaborador en la base de datos mediante su DNI
def buscar(dni):
    # Obtener la lista de todos los colaboradores almacenados en la base de datos
    colaboradores = cc.mostrarTodos()

    # Convertir el DNI a mayúsculas para una comparación sin distinción entre mayúsculas y minúsculas
    dni = dni.upper()

    # Verificar si existen colaboradores en la base de datos
    if colaboradores:
        fallos = 0

        # Validar el formato del DNI ingresado
        if ut.validarDNI(dni):
            print("\t\tDNI Valido\n")

            # Obtener el objeto colaborador en formato JSON desde Redis
            colaborador_json = con.get(f"colaborador:{dni}")

            # Verificar si el colaborador existe en la base de datos
            if colaborador_json:
                # Deserializar el JSON a un diccionario de Python para obtener la información del colaborador
                colaborador = json.loads(colaborador_json)
                return colaborador  # Devolver el colaborador encontrado
            else:
                print("El colaborador con DNI", dni, "no se encontró en la base de datos.")
                return None  # Devolver None si el colaborador no se encuentra en la base de datos
        else:
            print(f"El DNI debe tener 8 números seguidos de una letra.")

# Función para modificar los datos de un colaborador en la base de datos
def modificar(dni, nombre, apellido, telefono, fechaInscripcion):
    print(fechaInscripcion + " Estoy en modificar")

    # Crear un diccionario con los datos actualizados del colaborador
    colaborador = {
        'dni': dni,
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'fechaInscripcion': fechaInscripcion
    }

    # Convertir el diccionario a formato JSON
    colaborador_json = json.dumps(colaborador)

    # Actualizar los datos del colaborador en la base de datos
    con.set("colaborador:" + dni, colaborador_json)

    # Imprimir el DNI y el JSON del colaborador para verificar su actualización
    print(dni)
    print(colaborador_json)

    # Devolver True para indicar que se ha modificado el colaborador exitosamente
    return True

# Función para eliminar un colaborador de la base de datos
def eliminar(dni):
    # Buscar el colaborador en la base de datos mediante su DNI
    colaborador = buscar(dni)

    # Verificar si se encontró el colaborador
    if colaborador is not None:
        try:
            # Eliminar el colaborador de la base de datos
            con.delete("colaborador:" + colaborador["dni"])
            return True  # Devolver True para indicar que el colaborador ha sido eliminado exitosamente
        except Exception as errorEliminar:
            print("Error al eliminar el colaborador:", errorEliminar)
            return False  # Devolver False en caso de error al eliminar el colaborador
