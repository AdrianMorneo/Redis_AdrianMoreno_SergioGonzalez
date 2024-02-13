from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import ColaboradorConsola  # Importar módulo para manejar la lógica de colaboradores en la consola
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores gráficos

# Variable global para almacenar la ventana de eliminación de colaborador
eliminarAnimalWindow = None

# Función para eliminar un colaborador
def eliminarAnimal():
    dni = nombreLineEditEliminar.text().upper()
    colaborador = cg.buscar(dni)
    if colaborador:
        # Confirmar la eliminación del colaborador
        confirmacion = QMessageBox.question(eliminarAnimalWindow, "Confirmar eliminación",
                                             "¿Estás seguro de que quieres eliminar al colaborador con DNI {}?".format(dni),
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            # Si se confirma, eliminar al colaborador
            cg.eliminar(dni)
            QMessageBox.information(eliminarAnimalWindow, "Colaborador eliminado",
                                    "El colaborador con DNI {} ha sido eliminado correctamente.".format(dni),
                                    QMessageBox.Ok)

            nombreLineEditEliminar.clear()
    else:
        # Si el colaborador no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(eliminarAnimalWindow, "Colaborador no encontrado",
                                "El colaborador con el DNI especificado no fue encontrado.",
                                QMessageBox.Ok)
    nombreLineEditEliminar.clear()

# Función para mostrar la ventana de eliminación de colaborador
def eliminarAnimalVentana():
    #if ColaboradorConsola.mostrarTodos():
        global eliminarAnimalWindow
        if eliminarAnimalWindow is not None:
            eliminarAnimalWindow.show()
            return

        # Crear y configurar la ventana
        eliminarAnimalWindow = QMainWindow()
        eliminarAnimalWindow.setWindowTitle('Eliminar Animal')
        eliminarAnimalWindow.setGeometry(200, 200, 400, 200)

        # Estilo de la interfaz de usuario
        style_sheet = css.cogerEstiloAnimales()
        eliminarAnimalWindow.setStyleSheet(style_sheet)

        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para introducir el DNI del colaborador a eliminar
        nombreLabelEliminar = QLabel("Introduce el Nombre del Animal a eliminar:")
        layout.addWidget(nombreLabelEliminar)
        global nombreLineEditEliminar
        nombreLineEditEliminar = QLineEdit()
        layout.addWidget(nombreLineEditEliminar)

        # Botón para eliminar el colaborador
        eliminar_button = QPushButton("Eliminar")
        eliminar_button.clicked.connect(eliminarAnimal)
        layout.addWidget(eliminar_button)

        # Botón para volver
        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(eliminarAnimalWindow.close)
        layout.addWidget(volver_button)

        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        eliminarAnimalWindow.setCentralWidget(widget)
        eliminarAnimalWindow.show()
"""
    else:
        # Si no hay colaboradores en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay Animal en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
"""