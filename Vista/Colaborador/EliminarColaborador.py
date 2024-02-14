from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PySide2.QtCore import Qt

import ColaboradorConsola  # Importar módulo para manejar la lógica de colaboradores en la consola
import EstiloCSS as css  # Importar un módulo EstiloCSS para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para manejar la lógica de colaboradores gráficos

# Variable global para almacenar la ventana de eliminación de colaborador
eliminarColaboradorWindow = None

# Función para eliminar un colaborador
def eliminarColaborador():
    '''
    Metodo que elimina el colaborador, pide DNI lo busca y lo borra
    :return:
    '''
    dni = dniLineEditEliminar.text().upper()
    colaborador = cg.buscar(dni)
    if colaborador:
        # Confirmar la eliminación del colaborador
        confirmacion = QMessageBox.question(eliminarColaboradorWindow, "Confirmar eliminación",
                                             "¿Estás seguro de que quieres eliminar al colaborador con DNI {}?".format(dni),
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            # Si se confirma, eliminar al colaborador
            cg.eliminar(dni)
            QMessageBox.information(eliminarColaboradorWindow, "Colaborador eliminado",
                                    "El colaborador con DNI {} ha sido eliminado correctamente.".format(dni),
                                    QMessageBox.Ok)

            dniLineEditEliminar.clear()
    else:
        # Si el colaborador no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(eliminarColaboradorWindow, "Colaborador no encontrado",
                                "El colaborador con el DNI especificado no fue encontrado.",
                                QMessageBox.Ok)
    dniLineEditEliminar.clear()

# Función para mostrar la ventana de eliminación de colaborador
def eliminarColaboradorVentana():
    '''
    Metodo que gestiona la ventan de eliminar colaborador
    :return:
    '''
    if ColaboradorConsola.mostrarTodos():
        global eliminarColaboradorWindow
        if eliminarColaboradorWindow is not None:
            eliminarColaboradorWindow.show()
            return

        # Crear y configurar la ventana
        eliminarColaboradorWindow = QMainWindow()
        eliminarColaboradorWindow.setWindowTitle('Eliminar Colaborador')
        eliminarColaboradorWindow.setGeometry(200, 200, 400, 200)

        # Estilo de la interfaz de usuario
        style_sheet = css.cogerEstiloColaboradores()
        eliminarColaboradorWindow.setStyleSheet(style_sheet)

        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para introducir el DNI del colaborador a eliminar
        dniLabelEliminar = QLabel("Introduce el DNI del colaborador a eliminar:")
        layout.addWidget(dniLabelEliminar)
        global dniLineEditEliminar
        dniLineEditEliminar = QLineEdit()
        layout.addWidget(dniLineEditEliminar)

        # Botón para eliminar el colaborador
        eliminar_button = QPushButton("Eliminar")
        eliminar_button.clicked.connect(eliminarColaborador)
        layout.addWidget(eliminar_button)

        # Botón para volver
        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(eliminarColaboradorWindow.close)
        layout.addWidget(volver_button)

        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        eliminarColaboradorWindow.setCentralWidget(widget)
        eliminarColaboradorWindow.show()
    else:
        # Si no hay colaboradores en la base de datos, mostrar un mensaje informativo
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay colaboradores en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
