from PySide6.QtWidgets import (
    QMainWindow, 
    QLabel,
    QWidget,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QFormLayout
    )
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("People Memory App")
        self.setMinimumSize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.where_met_input = QLineEdit()
        self.notes_input = QTextEdit()

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Where Met:", self.where_met_input)
        form_layout.addRow("Notes:", self.notes_input)

        main_layout.addLayout(form_layout)

        self.add_button = QPushButton("Add Person")
        main_layout.addWidget(self.add_button)