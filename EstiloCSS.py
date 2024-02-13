def cogerEstiloPrincipal():
    return """
        QMainWindow {
            background-color: #0D050E;
        }

        QPushButton {
            font-size: 18px;
            background-color: #A3445D;
            color: white;
            border: 2px solid #8D2D56;
            border-radius: 10px;
            padding: 10px;
        }

        QPushButton:hover {
            background-color: #2B193E;
        }

        QPushButton:pressed {
            background-color: #D53C3C;
        }
    """
def cogerEstiloAnimales():
    return """
            QMainWindow {
                background-color: #e4ebf2;
                color: white;
            }

            QPushButton {
                font-size: 18px;
                background-color: #52733b;
                color: white;
                border: 2px solid #84a45a;
                border-radius: 10px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #818A6f;
            }

            QPushButton:pressed {
                background-color: #715e4e;
            }

            QLabel {
                font-size: 16px;
                color: black; /* Cambio de color de texto */
                background-color: white; /* Fondo blanco */
                border: 2px solid black; /* Borde negro */
                border-radius: 5px;
                padding: 5px;
            }

            QLineEdit {
                font-size: 16px;
                background-color: #d9d9d9;
                border: 2px solid #be8260;
                border-radius: 5px;
                padding: 5px;
            }

            QScrollArea {
                background-color: #f5f5f5;
            }

            QScrollBar:vertical {
                background-color: #e0e0e0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background-color: #be8260;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                background-color: #f5f5f5;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                background-color: #f5f5f5;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
        """

def cogerEstiloColaboradores():
    return """
        QMainWindow {
            background-color: #253f5b;
            color: white;
        }

        QPushButton {
            font-size: 18px;
            background-color: #4f728E;
            color: white;
            border: 2px solid #be8260;
            border-radius: 10px;
            padding: 10px;
        }

        QPushButton:hover {
            background-color: #7b0950;
        }

        QPushButton:pressed {
            background-color: #74412b;
        }

        QLabel {
            font-size: 16px;
            color: black; /* Cambio de color de texto */
            background-color: white; /* Fondo blanco */
            border: 2px solid black; /* Borde negro */
            border-radius: 5px;
            padding: 5px;
        }

        QLineEdit {
            font-size: 16px;
            background-color: #d9d9d9;
            border: 2px solid #be8260;
            border-radius: 5px;
            padding: 5px;
        }

        QScrollArea {
            background-color: #f5f5f5;
        }

        QScrollBar:vertical {
            background-color: #e0e0e0;
            width: 10px;
            margin: 0px 0px 0px 0px;
        }

        QScrollBar::handle:vertical {
            background-color: #be8260;
            min-height: 20px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical {
            background-color: #f5f5f5;
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            background-color: #f5f5f5;
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
    """


