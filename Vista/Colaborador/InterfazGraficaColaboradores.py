from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit
from . import AgregarColaborador as ac  # Importar módulo para agregar colaborador
from . import MostrarTodosColaboradores as mt  # Importar módulo para mostrar todos los colaboradores
from . import ModificarColaborador as mc  # Importar módulo para modificar colaborador
from . import BuscarColaborador as bc  # Importar módulo para buscar colaborador
from . import EliminarColaborador as ec  # Importar módulo para eliminar colaborador

# Importar el archivo EstiloCSS para el estilo de la interfaz de usuario
import EstiloCSS as css

# Definir funciones para manejar eventos de botones
def handleNuevoColaborador():
    # Manejar el evento de agregar un colaborador
    ac.agregarColaboradorVentana()

def handleBorrarColaborador():
    # Manejar el evento de eliminar un colaborador
    ec.eliminarColaboradorVentana()

def handleModificarColaborador():
    # Manejar el evento de modificar un colaborador
    mc.modificarColaboradorVentana()

def handleBuscarColaborador():
    # Manejar el evento de buscar un colaborador
    bc.buscarColaboradorVentana()

def handleMostrarTodosColaboradores():
    # Manejar el evento de mostrar todos los colaboradores
    mt.mostrarColaboradoresWindows()

def handleApadrinarAnimal():
    # Manejar el evento de apadrinar un animal (sin implementar)
    print("Apadrinar animal =)")

def handleDesapadrinarAnimal():
    # Manejar el evento de desapadrinar un animal (sin implementar)
    print("Desapadrinar animal :(")

def handleVolver():
    # Manejar el evento de volver al menú principal
    submenu_window_colaboradores.close()

# Función para mostrar el submenú de colaboradores
def mostrarSubMenuColaboradores():
    global submenu_window_colaboradores
    submenu_window_colaboradores = QMainWindow()
    submenu_window_colaboradores.setWindowTitle('Submenu de Colaboradores')
    submenu_window_colaboradores.setGeometry(200, 200, 600, 400)

    # Estilo de la interfaz de usuario
    style_sheet = css.cogerEstiloColaboradores()
    submenu_window_colaboradores.setStyleSheet(style_sheet)

    submenu_layout = QVBoxLayout()

    # Lista de botones y sus respectivas funciones de manejo de eventos
    submenu_buttons = [
        ("Agregar un colaborador", handleNuevoColaborador),
        ("Eliminar un colaborador", handleBorrarColaborador),
        ("Modificar un colaborador", handleModificarColaborador),
        ("Buscar un colaborador", handleBuscarColaborador),
        ("Mostrar todos los colaboradores", handleMostrarTodosColaboradores),
        ("Apadrinar animal =)", handleApadrinarAnimal),
        ("Desapadrinar animal :(", handleDesapadrinarAnimal),
        ("Volver al menú principal", handleVolver)
    ]

    # Crear botones y conectarlos con sus funciones de manejo de eventos
    for button_text, callback in submenu_buttons:
        button = QPushButton(button_text, submenu_window_colaboradores)
        button.clicked.connect(callback)
        submenu_layout.addWidget(button)

    # Alinear el layout verticalmente al centro
    submenu_layout.setAlignment(Qt.AlignCenter)

    # Crear un widget y establecer el layout como su diseño
    submenu_widget = QWidget()
    submenu_widget.setLayout(submenu_layout)

    # Establecer el widget central de la ventana del submenú
    submenu_window_colaboradores.setCentralWidget(submenu_widget)

    # Mostrar la ventana del submenú de colaboradores
    submenu_window_colaboradores.show()

