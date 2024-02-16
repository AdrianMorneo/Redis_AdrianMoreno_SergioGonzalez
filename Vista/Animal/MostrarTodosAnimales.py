
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
    QHeaderView, QMessageBox
import EstiloCSS as css
import Conexion as conect

cnt = conect.conectar()

# Variable global para almacenar la ventana de mostrar animales
mostrarAnimales = None

# Función para manejar el evento de volver al menú principal
def handleVuelveSubmenuClick():
    mostrarAnimales.close()

# Función para mostrar la ventana de todos los animales
def mostrarAnimalesWindows():
    global mostrarAnimales

    animales_info = mostrarTodos()  # Obtener la información de todos los animales

    if animales_info:
        # Crear la ventana para mostrar los animales
        mostrarAnimales = QMainWindow()
        mostrarAnimales.setWindowTitle('Mostrar Todos los Animales')
        mostrarAnimales.setGeometry(200, 200, 800, 400)

        # Aplicar estilo a la ventana utilizando CSS
        style_sheet = css.cogerEstiloAnimales()
        mostrarAnimales.setStyleSheet(style_sheet)

        # Crear un widget central para la ventana
        central_widget = QWidget()
        mostrarAnimales.setCentralWidget(central_widget)

        # Crear un layout vertical para organizar los elementos de la ventana
        layout = QVBoxLayout(central_widget)

        # Crear la tabla para mostrar los animales
        table = QTableWidget()
        column_names = ["Tipo", "Nombre", "Edad", "Apadrinado por"]
        table.setColumnCount(len(column_names))
        table.setHorizontalHeaderLabels(column_names)

        # Establecer el número de filas de la tabla
        table.setRowCount(len(animales_info))

        # Agregar los datos de los animales a la tabla
        for row, animal_id in enumerate(animales_info):
            animal = animales_info[animal_id]
            for col, valor in enumerate(animal.values()):
                table.setItem(row, col, QTableWidgetItem(valor))

        # Ajustar el tamaño de las columnas para que se ajusten todas iguales
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Botón para volver al menú principal
        botonVolver = QPushButton("Volver")
        botonVolver.clicked.connect(handleVuelveSubmenuClick)

        # Agregar la tabla y el botón al layout
        layout.addWidget(table)
        layout.addWidget(botonVolver)

        # Mostrar la ventana de todos los animales
        mostrarAnimales.show()
    else:
        # Si no hay animales en la base de datos, mostrar un mensaje de aviso
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay animales en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
def mostrarTodos():
    animales = {}
    keys = cnt.keys('A*')
    if keys:
        for key in keys:
            valor = cnt.get(key)
            detalles = valor.split('\n')
            detalles_dict = {}
            for detalle in detalles:
                if ':' in detalle:  # Verifica si la línea contiene el separador ':'
                    parametro, valor = detalle.split(': ', 1)  # Limita la división a solo 1 vez
                    detalles_dict[parametro.strip()] = valor.strip()  # Elimina los espacios en blanco alrededor de los valores
            animales[key] = detalles_dict
    return animales
