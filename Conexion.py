from configparser import ConfigParser

import redis


def conectar():
    configuracion = ConfigParser()
    configuracion.read("ConexionConfig.ini")

    con = redis.StrictRedis(host=configuracion.get('conexion', 'host'),
                            port=configuracion.getint('conexion', 'puerto'),
                            db=configuracion.getint('conexion', 'db'),
                            decode_responses=True)

    return con


def hset(self, clave, campo, valor):
    self.conectar().hset(clave, campo, valor)


def hgetall(self, clave):
    return self.conectar().hgetall(clave)


def keys(self, pattern):
    # Método para obtener todas las claves que coinciden con el patron en Redis
    return self.conectar().keys(pattern)
