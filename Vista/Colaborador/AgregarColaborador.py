from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores
import Utiles as ut  # Importar módulo con funciones útiles
import ColaboradorConsola as cc  # Importar módulo para manejar la lógica de colaboradores en la consola

# Función para manejar el evento de agregar un colaborador
def handleAgregar(dni, nombre, apellido, telefono):
    '''

    :param dni:  recibe dni introducido
    :param nombre:  recibe nombre introducido
    :param apellido: recibe apellido introducido
    :param telefono: recibe telefono introducido
    :return: nada
    '''
    # Validación del DNI
    if not ut.validarDNI(dni):
        # Si el DNI no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("DNI no válido, (00000000A)")
        alerta.exec_()
    # Comprobar si el DNI ya está en la base de datos
    elif cc.comprobarDNIBBDD(dni):
        # Si el DNI ya existe en la base de datos, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("DNI ya introducido en la BBDD")
        alerta.exec_()
    # Validación del nombre
    elif not ut.validarNombre(nombre):
        # Si el Nombre no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Nombre no válido, mínimo 2 dígitos")
        alerta.exec_()
    # Validación del apellido
    elif not ut.validarNombre(apellido):
        # Si el Apellido no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Apellido no válido, mínimo 2 dígitos")
        alerta.exec_()
    # Validación del teléfono
    elif not ut.validarTelefono(telefono):
        # Si el teléfono no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Telefono no válido, deben ser 9 dígitos")
        alerta.exec_()
    else:
        # Si todos los datos son válidos, agregar el colaborador
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Colaborador Agregado")
        alerta.setText("Colaborador Agregado")
        cg.nuevo(dni, nombre, apellido, telefono)
        print("Agregado")
        alerta.exec_()

# Función para mostrar la ventana de agregar colaborador
def agregarColaboradorVentana():
    '''
    metodo que llama a la ventana de agregar colaborador
    :return:
    '''
    global agregarColaboradorWindows
    # Crear y configurar la ventana
    agregarColaboradorWindows = QMainWindow()
    agregarColaboradorWindows.setWindowTitle('Agregar Colaborador')
    agregarColaboradorWindows.setGeometry(200, 200, 400, 200)

    # Estilo de la interfaz de usuario
    style_sheet = css.cogerEstiloColaboradores()
    agregarColaboradorWindows.setStyleSheet(style_sheet)

    layout = QVBoxLayout()

    # Etiquetas y campos de entrada para DNI, Nombre, Apellido y Teléfono
    dniLabel = QLabel("DNI: (00000000A)")
    layout.addWidget(dniLabel)
    dni = QLineEdit()
    layout.addWidget(dni)

    nombreLabel = QLabel("Nombre: (mínimo 2 letras)")
    layout.addWidget(nombreLabel)
    nombre = QLineEdit()
    layout.addWidget(nombre)

    apellidoLabel = QLabel("Apellido: (mínimo 2 letras)")
    layout.addWidget(apellidoLabel)
    apellido = QLineEdit()
    layout.addWidget(apellido)

    telefonoLabel = QLabel("Teléfono: (9 dígitos)")
    layout.addWidget(telefonoLabel)
    telefono = QLineEdit()
    layout.addWidget(telefono)

    # Manejador del evento clic para agregar colaborador
    # Se utiliza lambda porque no se ha encontrado otra manera de controlar el efecto,
    # ya que si usabamos otro método no hacía efecto el click
    handleAgregarClick = lambda: handleAgregar(dni.text().upper(), nombre.text().upper(), apellido.text().upper(), telefono.text().upper())

    # Botón para agregar colaborador
    add_button = QPushButton("Agregar")
    add_button.clicked.connect(handleAgregarClick)
    layout.addWidget(add_button)

    # Botón para volver al menú de colaboradores
    botonVolver = QPushButton("Volver")
    botonVolver.clicked.connect(agregarColaboradorWindows.close)
    layout.addWidget(botonVolver)

    layout.setAlignment(Qt.AlignCenter)

    # Configuración de la ventana y mostrarla
    widget = QWidget()
    widget.setLayout(layout)
    agregarColaboradorWindows.setCentralWidget(widget)
    agregarColaboradorWindows.show()

