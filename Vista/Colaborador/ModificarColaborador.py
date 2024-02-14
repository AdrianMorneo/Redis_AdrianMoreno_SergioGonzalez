from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, \
    QCalendarWidget, QMessageBox  # Importar clases necesarias desde PySide2
from PySide2.QtCore import Qt, QDate  # Importar clases necesarias desde PySide2

import ColaboradorConsola  # Importar módulo para interactuar con la base de datos de colaboradores (consola)
import EstiloCSS as css  # Importar módulo para el estilo de la interfaz de usuario
import ColaboradorGrafico as cg  # Importar módulo para interactuar con la base de datos de colaboradores (gráfico)
import Utiles as ut  # Importar módulo de utilidades para validaciones
import ColaboradorConsola as cc  # Importar módulo para interactuar con la base de datos de colaboradores (consola)

# Variable global para almacenar la ventana de modificación
modificarColaboradorWindow = None

def confirmarModificacion(dniAnt, dni, nombre, apellido, telefono, fecha):
    '''
    # Función para confirmar la modificación de un colaborador y control de parametros
    :param dniAnt: Recibe el dni antiguo por si se cambio para modificarlo
    :param dni: Recibe el nuevo DNI
    :param nombre: recibe el nombre
    :param apellido: recibe el apellido
    :param telefono: Recibe el telefono
    :param fecha: Recibe la fecha
    :return: Nada
    '''
    mensaje = QMessageBox()
    mensaje.setWindowTitle("Confirmar Modificación")
    mensaje.setText("¿Seguro que quieres modificar?")
    mensaje.setIcon(QMessageBox.Question)
    mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    mensaje.setDefaultButton(QMessageBox.Cancel)
    respuesta = mensaje.exec_()

    # Procesar la respuesta del usuario
    if respuesta == QMessageBox.Yes:
        if not ut.validarDNI(dni):
            # Si el DNI no es válido, mostrar una alerta
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Alerta")
            alerta.setText("DNI no válido, (00000000A)")
            alerta.exec_()
        elif cc.comprobarDNIBBDD(dni) and dniAnt != dni:
            # Si el DNI ya está en la base de datos y es diferente al original, mostrar alerta
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Alerta")
            alerta.setText("DNI ya introducido en la BBDD")
            alerta.exec_()
        elif not ut.validarNombre(nombre):
            # Si el nombre no es válido, mostrar una alerta
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Alerta")
            alerta.setText("Nombre no válido, mínimo 2 dígitos")
            alerta.exec_()
        elif not ut.validarNombre(apellido):
            # Si el apellido no es válido, mostrar una alerta
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Alerta")
            alerta.setText("Apellido no válido, mínimo 2 dígitos")
            alerta.exec_()
        elif not ut.validarTelefono(telefono):
            # Si el teléfono no es válido, mostrar una alerta
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Alerta")
            alerta.setText("Telefono no válido, deben ser 9 dígitos")
            alerta.exec_()
        else:
            # Si todos los datos son válidos, realizar la modificación
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Warning)
            alerta.setWindowTitle("Colaborador Modificado")
            alerta.setText("Colaborador Modificado")
            cg.eliminar(dniAnt)  # Eliminar el colaborador con el DNI anterior
            cg.modificar(dni, nombre, apellido, telefono, fecha)  # Modificar el colaborador en la base de datos
            dniLineEditBuscar.clear()  # Limpiar el campo de búsqueda
            dniLineEdit.clear()  # Limpiar el campo de DNI
            nombreLineEdit.clear()  # Limpiar el campo de nombre
            apellidoLineEdit.clear()  # Limpiar el campo de apellido
            telefonoLineEdit.clear()  # Limpiar el campo de teléfono
            print("Modificado")
            alerta.exec_()

def buscarColaborador():
    '''
    # Función para buscar un colaborador por su DNI
    :return:
    '''

    dni = dniLineEditBuscar.text().upper()
    colaborador = cg.buscar(dni)  # Buscar el colaborador en la base de datos
    if colaborador:
        # Si se encuentra el colaborador, llenar los campos con sus datos
        dniLineEdit.setText(colaborador['dni'])
        nombreLineEdit.setText(colaborador['nombre'])
        apellidoLineEdit.setText(colaborador['apellido'])
        telefonoLineEdit.setText(colaborador['telefono'])
        fechaInscripcion = colaborador['fechaInscripcion']
        calendarWidget.setSelectedDate(
            QDate.fromString(fechaInscripcion, "dd-MM-yyyy"))
    else:
        # Si el colaborador no es encontrado, mostrar un mensaje informativo
        QMessageBox.information(None, "Colaborador no encontrado", "El colaborador con el DNI especificado no fue encontrado.", QMessageBox.Ok)

def modificarColaboradorVentana():
    '''
    Función para mostrar la ventana de modificación de colaboradores
    :return:
    '''

    if ColaboradorConsola.mostrarTodos():
        global modificarColaboradorWindow
        # Si la ventana ya está creada, simplemente la mostramos
        if modificarColaboradorWindow is not None:
            modificarColaboradorWindow.show()
            return

        # Crear una nueva ventana principal para modificar colaboradores
        modificarColaboradorWindow = QMainWindow()
        modificarColaboradorWindow.setWindowTitle('Modificar Colaborador')
        modificarColaboradorWindow.setGeometry(200, 200, 400, 400)

        # Establecer el estilo de la ventana utilizando el CSS proporcionado
        style_sheet = css.cogerEstiloColaboradores()
        modificarColaboradorWindow.setStyleSheet(style_sheet)

        # Crear un layout vertical para organizar los elementos de la ventana
        layout = QVBoxLayout()

        # Agregar un QLabel y un QLineEdit para buscar un colaborador por su DNI
        dniLabelBuscar = QLabel("Buscar Colaborador por DNI:")
        layout.addWidget(dniLabelBuscar)
        global dniLineEditBuscar
        dniLineEditBuscar = QLineEdit()
        layout.addWidget(dniLineEditBuscar)
        buscar_button = QPushButton("Buscar")
        buscar_button.clicked.connect(buscarColaborador)
        layout.addWidget(buscar_button)

        # Agregar etiquetas y campos de entrada para DNI, nombre, apellido y teléfono
        dniLabel = QLabel("DNI: (00000000A)")
        layout.addWidget(dniLabel)
        global dniLineEdit
        dniLineEdit = QLineEdit()
        layout.addWidget(dniLineEdit)

        nombreLabel = QLabel("Nombre: (mínimo 2 letras)")
        layout.addWidget(nombreLabel)
        global nombreLineEdit
        nombreLineEdit = QLineEdit()
        layout.addWidget(nombreLineEdit)

        apellidoLabel = QLabel("Apellido: (mínimo 2 letras)")
        layout.addWidget(apellidoLabel)
        global apellidoLineEdit
        apellidoLineEdit = QLineEdit()
        layout.addWidget(apellidoLineEdit)

        telefonoLabel = QLabel("Teléfono: (9 dígitos)")
        layout.addWidget(telefonoLabel)
        global telefonoLineEdit
        telefonoLineEdit = QLineEdit()
        layout.addWidget(telefonoLineEdit)

        # Agregar un QLabel y un QCalendarWidget para seleccionar la fecha de inscripción
        fechaLabel = QLabel("Fecha de Inscripción:")
        layout.addWidget(fechaLabel)
        global calendarWidget
        calendarWidget = QCalendarWidget()
        layout.addWidget(calendarWidget)

        # Agregar un QPushButton para confirmar la modificación del colaborador
        modificar_button = QPushButton("Modificar")
        # Conectar el botón de modificar con la función de confirmar modificación
        modificar_button.clicked.connect(
            lambda: confirmarModificacion(dniLineEditBuscar.text().upper(), dniLineEdit.text().upper(),
                                          nombreLineEdit.text().upper(),
                                          apellidoLineEdit.text().upper(), telefonoLineEdit.text().upper(),
                                          calendarWidget.selectedDate().toString("dd-MM-yyyy")))
        layout.addWidget(modificar_button)

        # Agregar un QPushButton para cerrar la ventana de modificación
        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(modificarColaboradorWindow.close)
        layout.addWidget(volver_button)

        # Alinear el layout en el centro de la ventana
        layout.setAlignment(Qt.AlignCenter)

        # Crear un widget principal y establecer el layout creado anteriormente
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget principal como widget central de la ventana
        modificarColaboradorWindow.setCentralWidget(widget)

        # Mostrar la ventana de modificación de colaboradores
        modificarColaboradorWindow.show()
    else:
        # Si no hay colaboradores en la base de datos, mostrar un mensaje de aviso
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Aviso")
        mensaje.setText("No hay colaboradores en la BBDD.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()
