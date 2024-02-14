# Importación de módulos necesarios
from configparser import ConfigParser  # Para leer la configuración de conexión desde un archivo INI
import redis  # Para interactuar con la base de datos Redis
import Utiles as ut  # Importar módulo de utilidades

# Función para establecer conexión con la base de datos Redis
def conectar():
    '''
    Crear un objeto ConfigParser para leer la configuración de conexión desde un archivo INI
    :return:  con, devuelve la conexión
    '''

    configuracion = ConfigParser()
    configuracion.read("ConexionConfig.ini")

    try:
        # Establecer conexión con la base de datos Redis utilizando los parámetros de configuración
        con = redis.StrictRedis(
            host=configuracion.get('conexion', 'host'),
            port=configuracion.getint('conexion', 'puerto'),
            db=configuracion.getint('conexion', 'db'),
            decode_responses=True
        )
        return con  # Devolver el objeto de conexión establecido

    except redis.ConnectionError as e:
        # Capturar la excepción ConnectionError si falla la conexión a Redis
        print("Error de conexión a Redis:", e)
        return None  # Devolver None en caso de error de conexión

# Función para eliminar todos los datos de la base de datos Redis
def borrarBase():
    '''
    Elimina la base dedatos, usado sobre todo para pruebas y limpieza
    :return:
    '''
    # Solicitar confirmación al usuario antes de borrar la base de datos
    if ut.confirmacion("Borrar", "Eliminación de BBDD"):
        # Establecer conexión con la base de datos Redis
        con = conectar()
        # Eliminar todos los datos de la base de datos Redis
        con.flushdb()

# Función para eliminar todos los datos de la base de datos Redis sin solicitar confirmación
def borrarBaseGrafico():
    """
    Metodo que elmina la base de datos desde la interfaz grafica
    :return:
    """
    # Establecer conexión con la base de datos Redis
    con = conectar()
    # Eliminar todos los datos de la base de datos Redis
    con.flushdb()

