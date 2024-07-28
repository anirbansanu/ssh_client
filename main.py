from gui.main import MainApplication
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = MainApplication()
    window.show()
    app.exec_()
