import sys
from PySide6.QtWidgets import QApplication
from view.main_window import MainWindow
from controller.app_controller import AppController

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    controller = AppController(window)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()