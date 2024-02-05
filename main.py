
import Interfaz as interfaz




'''
configuracion = ConfigParser()
configuracion.read("ConexionConfig.ini")
        
con = redis.StrictRedis(host=configuracion.get('conexion', 'host'), port=configuracion.getint('conexion', 'puerto'), db=configuracion.getint('conexion', 'db'), decode_responses=True)

con.set('nombre', 'Juan')
con.set('edad', 30)

# Obtener datos de Redis
nombre = con.get('nombre')
edad = con.get('edad')

print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
'''
#conexion.conectar()
interfaz.ejecutar()

