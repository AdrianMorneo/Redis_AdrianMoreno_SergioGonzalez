from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import ColaboradorConsola  # Importar módulo para manejar la lógica de colaboradores en la consola
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores gráficos

# Variables globales para almacenar elementos de la ventana
buscarColaboradorWindow = None
dni_label = None
nombre_label = None
apellido_label = None
telefono_label = None
fecha_inscripcion_label = None

# Función para buscar un colaborador por su DNI
def buscarColaborador():
    dni = dniLineEditBuscar.text().upper()
    colaborador = cg.buscar(dni)
    if colaborador:
        # Si el colaborador es encontrado, mostrar sus detalles
        dni_label.setText("DNI: " + colaborador.get('dni', ''))
        nombre_label.setText("Nombre: " + colaborador.get('nombre', ''))
        apellido_label.setText("Apellidos: " + colaborador.get('apellido', ''))
        telefono_label.setText("Teléfono: " + colaborador.get('telefono', ''))
        fecha_inscripcion_label.setText("Fecha de Inscripción: " + colaborador.get('fechaInscripcion', ''))
        dniLineEditBuscar.clear()
    else:
        # Si el colaborador no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(None, "Colaborador no encontrado", "El colaborador con el DNI especificado no fue encontrado.", QMessageBox.Ok)

# Función para mostrar la ventana de búsqueda de colaboradores
def buscarColaboradorVentana():
    if ColaboradorConsola.mostrarTodos():
        global buscarColaboradorWindow
        global dni_label, nombre_label, apellido_label, telefono_label, fecha_inscripcion_label
        if buscarColaboradorWindow is not None:
            buscarColaboradorWindow.show()
            return

        # Crear y configurar la ventana
        buscarColaboradorWindow = QMainWindow()
        buscarColaboradorWindow.setWindowTitle('Buscar Colaborador')
        buscarColaboradorWindow.setGeometry(200, 200, 400, 400)

        # Estilo de la interfaz de usuario
        style_sheet = css.cogerEstiloColaboradores()
        buscarColaboradorWindow.setStyleSheet(style_sheet)

        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para introducir el DNI del colaborador
        dniLabelBuscar = QLabel("Introduce el DNI del colaborador:")
        layout.addWidget(dniLabelBuscar)
        global dniLineEditBuscar
        dniLineEditBuscar = QLineEdit()
        layout.addWidget(dniLineEditBuscar)

        # Botón para buscar el colaborador
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(buscarColaborador)
        layout.addWidget(buscar_button)

        # Etiquetas para mostrar los detalles del colaborador encontrado
        dni_label = QLabel("DNI:")
        layout.addWidget(dni_label)
        nombre_label = QLabel("Nombre:")
        layout.addWidget(nombre_label)
        apellido_label = QLabel("Apellidos:")
        layout.addWidget(apellido_label)
        telefono_label = QLabel("Teléfono:")
        layout.addWidget(telefono_label)
        fecha_inscripcion_label = QLabel("Fecha de Inscripción:")
        layout.addWidget(fecha_inscripcion_label)

        # Botón para volver
        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(buscarColaboradorWindow.close)
        layout.addWidget(volver_button)

        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        buscarColaboradorWindow.setCentralWidget(widget)
        buscarColaboradorWindow.show()
    else:
        # Si no hay colaboradores en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay colaboradores en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
