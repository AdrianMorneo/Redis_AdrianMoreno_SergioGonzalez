import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import QTimer, Qt
import EstiloCSS as css

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
    welcome_label = QPushButton("¡Bienvenido al Santuario de Animales!", main_window)
    welcome_label.setGeometry(100, 150, 600, 50)

    # Ocultar la etiqueta después de 3 segundos
    QTimer.singleShot(3000, welcome_label.hide)
    QTimer.singleShot(3000, mostrarBotonesMenuDelayed)  # Mostrar los botones del menú después de 3 segundos

    # Mostrar la ventana principal
    main_window.show()
    sys.exit(app.exec_())

# Función que maneja el clic en el botón de "Animales"
def handle_animal_button_click():
    mostrarSubMenuAnimales()
    botonAnimal()

# Función que maneja el clic en el botón de "Colaboradores"
def handle_collaborator_button_click():
    mostrarSubMenuColaboradores()
    botonColaborador()

# Función que maneja el clic en el botón de "Borrar BD"
def handle_delete_button_click():
    botonBorrarBBDD()

# Función que muestra los botones del menú en la ventana principal
def mostrarBotonesMenu(main_window):
    # Crear el widget central y configurarlo en la ventana principal
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

# Función que maneja el clic en el botón de "Animales"
def botonAnimal():
    print("Animales")


# Función que maneja el clic en el botón de "Colaboradores"
def botonColaborador():
    print("Colaboradores")


# Función que maneja el clic en el botón de "Borrar BD"
def botonBorrarBBDD():
    print("Borrar BD")
###########################################
#################
################# ANIMALES
###############
#############################################

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

    ##############################
    ############# colaboradores
    ##############################

def handleAddCollaboratorClick():
    print("Agregar un colaborador")


def handleDeleteCollaboratorClick():
    print("Eliminar un colaborador")


def handleModifyCollaboratorClick():
    print("Modificar un colaborador")


def handleSearchCollaboratorClick():
    print("Buscar un colaborador")


def handleShowAllCollaboratorsClick():
    print("Mostrar todos los colaboradores")


def handleSponsorAnimalClick():
    print("Apadrinar animal =)")


def handleUnsponsorAnimalClick():
    print("Desapadrinar animal :(")


def handleBackToMainMenuClick():
    submenu_window_colaboradores.close()
def mostrarSubMenuColaboradores():
    global submenu_window_colaboradores  #
    submenu_window_colaboradores = QMainWindow()  # Asigna la ventana a la variable global
    submenu_window_colaboradores.setWindowTitle('Submenu de Colaboradores')
    submenu_window_colaboradores.setGeometry(200, 200, 600, 400)

    style_sheet = css.cogerEstiloColaboradores()

    submenu_window_colaboradores.setStyleSheet(style_sheet)

    submenu_layout = QVBoxLayout()

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





