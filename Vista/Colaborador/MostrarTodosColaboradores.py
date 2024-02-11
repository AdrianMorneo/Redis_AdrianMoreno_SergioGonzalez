
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTableWidget, QTableWidgetItem, \
    QHeaderView, QMessageBox
import EstiloCSS as css
import ColaboradorConsola as cc


def handleVuelveSubmenuClick():
    # Función para manejar el evento de volver al menú principal
    mostrarColaboradores.close()


def mostrarColaboradoresWindows():
    # Función para mostrar la ventana de todos los colaboradores
    if cc.mostrarTodos():
        # Verificar si hay colaboradores en la base de datos
        global mostrarColaboradores
        # Crear una nueva ventana para mostrar los colaboradores
        mostrarColaboradores = QMainWindow()
        mostrarColaboradores.setWindowTitle('Mostrar Todos Colaboradores')
        mostrarColaboradores.setGeometry(200, 200, 800, 400)

        # Aplicar estilo a la ventana utilizando CSS
        style_sheet = css.cogerEstiloColaboradores()
        mostrarColaboradores.setStyleSheet(style_sheet)

        # Crear un widget central para la ventana
        central_widget = QWidget()
        mostrarColaboradores.setCentralWidget(central_widget)

        # Crear un layout vertical para organizar los elementos de la ventana
        layout = QVBoxLayout(central_widget)

        # Crear la tabla para mostrar los colaboradores
        table = QTableWidget()

        # Definir los nombres de las columnas de la tabla
        column_names = ["DNI", "Nombre", "Apellido", "Teléfono", "Fecha de Inscripción"]
        table.setColumnCount(len(column_names))  # Establecer el número de columnas
        table.setHorizontalHeaderLabels(column_names)  # Establecer los nombres de las columnas

        # Obtener la información de los colaboradores desde la base de datos
        colaboradores_info = cc.mostrarTodos()

        # Agregar los datos de los colaboradores a la tabla
        if colaboradores_info:
            table.setRowCount(len(colaboradores_info))
            for row, colaborador in enumerate(colaboradores_info):
                table.setItem(row, 0, QTableWidgetItem(colaborador['dni']))
                table.setItem(row, 1, QTableWidgetItem(colaborador['nombre']))
                table.setItem(row, 2, QTableWidgetItem(colaborador['apellido']))
                table.setItem(row, 3, QTableWidgetItem(colaborador['telefono']))
                table.setItem(row, 4, QTableWidgetItem(colaborador['fechaInscripcion']))
        else:
            # Si no hay datos de colaboradores, mostrar un mensaje en la tabla
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

        # Agregar la tabla y el botón al layout
        layout.addWidget(table)
        layout.addWidget(botonVolver)

        # Mostrar la ventana de todos los colaboradores
        mostrarColaboradores.show()
    else:
        # Si no hay colaboradores en la base de datos, mostrar un mensaje de aviso
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay colaboradores en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
