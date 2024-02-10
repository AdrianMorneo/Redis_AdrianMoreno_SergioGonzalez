###########################################
#################
################# ANIMALES
###############
#############################################
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget
import EstiloCSS as css


def handleAddAnimalClick():
    print("Agregar un animal")


def handleDeleteAnimalClick():
    print("Eliminar un animal")


def handleModifyAnimalClick():
    print("Modificar un animal")


def handleSearchAnimalClick():
    print("Buscar un animal")


def handleShowAllAnimalsClick():
    print("Mostrar todos los animales")

def handleBackToMainMenuClickA():
    submenu_window_animales.close()
def mostrarSubMenuAnimales():
    global submenu_window_animales
    submenu_window_animales = QMainWindow()
    submenu_window_animales.setWindowTitle('Submenu de Animales')
    submenu_window_animales.setGeometry(200, 200, 600, 400)

    style_sheet = css.cogerEstiloAnimales()

    submenu_window_animales.setStyleSheet(style_sheet)

    submenu_layout = QVBoxLayout()

    submenu_buttons = [
        ("Agregar un animal", handleAddAnimalClick),
        ("Eliminar un animal", handleDeleteAnimalClick),
        ("Modificar un animal", handleModifyAnimalClick),
        ("Buscar un animal", handleSearchAnimalClick),
        ("Mostrar todos los animales", handleShowAllAnimalsClick),
        ("Volver al menú principal", handleBackToMainMenuClickA)
    ]

    for button_text, callback in submenu_buttons:
        button = QPushButton(button_text, submenu_window_animales)
        button.clicked.connect(callback)
        submenu_layout.addWidget(button)

    submenu_layout.setAlignment(Qt.AlignCenter)

    submenu_widget = QWidget()
    submenu_widget.setLayout(submenu_layout)

    submenu_window_animales.setCentralWidget(submenu_widget)

    submenu_window_animales.show()