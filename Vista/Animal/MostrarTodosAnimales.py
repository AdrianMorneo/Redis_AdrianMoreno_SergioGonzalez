
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
    QHeaderView, QMessageBox
import EstiloCSS as css
import ColaboradorConsola as cc


def handleVuelveSubmenuClick():
    # Función para manejar el evento de volver al menú principal
    mostrarAnimales.close()


def mostrarAnimalesWindows():
#    # Función para mostrar la ventana de todos los colaboradores
    if cc.mostrarTodos():
        # Verificar si hay colaboradores en la base de datos
        global mostrarAnimales
        # Crear una nueva ventana para mostrar los colaboradores
        mostrarAnimales = QMainWindow()
        mostrarAnimales.setWindowTitle('Mostrar Todos Colaboradores')
        mostrarAnimales.setGeometry(200, 200, 800, 400)

        # Aplicar estilo a la ventana utilizando CSS
        style_sheet = css.cogerEstiloAnimales()
        mostrarAnimales.setStyleSheet(style_sheet)

        # Crear un widget central para la ventana
        central_widget = QWidget()
        mostrarAnimales.setCentralWidget(central_widget)

        # Crear un layout vertical para organizar los elementos de la ventana
        layout = QVBoxLayout(central_widget)

        # Crear la tabla para mostrar los colaboradores
        table = QTableWidget()

        # Definir los nombres de las columnas de la tabla
        column_names = ["Tipo", "Nombre", "Edad", "Apadrinado por"]
        table.setColumnCount(len(column_names))  # Establecer el número de columnas
        table.setHorizontalHeaderLabels(column_names)  # Establecer los nombres de las columnas

        # Obtener la información de los colaboradores desde la base de datos
        animales_info = cc.mostrarTodos()

        # Agregar los datos de los colaboradores a la tabla
        '''
        if animales_info:
            table.setRowCount(len(animales_info))
            for row, animal in enumerate(animales_info):
                table.setItem(row, 0, QTableWidgetItem(animal['tipo']))
                table.setItem(row, 1, QTableWidgetItem(animal['nombre']))
                table.setItem(row, 2, QTableWidgetItem(animal['edad']))
                table.setItem(row, 3, QTableWidgetItem(animal['apadrinado']))

        else:
            # Si no hay datos de animal, mostrar un mensaje en la tabla
            table.setRowCount(1)
            no_data_item = QTableWidgetItem("No hay animal registrado.")
            table.setItem(0, 0, no_data_item)
            table.setColumnSpan(0, 0, len(column_names))  # Fusionar todas las columnas
        
        '''
        # Ajustar el tamaño de las columnas para que se ajusten al contenido
        table.resizeColumnsToContents()

        # Establecer el ajuste horizontal de la tabla
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Botón para volver al menú principal
        botonVolver = QPushButton("Volver")
        botonVolver.clicked.connect(handleVuelveSubmenuClick)

        # Agregar la tabla y el botón al layout
        layout.addWidget(table)
        layout.addWidget(botonVolver)

        # Mostrar la ventana de todos los animal
        mostrarAnimales.show()

"""
    else:
        # Si no hay animal en la base de datos, mostrar un mensaje de aviso
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay animal en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
"""