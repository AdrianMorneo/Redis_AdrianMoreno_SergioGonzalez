from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
import EstiloCSS as css
import ColaboradorGrafico as cg
import Utiles as ut
import ColaboradorConsola as cc

# Función para manejar el evento de agregar un colaborador
def handleAgregar(dni, nombre, apellido, telefono):

    if not ut.validarDNI(dni):
        # Si el DNI no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("DNI no válido, (00000000A)")
        alerta.exec_()
    elif cc.comprobarDNIBBDD(dni):
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("DNI ya introducido en la BBDD")
        alerta.exec_()
    elif not ut.validarNombre(nombre):
        # Si el Nombre no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Nombre no válido, mínimo 2 dígitos")
        alerta.exec_()
    elif not ut.validarNombre(apellido):
        # Si el Apellido no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Apellido no válido, mínimo 2 dígitos")
        alerta.exec_()
    elif not ut.validarTelefono(telefono):
        # Si el telefono no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("Telefono no válido, deben ser 9 dígitos")
        alerta.exec_()
    else:
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Colaborador Agregado")
        alerta.setText("Colaborador Agregado")
        cg.nuevo(dni, nombre, apellido, telefono)
        print("Agregado")
        alerta.exec_()




# Función para manejar el evento de agregar colaborador
def handleAgregarButtonClick(dni, nombre, apellido, telefono):
    handleAgregar(dni, nombre, apellido, telefono)


# Función para manejar el evento de volver al menú principal desde la ventana de agregar colaborador
def handleVuelveSubmenuClick():
    agregarColaboradorWindows.close()

# Función para mostrar la ventana de agregar colaborador
def showAddCollaboratorWindow():
    global agregarColaboradorWindows
    agregarColaboradorWindows = QMainWindow()
    agregarColaboradorWindows.setWindowTitle('Agregar Colaborador')
    agregarColaboradorWindows.setGeometry(200, 200, 400, 200)

    style_sheet = css.cogerEstiloColaboradores()
    agregarColaboradorWindows.setStyleSheet(style_sheet)

    layout = QVBoxLayout()

    # Creamos etiquetas y campos de entrada para nombre, apellido y teléfono
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

    handleAgregarClick = lambda: handleAgregar(dni.text(), nombre.text(), apellido.text(), telefono.text())

    # Botón para agregar colaborador
    add_button = QPushButton("Agregar")
    add_button.clicked.connect(handleAgregarClick)
    layout.addWidget(add_button)

    # Botón para volver al menú de colaboradores
    botonVolver = QPushButton("Volver")
    botonVolver.clicked.connect(handleVuelveSubmenuClick)
    layout.addWidget(botonVolver)

    layout.setAlignment(Qt.AlignCenter)

    widget = QWidget()
    widget.setLayout(layout)

    agregarColaboradorWindows.setCentralWidget(widget)
    agregarColaboradorWindows.show()
