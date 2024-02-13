from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox, QComboBox
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import AnimalGrafico as ag  # Importar módulo para manejar la lógica de colaboradores
import Utiles as ut  # Importar módulo con funciones útiles
import ColaboradorConsola as cc  # Importar módulo para manejar la lógica de colaboradores en la consola

# Función para manejar el evento de agregar un colaborador
def handleAgregar(tipo, nombre, edad):
    # Validación del DNI
    if not ut.validarTipoA(tipo):
        # Si el DNI no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Tipo no válido")
        alerta.exec_()
    ###########################
    ############### comprobar si el nombre esta en la bbdd
    ###############


        '''    elif cc.comprobarDNIBBDD(nombre):
                # Si el DNI ya existe en la base de datos, mostrar una alerta
                alerta = QMessageBox()
                alerta.setIcon(QMessageBox.Warning)
                alerta.setWindowTitle("Alerta")
                alerta.setText("Nombre ya introducido en la BBDD")
                alerta.exec_()
        '''
    # Validación del nombre
    elif not ut.validarNombre(nombre):
        # Si el Nombre no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Nombre no válido, mínimo 2 dígitos")
        alerta.exec_()
    # Validación del apellido
    elif not ut.validarEdad(edad):
        # Si la Edad no es válida, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Edad no válida, debe ser un número entre 0 y 100")
        alerta.exec_()
    else:
        # Si todos los datos son válidos, agregar el colaborador
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Colaborador Agregado")
        alerta.setText("Colaborador Agregado")
        ag.nuevo(tipo, nombre, edad)
        print("Agregado")
        alerta.exec_()

# Función para mostrar la ventana de agregar colaborador
def agregarAnimalVentana():
    global agregarAnimalWindows
    # Crear y configurar la ventana
    agregarAnimalWindows = QMainWindow()
    agregarAnimalWindows.setWindowTitle('Agregar Colaborador')
    agregarAnimalWindows.setGeometry(200, 200, 400, 200)

    # Estilo de la interfaz de usuario
    style_sheet = css.cogerEstiloAnimales()
    agregarAnimalWindows.setStyleSheet(style_sheet)

    layout = QVBoxLayout()

    # Etiquetas y campos de entrada para DNI, Nombre, Apellido y Teléfono
    tipoLabel = QLabel("Tipo: ")
    layout.addWidget(tipoLabel)
    tipoComboBox = QComboBox()
    tipoComboBox.addItems(["Mamífero", "Ave", "Pez", "Reptil", "Anfibio"])
    layout.addWidget(tipoComboBox)

    nombreLabel = QLabel("Nombre: (mínimo 2 letras)")
    layout.addWidget(nombreLabel)
    nombre = QLineEdit()
    layout.addWidget(nombre)

    edadLabel = QLabel("Edad: (Entre 0 y 100)")
    layout.addWidget(edadLabel)
    edad = QLineEdit()
    layout.addWidget(edad)

    # Manejador del evento clic para agregar colaborador
    handleAgregarClick = lambda: handleAgregar(tipoComboBox.currentText().upper(), nombre.text().upper(), edad.text().upper())

    # Botón para agregar colaborador
    add_button = QPushButton("Agregar")
    add_button.clicked.connect(handleAgregarClick)
    layout.addWidget(add_button)

    # Botón para volver al menú de colaboradores
    botonVolver = QPushButton("Volver")
    botonVolver.clicked.connect(agregarAnimalWindows.close)
    layout.addWidget(botonVolver)

    layout.setAlignment(Qt.AlignCenter)

    # Configuración de la ventana y mostrarla
    widget = QWidget()
    widget.setLayout(layout)
    agregarAnimalWindows.setCentralWidget(widget)
    agregarAnimalWindows.show()
