import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide2.QtCore import QTimer, Qt
import EstiloCSS as css
from .Animal import InterfazGraficaAnimales as iga
from .Colaborador import InterfazGraficaColaboradores as igc
import Conexion as cx

# Crear la instancia de QApplication
app = QApplication(sys.argv)

submenu_window_animales = None
submenu_window_colaboradores = None

# Función principal que muestra la ventana de bienvenida
def mensajeBienvenida():
    # Crear la ventana principal
    main_window = QMainWindow()
    main_window.setWindowTitle('Santuario de Animales')
    main_window.setGeometry(100, 100, 800, 600)

    # Estilos CSS para los botones y etiquetas
    style_sheet = css.cogerEstiloPrincipal()
    main_window.setStyleSheet(style_sheet)

    # Etiqueta de bienvenida
    welcome_label = QPushButton("¡Bienvenido al Santuario de Animales!\nAdrian y Sergio", main_window)
    welcome_label.setGeometry(100, 150, 600, 200)

    # Ocultar la etiqueta después de 3 segundos
    QTimer.singleShot(3000, welcome_label.hide)
    QTimer.singleShot(3000, mostrarBotonesMenuDelayed)  # Mostrar los botones del menú después de 3 segundos

    # Mostrar la ventana principal
    main_window.show()
    sys.exit(app.exec_())

# Función que maneja el clic en el botón de "Animales"
def handle_animal_button_click():
    iga.mostrarSubMenuAnimales()

# Función que maneja el clic en el botón de "Colaboradores"
def handle_collaborator_button_click():
    igc.mostrarSubMenuColaboradores()

# Función que maneja el clic en el botón de "Borrar BD"
def handle_delete_button_click():
    confirmacion = QMessageBox.question(None, "Confirmar eliminación",
                                         "¿Estás seguro de que quieres eliminar la BBDD?",
                                         QMessageBox.Yes | QMessageBox.No)
    if confirmacion == QMessageBox.Yes:
        cx.borrarBaseGrafico()
        QMessageBox.information(None, "BASE DE DATOS ELIMINADA",
                                "BASE DE DATOS ELIMINADA CORRECTAMENTE",
                                QMessageBox.Ok)
    else:
        QMessageBox.information(None, "BASE DE DATOS NO ELIMINADA",
                                "LA BASE DE DATOS NO SE HA ELIMINADO",
                                QMessageBox.Ok)

# Función que muestra los botones del menú en la ventana principal
def mostrarBotonesMenu(main_window):
    '''
    Control y configuración de la ventana principal
    :param main_window:
    :return:
    '''

    central_widget = QWidget(main_window)
    main_window.setCentralWidget(central_widget)

    # Crear un layout vertical para los botones
    layout = QVBoxLayout(central_widget)

    # Lista de botones de menú con su texto y función de clic asociada
    buttons = [
        ("Animales", handle_animal_button_click),
        ("Colaboradores", handle_collaborator_button_click),
        ("Borrar BD", handle_delete_button_click),
        ("Salir", main_window.close)
    ]

    # Agregar cada botón al layout
    for button_text, callback in buttons:
        button = QPushButton(button_text, main_window)
        button.clicked.connect(callback)
        layout.addWidget(button)

    # Alinear los botones al centro del layout
    layout.setAlignment(Qt.AlignCenter)

# Función que llama a mostrarBotonesMenu después de un retraso de 3 segundos
def mostrarBotonesMenuDelayed():
    # Obtener la instancia de la aplicación y la ventana principal
    main_window = QApplication.instance().topLevelWidgets()[0]
    # Llamar a mostrarBotonesMenu con la ventana principal como argumento
    mostrarBotonesMenu(main_window)
