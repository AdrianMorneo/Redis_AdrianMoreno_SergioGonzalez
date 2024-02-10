from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
import EstiloCSS as css
import ColaboradorGrafico as cg
import Utiles as ut

# Función para manejar el evento de agregar un colaborador
def handleAgregar(dni, nombre, apellido, telefono):
    if not ut.validarDNI(dni):
        # Si el DNI no es válido, mostrar una alerta
        alerta = QMessageBox()
        alerta.setIcon(QMessageBox.Warning)
        alerta.setWindowTitle("Alerta")
        alerta.setText("DNI no válido, (00000000A)")
        alerta.exec_()
    else:
        if not ut.validarNombre(nombre):
            # Si el Nombre no es válido, mostrar una alerta
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Alerta")
            alerta.setText("Nombre no válido, mínimo 2 dígitos")
            alerta.exec_()
        else:
            if not ut.validarNombre(apellido):
                # Si el DNI no es válido, mostrar una alerta
                alerta = QMessageBox()
                alerta.setIcon(QMessageBox.Warning)
                alerta.setWindowTitle("Alerta")
                alerta.setText("Apellido no válido, mínimo 2 dígitos")
                alerta.exec_()
            else:
                if not ut.validarNombre(telefono):
                    # Si el DNI no es válido, mostrar una alerta
                    alerta = QMessageBox()
                    alerta.setIcon(QMessageBox.Warning)
                    alerta.setWindowTitle("Alerta")
                    alerta.setText("Telefono no válido, deben ser 9 dígitos")
                    alerta.exec_()
                else:
                    cg.nuevo(dni,nombre,apellido,telefono)


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
    dniLabel = QLabel("DNI:")
    layout.addWidget(dniLabel)
    dni = QLineEdit()
    layout.addWidget(dni)

    nombreLabel = QLabel("Nombre:")
    layout.addWidget(nombreLabel)
    nombre = QLineEdit()
    layout.addWidget(nombre)

    apellidoLabel = QLabel("Apellido:")
    layout.addWidget(apellidoLabel)
    apellido = QLineEdit()
    layout.addWidget(apellido)

    telefonoLabel = QLabel("Teléfono:")
    layout.addWidget(telefonoLabel)
    telefono = QLineEdit()
    layout.addWidget(telefono)

    # Botón para agregar colaborador
    add_button = QPushButton("Agregar")
    add_button.clicked.connect(handleAgregar(dni.text(), nombre.text(),apellido.text(), telefono.text()))
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
