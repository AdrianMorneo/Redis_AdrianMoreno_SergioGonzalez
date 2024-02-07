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
            if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha():
                print("\t\tDNI Valido\n")
                finEntradaAlta = True
            else:
                fallos += 1
                print("El DNI debe tener 8 números seguidos de una letra.")
                if fallos >= 5:
                    print("Demasiados fallos. Abortando.")
                    return

        finEntradaAlta = False

        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                nombre = input("Nombre: ").strip().upper()
                # Comprueba si el nombre tiene al menos 2 caracteres
                if len(nombre) >= 2:
                    print("\t\tNombre Valido\n")
                    finEntradaAlta = True
                else:
                    fallos += 1
                    print("El nombre debe contener al menos 2 caracteres.")

        finEntradaAlta = False
        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                apellido = input("Apellido:").strip().upper()
                # Comprueba si el apellido tiene al menos 2 caracteres
                if len(apellido) >= 2:
                    print("\t\tApellido Valido\n")
                    finEntradaAlta = True
                else:
                    fallos += 1
                    print("El apellido debe contener al menos 2 caracteres.")

        finEntradaAlta = False
        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                telefono = input("Telefono:")
                # No se realiza validación para el teléfono en este ejemplo
                print("\t\tTelefono Valido\n")
                finEntradaAlta = True

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

        print("Colaborador guardado exitosamente en Redis.")



def borrar():
    dni = input("DNI: ")
    colaborador = buscar()
    if colaborador is not None:
        if ut.confirmacion("Seguro que quieres ELIMINAR el Colaborador?",
                           f"Eliminacion del Colaborador: {dni} realizada"):
            try:
                con.delete(colaborador)
                print("eliminar colaborador")
            except Exception as errorEliminar:
                print(f"Error al eliminar el colaborador")


def modificar():
    None


def buscar():
    dni = input("Introduce DNI:").upper()
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



def mostrarTodos():
    keys = con.keys("colaborador:*")
    colaboradores_info = []
    for key in keys:
        colaborador_json = con.get(key)
        if colaborador_json:
            colaborador = json.loads(colaborador_json)
            colaboradores_info.append(colaborador)
    return colaboradores_info

