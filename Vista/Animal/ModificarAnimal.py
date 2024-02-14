from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, \
    QCalendarWidget, QMessageBox, QComboBox  # Importar clases necesarias desde PySide2
from PySide2.QtCore import Qt, QDate  # Importar clases necesarias desde PySide2

import ColaboradorConsola  # Importar módulo para interactuar con la base de datos de colaboradores (consola)
import EstiloCSS as css  # Importar módulo para el estilo de la interfaz de usuario
import AnimalGrafico as ag  # Importar módulo para interactuar con la base de datos de colaboradores (gráfico)
import Utiles as ut  # Importar módulo de utilidades para validaciones
import ColaboradorConsola as cc  # Importar módulo para interactuar con la base de datos de colaboradores (consola)
import Animal as aml
import Conexion as conect

# Variable global para almacenar la ventana de modificación
modificarAnimalWindow = None
cnt = conect.conectar()
dniLineEditBuscar = None
nombreLineEdit = None
tipoComboBox = None
edadLineEdit = None

def confirmarModificacion(tipo, nombre, edad):

    # Procesar la respuesta del usuario
    if not ut.validarTipoA(tipo):
        # Si el tipo no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Tipo no válido")
        alerta.exec_()
        ###########################
        ############### comprobar si el nombre esta en la bbdd
        ###############

    elif not aml.comprobarAnimal(nombre):
        # Si el nombre ya existe en la base de datos, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Nombre ya introducido en la BBDD")
        alerta.exec_()
    # Validación del nombre
    elif not ut.validarNombre(nombre):
        # Si el Nombre no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Nombre no válido, mínimo 2 dígitos")
        alerta.exec_()
    # Validación de la edad
    elif not ut.validarEdad(edad):
        # Si la Edad no es válida, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Edad no válida, debe ser un número entre 0 y 100")
        alerta.exec_()
    # Validación de la edad
    elif not edad.isdigit():
        # Si la Edad no es válida, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Edad no válida, debe ser un número")
        alerta.exec_()
    else:
        # Si todos los datos son válidos, agregar el animal
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        ag.eliminar(nombre)
        ag.agregar(tipo, nombre, edad)
        alerta.setWindowTitle("Modificado")
        alerta.setText("Animal modificado")
        alerta.exec_()
        # Función para confirmar la modificación de un animal
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Confirmar Modificación")
        mensaje.setText("¿Seguro que quieres modificar?")
        mensaje.setIcon(QMessageBox.Question)
        mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        mensaje.setDefaultButton(QMessageBox.Cancel)
        respuesta = mensaje.exec_()

        print("Modificado")
        alerta.exec_()


def buscarAnimal():
    # Función para buscar un animal por su DNI
    animalN = dniLineEditBuscar.text().upper()
    print(animalN)
    animal = ag.comprobarAnimal(animalN)  # Buscar el animal en la base de datos
    print(animal[0])
    if animal[0]:
        valoresAnimal = cnt.get(animal[1]).split("\n")
        nombre= valoresAnimal[2].split(": ")
        tipo=valoresAnimal[1].split(": ")
        edad=valoresAnimal[3].split(": ")
        # Si se encuentra el colaborador, llenar los campos con sus datos
        tipoComboBox.setCurrentText(tipo[1])
        nombreLineEdit.setText(nombre[1])
        edadLineEdit.setText(edad[1])

    else:
        # Si el animal no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(None, "animal no encontrado", "El animal especificado no fue encontrado.", QMessageBox.Ok)

def modificarAnimalVentana():
    # Función para mostrar la ventana de modificación de animal
    if ag.comprobarVacioA():
        global modificarAnimalWindow
        # Si la ventana ya está creada, simplemente la mostramos
        if modificarAnimalWindow is not None:
            modificarAnimalWindow.show()
            return

        # Crear una nueva ventana principal para modificar animal
        modificarAnimalWindow = QMainWindow()
        modificarAnimalWindow.setWindowTitle('Modificar Colaborador')
        modificarAnimalWindow.setGeometry(200, 200, 400, 400)

        # Establecer el estilo de la ventana utilizando el CSS proporcionado
        style_sheet = css.cogerEstiloAnimales()
        modificarAnimalWindow.setStyleSheet(style_sheet)

        # Crear un layout vertical para organizar los elementos de la ventana
        layout = QVBoxLayout()

        # Agregar un QLabel y un QLineEdit para buscar un colaborador por su DNI
        dniLabelBuscar = QLabel("Buscar Animal por nombre:")
        layout.addWidget(dniLabelBuscar)

        global dniLineEditBuscar
        dniLineEditBuscar = QLineEdit()
        layout.addWidget(dniLineEditBuscar)
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(buscarAnimal)
        layout.addWidget(buscar_button)

        # Agregar etiquetas y campos de entrada para nombre, tipo y edad
        dniLabel = QLabel("TIPO")
        layout.addWidget(dniLabel)
        global tipoComboBox
        tipoComboBox = QComboBox()
        tipoComboBox.addItems(["MAMIFERO", "AVE", "PEZ", "REPTIL", "ANFIBIO"])
        layout.addWidget(tipoComboBox)
        global nombreLabel
        nombreLabel = QLabel("Nombre: (mínimo 2 letras)")
        layout.addWidget(nombreLabel)
        global nombreLineEdit
        nombreLineEdit = QLineEdit()
        layout.addWidget(nombreLineEdit)
        global edadLabel
        edadLabel = QLabel("Edad: (Entre 0 y 100)")
        layout.addWidget(edadLabel)
        global edadLineEdit
        edadLineEdit = QLineEdit()
        layout.addWidget(edadLineEdit)

        # Agregar un QPushButton para confirmar la modificación del animal
        modificar_button = QPushButton("Modificar")
        # Conectar el botón de modificar con la función de confirmar modificación
        modificar_button.clicked.connect(
            lambda: confirmarModificacion(tipoComboBox.currentText().upper(),
                                          nombreLineEdit.text().upper(),
                                          edadLineEdit.text().upper()))
        layout.addWidget(modificar_button)

        # Agregar un QPushButton para cerrar la ventana de modificación
        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(modificarAnimalWindow.close)
        layout.addWidget(volver_button)

        # Alinear el layout en el centro de la ventana
        layout.setAlignment(Qt.AlignCenter)

        # Crear un widget principal y establecer el layout creado anteriormente
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget principal como widget central de la ventana
        modificarAnimalWindow.setCentralWidget(widget)
        # Mostrar la ventana de modificación de animal
        modificarAnimalWindow.show()
    else:
        # Si no hay animales en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay Animales en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
