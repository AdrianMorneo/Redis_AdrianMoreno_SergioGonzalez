from configparser import ConfigParser

import redis
import Utiles as ut

def conectar():
    configuracion = ConfigParser()
    configuracion.read("ConexionConfig.ini")

    try:
        con = redis.StrictRedis(host=configuracion.get('conexion', 'host'),
                                port=configuracion.getint('conexion', 'puerto'),
                                db=configuracion.getint('conexion', 'db'),
                                decode_responses=True)
        return con

    except redis.ConnectionError as e:
        # Captura la excepción ConnectionError cuando falla la conexión a Redis
        print("Error de conexión a Redis:", e)
        return None


def borrarBase():
    if ut.confirmacion("Borrar", "Eliminación de BBDD"):
        con = conectar()
        con.flushdb()
