from datetime import datetime

from Conexion import Conexion

import Utiles as ut


class Colaborador:
    def __init__(self):
        self.con = Conexion()
    def nuevo(self):
        finAlta = False
        while not finAlta:
            finAlta = True
            finEntradaAlta = False
            fallos = 0

            while not finEntradaAlta and fallos < 5:
                dni = input("\nDNI:").strip().upper()
                if ut.validarDNI(dni):
                    if not Colaborador.buscar(self, dni):
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

            fechaInscripcion = datetime.now().strftime("%d-%m-%Y")

            # Crea un diccionario con los datos del colaborador
            colaborador = {
                'dni': dni,
                'nombre': nombre,
                'apellido': apellido,
                'fechaInscripcion': fechaInscripcion
            }
            print(colaborador)
            key = f'colaborador:{dni}'
            self.con.hset(key, "nombre", colaborador['nombre'])
            self.con.hset(key, "apellido", colaborador['apellido'])
            self.con.hset(key, "fechaInscripcion", colaborador['fechaInscripcion'])



    def borrar(self):
        dni = input("DNI: ")
        if dni != "":
            if ut.confirmacion("Seguro que quieres ELIMINAR el Colaborador?",f"Eliminacion del Colaborador: {dni} realizada"):
                try:
                    print("eliminar colaborador")
                except Exception as errorEliminar:
                    print(f"Error al eliminar el colaborador")


    def modificar(self):
        None

    def buscar(self, dni):
        return False

    def hgetall(self, key):
        # Método para obtener todos los campos y valores de un hash en Redis
        return self.con.hgetall(key)
    def mostrarTodos(self):
        keys = self.con.keys("colaborador:*")

        # Obtener información de todos los colaboradores
        colaboradores_info = [self.hgetall(key) for key in keys]

        return colaboradores_info


