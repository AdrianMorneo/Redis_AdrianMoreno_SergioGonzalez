from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit
from . import AgregarColaborador as ac
from . import MostrarTodosColaboradores as mt

# Importamos el archivo EstiloCSS
import EstiloCSS as css

# Definimos las funciones para manejar los eventos de los botones
def handleAddCollaboratorClick():
    print("Agregar un colaborador")
    ac.showAddCollaboratorWindow()

def handleDeleteCollaboratorClick():
    print("Eliminar un colaborador")

def handleModifyCollaboratorClick():
    print("Modificar un colaborador")

def handleSearchCollaboratorClick():
    print("Buscar un colaborador")

def handleShowAllCollaboratorsClick():
    print("Mostrar todos los colaboradores")
    mt.mostrarColaboradoresWindows()

def handleSponsorAnimalClick():
    print("Apadrinar animal =)")

def handleUnsponsorAnimalClick():
    print("Desapadrinar animal :(")

def handleBackToMainMenuClick():
    submenu_window_colaboradores.close()

# Función para mostrar el submenú de colaboradores
def mostrarSubMenuColaboradores():
    global submenu_window_colaboradores
    submenu_window_colaboradores = QMainWindow()
    submenu_window_colaboradores.setWindowTitle('Submenu de Colaboradores')
    submenu_window_colaboradores.setGeometry(200, 200, 600, 400)

    style_sheet = css.cogerEstiloColaboradores()
    submenu_window_colaboradores.setStyleSheet(style_sheet)

    submenu_layout = QVBoxLayout()

    # Creamos botones para diferentes acciones y los conectamos a las funciones correspondientes
    submenu_buttons = [
        ("Agregar un colaborador", handleAddCollaboratorClick),
        ("Eliminar un colaborador", handleDeleteCollaboratorClick),
        ("Modificar un colaborador", handleModifyCollaboratorClick),
        ("Buscar un colaborador", handleSearchCollaboratorClick),
        ("Mostrar todos los colaboradores", handleShowAllCollaboratorsClick),
        ("Apadrinar animal =)", handleSponsorAnimalClick),
        ("Desapadrinar animal :(", handleUnsponsorAnimalClick),
        ("Volver al menú principal", handleBackToMainMenuClick)
    ]

    for button_text, callback in submenu_buttons:
        button = QPushButton(button_text, submenu_window_colaboradores)
        button.clicked.connect(callback)
        submenu_layout.addWidget(button)

    submenu_layout.setAlignment(Qt.AlignCenter)

    submenu_widget = QWidget()
    submenu_widget.setLayout(submenu_layout)

    submenu_window_colaboradores.setCentralWidget(submenu_widget)
    submenu_window_colaboradores.show()
