from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import ColaboradorConsola  # Importar módulo para manejar la lógica de colaboradores en la consola
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores gráficos

# Variables globales para almacenar elementos de la ventana
buscarAnimalWindow = None
dni_label = None
nombre_label = None
apellido_label = None
edad_label = None
fecha_inscripcion_label = None

# Función para buscar un colaborador por su DNI
def buscarAnimal():
    dni = dniLineEditBuscar.text().upper()
    Animal = cg.buscar(dni)
    if Animal:
        # Si el Animal es encontrado, mostrar sus detalles
        dni_label.setText("DNI: " + Animal.get('dni', ''))
        nombre_label.setText("Nombre: " + Animal.get('nombre', ''))
        apellido_label.setText("Apellidos: " + Animal.get('apellido', ''))
        edad_label.setText("Teléfono: " + Animal.get('telefono', ''))
        fecha_inscripcion_label.setText("Fecha de Inscripción: " + Animal.get('fechaInscripcion', ''))
        dniLineEditBuscar.clear()
    else:
        # Si el Animal no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(None, "Animal no encontrado", "El Animal con el Nombre especificado no fue encontrado.", QMessageBox.Ok)

# Función para mostrar la ventana de búsqueda de Animal
def buscarAnimalVentana():
   # if ColaboradorConsola.mostrarTodos():
    global buscarAnimalWindow
    global dni_label, nombre_label, apellido_label, edad_label, fecha_inscripcion_label
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

    # Etiqueta y campo de entrada para introducir el DNI del Animal
    dniLabelBuscar = QLabel("Introduce el Nombre del Animal:")
    layout.addWidget(dniLabelBuscar)
    #global nombreLineEditBuscar
    #nombreLineEditBuscar = QLineEdit()
    #layout.addWidget(nombreLineEditBuscar)

    # Botón para buscar el Animal
    buscar_button = QPushButton("Buscar")
    buscar_button.clicked.connect(buscarAnimal)
    layout.addWidget(buscar_button)

    # Etiquetas para mostrar los detalles del Animal encontrado
    dni_label = QLabel("Tipo:")
    layout.addWidget(dni_label)
    nombre_label = QLabel("Nombre:")
    layout.addWidget(nombre_label)
    apellido_label = QLabel("Edad:")
    layout.addWidget(apellido_label)
    edad_label = QLabel("Apadrinado por:")
    layout.addWidget(edad_label)


    # Botón para volver
    volver_button = QPushButton("Volver")
    volver_button.clicked.connect(buscarAnimalWindow.close)
    layout.addWidget(volver_button)

    layout.setAlignment(Qt.AlignCenter)

    widget = QWidget()
    widget.setLayout(layout)

    buscarAnimalWindow.setCentralWidget(widget)
    buscarAnimalWindow.show()
'''
    else:
        # Si no hay Animal en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay Animal en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
'''