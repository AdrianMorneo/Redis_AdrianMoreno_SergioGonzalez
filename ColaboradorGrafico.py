from datetime import datetime

import Conexion as cx

import Utiles as ut

import json

from ColaboradorConsola import comprobarDNIBBDD

con = cx.conectar()
def nuevo(dni, nombre, apellido, telefono):

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
        print(colaborador_json)
        return True