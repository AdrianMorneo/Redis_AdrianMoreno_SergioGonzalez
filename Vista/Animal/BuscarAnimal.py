from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import ColaboradorConsola  # Importar módulo para manejar la lógica de colaboradores en la consola
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores gráficos
import AnimalGrafico as ag  # Importar módulo para interactuar con la base de datos de colaboradores (gráfico)
import Conexion as conect
cnt = conect.conectar()


# Variables globales para almacenar elementos de la ventana
buscarAnimalWindow = None
tipo_label = None
nombre_label = None
edad_label = None
padrino_label = None


# Función para buscar un Animal por su nombre
def buscarAnimal():

    animalN = nombreLineEditBuscar.text().upper()
    animal = ag.comprobarAnimal(animalN)  # Buscar el animal en la base de datos
    if animal[0]:
        valoresAnimal = cnt.get(animal[1]).split("\n")
        nombre = valoresAnimal[2]
        tipo = valoresAnimal[1]
        edad = valoresAnimal[3]
        padrino = valoresAnimal[4]

    if animal:
        # Si el animal es encontrado, mostrar sus detalles
        tipo_label.setText(tipo)
        nombre_label.setText(nombre)
        apellido_label.setText(edad)
        padrino_label.setText(padrino)

        nombreLineEditBuscar.clear()
    else:
        # Si el animal no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(None, "animal no encontrado", "El animal especificado no fue encontrado.", QMessageBox.Ok)


# Función para mostrar la ventana de búsqueda de Animal
def buscarAnimalVentana():
    if ag.comprobarVacioA():
        global buscarAnimalWindow
        global tipo_label, nombre_label, apellido_label, padrino_label
        if buscarAnimalWindow is not None:
            buscarAnimalWindow.show()
            return

        # Crear y configurar la ventana
        buscarAnimalWindow = QMainWindow()
        buscarAnimalWindow.setWindowTitle('Buscar Animal')
        buscarAnimalWindow.setGeometry(200, 200, 400, 400)

        # Estilo de la interfaz de usuario
        style_sheet = css.cogerEstiloAnimales()
        buscarAnimalWindow.setStyleSheet(style_sheet)

        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para introducir el nombre del Animal
        dniLabelBuscar = QLabel("Introduce el Nombre del Animal:")
        layout.addWidget(dniLabelBuscar)
        global nombreLineEditBuscar
        nombreLineEditBuscar = QLineEdit()
        layout.addWidget(nombreLineEditBuscar)

        # Botón para buscar el Animal
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(buscarAnimal)
        layout.addWidget(buscar_button)

        # Etiquetas para mostrar los detalles del Animal encontrado
        tipo_label = QLabel()
        layout.addWidget(tipo_label)
        nombre_label = QLabel()
        layout.addWidget(nombre_label)
        apellido_label = QLabel()
        layout.addWidget(apellido_label)
        padrino_label = QLabel()
        layout.addWidget(padrino_label)


        # Botón para volver
        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(buscarAnimalWindow.close)
        layout.addWidget(volver_button)

        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        buscarAnimalWindow.setCentralWidget(widget)
        buscarAnimalWindow.show()
    else:
        # Si no hay animales en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay Animales en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()