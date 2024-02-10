from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
    QHeaderView
import EstiloCSS as css
import ColaboradorConsola as cc

def handleVuelveSubmenuClick():
    mostrarColaboradores.close()

def mostrarColaboradoresWindows():
    global mostrarColaboradores
    mostrarColaboradores = QMainWindow()
    mostrarColaboradores.setWindowTitle('Mostrar Todos Colaboradores')
    mostrarColaboradores.setGeometry(200, 200, 800, 400)

    style_sheet = css.cogerEstiloColaboradores()
    mostrarColaboradores.setStyleSheet(style_sheet)

    central_widget = QWidget()
    mostrarColaboradores.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    # Crear la tabla
    table = QTableWidget()

    # Definir los nombres de las columnas
    column_names = ["DNI", "Nombre", "Apellido", "Teléfono", "Fecha de Inscripción"]
    table.setColumnCount(len(column_names))  # Definir el número de columnas
    table.setHorizontalHeaderLabels(column_names)

    # Obtener la información de los colaboradores
    colaboradores_info = cc.mostrarTodos()

    # Agregar los datos a la tabla
    if colaboradores_info:
        table.setRowCount(len(colaboradores_info))
        for row, colaborador in enumerate(colaboradores_info):
            table.setItem(row, 0, QTableWidgetItem(colaborador['dni']))
            table.setItem(row, 1, QTableWidgetItem(colaborador['nombre']))
            table.setItem(row, 2, QTableWidgetItem(colaborador['apellido']))
            table.setItem(row, 3, QTableWidgetItem(colaborador['telefono']))
            table.setItem(row, 4, QTableWidgetItem(colaborador['fechaInscripcion']))
    else:
        # Si no hay datos, mostrar un mensaje en una fila
        table.setRowCount(1)
        no_data_item = QTableWidgetItem("No hay colaboradores registrados.")
        table.setItem(0, 0, no_data_item)
        table.setColumnSpan(0, 0, len(column_names))  # Fusionar todas las columnas

    # Ajustar el tamaño de las columnas para que se ajusten al contenido
    table.resizeColumnsToContents()

    # Establecer el ajuste horizontal de la tabla
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # Botón para volver al menú principal
    botonVolver = QPushButton("Volver")
    botonVolver.clicked.connect(handleVuelveSubmenuClick)
    layout.addWidget(table)
    layout.addWidget(botonVolver)

    mostrarColaboradores.show()


