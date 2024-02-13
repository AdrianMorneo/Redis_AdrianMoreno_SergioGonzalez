from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import ColaboradorConsola  # Importar módulo para manejar la lógica de colaboradores en la consola
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores gráficos

# Variables globales para almacenar elementos de la ventana
buscarAnimalWindow = None
tipo_label = None
nombre_label = None
edad_label = None
padrino_label = None


# Función para buscar un Animal por su DNI
def buscarAnimal():
    dni = nombreLineEditBuscar.text().upper()
    animal = cg.buscar(dni)
    if animal:
        # Si el animal es encontrado, mostrar sus detalles
        tipo_label.setText("Tipo: " + animal.get('dni', ''))
        nombre_label.setText("Nombre: " + animal.get('nombre', ''))
        apellido_label.setText("Edad: " + animal.get('apellido', ''))
        padrino_label.setText("Padrino: " + animal.get('telefono', ''))

        nombreLineEditBuscar.clear()
    else:
        # Si el animal no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(None, "animal no encontrado", "El animal con el DNI especificado no fue encontrado.", QMessageBox.Ok)

# Función para mostrar la ventana de búsqueda de Animal
def buscarAnimalVentana():
    #if ColaboradorConsola.mostrarTodos():
        global buscarAnimalWindow
        global tipo_label, nombre_label, apellido_label, telefono_label, fecha_inscripcion_label
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
        global nombreLineEditBuscar
        nombreLineEditBuscar = QLineEdit()
        layout.addWidget(nombreLineEditBuscar)

        # Botón para buscar el Animal
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(buscarAnimal)
        layout.addWidget(buscar_button)

        # Etiquetas para mostrar los detalles del Animal encontrado
        tipo_label = QLabel("Tipo:")
        layout.addWidget(tipo_label)
        nombre_label = QLabel("Nombre:")
        layout.addWidget(nombre_label)
        apellido_label = QLabel("Edad:")
        layout.addWidget(apellido_label)
        padrino_label = QLabel("Apadrinado por:")
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
'''    
    else:
        # Si no hay colaboradores en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay colaboradores en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
'''