from datetime import datetime

import Conexion as cx

import Utiles as ut


con = cx.conectar()

def nuevo():
    finAlta = False
    while not finAlta:
        finAlta = True
        finEntradaAlta = False
        fallos = 0

        while not finEntradaAlta and fallos < 5:
            dni = input("\nDNI:").strip().upper()
            if ut.validarDNI(dni):
                if not buscar(dni):
                    print("\t\tDNI Valido\n")
                    finEntradaAlta = True
                else:
                    fallos = ut.fallo(fallos, "DNI está ya en la BBDD")
            else:
                fallos = ut.fallo(fallos, "El DNI debe tener 8 numeros y una letra")

        finEntradaAlta = False

        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:

                nombre = input("Nombre: ").strip().upper()
                if ut.validarNombre(nombre):
                    print("\t\tNombre Valido\n")
                    finEntradaAlta = True
                else:
                    fallos = ut.fallo(fallos, "El nombre debe contener al menos 2 caracteres.")

        finEntradaAlta = False
        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                apellido = input("Apellido:")
                if ut.validarNombre(apellido):
                    print("\t\tApellido Valido\n")
                    finEntradaAlta = True
                else:
                    fallos = ut.fallo(fallos, "El nombre debe contener al menos 2 caracteres.")

        finEntradaAlta = False
        if fallos < 5:
            fallos = 0
            while not finEntradaAlta and fallos < 5:
                telefono = input("Telefono:")
                if ut.validarTelefono(telefono):
                    print("\t\tTelefono Valido\n")
                    finEntradaAlta = True
                else:
                    fallos = ut.fallo(fallos, "El nombre debe contener al menos 2 caracteres.")

        fechaInscripcion = datetime.now().strftime("%d-%m-%Y")

        # Crea un diccionario con los datos del colaborador
        colaborador = {
            'dni': dni,
            'nombre': nombre,
            'apellido': apellido,
            'telefono': telefono,
            'fechaInscripcion': fechaInscripcion
        }
        print(colaborador.keys())
        print(colaborador)
        key = f'colaborador:{dni}'
        con.hset(key, "dni", colaborador['dni'])
        con.hset(key, "nombre", colaborador['nombre'])
        con.hset(key, "apellido", colaborador['apellido'])
        con.hset(key, "telefono", colaborador['telefono'])
        con.hset(key, "fechaInscripcion", colaborador['fechaInscripcion'])


def borrar():
    dni = input("DNI: ")
    if dni != "":
        if ut.confirmacion("Seguro que quieres ELIMINAR el Colaborador?",
                           f"Eliminacion del Colaborador: {dni} realizada"):
            try:
                print("eliminar colaborador")
            except Exception as errorEliminar:
                print(f"Error al eliminar el colaborador")


def modificar():
    None


def buscar(dni):
    return False


def hgetall(key):
    # Método para obtener todos los campos y valores de un hash en Redis
    return con.hgetall(key)


def mostrarTodos():
    # Obtener todas las claves que coinciden con el patrón "colaborador:*"
    keys = con.keys("colaborador:*")

    # Obtener información de todos los colaboradores
    colaboradores_info = []
    for key in keys:
        # Obtener información de cada colaborador
        colaborador_info = con.hgetall(key)
        colaboradores_info.append(colaborador_info)

    return colaboradores_info
