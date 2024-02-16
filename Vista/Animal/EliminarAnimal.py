from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import AnimalGrafico as ag  # Importar módulo para manejar la lógica de Animal


# Variable global para almacenar la ventana de eliminación de animal
eliminarAnimalWindow = None

# Función para eliminar un animal
def eliminarAnimal():
    nombre = nombreLineEditEliminar.text().upper()
    animal = ag.comprobarAnimal(nombre)
    if animal[0]:
        # Confirmar la eliminación del animal
        confirmacion = QMessageBox.question(eliminarAnimalWindow, "Confirmar eliminación",
                                             f"¿Estás seguro de que quieres eliminar al animal {nombre}?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            # Si se confirma, eliminar al animal
            ag.eliminar(nombre)
            QMessageBox.information(eliminarAnimalWindow, "Animal eliminado",
                                    f"El animal {nombre} ha sido eliminado correctamente.",
                                    QMessageBox.Ok)

            nombreLineEditEliminar.clear()
    else:
        # Si el animal no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(eliminarAnimalWindow, "Animal no encontrado",
                                f"El Animal {nombre} especificado no fue encontrado.",
                                QMessageBox.Ok)
    nombreLineEditEliminar.clear()

# Función para mostrar la ventana de eliminación de animal
def eliminarAnimalVentana():
    if ag.comprobarVacioA():
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

        # Etiqueta y campo de entrada para introducir el nombre del animal a eliminar
        nombreLabelEliminar = QLabel("Introduce el Nombre del Animal a eliminar:")
        layout.addWidget(nombreLabelEliminar)
        global nombreLineEditEliminar
        nombreLineEditEliminar = QLineEdit()
        layout.addWidget(nombreLineEditEliminar)

        # Botón para eliminar el animal
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

    else:
        # Si no hay animales en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay Animales en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
