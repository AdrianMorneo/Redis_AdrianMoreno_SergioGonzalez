from configparser import ConfigParser

import redis

class Conexion():

    def __init__(self):
        self.redis = None

    def conectar(self):
        configuracion = ConfigParser()
        configuracion.read("ConexionConfig.ini")

        con = redis.StrictRedis(host=configuracion.get('conexion', 'host'), port=configuracion.getint('conexion', 'puerto'), db=configuracion.getint('conexion', 'db'), decode_responses=True)

        return con

    def hset(self, clave, campo, valor):
        self.conectar().hset(clave, campo, valor)

    def hgetall(self, clave):
        return self.conectar().hgetall(clave)

    def keys(self, pattern):
        # Método para obtener todas las claves que coinciden con el patrón en Redis
        return self.conectar().keys(pattern)

