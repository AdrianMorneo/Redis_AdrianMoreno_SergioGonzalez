import Conexion as conect
import Utiles as ut
import ColaboradorConsola as cc

cnt = conect.conectar()

def agregar(tipo, nombre, edad):
    '''
    Metodo para dar de alta un animal nuevo en la base de datos redis para la interfaz grafica
    :return:
    '''
    id = cnt.incr('idAnimal')
    dniPadrino = "Sin Padrino"
    informacionA = f"\nTipo: {tipo}\nNombre: {nombre}\nEdad: {edad}\nDniPadrino: {dniPadrino}\n"
    cnt.set("A"+str(id), informacionA)

def agregarNid(id ,tipo, nombre, edad):
    '''
    Metodo para dar de alta un animal nuevo en la base de datos redis para la interfaz grafica
    pero esta vez recibiendo un id ya que se usa en el modificar y esta implementacion resulta mas sencilla
    debido a algunos problemas relacionados con el modificar animales en la interfaz grafica
    :return:
    '''
    dniPadrino = "Sin Padrino"
    informacionA = f"\nTipo: {tipo}\nNombre: {nombre}\nEdad: {edad}\nDniPadrino: {dniPadrino}\n"
    cnt.set(str(id), informacionA)

def eliminar(nombreA):
    '''
    Metodo para eliminar un animal de la base de datos redis para la interfaz grafica
    :param id_animal:
    :return:
    '''
    keys = cnt.keys('A*')
    if keys:
        for key in keys:
            valor = cnt.get(key)
            if "Nombre: " + nombreA in valor:
                cnt.delete(key)

def comprobarAnimal(nombreA):
    '''
    Metodo para verificar que cada animal tiene un nombre o que el animal que se desea buscar existe
    :param id_animal:
    :return:
    '''
    keys = cnt.keys('A*')
    encontrado = False
    keyE = ""
    if keys:
        for key in keys:
            valor = cnt.get(key)
            if "Nombre: " + nombreA in valor:
                keyE = key
                encontrado = True

    return encontrado , keyE

def comprobarVacioA():
    '''
        Metodo para comprobar rapido si hay animales en la bbdd o no
        :return: True o False si hay algun animal o  todavia no
    '''
    keys = cnt.keys('A*')
    if keys:
       return True
    else:
        return False



