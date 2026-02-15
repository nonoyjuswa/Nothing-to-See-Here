from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("People Memory App")
        self.setMinimumSize(600, 400)

        label = QLabel("App Initialized")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)